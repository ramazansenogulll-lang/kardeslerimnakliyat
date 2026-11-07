"""Tüm siteyi üretir:  python _tools/build.py

Ayarlar (telefon, görseller): _tools/config.py
Metinler: _tools/content_main.py ve _tools/content_ilce.py
Tasarım: assets/css/style.css (küçültülüp her sayfaya gömülür)
"""
import html
import json
import os
import re
import sys
import urllib.parse
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C  # noqa: E402
from content_main import PAGES, SERVICES, STEPS  # noqa: E402
from content_ilce import ILCELER  # noqa: E402
from content_sss import SSS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()
U = C.SITE_URL.rstrip("/")

PHONE_DIGITS = re.sub(r"\D", "", C.PHONE)
TEL = "+90" + PHONE_DIGITS.lstrip("0")
WA_DIGITS = re.sub(r"\D", "", C.WHATSAPP or C.PHONE)
WA_NUM = "90" + WA_DIGITS.lstrip("0")
WA_URL = "https://wa.me/" + WA_NUM + "?text=" + urllib.parse.quote("Merhaba, taşınma için fiyat almak istiyorum. Eşyalarımın fotoğraflarını gönderiyorum.\nNereden: …\nNereye: …")
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(C.MAPS_QUERY)
ADDR_LINE = f'{C.ADDRESS["street"]}, {C.ADDRESS["postal"]} {C.ADDRESS["district"]}/{C.ADDRESS["city"]}'

ICON = {
    "phone": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.7-1.2 2.2 2.2 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/></svg>',
}
SVC_ICON = {
    "ev": '<svg viewBox="0 0 24 24" fill="none" stroke="#d95f0e" stroke-width="2" stroke-linejoin="round"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>',
    "yol": '<svg viewBox="0 0 24 24" fill="none" stroke="#d95f0e" stroke-width="2" stroke-linejoin="round"><path d="M1 6h13v10H1zM14 10h4l4 4v2h-8z"/><circle cx="5" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
    "ofis": '<svg viewBox="0 0 24 24" fill="none" stroke="#d95f0e" stroke-width="2" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="1"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M10 21v-4h4v4"/></svg>',
    "asansor": '<svg viewBox="0 0 24 24" fill="none" stroke="#d95f0e" stroke-width="2" stroke-linejoin="round"><path d="M4 21L14 3M7 21l10-18"/><path d="M15 9h6v6h-6z"/></svg>',
    "depo": '<svg viewBox="0 0 24 24" fill="none" stroke="#d95f0e" stroke-width="2" stroke-linejoin="round"><path d="M3 9l9-5 9 5v12H3z"/><path d="M7 21v-8h10v8M7 17h10"/></svg>',
    "montaj": '<svg viewBox="0 0 24 24" fill="none" stroke="#d95f0e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.5-.5-.5-2.5z"/></svg>',
    "parca": '<svg viewBox="0 0 24 24" fill="none" stroke="#d95f0e" stroke-width="2" stroke-linejoin="round"><path d="M3 7l9-4 9 4-9 4zM3 7v10l9 4 9-4V7M12 11v10"/></svg>',
}
LOGO = ('<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="12" fill="#12315a"/>'
        '<path d="M8 17h20v14H8z" fill="#f2711c"/><path d="M28 21h7l5 5v5H28z" fill="#fff"/>'
        '<circle cx="14" cy="33" r="3.5" fill="#fff" stroke="#12315a" stroke-width="2"/>'
        '<circle cx="34" cy="33" r="3.5" fill="#fff" stroke="#12315a" stroke-width="2"/></svg>')

