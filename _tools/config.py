"""Sitenin tek ayar dosyası. Burayı değiştirip  python _tools/build.py  çalıştırın.

(_ ile başlayan klasörleri GitHub Pages yayınlamaz.)
"""

SITE_URL = "https://kardeslerimnakliyat.com.tr"
NAME = "Kardeşlerim Nakliyat"

# --- TELEFON / WHATSAPP (YER TUTUCU: gerçek numara gelince yalnızca bu satırı değiştirin) ---
# Örnek: PHONE = "0532 123 45 67"   (boşluklu yazılabilir; linkler otomatik üretilir)
PHONE = "0534 043 11 91"
# WhatsApp numarası farklıysa buraya yazın; boş bırakılırsa PHONE kullanılır.
WHATSAPP = ""

ADDRESS = {
    "street": "Yazlık Mah. Plevne Cd. No:27 D:2",
    "postal": "54130",
    "district": "Serdivan",
    "city": "Sakarya",
}
MAPS_QUERY = "Kardeşlerim Nakliyat, Plevne Cd. No:27, Yazlık, Serdivan, Sakarya"

# --- GÖRSELLER (tek yerden yönetilir) ---
# Boş bırakılan anahtar için CSS/SVG yer tutucu çizilir.
# Fotoğraf gelince assets/img/ altına koyup yolunu yazın, ör: "/assets/img/kamyon-1200.webp"
IMAGES = {
    "hero": "",            # ana sayfa üst görsel
    "hakkimizda": "",      # hakkımızda sayfası
    "hizmetler": "",       # hizmetler sayfası üst görsel
    "iletisim": "",        # iletişim sayfası
    "ilce": "",            # ilçe sayfalarının ortak üst görseli
    # İlçeye özel görsel isterseniz: "ilce-sapanca": "/assets/img/sapanca.webp"
}
OG_IMAGE = "/assets/img/og-image.png"   # paylaşım görseli (1200x630)
