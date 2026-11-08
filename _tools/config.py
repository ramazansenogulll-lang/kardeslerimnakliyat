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
# --- ÇALIŞMA SAATLERİ (kullanıcı: her gün 08:00–22:00) ---
HOURS = [
    ("Her gün", "08:00 – 22:00"),
]
OPENING_HOURS = "Mo-Su 08:00-22:00"   # şema için

# --- "NEDEN BİZ" RAKAMLARI (teyit edilmemiş rakam yazmayın) ---
# Kullanıcı tarafından teyit edildi (2026-11-07).
STATS = [
    ("16", "Sakarya ilçesinde hizmet"),
    ("10+", "Yıllık tecrübe"),
    ("2.225+", "Tamamlanan taşıma"),
    ("8", "Kişilik ekip"),
]

MAPS_QUERY ="Kardeşlerim Nakliyat, Plevne Cd. No:27, Yazlık, Serdivan, Sakarya"

# --- GÖRSELLER (tek yerden yönetilir) ---
# Boş bırakılan anahtar için CSS/SVG yer tutucu çizilir.
# Fotoğraf gelince assets/img/ altına koyup yolunu yazın, ör: "/assets/img/kamyon-1200.webp"
# Fotoğraflar _tools/foto.py ile AVIF'e çevrilir (GPS + açıklama EXIF'e yazılır).
IMAGES = {
    "hero": "/assets/img/serdivan-asansorlu-tasima-1200.avif",                 # ana sayfa üst görsel
    "hakkimizda": "/assets/img/sakarya-evden-eve-nakliyat-ekip-1200.avif",     # hakkımızda sayfası
    "hizmetler": "/assets/img/tabak-paketleme-1200.avif",                      # hizmetler sayfası üst görsel
    "iletisim": "/assets/img/sakarya-sehirler-arasi-nakliyat-kamyonu-1200.avif",  # iletişim sayfası
    "ilce": "/assets/img/serdivan-asansorlu-tasima-1200.avif",  # ilçe sayfalarının ortak üst görseli
    # İlçeye özel görsel isterseniz: "ilce-sapanca": "/assets/img/sapanca.avif"
    # Hizmet kartları (svc-<id>)
    "svc-evden-eve": "/assets/img/sakarya-evden-eve-nakliyat-ekip-640.avif",
    "svc-paketleme": "/assets/img/mobilya-paketleme-strec-640.avif",
    "svc-mobilya-montaj": "/assets/img/mobilya-sokum-montaj-640.avif",
    "svc-sehirler-arasi": "/assets/img/sakarya-sehirler-arasi-nakliyat-kamyonu-640.avif",
    "svc-asansorlu-tasima": "/assets/img/serdivan-asansorlu-tasima-640.avif",
    "svc-ofis-tasima": "/assets/img/sakarya-ofis-tasima-640.avif",
    "svc-parca-esya": "/assets/img/serdivan-parca-esya-tasima-kamyon-640.avif",
}

# Konum (Yazlık Mah. Plevne Cd., Serdivan; OpenStreetMap cadde düzeyi). Şema ve geo meta'da kullanılır.
GEO = (40.8042795, 30.3603170)
OG_IMAGE = "/assets/img/og-image.jpg"   # paylaşım görseli (1200x630), _tools/logo.py üretir