# Yer tutucu illüstrasyon (fotoğraf gelene kadar)
PLACEHOLDER = (
    '<svg class="ph" viewBox="0 0 400 300" role="img" aria-label="{alt}">'
    '<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a5a92"/><stop offset="1" stop-color="#1b3f6e"/></linearGradient></defs>'
    '<rect width="400" height="300" fill="url(#sky)"/>'
    '<path d="M0 205 L70 150 L130 185 L210 120 L300 175 L400 130 V300 H0Z" fill="#17375f"/>'
    '<rect x="0" y="232" width="400" height="68" fill="#0f2a4a"/>'
    '<path d="M0 262h400" stroke="#ffb27a" stroke-width="3" stroke-dasharray="22 18"/>'
    '<g transform="translate(70 128)"><rect x="0" y="0" width="160" height="92" rx="6" fill="#fff"/>'
    '<rect x="0" y="0" width="160" height="18" rx="6" fill="#f2711c"/>'
    '<text x="80" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="17" fill="#12315a">KARDEŞLERİM</text>'
    '<text x="80" y="77" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#5b6775">NAKLİYAT</text>'
    '<path d="M160 28h44l26 30v34h-70z" fill="#f2711c"/><path d="M170 36h30l18 22h-48z" fill="#cfe1f5"/>'
    '<circle cx="38" cy="98" r="15" fill="#1d2733"/><circle cx="38" cy="98" r="6" fill="#cfd9e6"/>'
    '<circle cx="190" cy="98" r="15" fill="#1d2733"/><circle cx="190" cy="98" r="6" fill="#cfd9e6"/></g>'
    '<g transform="translate(18 0)"><g fill="#d9a066" stroke="#8a5a2b" stroke-width="2"><rect x="292" y="186" width="44" height="40"/><rect x="300" y="152" width="34" height="34"/><rect x="336" y="198" width="32" height="28"/></g>'
    '<path d="M292 206h44M317 152v34" stroke="#8a5a2b" stroke-width="2"/></g></svg>'
)


def esc(s):
    return html.escape(s, quote=True)


def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};:,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()


CSS = minify_css(open(os.path.join(ROOT, "assets", "css", "style.css"), encoding="utf-8").read())


def inline_md(s):
    s = esc(s).replace("&#x27;", "'")
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
    return s


def md(text):
    """Basit işaretleme: '## ' başlık, '- ' liste, boş satır paragraf, [metin](/yol/) link, **kalın**."""
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [ln.strip() for ln in block.strip().splitlines()]
        if lines[0].startswith("## "):
            out.append(f'<h2 id="{slugify(lines[0][3:])}">{inline_md(lines[0][3:])}</h2>')
            lines = lines[1:]
            if not lines:
                continue
        if all(ln.startswith("- ") for ln in lines):
            out.append("<ul>" + "".join(f"<li>{inline_md(ln[2:])}</li>" for ln in lines) + "</ul>")
        else:
            out.append("<p>" + inline_md(" ".join(lines)) + "</p>")
    return "\n".join(out)


def slugify(s):
    tr = str.maketrans("çğıöşüÇĞİÖŞÜâ", "cgiosuCGIOSUa")
    s = s.translate(tr).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def words(text):
    return len(re.findall(r"\w+", re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)))


def media(key, alt):
    path = C.IMAGES.get(key) or (C.IMAGES.get("ilce") if key.startswith("ilce-") else "")
    if path:
        return (f'<div class="media"><img src="{esc(path)}" alt="{esc(alt)}" width="800" height="600" '
                f'fetchpriority="high" decoding="async"></div>')
    return f'<div class="media">{PLACEHOLDER.format(alt=esc(alt))}</div>'


def btn_call(cls="btn btn-call", label=None):
    return f'<a class="{cls}" href="tel:{TEL}">{ICON["phone"]}<span>{esc(label or C.PHONE)}</span></a>'


def btn_wa(cls="btn btn-wa", label="WhatsApp'tan Fiyat Al"):
    return f'<a class="{cls}" href="{esc(WA_URL)}" target="_blank" rel="noopener">{ICON["wa"]}<span>{label}</span></a>'


NAV = [("/", "Ana Sayfa"), ("/hizmetler/", "Hizmetler"), ("/#bolgeler", "Hizmet Bölgeleri"),
       ("/hakkimizda/", "Hakkımızda"), ("/iletisim/", "İletişim")]


def header(path):
    def cur(href):
        return ' aria-current="page"' if href == path else ""
    items = "".join(f'<li><a href="{h}"{cur(h)}>{t}</a></li>' for h, t in NAV)
    desk = "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in NAV)
    return f"""<a class="skip" href="#icerik">İçeriğe geç</a>
<div class="top"><div class="wrap"><span class="addr">{esc(C.ADDRESS["district"])} / {esc(C.ADDRESS["city"])} · Sakarya'nın 16 ilçesine taşımacılık</span><a href="tel:{TEL}">☎ {esc(C.PHONE)}</a></div></div>
<header class="site"><div class="wrap">
<a class="logo" href="/">{LOGO}<span>Kardeşlerim<small>NAKLİYAT · SAKARYA</small></span></a>
<nav class="main" aria-label="Ana menü"><details><summary>Menü</summary><ul>{items}</ul></details>
<div class="desk">{desk}{btn_call("btn btn-call", "Hemen Ara")}</div></nav>
</div></header>"""


