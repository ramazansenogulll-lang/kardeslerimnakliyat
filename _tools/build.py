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
from content_main import PAGES, SERVICES, STEPS, HOME_SSS  # noqa: E402
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

def _i(d, fill=False, sw="1.8"):
    if fill:
        return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{d}</svg>'
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')


ICON = {
    "phone": _i('<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/>', True),
    "wa": _i('<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.7-1.2 2.2 2.2 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/>', True),
    "pin": _i('<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>'),
    "clock": _i('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    "check": _i('<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.5 2.5L16 9.5"/>'),
    "search": _i('<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2"/>'),
    "box": _i('<path d="M3 7.5l9-4.5 9 4.5-9 4.5z"/><path d="M3 7.5v9l9 4.5 9-4.5v-9M12 12v9"/>'),
    "tool": _i('<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.5-.5-.5-2.5z"/>'),
    "lift": _i('<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 9l3-3 3 3M9 15l3 3 3-3"/>'),
    "map": _i('<path d="M9 4L3 6.5v13L9 17l6 2.5 6-2.5v-13L15 6.5z"/><path d="M9 4v13M15 6.5v13"/>'),
}
SVC_ICON = {
    "ev": _i('<path d="M3 11l9-7 9 7"/><path d="M5 9.5V20h14V9.5"/><path d="M10 20v-5h4v5"/>'),
    "paketleme": ICON["box"],
    "montaj": ICON["tool"],
    "yol": _i('<path d="M2 6h12v10H2z"/><path d="M14 10h4l4 4v2h-8"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>'),
    "ofis": _i('<rect x="4" y="3" width="16" height="18" rx="1.5"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M10 21v-4h4v4"/>'),
    "asansor": ICON["lift"],
    "depo": _i('<path d="M3 9l9-5 9 5v12H3z"/><path d="M7 21v-8h10v8M7 17h10"/>'),
    "parca": _i('<rect x="4" y="9" width="16" height="11" rx="1.5"/><path d="M8 9V6a4 4 0 0 1 8 0v3"/>'),
}
SVC_ICON_FOR = {"paketleme": "paketleme"}
LOGO = ('<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="12" fill="#0e2236"/>'
        '<path d="M9 17h19v14H9z" fill="#c2410c"/><path d="M28 21h6.5l5 5V31H28z" fill="#fff"/>'
        '<circle cx="15" cy="33" r="3.5" fill="#fff" stroke="#0e2236" stroke-width="2"/>'
        '<circle cx="33" cy="33" r="3.5" fill="#fff" stroke="#0e2236" stroke-width="2"/></svg>')

# Fotoğraf gelene kadar kullanılan illüstrasyon (şehir silueti önünde kamyon)
PLACEHOLDER = (
    '<svg class="ph" viewBox="0 0 500 400" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{alt}">'
    '<defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22466d"/><stop offset="1" stop-color="#132c47"/></linearGradient>'
    '<linearGradient id="g2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#e6ebf1"/></linearGradient></defs>'
    '<rect width="500" height="400" fill="url(#g1)"/>'
    '<circle cx="400" cy="90" r="38" fill="#fdba74" opacity=".9"/>'
    '<g fill="#1a3a5c"><rect x="20" y="150" width="70" height="170"/><rect x="100" y="110" width="60" height="210"/><rect x="170" y="170" width="80" height="150"/><rect x="262" y="130" width="56" height="190"/><rect x="330" y="185" width="90" height="135"/><rect x="430" y="150" width="60" height="170"/></g>'
    '<g fill="#2c5682">' + "".join(f'<rect x="{x}" y="{y}" width="9" height="12" rx="1"/>' for x in (32, 52, 72, 112, 132, 274, 294, 442, 462) for y in (170, 196, 222, 248)) + '</g>'
    '<g fill="#fdba74" opacity=".75"><rect x="52" y="196" width="9" height="12" rx="1"/><rect x="132" y="170" width="9" height="12" rx="1"/><rect x="294" y="248" width="9" height="12" rx="1"/><rect x="462" y="222" width="9" height="12" rx="1"/></g>'
    '<rect x="0" y="318" width="500" height="82" fill="#0b1d30"/>'
    '<path d="M0 356h500" stroke="#3a5a7c" stroke-width="3" stroke-dasharray="26 20"/>'
    '<g transform="translate(64 214)"><rect x="0" y="0" width="210" height="112" rx="8" fill="url(#g2)"/>'
    '<rect x="0" y="0" width="210" height="10" rx="5" fill="#c2410c"/>'
    '<text x="105" y="62" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="21" letter-spacing="1" fill="#0e2236">KARDEŞLERİM</text>'
    '<text x="105" y="84" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" letter-spacing="4" fill="#5a6676">NAKLİYAT</text>'
    '<path d="M210 30h58l34 38v44h-92z" fill="#c2410c"/><path d="M222 40h40l24 28h-64z" fill="#cfe0f2"/>'
    '<rect x="296" y="96" width="10" height="8" rx="2" fill="#fdba74"/>'
    '<circle cx="50" cy="114" r="19" fill="#0b1d30"/><circle cx="50" cy="114" r="8" fill="#9fb3c8"/>'
    '<circle cx="250" cy="114" r="19" fill="#0b1d30"/><circle cx="250" cy="114" r="8" fill="#9fb3c8"/></g>'
    '<g transform="translate(390 252)"><rect x="0" y="22" width="52" height="46" rx="3" fill="#d6a46a"/><rect x="8" y="-14" width="40" height="36" rx="3" fill="#e2b47c"/><rect x="52" y="34" width="38" height="34" rx="3" fill="#c99358"/>'
    '<path d="M0 44h52M28 -14v36M52 50h38" stroke="#9c6a35" stroke-width="2"/></g></svg>'
)

BADGES = [("search", "Ücretsiz keşif"), ("box", "Paketleme fiyata dahil"),
          ("tool", "Mobilya söküm ve montaj"), ("lift", "Dış cephe asansörü")]

REASONS = [
    ("search", "Ücretsiz keşif", "Eşya çoksa ya da bina zorsa gelip yerinde bakıyoruz. Keşif için ücret almıyoruz."),
    ("box", "Paketleme fiyata dahil", "Koli, balonlu naylon, streç film ve battaniye bizden; paketlemeyi ekibimiz yapıyor."),
    ("tool", "Söküm ve montaj", "Dolap ve yatakları söküyor, yeni evde yeniden kuruyor, kapak ayarlarını yapıyoruz."),
    ("lift", "Dış cephe asansörü", "Merdivene sığmayan eşyayı pencereden indiriyor, yüksek katlarda süreyi kısaltıyoruz."),
]


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


def media(key, alt, chips=""):
    path = C.IMAGES.get(key) or (C.IMAGES.get("ilce") if key.startswith("ilce-") else "")
    if path:
        inner = (f'<img src="{esc(path)}" alt="{esc(alt)}" width="1000" height="800" '
                 f'fetchpriority="high" decoding="async">')
    else:
        inner = PLACEHOLDER.format(alt=esc(alt))
    return f'<div class="frame"><div class="media">{inner}</div>{chips}</div>'


def chip(cls, icon, title, text):
    return f'<div class="chip {cls}"><span class="ci">{ICON[icon]}</span><span><b>{esc(title)}</b>{esc(text)}</span></div>'


def btn_call(cls="btn btn-call", label=None):
    return f'<a class="{cls}" href="tel:{TEL}">{ICON["phone"]}<span>{esc(label or C.PHONE)}</span></a>'


def btn_wa(cls="btn btn-wa", label="WhatsApp'tan Fiyat Al"):
    return f'<a class="{cls}" href="{esc(WA_URL)}" target="_blank" rel="noopener">{ICON["wa"]}<span>{esc(label)}</span></a>'


NAV = [("/", "Ana Sayfa"), ("/hizmetler/", "Hizmetler"), ("/#bolgeler", "Hizmet Bölgeleri"),
       ("/hakkimizda/", "Hakkımızda"), ("/iletisim/", "İletişim")]


def hours_text():
    return " · ".join(f"{d} {h}" for d, h in C.HOURS)


def header(path):
    def cur(href):
        return ' aria-current="page"' if href == path else ""
    items = "".join(f'<li><a href="{h}"{cur(h)}>{t}</a></li>' for h, t in NAV)
    desk = "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in NAV)
    return f"""<a class="skip" href="#icerik">İçeriğe geç</a>
<div class="top"><div class="wrap"><div class="t-info"><span>{ICON["pin"]}{esc(C.ADDRESS["street"])}, {esc(C.ADDRESS["district"])}/{esc(C.ADDRESS["city"])}</span><span>{ICON["clock"]}{esc(hours_text())}</span></div><a href="tel:{TEL}">{esc(C.PHONE)}</a></div></div>
<header class="site"><div class="wrap">
<a class="logo" href="/">{LOGO}<span>Kardeşlerim<small>NAKLİYAT · SAKARYA</small></span></a>
<nav class="main" aria-label="Ana menü"><details><summary><i></i>Menü</summary><ul>{items}</ul></details>
<div class="desk">{desk}{btn_call("btn btn-call", "Hemen Ara")}</div></nav>
</div></header>"""


def footer():
    ilce = "".join(f'<li><a href="/{d["slug"]}/">{esc(d["name"])}</a></li>' for d in ILCELER)
    svc = "".join(f'<li><a href="/hizmetler/#{s["id"]}">{esc(s["name"])}</a></li>' for s in SERVICES)
    hours = "".join(f"<div><dt>{esc(d)}</dt><dd>{esc(h)}</dd></div>" for d, h in C.HOURS)
    return f"""<footer class="site"><div class="wrap"><div class="cols">
<div class="f-about"><a class="logo" href="/">{LOGO}<span>Kardeşlerim<small>NAKLİYAT · SAKARYA</small></span></a>
<p>Serdivan merkezli nakliyat firması. Sakarya'nın 16 ilçesinde evden eve, şehirler arası, ofis ve asansörlü taşıma; paketleme ve mobilya söküm-montaj.</p>
<div class="f-contact"><div>{ICON["pin"]}<span>{esc(ADDR_LINE)}<br><a href="{esc(MAPS_URL)}" target="_blank" rel="noopener">Haritada aç →</a></span></div>
<div>{ICON["phone"]}<a href="tel:{TEL}">{esc(C.PHONE)}</a></div>
<div>{ICON["wa"]}<a href="{esc(WA_URL)}" target="_blank" rel="noopener">WhatsApp'tan fotoğrafla fiyat al</a></div></div></div>
<div><h3>Hizmetler</h3><ul>{svc}</ul></div>
<div><h3>Hizmet bölgeleri</h3><ul class="f-ilce">{ilce}</ul></div>
<div><h3>Çalışma saatleri</h3><dl class="hours">{hours}</dl>
<h3 style="margin-top:26px">Kurumsal</h3><ul><li><a href="/hakkimizda/">Hakkımızda</a></li><li><a href="/hizmetler/">Hizmetler</a></li><li><a href="/iletisim/">İletişim</a></li></ul></div>
</div><div class="copy"><span>© {date.today().year} {esc(C.NAME)}. Tüm hakları saklıdır.</span><span>Serdivan, Sakarya</span></div></div></footer>
<div class="fab">{btn_call("f-call", "Ara")}{btn_wa("f-wa", "Fotoğrafla Fiyat Al")}</div>"""


def business_schema():
    sch = {
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
        **({"geo": {"@type": "GeoCoordinates", "latitude": C.GEO[0], "longitude": C.GEO[1]}}
           if getattr(C, "GEO", None) else {}),
        **({"openingHours": C.OPENING_HOURS} if getattr(C, "OPENING_HOURS", "") else {}),
        "areaServed": [{"@type": "AdministrativeArea", "name": f'{d["name"]}, Sakarya'} for d in ILCELER],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"]}} for s in SERVICES],
    }
    return sch


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
<meta name="geo.position" content="{C.GEO[0]};{C.GEO[1]}">
<meta name="ICBM" content="{C.GEO[0]}, {C.GEO[1]}">
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
<meta name="theme-color" content="#0e2236">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/jakarta-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/jakarta-latin-ext.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/inter-latin.woff2" crossorigin>
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


HIGHLIGHTS = [("Ücretsiz", "yerinde keşif"), ("Paketleme", "fiyata dahil"), ("16 ilçe", "Sakarya geneli")]

# Ana sayfadaki "taşıdığımız yerler" şeridi (içerikte geçen gerçek iş türleri)
STRIP = ["Daireler", "Müstakil evler", "Villalar", "Yazlıklar", "Öğrenci evleri", "Ofisler", "Dükkanlar"]


def badges():
    return '<ul class="hl">' + "".join(f"<li><b>{esc(a)}</b>{esc(b)}</li>" for a, b in HIGHLIGHTS) + "</ul>"


def strip():
    return '<div class="strip"><div class="wrap"><b>Taşıdığımız yerler:</b>' + "".join(f"<span>{esc(x)}</span>" for x in STRIP) + "</div></div>"


def hero(h1, lead, img_key, alt, crumbs=None, eyebrow="Serdivan merkezli · Sakarya geneli", small=False, place=None):
    cr = ""
    if crumbs:
        cr = '<p class="crumbs">' + " / ".join(
            f'<a href="{p}">{esc(n)}</a>' if p else esc(n) for n, p in crumbs) + "</p>"
    chips = chip("chip-1", "search", "Ücretsiz keşif", "Yerinde bakıp fiyat veriyoruz")
    chips += chip("chip-2", "pin" if place else "box", place or "Paketleme dahil", "Sakarya" if place else "Malzeme ve işçilik bizden")
    return f"""<section class="hero{' hero-small' if small else ''}"><div class="wrap">
<div>{cr}<span class="pill"><i></i>{esc(eyebrow)}</span><h1>{h1}</h1><p class="lead">{esc(lead)}</p>
<div class="btns">{btn_call()}{btn_wa("btn btn-out")}</div>{badges()}</div>
{media(img_key, alt, chips)}
</div></section>"""


def wa_flow():
    """WhatsApp'tan fotoğrafla fiyat alma çağrısı (ana sayfa, ilçe ve iletişim sayfaları)."""
    return f"""<section class="wa-sec"><div class="wrap"><div class="wa-flow">
<div><span class="eyebrow">Fotoğrafla fiyat</span><h2>Eşyalarınızın fotoğrafını WhatsApp'tan gönderin, fiyatı hemen söyleyelim</h2>
<p>Keşif beklemeden fiyat öğrenmenin en hızlı yolu. Odaların birkaç fotoğrafı ve iki adres yeterli.</p></div>
<ol class="wa-steps"><li><b>Fotoğraf çekin</b>Her odayı geniş açıdan, büyük eşyaları ayrıca çekin.</li>
<li><b>WhatsApp'tan gönderin</b>Nereden nereye taşınacağınızı da yazın.</li>
<li><b>Fiyatı öğrenin</b>Fiyatı söyleyelim; isterseniz ücretsiz keşfe gelelim.</li></ol>
<div class="btns">{btn_wa("btn btn-wa btn-lg", "Fotoğraf Gönder, Fiyat Al")}</div>
</div></div></section>"""


def band(title="Taşınma tarihiniz belli mi?", text="Arayın ya da fotoğrafları WhatsApp'tan gönderin; fiyatı birlikte netleştirelim."):
    return f"""<section class="band-sec"><div class="wrap"><div class="band"><div><h2>{esc(title)}</h2><p>{esc(text)}</p></div>
<div class="btns">{btn_call()}{btn_wa("btn btn-line", "WhatsApp'tan Yazın")}</div></div></div></section>"""


def service_cards():
    out = []
    for s in SERVICES:
        icon = SVC_ICON.get(s["id"]) or SVC_ICON[s["icon"]]
        img = C.IMAGES.get("svc-" + s["id"])  # hizmet fotoğrafı gelince config.IMAGES'e "svc-<id>" ile eklenir
        pic = (f'<img src="{esc(img)}" alt="{esc(s["name"])}" width="640" height="400" loading="lazy" decoding="async">'
               if img else f'<span class="big">{icon}</span>')
        out.append(f'<a class="card" href="/hizmetler/#{s["id"]}"><div class="c-media">{pic}</div>'
                   f'<div class="c-body"><h3>{esc(s["name"])}</h3><p>{esc(s["short"])}</p><span class="more">Ayrıntılar →</span></div></a>')
    return '<div class="cards">' + "".join(out) + "</div>"


def stats():
    return '<div class="stats">' + "".join(
        f'<div class="stat"><b>{esc(v)}</b><span>{esc(t)}</span></div>' for v, t in C.STATS) + "</div>"


def why():
    rs = "".join(f'<div class="why-card"><span class="ri">{ICON[i]}</span><h3>{esc(t)}</h3><p>{esc(x)}</p></div>' for i, t, x in REASONS)
    return f"""<section class="alt"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Neden biz</span><h2>Taşınmayı baştan sona tek ekip üstleniyor</h2><p>Keşiften kuruluma kadar aynı ekip; konuşulan iş, konuşulduğu gibi yapılır.</p></div>
<div class="why-cards">{rs}</div>{stats()}</div></section>"""


def steps_section():
    steps = "".join(f"<li><b>{esc(a)}</b><span>{esc(b)}</span></li>" for a, b in STEPS)
    return f"""<section><div class="wrap"><div class="sec-head center"><span class="eyebrow">Süreç</span><h2>4 adımda taşınma</h2><p>İlk mesajdan son koliye kadar.</p></div><ol class="steps">{steps}</ol></div></section>"""


def faq_html(items):
    return '<div class="faq">' + "".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in items) + "</div>"


