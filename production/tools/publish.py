#!/usr/bin/env python3
"""Publish rendered episodes in listening order: iCloud Drive, GitHub release assets, and RSS feeds.

Usage (from production/): uv run --with mutagen tools/publish.py [--icloud] [--github --site ../docs]

--icloud  copies each series to iCloud Drive as "NN - Title.mp3".
--github  uploads the MP3s as release assets (one release per series). Needs --site.
--site    writes the feeds, feed stylesheet, chapter JSON, OPML, covers and index page
          into this directory, the GitHub Pages folder. Without --github it rewrites
          them without uploading. Commit and push afterwards.
"""
import argparse
import datetime
import email.utils
import hashlib
import json
import pathlib
import shutil
import subprocess
from xml.sax.saxutils import escape, quoteattr

from mutagen.id3 import ID3, TALB, TCON, TIT2, TPE1, TRCK

ROOT = pathlib.Path(__file__).resolve().parent.parent
ICLOUD = pathlib.Path.home() / "Library/Mobile Documents/com~apple~CloudDocs"
REPO = "bjcoombs/pass-the-architect"
BASE_URL = "https://bjcoombs.github.io/pass-the-architect"
AUTHOR = "Pass the Architect"
# Listening order. Files are numbered from 00 by position, and the hosts say the same
# number aloud ("This is episode eleven"), so a reorder needs the spoken lines changing too:
# see tools/renumber_retake.py.
SERIES = [
    {
        "slug": "ccar-p",
        "title": "Pass the Architect: CCAR-P",
        "folder": "Pass the Architect CCAR-P",
        "colour": "#1f3a5f",
        "label": "CCAR-P",
        "description": "A two-host study series for the Claude Certified Architect - Professional exam: "
                       "every blueprint domain, drills, and the traps the distractors set.",
        "episodes": ["00", "01", "02", "03", "04", "05", "06", "07", "08", "10", "11", "09", "12"],
    },
    {
        "slug": "ccar-f-retake",
        "title": "Pass the Architect: CCAR-F retake",
        "folder": "Pass the Architect CCAR-F Retake",
        "colour": "#7a2e1f",
        "label": "CCAR-F",
        "description": "A two-host study series for resitting the Claude Certified Architect - Foundations exam: "
                       "the thirty task statements, the six scenarios, and the miss patterns that cost marks.",
        "episodes": ["F00", "10", "F04", "F05", "F06", "F01", "F02", "F03", "F07", "F08", "11", "F09", "F10", "F11"],
    },
    # Drafts are written but not yet rendered: publish skips them except for the cover.
    {
        "slug": "ccdv-f",
        "title": "Pass the Architect: CCDV-F",
        "folder": "Pass the Architect CCDV-F",
        "colour": "#1f5a4a",
        "label": "CCDV-F",
        "description": "A two-host study series for the Claude Certified Developer - Foundations exam: "
                       "the API, application design, agents, tools and MCP, models, prompts, security and debugging.",
        "episodes": [f"D{n:02d}" for n in range(12)],
        "draft": True,
    },
    {
        "slug": "ccao-f",
        "title": "Pass the Architect: CCAO-F",
        "folder": "Pass the Architect CCAO-F",
        "colour": "#5a2f6e",
        "label": "CCAO-F",
        "description": "A two-host study series for the Claude Certified Associate - Foundations exam: "
                       "prompting, checking outputs, products and models, workflows, Projects, responsible use and troubleshooting.",
        "episodes": [f"A{n:02d}" for n in range(10)],
        "draft": True,
    },
]
LIVE = [s for s in SERIES if not s.get("draft")]
# Episode ID prefix to transcript folder; IDs without a prefix are CCAR-P episodes.
FOLDERS = {"F": "foundations", "D": "developer", "A": "associate"}


def front_matter(path):
    _, front, _ = path.read_text().split("---", 2)
    meta = {}
    for line in front.strip().splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip().strip('"')
    return meta


def transcript(ep):
    folder = ROOT / FOLDERS[ep[0]] / "transcripts" if ep[0] in FOLDERS else ROOT / "transcripts"
    return next(folder.glob(f"{ep}-*.md"))


