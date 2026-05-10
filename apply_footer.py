import re
import os

# 새 푸터 CSS
FOOTER_CSS = """
        /* ===== 통일 푸터 ===== */
        .site-footer {
            background-color: #fff;
            border-top: 1px solid #e0e0e0;
            padding: 60px 8% 0;
            color: #000;
            overflow: hidden;
            font-family: 'LCT-Ciburial-Regular', 'Pretendard', sans-serif;
        }

        .footer-tagline {
            font-size: 1rem;
            font-weight: 700;
            margin: 0 0 12px 0;
            color: #000;
        }

        .footer-contact {
            font-size: 0.95rem;
            margin: 0 0 30px 0;
            line-height: 1.7;
            color: #000;
            font-weight: 400;
        }

        .footer-copy {
            font-size: 0.75rem;
            color: #888;
            margin: 0 0 30px 0;
        }

        .footer-name {
            font-size: 17vw;
            font-weight: 900;
            line-height: 0.85;
            letter-spacing: -0.01em;
            color: #000;
            display: block;
        }
"""

# 새 푸터 HTML
FOOTER_HTML = """    <footer class="site-footer">
        <p class="footer-tagline">Visual storytelling for Brand</p>
        <p class="footer-contact">koooong745@gmail.com<br>+01 4930 1082</p>
        <p class="footer-copy">©seindesign 2026. All rights reserved</p>
        <span class="footer-name">KIM SE IN</span>
    </footer>"""

files = [
    "Hope detail.html",
    "Inbody detail.html",
    "index.html",
    "PHYTONUTRI detail.html",
    "Punggi detail.html",
    "SIDE ENOUGH detail.html",
    "Shamp's detail.html",
]

base = "/Users/sekong/design portfolio"

for fname in files:
    path = os.path.join(base, fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1) 기존 footer 태그 전체 교체
    content = re.sub(r'<footer[\s\S]*?</footer>', FOOTER_HTML, content)

    # 2) </style> 직전에 새 CSS 삽입 (이미 있으면 중복 방지)
    if "site-footer" not in content:
        content = content.replace("</style>", FOOTER_CSS + "        </style>")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {fname}")

print("\n모든 파일 푸터 업데이트 완료!")