def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def area_list(current=None):
    return '<ul class="areas">' + "".join(
        f'<li><a href="/{d["slug"]}/"{" aria-current=\"page\"" if d["slug"] == current else ""}>{esc(d["name"])}</a></li>'
        for d in ILCELER) + "</ul>"


def areas_block(title, text="", current=None, cls="alt", sid=""):
    cta = (f'<div class="area-cta"><span class="eyebrow" style="color:#fdba74">Hemen fiyat alın</span>'
           f'<h3>Köy ve mahallelere de geliyoruz</h3><p>Adresinizi söyleyin ya da fotoğrafları gönderin, taşınmayı birlikte planlayalım.</p>{btn_call()}{btn_wa()}</div>')
    p = f"<p>{esc(text)}</p>" if text else ""
    sid_attr = f' id="{sid}"' if sid else ""
    return (f'<section class="{cls}"{sid_attr}><div class="wrap"><div class="sec-head"><span class="eyebrow">Hizmet bölgeleri</span>'
            f'<h2>{esc(title)}</h2>{p}</div><div class="areas-wrap">{area_list(current)}{cta}</div></div></section>')


def aside(extra=""):
    svc = "".join(f'<li><a href="/hizmetler/#{s["id"]}">{esc(s["name"])}</a></li>' for s in SERVICES)
    return f"""<aside>
<div class="box cta-box"><h3>Fotoğrafla fiyat alın</h3><p>Eşyalarınızın fotoğrafını WhatsApp'tan gönderin, fiyatı hemen söyleyelim. İsterseniz ücretsiz keşfe gelelim.</p>{btn_wa()}{btn_call("btn btn-call")}</div>
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
    body = hero(p["h1"], p["lead"], "hero", "Kardeşlerim Nakliyat taşıma kamyonu") + strip() + f"""