def footer():
    ilce = "".join(f'<li><a href="/{d["slug"]}/">{esc(d["name"])} nakliyat</a></li>' for d in ILCELER)
    svc = "".join(f'<li><a href="/hizmetler/#{s["id"]}">{esc(s["name"])}</a></li>' for s in SERVICES)
    return f"""<footer class="site"><div class="wrap"><div class="cols">
<div><h3>{esc(C.NAME)}</h3><address class="nap">{esc(ADDR_LINE)}<br><a href="tel:{TEL}">{esc(C.PHONE)}</a><br><a href="{esc(MAPS_URL)}" target="_blank" rel="noopener">Haritada aç</a></address>
<h3 style="margin-top:18px">Hizmetler</h3><ul style="columns:1">{svc}</ul></div>
<div style="grid-column:span 1"><h3>Hizmet bölgeleri</h3><ul>{ilce}</ul></div>
<div><h3>Kurumsal</h3><ul style="columns:1"><li><a href="/hakkimizda/">Hakkımızda</a></li><li><a href="/hizmetler/">Hizmetler</a></li><li><a href="/iletisim/">İletişim</a></li></ul></div>
</div><div class="copy">© {date.today().year} {esc(C.NAME)} · Serdivan, Sakarya</div></div></footer>
<div class="fab">{btn_call("f-call", "Ara")}{btn_wa("f-wa", "Fotoğrafla Fiyat Al")}</div>"""


def business_schema():
    return {
        "@type": "MovingCompany",
        "@id": U + "/#firma",
        "name": C.NAME,
        "url": U + "/",
        "telephone": TEL,
        "image": U + C.OG_IMAGE,
        "logo": U + "/assets/img/logo.png",
        "address": {"@type": "PostalAddress", "streetAddress": C.ADDRESS["street"],
                    "postalCode": C.ADDRESS["postal"], "addressLocality": C.ADDRESS["district"],
                    "addressRegion": C.ADDRESS["city"], "addressCountry": "TR"},
        "hasMap": MAPS_URL,
        "areaServed": [{"@type": "AdministrativeArea", "name": f'{d["name"]}, Sakarya'} for d in ILCELER],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"]}} for s in SERVICES],
    }


