import re
import os

# 새 푸터 CSS (시스템 영문 폰트, 화이트 배경, 이미지 디자인 그대로)
FOOTER_CSS = """
        /* ===== 통일 푸터 ===== */
        .site-footer {
            background-color: #fff;
            color: #000;
            padding: 60px 8% 0;
            overflow: hidden;
            font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;
        }

        .footer-tagline {
            font-size: 1rem;
            font-weight: 700;
            margin: 0 0 8px 0;
            line-height: 1.4;
            color: #000;
        }

        .footer-contact {
            font-size: 0.95rem;
            font-weight: 400;
            margin: 0 0 32px 0;
            line-height: 1.7;
            color: #000;
        }

        .footer-copy {
            font-size: 0.72rem;
            color: #888;
            margin: 0 0 20px 0;
            font-weight: 400;
        }

        .footer-name {
            display: block;
            font-size: 17vw;
            font-weight: 900;
            line-height: 0.88;
            letter-spacing: -0.02em;
            color: #000;
            font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;
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

    # 1) 기존 footer {} 단독 CSS 블록 제거 (다크 배경 등 구 스타일)
    content = re.sub(
        r'\s*/\*\s*[푸터footer].*?\*/\s*footer\s*\{[^}]*\}',
        '', content, flags=re.DOTALL
    )
    # footer { ... } 블록 직접 제거 (class 없는 것)
    content = re.sub(r'\n\s*footer\s*\{[^}]*\}', '', content)

    # btn-list 스타일도 제거 (구 푸터 내 버튼)
    content = re.sub(r'\n\s*\.btn-list\s*\{[^}]*\}', '', content)
    content = re.sub(r'\n\s*\.btn-list:hover\s*\{[^}]*\}', '', content)

    # 기존 site-footer 관련 CSS 제거 (이전에 잘못 삽입된 것)
    content = re.sub(
        r'/\* ===== 통일 푸터 =====.*?\.footer-name \{[^}]*\}',
        '', content, flags=re.DOTALL
    )

    # 2) </style> 직전에 새 CSS 삽입
    content = content.replace("</style>", FOOTER_CSS + "        </style>", 1)

    # 3) 기존 footer 태그 전체 교체
    content = re.sub(r'<footer[\s\S]*?</footer>', FOOTER_HTML, content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {fname}")

print("\n모든 파일 푸터 업데이트 완료!")