<section><div class="wrap"><div class="sec-head center"><span class="eyebrow">Hizmetlerimiz</span><h2>Taşınmanın her aşaması tek elden</h2><p>Sakarya içinde ve Sakarya'dan Türkiye'nin her yerine; paketlemeden kuruluma kadar.</p></div>{service_cards()}</div></section>
{why()}
<section style="padding-bottom:0">{wa_flow()[len('<section class="wa-sec">'):-len('</section>')]}</section>
{steps_section()}
<section class="alt"><div class="wrap layout"><article class="prose">{md(p["body"])}</article>{aside()}</div></section>
{areas_block("Sakarya'nın 16 ilçesindeyiz", "Serdivan'daki adresimizden ilin tüm ilçelerine gidiyoruz. İlçenizi seçip o bölgeye özel bilgileri okuyabilirsiniz.", cls="", sid="bolgeler")}
<section class="alt"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Sık sorulanlar</span><h2>Merak edilenler</h2></div><div class="faq mid">{faq_html(HOME_SSS)}</div></div></section>
{band()}"""
    write("/", page("/", p["title"], p["desc"], body, base_schema + [faq_schema(HOME_SSS)]))
    report.append(("/", words(p["body"])))

    # Hakkımızda, İletişim
    for key, path, img in (("about", "/hakkimizda/", "hakkimizda"), ("contact", "/iletisim/", "iletisim")):
        p = PAGES[key]
        extra = ""
        if key == "contact":
            hrs = "".join(f"<br>{esc(d)}: {esc(h)}" for d, h in C.HOURS)
            extra = f"""<div class="box"><h3>Adres ve saatler</h3><address class="nap"><strong>{esc(C.NAME)}</strong><br>{esc(ADDR_LINE)}<br>Telefon: <a href="tel:{TEL}">{esc(C.PHONE)}</a>{hrs}<br><a href="{esc(MAPS_URL)}" target="_blank" rel="noopener">Google Haritalar'da aç →</a></address></div>"""
        crumbs = [("Ana Sayfa", "/"), (p["crumb"], None)]
        body = hero(p["h1"], p["lead"], img, p["crumb"], crumbs, eyebrow=p["crumb"], small=True) + (wa_flow() if key == "contact" else "") + f"""
<section><div class="wrap layout"><article class="prose">{md(p["body"])}</article>{aside(extra)}</div></section>
{why() if key == "about" else ""}
{areas_block("Sakarya'nın 16 ilçesindeyiz")}
{band()}"""
        sch = base_schema + [breadcrumb([("Ana Sayfa", "/"), (p["crumb"], path)])]
        sch.append({"@type": "AboutPage" if key == "about" else "ContactPage", "url": U + path, "name": p["title"], "about": {"@id": U + "/#firma"}})
        write(path, page(path, p["title"], p["desc"], body, sch))
        report.append((path, words(p["body"])))

    # Hizmetler
    p = PAGES["services"]
    svc_md = p["body"] + "\n\n" + "\n\n".join(f'## {s["name"]}\n\n{s["text"]}' for s in SERVICES) + "\n\n" + p.get("outro", "")
    svc_html = md(svc_md)
    for s in SERVICES:  # başlık id'lerini kısa anchor'lara eşitle
        svc_html = svc_html.replace(f'<h2 id="{slugify(s["name"])}">', f'<h2 id="{s["id"]}">')
    body = hero(p["h1"], p["lead"], "hizmetler", "Nakliyat hizmetleri", [("Ana Sayfa", "/"), ("Hizmetler", None)], eyebrow="Hizmetler", small=True) + f"""
<section class="alt"><div class="wrap">{service_cards()}</div></section>
<section><div class="wrap layout"><article class="prose">{svc_html}</article>{aside()}</div></section>
{steps_section()}
{areas_block("Hangi ilçedesiniz?", cls="alt")}
{band()}"""
    sch = base_schema + [breadcrumb([("Ana Sayfa", "/"), ("Hizmetler", "/hizmetler/")])] + [
        {"@type": "Service", "name": s["name"], "serviceType": s["name"], "provider": {"@id": U + "/#firma"},
         "areaServed": {"@type": "AdministrativeArea", "name": "Sakarya"}, "url": U + "/hizmetler/#" + s["id"]} for s in SERVICES]
    write("/hizmetler/", page("/hizmetler/", p["title"], p["desc"], body, sch))
    report.append(("/hizmetler/", words(svc_md)))

    # İlçeler
    for d in ILCELER:
        path = f'/{d["slug"]}/'
        near = "".join(f'<li><a href="/{n}/">{esc(by_slug[n]["name"])} nakliyat</a></li>' for n in d["near"])
        extra = f'<div class="box"><h3>Yakın ilçeler</h3><ul>{near}</ul></div>'
        crumbs = [("Ana Sayfa", "/"), ("Hizmet Bölgeleri", "/#bolgeler"), (d["name"], None)]
        faq = SSS[d["slug"]]
        near_links = ", ".join(f'<a href="/{n}/">{esc(by_slug[n]["name"])}</a>' for n in d["near"])
        body = hero(d["h1"], d["lead"], "ilce-" + d["slug"], f'{d["name"]} evden eve nakliyat', crumbs,
                    eyebrow=f'{d["name"]} · Sakarya', small=True, place=d["name"]) + wa_flow() + f"""
<section><div class="wrap layout"><article class="prose">{md(d["body"])}
<p>Komşu ilçelerde de çalışıyoruz: {near_links}.</p>
<h2 id="sss">{esc(d["name"])} taşımalarında sık sorulanlar</h2>
{faq_html(faq)}</article>{aside(extra)}</div></section>
{steps_section()}
{areas_block("Sakarya'nın diğer ilçeleri", current=d["slug"], cls="alt")}
{band(f'{d["name"]} içinde ya da dışına mı taşınıyorsunuz?')}"""
        sch = base_schema + [
            breadcrumb([("Ana Sayfa", "/"), (d["name"] + " Nakliyat", path)]),
            {"@type": "Service", "name": f'{d["name"]} Evden Eve Nakliyat', "serviceType": "Evden eve nakliyat",
             "provider": {"@id": U + "/#firma"}, "url": U + path,
             "areaServed": {"@type": "AdministrativeArea", "name": f'{d["name"]}, Sakarya'}},
            faq_schema(faq),
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
            f"- Telefon / WhatsApp: {C.PHONE} ({TEL})", f"- Adres: {ADDR_LINE}", f"- Çalışma saatleri: {hours_text()}", f"- Web: {U}/", "",
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