def duration(mp3):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)],
                         capture_output=True, text=True, check=True)
    secs = int(float(out.stdout.strip()))
    return f"{secs // 3600:d}:{secs % 3600 // 60:02d}:{secs % 60:02d}"


def stage(series):
    """Retag each episode for its series and position; return [(n, transcript, meta, staged mp3)]."""
    dist = ROOT / "dist" / series["slug"]
    dist.mkdir(parents=True, exist_ok=True)
    staged = []
    for n, ep in enumerate(series["episodes"]):
        tr = transcript(ep)
        meta = front_matter(tr)
        audio = tr.parent.parent / "audio" / f"{tr.stem}.mp3"
        out = dist / f"{n:02d}-{tr.stem}.mp3"
        # Retag a copy with mutagen: ffmpeg would drop the chapter titles and artwork.
        shutil.copyfile(audio, out)
        tags = ID3(out)
        for frame in (TIT2(encoding=3, text=[f"{n:02d} {meta['title']}"]), TRCK(encoding=3, text=[str(n + 1)]),
                      TALB(encoding=3, text=[series["title"]]), TPE1(encoding=3, text=[AUTHOR]),
                      TCON(encoding=3, text=["Podcast"])):
            tags.setall(frame.FrameID, [frame])
        tags.save(out, v2_version=3)
        staged.append((n, tr, meta, out))
    return staged


def to_icloud(series, staged):
    folder = ICLOUD / series["folder"]
    folder.mkdir(parents=True, exist_ok=True)
    wanted = set()
    for n, _, meta, mp3 in staged:
        name = f'{n:02d} - {meta["title"].replace(":", "").replace("/", "")}.mp3'
        shutil.copyfile(mp3, folder / name)
        wanted.add(name)
    for old in folder.glob("*.mp3"):  # earlier numbering; to the Trash, not deleted
        if old.name not in wanted:
            old.rename(pathlib.Path.home() / ".Trash" / old.name)
    print(f"{folder}  episodes={len(staged)}")


def to_release(series, staged):
    tag = series["slug"]
    if subprocess.run(["gh", "release", "view", tag, "-R", REPO], capture_output=True).returncode:
        subprocess.run(["gh", "release", "create", tag, "-R", REPO, "--title", series["title"],
                        "--notes", "Episode audio for the podcast feed."], check=True)
    subprocess.run(["gh", "release", "upload", tag, "-R", REPO, "--clobber", *[str(s[3]) for s in staged]], check=True)


def digest(mp3):
    """Short content hash for the GUID, so podcast apps fetch an episode again when its audio or chapters change."""
    return hashlib.sha256(mp3.read_bytes()).hexdigest()[:8]


def cover(series, site):
    out = site / f"cover-{series['slug']}.png"
    if not out.exists():
        subprocess.run(
            ["magick", "-size", "1400x1400", f"xc:{series['colour']}", "-font", "/System/Library/Fonts/Helvetica.ttc",
             "-fill", "white", "-gravity", "center",
             "-pointsize", "130", "-annotate", "+0-220", "Pass the\nArchitect",
             "-pointsize", "210", "-annotate", "+0+200", series["label"], str(out)],
            check=True,
        )
    return out


