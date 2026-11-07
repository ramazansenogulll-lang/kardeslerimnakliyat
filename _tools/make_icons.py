"""Logo, favicon ve paylaşım (OG) görselini üretir. Gerçek logo/fotoğraf gelince değiştirilebilir."""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
NAVY, ORANGE, WHITE = (18, 49, 90), (242, 113, 28), (255, 255, 255)
F = "C:/Windows/Fonts/arialbd.ttf"

def truck(d, x, y, s):
    d.rectangle([x+8*s, y+17*s, x+28*s, y+31*s], fill=ORANGE)
    d.polygon([(x+28*s, y+21*s), (x+35*s, y+21*s), (x+40*s, y+26*s), (x+40*s, y+31*s), (x+28*s, y+31*s)], fill=WHITE)
    for cx in (14, 34):
        d.ellipse([x+(cx-3.5)*s, y+29.5*s, x+(cx+3.5)*s, y+36.5*s], fill=WHITE, outline=NAVY, width=max(1, int(2*s)))

def icon(size):
    im = Image.new("RGB", (size, size), NAVY); d = ImageDraw.Draw(im)
    truck(d, 0, 0, size / 48); return im

icon(180).save(os.path.join(IMG, "apple-touch-icon.png"))
icon(512).save(os.path.join(IMG, "logo.png"))
og = Image.new("RGB", (1200, 630), NAVY); d = ImageDraw.Draw(og)
d.rectangle([0, 560, 1200, 630], fill=ORANGE)
truck(d, 60, 120, 9)
d.text((500, 200), "Kardeşlerim", font=ImageFont.truetype(F, 84), fill=WHITE)
d.text((500, 300), "Nakliyat", font=ImageFont.truetype(F, 84), fill=(255, 178, 122))
d.text((500, 420), "Sakarya evden eve nakliyat · Serdivan", font=ImageFont.truetype(F, 34), fill=(219, 229, 241))
d.text((60, 578), "kardeslerimnakliyat.com.tr", font=ImageFont.truetype(F, 32), fill=WHITE)
og.save(os.path.join(IMG, "og-image.png"), optimize=True)
open(os.path.join(IMG, "favicon.svg"), "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="12" fill="#12315a"/><path d="M8 17h20v14H8z" fill="#f2711c"/><path d="M28 21h7l5 5v5H28z" fill="#fff"/><circle cx="14" cy="33" r="3.5" fill="#fff" stroke="#12315a" stroke-width="2"/><circle cx="34" cy="33" r="3.5" fill="#fff" stroke="#12315a" stroke-width="2"/></svg>')
print("ok")
