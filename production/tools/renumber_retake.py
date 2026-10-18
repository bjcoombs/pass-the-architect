#!/usr/bin/env python3
"""Make spoken episode numbers in the CCAR-F retake series match its listening position (00 = game plan).

Usage (from production/): python3 tools/renumber_retake.py [DIR]   (default foundations/transcripts)
Each replacement must match exactly once, so rerunning on edited files fails loudly instead of drifting.
"""
import pathlib
import sys

EDITS = {
    "F00": [
        ("This is episode F zero,", "This is episode zero,"),
        ("Episode F04 goes deeper.", "Episode two goes deeper."),
        ("alongside episodes ten and eleven?", "alongside episodes one and ten?"),
        ("score report. Ten drills your", "score report. Episode one drills your"),
        ("stem never stated. Eleven re-teaches", "stem never stated. Episode ten re-teaches"),
        ("This episode, then ten. Then F04 and F05 on Claude Code, F06 on prompts and structured output, "
         "F01 to F03 on agents, hooks and escalation, F07 on tools, F08 on context. Then eleven, which by then "
         "lands as revision, F09 on the six scenarios, and F10 the night before and the morning of.",
         "This episode, then one. Then two and three on Claude Code, four on prompts and structured output, "
         "five to seven on agents, hooks and escalation, eight on tools, nine on context. Then ten, which by then "
         "lands as revision, eleven on the six scenarios, and twelve the night before and the morning of."),
        ("Episode ten, your five miss patterns", "Episode one, your five miss patterns"),
    ],
    "F04": [
        ("This is episode F four:", "This is episode two:"),
        ("And episode eleven already did", "And episode ten already did"),
        ("Episode eleven taught me guidance", "Episode ten taught me guidance"),
        ("what episode eleven covered", "what episode ten covered"),
        ("Next, episode F05:", "Next, episode three:"),
    ],
    "F05": [
        ("This is episode F five:", "This is episode three:"),
        ("Episode F eight comes back to that.", "Episode nine comes back to that."),
        ("Next episode, F six:", "Next, episode four:"),
    ],
    "F06": [
        ("This is episode F06,", "This is episode four,"),
        ("Episode eleven made few-shot", "Episode ten made few-shot"),
        ("Episode eleven taught me: missing", "Episode ten taught me: missing"),
        ("Episode eleven covered nullable", "Episode ten covered nullable"),
        ("Next, episode F01:", "Next, episode five:"),
    ],
    "F01": [
        ("This is episode F one,", "This is episode five,"),
        ("Episode eleven said order", "Episode ten said order"),
        ("Episode eleven was money moving", "Episode ten was money moving"),
    ],
    "F02": [
        ("This is episode F two:", "This is episode six:"),
        ("Next, episode F zero three:", "Next, episode seven:"),
    ],
    "F03": [("This is episode F three:", "This is episode seven:")],
    "F07": [("This is episode F07,", "This is episode eight,")],
    "F08": [("This is episode F08,", "This is episode nine,")],
    "F09": [("This is episode F09,", "This is episode eleven,")],
    "F10": [
        ("This is episode F10,", "This is episode twelve,"),
        ("agents, F01 to F03; Claude Code, F04 and F05; prompts, F06; tools, F07; context, F08.",
         "agents, episodes five to seven; Claude Code, two and three; prompts, four; tools, eight; context, nine."),
    ],
}

folder = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "foundations/transcripts")
for ep, edits in EDITS.items():
    path = next(folder.glob(f"{ep}-*.md"))
    text = path.read_text()
    for old, new in edits:
        if text.count(old) != 1:
            sys.exit(f"{path.name}: expected one match for {old[:50]!r}, found {text.count(old)}")
        text = text.replace(old, new)
    path.write_text(text)
    print(f"{path.name}: {len(edits)} edits")