def feed(series, staged, site):
    chapters_dir = site / "chapters" / series["slug"]
    chapters_dir.mkdir(parents=True, exist_ok=True)
    # Podcast apps list newest first, so the first episode to play gets the oldest date.
    start = datetime.datetime(2026, 10, 18, 6, 0, tzinfo=datetime.timezone.utc)
    items = []
    for n, tr, meta, mp3 in staged:
        url = f"https://github.com/{REPO}/releases/download/{series['slug']}/{mp3.name}"
        chapters = tr.parent.parent / "audio" / f"{tr.stem}.chapters.json"
        chapter_tag = ""
        if chapters.exists():
            data = json.loads(chapters.read_text())
            img_src = chapters.parent / "cards" / tr.stem
            img_dst = chapters_dir / mp3.stem
            shutil.rmtree(img_dst, ignore_errors=True)
            if img_src.exists():
                shutil.copytree(img_src, img_dst)
            for c in data["chapters"]:
                if "img" in c:
                    c["img"] = f"{BASE_URL}/chapters/{series['slug']}/{mp3.stem}/{c['img']}"
            (chapters_dir / f"{mp3.stem}.json").write_text(json.dumps(data, indent=2) + "\n")
            chapter_tag = (f'\n      <podcast:chapters url="{BASE_URL}/chapters/{series["slug"]}/{mp3.stem}.json"'
                           f' type="application/json+chapters"/>')
        items.append(f"""    <item>
      <title>{escape(f"{n:02d}. {meta['title']}")}</title>
      <description>{escape(meta.get('description', ''))}</description>
      <enclosure url={quoteattr(url)} length="{mp3.stat().st_size}" type="audio/mpeg"/>
      <guid isPermaLink="false">pass-the-architect-{series['slug']}-{tr.stem}-{digest(mp3)}</guid>
      <pubDate>{email.utils.format_datetime(start + datetime.timedelta(minutes=n))}</pubDate>
      <itunes:duration>{duration(mp3)}</itunes:duration>
      <itunes:episodeType>full</itunes:episodeType>{chapter_tag}
    </item>""")
    image = f"{BASE_URL}/{cover(series, site).name}"
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="feed.xsl"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:podcast="https://podcastindex.org/namespace/1.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{escape(series['title'])}</title>
    <link>{BASE_URL}/</link>
    <atom:link href="{BASE_URL}/{series['slug']}.xml" rel="self" type="application/rss+xml"/>
    <language>en-gb</language>
    <description>{escape(series['description'])}</description>
    <itunes:summary>{escape(series['description'])}</itunes:summary>
    <itunes:author>{AUTHOR}</itunes:author>
    <itunes:image href="{image}"/>
    <image><url>{image}</url><title>{escape(series['title'])}</title><link>{BASE_URL}/</link></image>
    <itunes:type>serial</itunes:type>
    <itunes:block>Yes</itunes:block>
    <itunes:explicit>false</itunes:explicit>
    <itunes:category text="Education"/>
{chr(10).join(reversed(items))}
  </channel>
</rss>
"""
    (site / f"{series['slug']}.xml").write_text(xml)
    print(f"{site / (series['slug'] + '.xml')}  episodes={len(items)}")


def opml_and_index(site):
    outlines = "\n".join(
        f'    <outline type="rss" text={quoteattr(s["title"])} title={quoteattr(s["title"])}'
        f' xmlUrl="{BASE_URL}/{s["slug"]}.xml" htmlUrl="{BASE_URL}/"/>' for s in LIVE)
    (site / "podcasts.opml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="opml.xsl"?>
<opml version="2.0">
  <head>
    <title>Pass the Architect</title>
  </head>
  <body>
{outlines}
  </body>
</opml>
""")
    rows = "\n".join(
        f'<li><strong>{escape(s["title"])}</strong><br><a href="{s["slug"]}.xml">{BASE_URL}/{s["slug"]}.xml</a></li>'
        for s in LIVE)
    (site / "index.html").write_text(f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>Pass the Architect</title>
<style>body{{font-family:system-ui,sans-serif;max-width:40rem;margin:2rem auto;padding:0 1rem;line-height:1.5}}li{{margin:1rem 0}}</style>
</head><body><h1>Pass the Architect</h1>
<p>Private study podcasts. Add a feed URL to a podcast app (Apple Podcasts: Library, then Follow a Show by URL), or import <a href="podcasts.opml">podcasts.opml</a> for both.</p>
<ul>
{rows}
</ul></body></html>
""")
    (site / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    # Browsers render the feeds and the OPML through these stylesheets; podcast apps ignore them.
    for xsl in ("feed.xsl", "opml.xsl"):
        shutil.copyfile(pathlib.Path(__file__).with_name(xsl), site / xsl)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--icloud", action="store_true")
    ap.add_argument("--github", action="store_true")
    ap.add_argument("--site", type=pathlib.Path)
    args = ap.parse_args()
    if args.github and not args.site:
        ap.error("--github needs --site")
    for series in LIVE:
        staged = stage(series)
        if args.icloud:
            to_icloud(series, staged)
        if args.github:
            to_release(series, staged)
        if args.site:
            feed(series, staged, args.site)
    if args.site:
        opml_and_index(args.site)
        for series in SERIES:
            if series.get("draft"):
                cover(series, args.site)


if __name__ == "__main__":
    main()
