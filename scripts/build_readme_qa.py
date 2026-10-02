#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; QA=ROOT/"qa-readme"; QA.mkdir(exist_ok=True)
A=[("Hero","hero.svg","hero-mobile.svg"),("Official lineage","official-lineage.svg","official-lineage-mobile.svg"),("Artifact boundary","artifact-boundary.svg","artifact-boundary-mobile.svg")]
def html(mobile=False):
    w="390px" if mobile else "min(1600px, calc(100vw - 64px))"
    cards="".join(f'<section><b>{n}</b><picture><source media="(max-width:640px)" srcset="../docs/assets/readme/{m}"><img src="../docs/assets/readme/{d}"></picture></section>' for n,d,m in A)
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>*{{box-sizing:border-box}}body{{margin:0;background:#E8EDF4;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}main{{width:{w};margin:auto;padding:28px 0 60px;display:grid;gap:20px}}section{{background:white;padding:12px;border:1px solid #CBD5E1;border-radius:18px;overflow:hidden}}b{{display:block;color:#64748B;font-size:12px;letter-spacing:.08em;margin-bottom:10px}}img{{display:block;width:100%;height:auto;border-radius:12px}}</style></head><body><main>{cards}</main></body></html>'''
(QA/"desktop.html").write_text(html(False),encoding="utf-8")
(QA/"mobile.html").write_text(html(True),encoding="utf-8")
print("PSP README QA pages generated")
