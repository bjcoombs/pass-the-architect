"""Chapter artwork: square JPEG cards for segments, questions, answers and recall prompts.

Used by render.py. A question card shows the stem and options so a listener who pauses
can answer from the screen; the answer card that replaces it marks the correct options.
"""
import io

from PIL import Image, ImageDraw, ImageFont

SIZE = 1400
MARGIN = 90
# Arial, not Helvetica: Helvetica has no arrow glyph, which the recap bullets use.
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
BG = (24, 32, 48)
TEXT = (240, 242, 245)
MUTED = (140, 150, 168)
ACCENT = {"segment": (88, 150, 230), "question": (240, 176, 64), "answer": (72, 190, 120), "recall": (170, 120, 230)}
RIGHT_FILL = (40, 110, 70)
WRONG_TEXT = (110, 118, 134)


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


def wrap(text, fnt, width):
    """Greedy wrap by measured pixel width."""
    words, lines, line = text.split(), [], ""
    for w in words:
        trial = f"{line} {w}".strip()
        if fnt.getlength(trial) <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def header(draw, kind, kicker, episode):
    draw.rectangle([0, 0, SIZE, 18], fill=ACCENT[kind])
    draw.text((MARGIN, 60), episode.upper(), font=font(30, True), fill=MUTED)
    draw.text((MARGIN, 105), kicker, font=font(46, True), fill=ACCENT[kind])
    return 190


def encode(img):
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=85, optimize=True)
    return buf.getvalue()


def segment(title, episode, bullets=None):
    """Title card; with bullets, the chapter's points under the title, shrunk until they fit."""
    width = SIZE - 2 * MARGIN
    if not bullets:
        img = Image.new("RGB", (SIZE, SIZE), BG)
        d = ImageDraw.Draw(img)
        header(d, "segment", "PASS THE ARCHITECT", episode)
        f = font(96, True)
        lines = wrap(title, f, width)
        y = (SIZE - len(lines) * 116) // 2
        for line in lines:
            d.text((MARGIN, y), line, font=f, fill=TEXT)
            y += 116
        return encode(img)
    for size in range(52, 23, -2):
        img = Image.new("RGB", (SIZE, SIZE), BG)
        d = ImageDraw.Draw(img)
        y = header(d, "segment", "PASS THE ARCHITECT", episode)
        title_font = font(size + 22, True)
        for line in wrap(title, title_font, width):
            d.text((MARGIN, y), line, font=title_font, fill=TEXT)
            y += int((size + 22) * 1.2)
        y += size
        body = font(size)
        for b in bullets:
            lines = wrap(b, body, width - 60)
            d.ellipse([MARGIN, y + size * 0.38, MARGIN + size * 0.36, y + size * 0.74], fill=ACCENT["segment"])
            for line in lines:
                d.text((MARGIN + 60, y), line, font=body, fill=TEXT)
                y += int(size * 1.22)
            y += int(size * 0.55)
        if y <= SIZE - 60:
            break
    return encode(img)


def _qa(drill, episode, number, reveal):
    """Lay out stem and options, shrinking the type until everything fits."""
    kind = "answer" if reveal else "question"
    choose = "Choose two" if drill.get("choose") == 2 else "Choose one"
    kicker = f"{'ANSWER' if reveal else 'QUESTION'} {number}  ·  {drill.get('label', 'Drill')}  ·  {choose}"
    width = SIZE - 2 * MARGIN
    for size in range(50, 21, -2):
        img = Image.new("RGB", (SIZE, SIZE), BG)
        d = ImageDraw.Draw(img)
        y = header(d, kind, kicker, episode)
        if drill.get("scenario"):
            d.text((MARGIN, y), drill["scenario"], font=font(size - 6), fill=MUTED)
            y += int(size * 1.3)
        stem_font, opt_font = font(size, True), font(size - 4)
        for line in wrap(drill["stem"], stem_font, width):
            d.text((MARGIN, y), line, font=stem_font, fill=TEXT)
            y += int(size * 1.22)
        y += size // 2
        for letter, text in drill["options"].items():
            right = letter in drill["correct"]
            lines = wrap(text, opt_font, width - 110)
            h = len(lines) * int(size * 1.18) + 24
            if reveal and right:
                d.rounded_rectangle([MARGIN - 16, y - 10, SIZE - MARGIN + 16, y + h - 14], 14, fill=RIGHT_FILL)
            colour = TEXT if (not reveal or right) else WRONG_TEXT
            d.text((MARGIN, y), letter, font=font(size, True), fill=ACCENT[kind] if not reveal or right else WRONG_TEXT)
            for i, line in enumerate(lines):
                d.text((MARGIN + 80, y + i * int(size * 1.18)), line, font=opt_font, fill=colour)
            y += h + 10
        if reveal and drill.get("why"):
            y += 10
            for line in wrap(drill["why"], font(size - 6), width):
                d.text((MARGIN, y), line, font=font(size - 6), fill=MUTED)
                y += int((size - 6) * 1.2)
        if y <= SIZE - 60:
            return encode(img)
    return encode(img)


def question(drill, episode, number):
    return _qa(drill, episode, number, reveal=False)


def answer(drill, episode, number):
    return _qa(drill, episode, number, reveal=True)


def recall(drill, episode, number, reveal):
    img = Image.new("RGB", (SIZE, SIZE), BG)
    d = ImageDraw.Draw(img)
    y = header(d, "answer" if reveal else "recall", f"{'ANSWER' if reveal else 'PAUSE AND ANSWER'} {number}", episode)
    width = SIZE - 2 * MARGIN
    for size in range(64, 23, -2):
        lines = wrap(drill["prompt"], font(size, True), width)
        extra = wrap(drill.get("answer", ""), font(size - 6), width) if reveal else []
        if (len(lines) * 1.25 * size + len(extra) * 1.2 * (size - 6) + size) < SIZE - y - 80:
            break
    y += 40
    for line in lines:
        d.text((MARGIN, y), line, font=font(size, True), fill=TEXT)
        y += int(size * 1.25)
    y += size
    for line in extra:
        d.text((MARGIN, y), line, font=font(size - 6), fill=ACCENT["answer"])
        y += int((size - 6) * 1.2)
    return encode(img)
