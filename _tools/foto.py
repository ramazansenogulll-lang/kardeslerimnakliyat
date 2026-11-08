"""Fotoğrafları sıkıştırıp AVIF'e çevirir, EXIF'e GPS + açıklama yazar.

Kullanım:  python _tools/foto.py
Kaynak dosyalar ve hedef adlar aşağıdaki PHOTOS listesinde. Her foto iki boyutta üretilir:
  <ad>-1200.avif  (sayfa üst görselleri)   <ad>-640.avif  (hizmet kartları)
"""
from pathlib import Path
from fractions import Fraction
from PIL import Image
import piexif

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img"
SRC = Path.home() / "Downloads"

# Yazlık Mah. Plevne Cd., Serdivan / Sakarya (OpenStreetMap, cadde düzeyi)
LAT, LNG = 40.8042795, 30.3603170
QUALITY = 55
SIZES = (1200, 640)

PHOTOS = [
    ("Kardeşlerim Nakliyat’la Balkon Taşınması.png", "serdivan-asansorlu-tasima",
     "Serdivan'da asansörlü taşıma: eşya balkondan asansörle Kardeşlerim Nakliyat kamyonuna yükleniyor"),
    ("Gün Batımında Kardeşlerim Nakliyat Kamyonu.png", "sakarya-sehirler-arasi-nakliyat-kamyonu",
     "Kardeşlerim Nakliyat şehirler arası nakliyat kamyonu otoyolda"),
    ("Taşınma Günü_ Aile ve Ekip.png", "sakarya-evden-eve-nakliyat-ekip",
     "Kardeşlerim Nakliyat ekibi taşınma gününde eşyaları kamyona yüklüyor"),
    ("Mobilya Montajında Usta Eller.png", "mobilya-sokum-montaj",
     "Kardeşlerim Nakliyat ekibi yeni evde gardırop montajı yapıyor"),
    ("Taşınma Hazırlığında Tabak Paketleme.png", "tabak-paketleme",
     "Taşınma öncesi tabak ve bardakların balonlu naylonla paketlenmesi"),
    ("paketleme3.jpg", "mobilya-paketleme-strec",
     "Taşınma için streç filmle paketlenmiş mobilyalar"),
    ("Modern Ofis Taşıma Operasyonu.png", "sakarya-ofis-tasima",
     "Kardeşlerim Nakliyat ekibi ofis taşımasında paketlenmiş masa ve sandalyeleri taşıyor"),
    ("Kardeşlerim Taşımacılıkta Yoğun Gün.png", "serdivan-parca-esya-tasima-kamyon",
     "Kardeşlerim Nakliyat ekibi parça eşya taşımasında çamaşır makinesini kamyona yüklüyor"),
]


def _rat(x):
    f = Fraction(x).limit_denominator(1000000)
    return (f.numerator, f.denominator)


def _dms(v):
    v = abs(v)
    d = int(v); m = int((v - d) * 60); s = (v - d - m / 60) * 3600
    return (_rat(d), _rat(m), _rat(round(s, 4)))


def exif_bytes(desc):
    zeroth = {
        piexif.ImageIFD.ImageDescription: desc.encode("utf-8"),
        piexif.ImageIFD.Artist: "Kardeşlerim Nakliyat".encode("utf-8"),
        piexif.ImageIFD.Copyright: "Kardeşlerim Nakliyat - kardeslerimnakliyat.com.tr".encode("utf-8"),
    }
    gps = {
        piexif.GPSIFD.GPSVersionID: (2, 3, 0, 0),
        piexif.GPSIFD.GPSLatitudeRef: b"N" if LAT >= 0 else b"S",
        piexif.GPSIFD.GPSLatitude: _dms(LAT),
        piexif.GPSIFD.GPSLongitudeRef: b"E" if LNG >= 0 else b"W",
        piexif.GPSIFD.GPSLongitude: _dms(LNG),
    }
    return piexif.dump({"0th": zeroth, "GPS": gps})


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for src, name, desc in PHOTOS:
        im = Image.open(SRC / src).convert("RGB")
        ex = exif_bytes(desc)
        for w in SIZES:
            r = im.copy()
            if r.width > w:
                r = r.resize((w, round(r.height * w / r.width)), Image.LANCZOS)
            dst = OUT / f"{name}-{w}.avif"
            r.save(dst, "AVIF", quality=QUALITY, speed=4, exif=ex)
            print(f"{dst.name:52} {r.size[0]}x{r.size[1]}  {dst.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
