"""İndirilenler'deki logolardan site logosu, favicon, telefon simgesi ve paylaşım (OG) görselini üretir.

Kullanım:  python _tools/logo.py
"""
from pathlib import Path
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
SRC = Path.home() / "Downloads"
YATAY = SRC / "Kardeşlerim Nakliyat Logo.png"       # simge + yazı (yatay)
SIMGE = SRC / "Ev ve Taşıma Kamyonu Logosu.png"     # yalnızca simge
OG_FOTO = SRC / "Kardeşlerim Nakliyat’la Balkon Taşınması.png"


def trim(im, pad=0):
    """Beyaz kenar boşluklarını kırpar."""
    rgb = im.convert("RGB")
    bg = Image.new("RGB", rgb.size, (255, 255, 255))
    diff = ImageChops.difference(rgb, bg).convert("L").point(lambda v: 255 if v > 18 else 0)
    box = diff.getbbox()
    x0, y0, x1, y1 = box
    return im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))


def white_to_alpha(im):
    """Beyaz arka planı şeffaf yapar (kenarları yumuşak)."""
    im = im.convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, _ = px[x, y]
            m = min(r, g, b)
            if m > 235:
                px[x, y] = (r, g, b, 0)
            elif m > 200:
                px[x, y] = (r, g, b, int(255 * (235 - m) / 35))
    return im


def square(im, size, bg=(255, 255, 255), fill=0.84):
    im = im.convert("RGBA")
    s = size * fill / max(im.size)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), bg + (255,))
    out.alpha_composite(im, ((size - im.width) // 2, (size - im.height) // 2))
    return out.convert("RGB")


def main():
    # 1) Yatay logo: şeffaf PNG, 2x ekran için 112 px yükseklik
    y = white_to_alpha(trim(Image.open(YATAY)))
    h = 112
    y = y.resize((round(y.width * h / y.height), h), Image.LANCZOS)
    y.save(IMG / "logo-yatay.png", optimize=True)
    print("logo-yatay.png", y.size)

    # 2) Simge: favicon, telefon simgesi, şema logosu
    s = trim(Image.open(SIMGE))
    square(s, 512).save(IMG / "logo.png", optimize=True)
    square(s, 180).save(IMG / "apple-touch-icon.png", optimize=True)
    square(s, 48, fill=0.94).save(IMG / "favicon-48.png", optimize=True)
    square(s, 192, fill=0.94).save(IMG / "favicon-192.png", optimize=True)
    square(s, 48, fill=0.94).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    # 3) Paylaşım görseli 1200x630: fotoğraf + altta beyaz şerit içinde logo
    W, H, BAR = 1200, 630, 150
    f = Image.open(OG_FOTO).convert("RGB")
    sc = max(W / f.width, (H - BAR) / f.height)
    f = f.resize((round(f.width * sc), round(f.height * sc)), Image.LANCZOS)
    top = (f.height - (H - BAR)) // 2
    f = f.crop(((f.width - W) // 2, top, (f.width - W) // 2 + W, top + H - BAR))
    og = Image.new("RGBA", (W, H), (255, 255, 255, 255))
    og.paste(f, (0, 0))
    lh = 100
    lg = y.resize((round(y.width * lh / y.height), lh), Image.LANCZOS)
    og.alpha_composite(lg, ((W - lg.width) // 2, H - BAR + (BAR - lh) // 2))
    og.convert("RGB").save(IMG / "og-image.jpg", quality=86, optimize=True, progressive=True)
    print("og-image.jpg", og.size)

    # 4) PNG'leri renk paletine indirip küçült
    for name, c in [("logo-yatay.png", 128), ("logo.png", 64), ("apple-touch-icon.png", 64), ("favicon-192.png", 64)]:
        im = Image.open(IMG / name)
        meth = Image.Quantize.FASTOCTREE if im.mode == "RGBA" else Image.Quantize.MEDIANCUT
        im.quantize(colors=c, method=meth, dither=Image.Dither.NONE).save(IMG / name, optimize=True)


if __name__ == "__main__":
    main()
