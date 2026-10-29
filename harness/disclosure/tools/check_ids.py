#!/usr/bin/env python3
"""Validate Disclosure claim IDs and manuscript citations."""
import re,sys,pathlib,argparse
ap=argparse.ArgumentParser();ap.add_argument("--history",default="history");ap.add_argument("--manuscript")
a=ap.parse_args();h=pathlib.Path(a.history);ok=True;ids=set()
for f,p in [("TIMELINE.md","T"),("MODERN_CASES_FACTS.md","MC"),("ANCIENT_LORE.md","A"),("ARYAN_OCCULT.md","AO"),("MYTH_CROSSREF.md","MX")]:
    fp=h/f
    if not fp.exists(): print(f"missing {f}"); continue
    found=re.findall(r'\[('+p+r'-\d{3})\]',fp.read_text())
    heads=re.findall(r'^(?:#{2,3} (?:\d+\. )?|- )\[('+p+r'-\d{3})\]',fp.read_text(),re.M)
    d={i for i in heads if heads.count(i)>1}
    if d: ok=False;print(f"DUPLICATE in {f}: {sorted(d)}")
    s=set(found)&set(re.findall(p+r'-\d{3}',fp.read_text())); ids|=set(found)
    n=max((int(i.split('-')[1]) for i in found if i.startswith(p+'-')),default=0); print(f"{f}: next free {p}-{n+1:03d}")
if a.manuscript:
    for md in pathlib.Path(a.manuscript).rglob("*.md"):
        for c in re.findall(r'\[\^((?:T|MC|AO|MX)-\d{3})\]',md.read_text()):
            if c not in ids: ok=False;print(f"UNRESOLVED {c} in {md}")
sys.exit(0 if ok else 1)
