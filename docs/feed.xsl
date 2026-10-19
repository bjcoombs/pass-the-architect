<?xml version="1.0" encoding="UTF-8"?>
<!-- Renders a podcast feed as a web page when opened in a browser. Podcast apps ignore it. -->
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
    xmlns:podcast="https://podcastindex.org/namespace/1.0"
    xmlns:atom="http://www.w3.org/2005/Atom"
    exclude-result-prefixes="itunes podcast atom">
  <xsl:output method="html" encoding="UTF-8" doctype-system="about:legacy-compat"/>

  <xsl:template match="/rss/channel">
    <xsl:variable name="feed" select="atom:link[@rel='self']/@href"/>
    <html lang="en-GB">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <meta name="robots" content="noindex"/>
        <title><xsl:value-of select="title"/></title>
        <style>
          :root { --bg: #f7f7f5; --fg: #1d2330; --muted: #5d6675; --card: #ffffff; --line: #e2e4e8; --accent: #2f6fd6; }
          @media (prefers-color-scheme: dark) {
            :root { --bg: #141a26; --fg: #eef0f3; --muted: #9aa3b2; --card: #1c2433; --line: #2b3546; --accent: #6ea2f0; }
          }
          * { box-sizing: border-box; }
          body { margin: 0; background: var(--bg); color: var(--fg); font: 16px/1.5 system-ui, -apple-system, sans-serif; }
          main { max-width: 46rem; margin: 0 auto; padding: 2rem 16px 4rem; }
          header { display: flex; gap: 1.25rem; align-items: center; margin-bottom: 1.5rem; }
          header img { width: 120px; height: 120px; border-radius: 12px; flex: none; }
          h1 { font-size: 1.6rem; line-height: 1.2; margin: 0 0 .4rem; }
          p { margin: .4rem 0; }
          .muted { color: var(--muted); }
          .subscribe { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 1rem; margin-bottom: 1.5rem; }
          code { display: block; overflow-wrap: anywhere; font-size: .9rem; margin-top: .4rem; }
          ol { list-style: none; padding: 0; margin: 0; }
          li { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 1rem; margin-bottom: .75rem; }
          h2 { font-size: 1.05rem; margin: 0 0 .25rem; }
          audio { width: 100%; margin-top: .6rem; }
          a { color: var(--accent); }
          @media (max-width: 480px) { header { flex-direction: column; align-items: flex-start; } }
        </style>
      </head>
      <body>
        <main>
          <header>
            <img src="{itunes:image/@href}" alt=""/>
            <div>
              <h1><xsl:value-of select="title"/></h1>
              <p class="muted"><xsl:value-of select="description"/></p>
            </div>
          </header>
          <div class="subscribe">
            <strong>This is a podcast feed.</strong> Copy the address into a podcast app to subscribe
            (Apple Podcasts: Library, then Follow a Show by URL).
            <code><xsl:value-of select="$feed"/></code>
          </div>
          <ol>
            <!-- The feed lists newest first; show listening order. -->
            <xsl:for-each select="item">
              <xsl:sort select="position()" data-type="number" order="descending"/>
              <li>
                <h2><xsl:value-of select="title"/></h2>
                <p class="muted"><xsl:value-of select="itunes:duration"/></p>
                <p><xsl:value-of select="description"/></p>
                <audio controls="controls" preload="none" src="{enclosure/@url}"/>
              </li>
            </xsl:for-each>
          </ol>
        </main>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