def breadcrumb(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": U + p} for i, (n, p) in enumerate(items)]}


def page(path, title, desc, body, schema, og_type="website"):
    url = U + path
    ld = json.dumps({"@context": "https://schema.org", "@graph": schema}, ensure_ascii=False, separators=(",", ":"))
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="TR-54">
<meta name="geo.placename" content="Serdivan, Sakarya">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="{esc(C.NAME)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{U}{C.OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#12315a">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<style>{CSS}</style>
<script type="application/ld+json">{ld}</script>
</head>
<body>
{header(path)}
<main id="icerik">
{body}
</main>
{footer()}
</body>
</html>
"""


def hero(h1, lead, img_key, alt, crumbs=None):
    cr = ""
    if crumbs:
        cr = '<p class="crumbs">' + " › ".join(
            f'<a href="{p}">{esc(n)}</a>' if p else esc(n) for n, p in crumbs) + "</p>"
    return f"""<section class="hero"><div class="wrap">
<div>{cr}<h1>{h1}</h1><p class="lead">{esc(lead)}</p>
<div class="btns">{btn_call()}{btn_wa()}</div></div>
{media(img_key, alt)}
</div></section>"""


def wa_flow(place=""):
    """WhatsApp'tan fotoğrafla fiyat alma çağrısı (ana sayfa, ilçe ve iletişim sayfaları)."""
    return f"""<section class="wa-sec"><div class="wrap"><div class="wa-flow">
<div><h2>Eşyalarınızın fotoğrafını WhatsApp'tan gönderin, fiyatı hemen söyleyelim</h2>
<p>Keşif beklemeden fiyat öğrenmenin en hızlı yolu bu. Odaların birkaç fotoğrafı ve iki adres yeterli.</p></div>
<ol class="wa-steps"><li><b>Fotoğraf çekin</b>Her odayı geniş açıdan, büyük eşyaları ayrıca çekin.</li>
<li><b>WhatsApp'tan gönderin</b>Nereden nereye taşınacağınızı da yazın.</li>
<li><b>Fiyatı öğrenin</b>Fiyatı söyleyelim; isterseniz ücretsiz keşfe gelelim.</li></ol>
<div class="btns">{btn_wa("btn btn-wa btn-lg", "Fotoğraf Gönder, Fiyat Al")}</div>
</div></div></section>"""


def band(title="Taşınma tarihiniz belli mi?", text="Arayın ya da WhatsApp'tan yazın; eşya listesine göre fiyatı birlikte netleştirelim."):
    return f"""<section class="band"><div class="wrap"><div><h2>{esc(title)}</h2><p>{esc(text)}</p></div>
<div class="btns">{btn_call()}{btn_wa("btn btn-wa btn-ghost")}</div></div></section>"""


def service_cards():
    return '<div class="cards">' + "".join(
        f'<a class="card" href="/hizmetler/#{s["id"]}"><div class="ic">{SVC_ICON[s["icon"]]}</div>'
        f'<h3>{esc(s["name"])}</h3><p>{esc(s["short"])}</p></a>' for s in SERVICES) + "</div>"


def area_list(current=None):
    return '<ul class="areas">' + "".join(
        f'<li><a href="/{d["slug"]}/"{" aria-current=\"page\"" if d["slug"] == current else ""}>{esc(d["name"])}</a></li>'
        for d in ILCELER) + "</ul>"


def aside(extra=""):
    svc = "".join(f'<li><a href="/hizmetler/#{s["id"]}">{esc(s["name"])}</a></li>' for s in SERVICES)
    return f"""<aside>
<div class="box cta-box"><h3>Fotoğrafla fiyat alın</h3><p>Eşyalarınızın fotoğrafını WhatsApp'tan gönderin, fiyatı hemen söyleyelim. İsterseniz ücretsiz keşfe gelelim.</p>{btn_wa()}{btn_call()}</div>
{extra}
<div class="box"><h3>Hizmetlerimiz</h3><ul>{svc}</ul></div>
</aside>"""


def write(path, content):
    full = os.path.join(ROOT, path.strip("/").replace("/", os.sep), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def build():
    report = []
    by_slug = {d["slug"]: d for d in ILCELER}
    base_schema = [business_schema(), {"@type": "WebSite", "@id": U + "/#site", "url": U + "/", "name": C.NAME, "inLanguage": "tr-TR"}]

    # Ana sayfa
    p = PAGES["home"]
    steps = "".join(f"<li><b>{esc(a)}</b>{esc(b)}</li>" for a, b in STEPS)
    body = hero(p["h1"], p["lead"], "hero", "Kardeşlerim Nakliyat taşıma kamyonu") + wa_flow() + f"""
<section><div class="wrap"><div class="sec-head"><h2>Neler yapıyoruz?</h2><p>Sakarya içinde ve Sakarya'dan Türkiye'nin her yerine taşıma yapıyoruz.</p></div>{service_cards()}</div></section>
<section class="alt"><div class="wrap"><div class="sec-head"><h2>Taşınma nasıl ilerliyor?</h2><p>İlk telefondan son koliye kadar dört adım.</p></div><ol class="steps">{steps}</ol></div></section>
<section><div class="wrap layout"><article class="prose">{md(p["body"])}</article>{aside()}</div></section>
<section class="alt" id="bolgeler"><div class="wrap"><div class="sec-head"><h2>Sakarya'da hizmet verdiğimiz ilçeler</h2><p>Serdivan'daki adresimizden çıkıp ilin 16 ilçesine de gidiyoruz. İlçenize tıklayıp o bölgeye özel bilgileri okuyabilirsiniz.</p></div>{area_list()}</div></section>
{band()}"""
    write("/", page("/", p["title"], p["desc"], body, base_schema))
    report.append(("/", words(p["body"])))

    # Hakkımızda, İletişim
    for key, path, img in (("about", "/hakkimizda/", "hakkimizda"), ("contact", "/iletisim/", "iletisim")):
        p = PAGES[key]
        extra = ""
        if key == "contact":
            extra = f"""<div class="box"><h3>Adres</h3><address class="nap"><strong>{esc(C.NAME)}</strong><br>{esc(ADDR_LINE)}<br>Telefon: <a href="tel:{TEL}">{esc(C.PHONE)}</a><br><a href="{esc(MAPS_URL)}" target="_blank" rel="noopener">Google Haritalar'da aç →</a></address></div>"""
        crumbs = [("Ana Sayfa", "/"), (p["crumb"], None)]
        body = hero(p["h1"], p["lead"], img, p["crumb"], crumbs) + (wa_flow() if key == "contact" else "") + f"""
<section><div class="wrap layout"><article class="prose">{md(p["body"])}</article>{aside(extra)}</div></section>
<section class="alt"><div class="wrap"><div class="sec-head"><h2>Hizmet bölgelerimiz</h2></div>{area_list()}</div></section>
{band()}"""
        sch = base_schema + [breadcrumb([("Ana Sayfa", "/"), (p["crumb"], path)])]
        if key == "about":
            sch.append({"@type": "AboutPage", "url": U + path, "name": p["title"], "about": {"@id": U + "/#firma"}})
        else:
            sch.append({"@type": "ContactPage", "url": U + path, "name": p["title"], "about": {"@id": U + "/#firma"}})
        write(path, page(path, p["title"], p["desc"], body, sch))
        report.append((path, words(p["body"])))

    # Hizmetler
    p = PAGES["services"]
    svc_md = p["body"] + "\n\n" + "\n\n".join(f'## {s["name"]}\n\n{s["text"]}' for s in SERVICES) + "\n\n" + p.get("outro", "")
    svc_html = md(svc_md)
    for s in SERVICES:  # başlık id'lerini kısa anchor'lara eşitle
        svc_html = svc_html.replace(f'<h2 id="{slugify(s["name"])}">', f'<h2 id="{s["id"]}">')
    body = hero(p["h1"], p["lead"], "hizmetler", "Nakliyat hizmetleri", [("Ana Sayfa", "/"), ("Hizmetler", None)]) + f"""
<section><div class="wrap layout"><article class="prose">{svc_html}</article>{aside()}</div></section>
<section class="alt"><div class="wrap"><div class="sec-head"><h2>Hangi ilçedesiniz?</h2></div>{area_list()}</div></section>
{band()}"""
    sch = base_schema + [breadcrumb([("Ana Sayfa", "/"), ("Hizmetler", "/hizmetler/")])] + [
        {"@type": "Service", "name": s["name"], "serviceType": s["name"], "provider": {"@id": U + "/#firma"},
         "areaServed": {"@type": "AdministrativeArea", "name": "Sakarya"}, "url": U + "/hizmetler/#" + s["id"]} for s in SERVICES]
    write("/hizmetler/", page("/hizmetler/", p["title"], p["desc"], body, sch))
    report.append(("/hizmetler/", words(svc_md)))

    # İlçeler
    for d in ILCELER:
        path = f'/{d["slug"]}/'
        near = "".join(f'<li><a href="/{n}/">{esc(by_slug[n]["name"])} evden eve nakliyat</a></li>' for n in d["near"])
        extra = f'<div class="box"><h3>Yakın ilçeler</h3><ul>{near}</ul></div>'
        crumbs = [("Ana Sayfa", "/"), ("Hizmet Bölgeleri", "/#bolgeler"), (d["name"], None)]
        faq = SSS[d["slug"]]
        faq_html = "".join(f'<h3>{esc(q)}</h3><p>{esc(a)}</p>' for q, a in faq)
        near_links = ", ".join(f'<a href="/{n}/">{esc(by_slug[n]["name"])}</a>' for n in d["near"])
        body = hero(d["h1"], d["lead"], "ilce-" + d["slug"], f'{d["name"]} evden eve nakliyat', crumbs) + wa_flow(d["name"]) + f"""
<section><div class="wrap layout"><article class="prose">{md(d["body"])}
<p>Komşu ilçelerde de çalışıyoruz: {near_links}.</p>
<h2 id="sss">{esc(d["name"])} taşımalarında sık sorulanlar</h2>
{faq_html}</article>{aside(extra)}</div></section>
<section class="alt"><div class="wrap"><div class="sec-head"><h2>Sakarya'nın diğer ilçeleri</h2></div>{area_list(d["slug"])}</div></section>
{band(f'{d["name"]} içinde ya da dışına mı taşınıyorsunuz?')}"""
        sch = base_schema + [
            breadcrumb([("Ana Sayfa", "/"), (d["name"] + " Nakliyat", path)]),
            {"@type": "Service", "name": f'{d["name"]} Evden Eve Nakliyat', "serviceType": "Evden eve nakliyat",
             "provider": {"@id": U + "/#firma"}, "url": U + path,
             "areaServed": {"@type": "AdministrativeArea", "name": f'{d["name"]}, Sakarya'}},
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
        ]
        write(path, page(path, d["title"], d["desc"], body, sch))
        report.append((path, words(d["body"]) + sum(words(q + " " + a) for q, a in faq)))

    # 404
    body404 = f"""<section class="hero"><div class="wrap"><div><h1>Aradığınız sayfa bulunamadı</h1><p class="lead">Adres değişmiş olabilir. Ana sayfadan devam edebilir ya da bizi doğrudan arayabilirsiniz.</p><div class="btns"><a class="btn btn-call" href="/">Ana sayfa</a>{btn_wa()}</div></div></div></section>
<section><div class="wrap">{area_list()}</div></section>"""
    html404 = page("/404.html", "Sayfa bulunamadı | " + C.NAME, "Aradığınız sayfa bulunamadı.", body404, base_schema)
    html404 = html404.replace('content="index, follow, max-image-preview:large"', 'content="noindex"')
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8", newline="\n").write(html404)

    # sitemap, robots, llms
    urls = ["/", "/hizmetler/", "/hakkimizda/", "/iletisim/"] + [f'/{d["slug"]}/' for d in ILCELER]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{U}{u}</loc><lastmod>{TODAY}</lastmod></url>")
    sm.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write("\n".join(sm) + "\n")

    robots = "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in ("GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended")) + f"Sitemap: {U}/sitemap.xml\n"
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n").write(robots)

    llms = [f"# {C.NAME}", "",
            f"> {C.NAME}, Serdivan/Sakarya merkezli bir nakliyat firmasıdır. Sakarya'nın 16 ilçesinde evden eve (şehir içi) nakliyat, paketleme, mobilya söküm-montaj, asansörlü taşıma hizmeti verir. Yerinde keşif ücretsizdir, paketleme ve malzeme taşıma fiyatına dahildir; Sakarya'dan Türkiye'nin her iline şehirler arası taşıma yapar.", "",
            f"- Telefon / WhatsApp: {C.PHONE} ({TEL})", f"- Adres: {ADDR_LINE}", f"- Web: {U}/", "",
            "## Hizmetler"] + [f"- [{s['name']}]({U}/hizmetler/#{s['id']}): {s['short']}" for s in SERVICES] + [
            "", "## Hizmet bölgeleri (Sakarya ilçeleri)"] + [f"- [{d['name']}]({U}/{d['slug']}/): {d['desc']}" for d in ILCELER] + [
            "", "## Sayfalar", f"- [Ana sayfa]({U}/)", f"- [Hizmetler]({U}/hizmetler/)", f"- [Hakkımızda]({U}/hakkimizda/)", f"- [İletişim]({U}/iletisim/)", ""]
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(llms))

    open(os.path.join(ROOT, "CNAME"), "w", encoding="utf-8", newline="\n").write("kardeslerimnakliyat.com.tr\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").close()

    # Kontroller
    titles = [p["title"] for p in PAGES.values()] + [d["title"] for d in ILCELER]
    descs = [p["desc"] for p in PAGES.values()] + [d["desc"] for d in ILCELER]
    assert len(set(titles)) == len(titles), "Tekrarlanan title var"
    assert len(set(descs)) == len(descs), "Tekrarlanan description var"
    for t in titles:
        if len(t) > 65:
            print("  ! uzun title:", len(t), t)
    for t in descs:
        if not 110 <= len(t) <= 165:
            print("  ! description uzunluğu:", len(t), t[:60])
    print("Sayfa / kelime:")
    for pth, w in report:
        print(f"  {w:4d}  {pth}")


if __name__ == "__main__":
    build()
