#!/usr/bin/env python3
from __future__ import annotations
import re, sys
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
README=ROOT/"README.md"
ASSETS=ROOT/"docs"/"assets"/"readme"
REQUIRED={"hero.svg","hero-mobile.svg","official-lineage.svg","official-lineage-mobile.svg","artifact-boundary.svg","artifact-boundary-mobile.svg"}
GRID=16.0

def fail(m): raise AssertionError(m)
def num(v,where):
    if v is None: fail(f"missing {where}")
    return float(v)
def q(v): return abs(v/GRID-round(v/GRID))<1e-9

def validate_readme():
    text=README.read_text(encoding="utf-8"); lower=text.lower()
    for s in ("0.74232","0.74231","official project","not a clinical diagnostic","public_notebook_sanitization.md","manifest.md"):
        if s.lower() not in lower: fail(f"README canonical fact missing: {s}")
    for s in ("thisisstress","forest-green","production model","production adopted"):
        if s in lower: fail(f"cross-project or ambiguous term: {s}")
    refs=set(re.findall(r"docs/assets/readme/([A-Za-z0-9._-]+\.svg)",text))
    if refs!=REQUIRED: fail(f"README asset refs mismatch: {sorted(refs)}")
    if text.count("<picture>")!=3 or text.count("max-width: 640px")!=3: fail("responsive picture contract failed")
    order=["## Start Here","## Official Result","## Research System","## Artifact & Reproducibility Boundary","## Current Execution Surface","## Repository Guide","## Related Research","## Public Data Boundary"]
    p=[text.find(x) for x in order]
    if any(x<0 for x in p) or p!=sorted(p): fail("README reading order failed")

def validate_svg(path):
    raw=path.read_text(encoding="utf-8")
    if "system-ui" not in raw: fail(f"{path.name}: system-ui missing")
    if re.search(r"[\uac00-\ud7a3]",raw): fail(f"{path.name}: Hangul in SVG may render as fallback boxes")
    if re.search(r"Arial|Times New Roman",raw,re.I): fail(f"{path.name}: forbidden explicit fallback font")
    try: root=ET.fromstring(raw)
    except ET.ParseError as e: raise AssertionError(f"{path.name}: XML parse error {e}") from e
    expected=800 if path.name.endswith("-mobile.svg") else 1600
    vb=root.attrib.get("viewBox","").split()
    if len(vb)!=4 or vb[:2]!=["0","0"] or float(vb[2])!=expected or root.attrib.get("width")!=str(expected): fail(f"{path.name}: viewBox/width contract")
    ns={"svg":"http://www.w3.org/2000/svg"}
    if root.find("svg:title",ns) is None or root.find("svg:desc",ns) is None: fail(f"{path.name}: title/desc missing")
    for g in root.findall(".//svg:g[@data-title='true']",ns):
        t=g.findall("svg:text",ns)
        if len(t)!=1 or not t[0].findall("svg:tspan",ns): fail(f"{path.name}: title text+tspan contract")
    for g in root.findall(".//svg:g[@data-grid='16']",ns):
        for r in g.findall("svg:rect",ns):
            for a in ("x","y","width","height"):
                v=num(r.attrib.get(a),f"{path.name}:{a}")
                if not q(v): fail(f"{path.name}: non-quantized {a}={v}")
    if path.name.endswith("-mobile.svg"):
        sizes=[float(x) for x in re.findall(r'font-size="([0-9.]+)"',raw)]
        if sizes and min(sizes)<22: fail(f"{path.name}: mobile font <22")
    anim=len(root.findall(".//svg:animate",ns))+len(root.findall(".//svg:animateTransform",ns))
    if path.name=="hero.svg" and anim<2: fail("hero motion missing")
    if path.name!="hero.svg" and anim>1: fail(f"{path.name}: motion budget exceeded")

def main():
    actual={p.name for p in ASSETS.glob("*.svg")}
    if actual!=REQUIRED: fail(f"asset set mismatch: {sorted(actual)}")
    validate_readme()
    for p in sorted(ASSETS.glob("*.svg")): validate_svg(p)
    print("PSP README visual validator: PASS")
    print("responsive assets: 3 desktop + 3 mobile")
    return 0

if __name__=="__main__":
    try: raise SystemExit(main())
    except AssertionError as e:
        print(f"PSP README visual validator: FAIL — {e}",file=sys.stderr); raise SystemExit(1)
