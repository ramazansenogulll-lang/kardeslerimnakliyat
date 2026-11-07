"""Ana sayfa, Hakkımızda, Hizmetler, İletişim metinleri.

İşaretleme: '## ' başlık, '- ' liste maddesi, boş satır yeni paragraf, [metin](/yol/) link, **kalın**.
"""

SERVICES = [
    {"id": "evden-eve", "icon": "ev", "name": "Evden Eve Nakliyat",
     "short": "Paketleme, söküm-kurulum ve taşıma; aynı gün içinde yeni evinizde.",
     "text": """Evden eve taşımada işin yarısı paketlemedir. Tabakları tek tek kağıda sarıyor, bardakları bölmeli kolilere diziyoruz. Dolap ve yatak gibi büyük parçaları söküp battaniye ve streç filmle koruyoruz, yeni evde yine biz kuruyoruz.

Kamyona yükleme sırasını da rastgele yapmıyoruz. Ağır ve sağlam eşyalar alta, kırılacaklar üste ve kenara geliyor. Böylece yolda bir şey birbirine sürtünmüyor. Kolilerin üzerine hangi odaya ait olduğunu yazıyoruz; boşaltırken her koli doğru odaya gidiyor."""},
    {"id": "paketleme", "icon": "parca", "name": "Paketleme",
     "short": "Mutfaktan gardıroba, eşyanızı kolilere biz yerleştirip sarıyoruz.",
     "text": """Paketlemeyi tamamen bize bırakabilirsiniz; paketleme ve malzemeler taşıma fiyatına dahil. Koli, balonlu naylon, streç film ve battaniyeyle geliyoruz. Tabakları tek tek kağıda sarıyor, bardakları bölmeli kolilere diziyor, kıyafetleri askıdan alıp düzgünce yerleştiriyoruz.

Her kolinin üzerine hangi odaya ait olduğunu ve içinde kırılacak eşya olup olmadığını yazıyoruz. Yeni evde koliler doğru odaya gidiyor, açarken neyin nerede olduğunu aramıyorsunuz. İsterseniz yalnızca mutfak gibi zahmetli bölümleri paketleyip gerisini size bırakabiliyoruz."""},
    {"id": "mobilya-montaj", "icon": "montaj", "name": "Mobilya Söküm ve Montaj",
     "short": "Dolap, yatak ve gardırobu söküp yeni evde yeniden kuruyoruz.",
     "text": """Gardırop, yatak, çocuk odası takımı ve modüler dolaplar sökülmeden taşınırsa hem kapıdan geçmiyor hem de yolda zarar görüyor. Bu parçaları eski evde söküyor, vidalarını ve bağlantı parçalarını poşetleyip mobilyanın üzerine bantlıyoruz.

Yeni evde aynı mobilyayı yeniden kuruyor, kapak ayarlarını yapıyoruz. Taşınma dışında, yeni aldığınız ya da yer değiştirmek istediğiniz bir mobilyanın sökülüp takılması için de çağırabilirsiniz."""},
    {"id": "sehirler-arasi", "icon": "yol", "name": "Şehirler Arası Nakliyat",
     "short": "Sakarya'dan İstanbul, Ankara, İzmir ve diğer illere planlı taşıma.",
     "text": """Sakarya'dan başka bir ile taşınıyorsanız, en çok merak edilen şey eşyanın ne zaman varacağıdır. Bunu baştan, net bir gün olarak söylüyoruz. İstanbul, Kocaeli, Bursa ve Ankara gibi yakın illerde çoğu zaman aynı gün yükleyip ertesi sabah teslim ediyoruz.

Uzak illerde araç sizin eşyanıza ayrılıyor; yolda başka yük almak için gün kaybetmiyoruz. Taşıma boyunca şoförümüzün numarası sizde oluyor, aracın nerede olduğunu istediğiniz an sorabiliyorsunuz."""},
    {"id": "ofis-tasima", "icon": "ofis", "name": "Ofis Taşıma",
     "short": "Hafta sonu ya da mesai sonrası taşıma; işiniz durmasın.",
     "text": """Ofis taşırken asıl mesele işin kaç gün aksadığıdır. Bu yüzden ofis taşımalarını çoğunlukla cuma akşamı ya da hafta sonu yapıyoruz. Pazartesi sabahı masalar yerinde, bilgisayarlar kutularından çıkmış oluyor.

Dosya dolaplarını içindekilerle birlikte etiketliyoruz, kabloları masa numarasıyla eşleştiriyoruz. Serdivan ve Adapazarı'ndaki iş yerleri, muayenehaneler ve küçük mağazalar en sık çalıştığımız yerler."""},
    {"id": "asansorlu-tasima", "icon": "asansor", "name": "Asansörlü Taşıma",
     "short": "Dış cephe asansörüyle yüksek katlara hızlı ve güvenli taşıma.",
     "text": """Bina asansörüne sığmayan koltuklar, merdiven boşluğunda dönmeyen gardıroplar için dış cephe asansörü kullanıyoruz. Eşya pencereden ya da balkondan doğrudan kamyona iniyor. Merdivenlerde sürtünme olmadığı için hem eşya hem bina duvarları zarar görmüyor.

Asansör kurulumu için binanın önünde araç park edecek yer gerekiyor. Sokağınızı ve kat bilgisini telefonda sorduğumuzda bu yüzden soruyoruz. Gerekirse taşınma gününden önce gelip yerinde bakıyoruz."""},
    {"id": "esya-depolama", "icon": "depo", "name": "Eşya Depolama",
     "short": "Ev tadilatı ya da tarih uyuşmazlığında eşyanız kapalı depoda bekler.",
     "text": """Bazen eski evden çıkış ile yeni eve giriş aynı güne denk gelmiyor. Tadilat uzuyor ya da yurt dışına bir süreliğine gidiliyor. Böyle durumlarda eşyanızı paketleyip kapalı ve kuru bir depoda tutuyoruz.

Depoya giren her parçanın listesini çıkarıp size veriyoruz. Süre birkaç haftadan birkaç aya kadar uzayabiliyor; teslim günü geldiğinde eşyayı istediğiniz adrese getiriyoruz."""},
    {"id": "parca-esya", "icon": "parca", "name": "Parça Eşya Taşıma",
     "short": "Tek bir buzdolabı, koltuk takımı ya da birkaç koli için uygun fiyat.",
     "text": """Her taşıma bütün ev değil. İkinci el aldığınız bir buzdolabı, anneden kalan bir vitrin ya da öğrenci evine gidecek birkaç koli için koca kamyon tutmanıza gerek yok. Parça eşyayı uygun boyutta araçla taşıyoruz.

Fiyatı eşyanın boyutuna, kat bilgisine ve mesafeye göre veriyoruz. Fotoğrafını WhatsApp'tan gönderirseniz çoğu zaman birkaç dakika içinde rakam söyleyebiliyoruz."""},
]

STEPS = [
    ("Bize ulaşın", "Telefonla arayın ya da WhatsApp'tan eşyalarınızın birkaç fotoğrafını gönderin."),
    ("Ücretsiz keşif", "Gerekirse evinize ücretsiz gelip bakıyoruz. Neyin dahil olduğunu açıkça konuşup fiyatı söylüyoruz."),
    ("Paketleme ve yükleme", "Taşınma günü ekibimiz malzemeleriyle geliyor; söküp paketleyip yüklüyoruz."),
    ("Teslim ve kurulum", "Yeni adreste eşyayı odalara yerleştiriyor, dolap ve yatakları kuruyoruz."),
]

PAGES = {
    "home": {
        "title": "Kardeşlerim Nakliyat | Sakarya Evden Eve Nakliyat, Serdivan",
        "desc": "Serdivan merkezli Kardeşlerim Nakliyat; Sakarya'nın 16 ilçesinde evden eve, asansörlü ve şehirler arası taşıma. Ücretsiz keşif, paketleme dahil.",
        "h1": "Sakarya'da evden eve nakliyat: <span>paketinden kurulumuna</span>",
        "lead": "Serdivan'daki adresimizden Sakarya'nın 16 ilçesine ve Türkiye'nin her iline taşıma yapıyoruz. Eşyanızı paketliyor, taşıyor ve yeni evinizde kuruyoruz.",
        "body": """## Serdivan'dan Sakarya'nın her yerine

Biz Kardeşlerim Nakliyat olarak Serdivan Yazlık'ta, Plevne Caddesi üzerindeyiz. Günlük işlerimizin çoğu Serdivan, Adapazarı ve Erenler arasında geçiyor. Ama Karasu'daki bir yazlıktan Taraklı'daki eski bir konağa kadar ilin her köşesine gidiyoruz.

Bir taşınmanın nasıl geçeceği aslında ilk telefonda belli olur. Bize ulaştığınızda önce birkaç şey soruyoruz: kaç oda, hangi kat, asansör var mı, yeni ev nerede. Bunlar fiyatı doğrudan etkiliyor. Sonra ya fotoğraflara bakıp rakam veriyoruz ya da ücretsiz keşfe gelip yerinde görüyoruz. Ne yapılacağı baştan netleştiği için taşınma günü konuşulmamış bir iş çıkmıyor.

## Paketleme bizim işimiz

Taşınmada en çok zaman alan iş koli doldurmaktır. İsterseniz bunu tamamen bize bırakabilirsiniz. Koliyi, balonlu naylonu, streç filmi ve battaniyeyi biz getiriyoruz. Mutfaktan başlıyoruz, çünkü en çok kırılacak eşya oradadır. Kitaplık, giyinme odası ve banyo daha hızlı ilerliyor.

Paketleme ve paketleme malzemesi taşıma fiyatına dahil; ayrıca ücret çıkarmıyoruz. Kolilerin bir kısmını kendiniz hazırlamak isterseniz de olur, biz kalanını tamamlarız.

## Fiyatı neler belirliyor?

Sabit bir "3+1 şu kadar" fiyatımız yok, çünkü iki 3+1 ev aynı miktarda eşya çıkarmıyor. Fiyatı şunlara bakarak veriyoruz:

- Eşyanın miktarı ve büyük parça sayısı
- Eski ve yeni evin katı, bina asansörü olup olmadığı
- Dış cephe asansörü gerekip gerekmediği
- İki adres arasındaki mesafe

Bunları konuştuktan sonra fiyatı söylüyoruz. Kararı acele etmeden, kendi zamanınızda verebilirsiniz.

## Sakarya'nın yollarını tanıyoruz

Adapazarı'nın merkezinde dar sokaklar ve park sorunu var. Serdivan'da yeni sitelerin çoğunda yönetim izni ve asansör rezervasyonu isteniyor. Sapanca'da göl kenarındaki villalara büyük kamyon her zaman giremiyor. Bunları bildiğimiz için aracı ve ekibi ona göre seçiyoruz. Gerekirse küçük araçla aktarma yapıyoruz.

Şehir dışına taşınanlar için de durum aynı. [Şehirler arası nakliyat](/hizmetler/#sehirler-arasi) işlerinde teslim gününü baştan söylüyor, o güne göre planlıyoruz.

## Sizden ne istiyoruz?

Taşınmadan birkaç gün önce aramanız yeterli. Ay sonu ve hafta sonları yoğun geçiyor, o tarihler için biraz daha erken haber verirseniz iyi olur. Kıymetli takılarınızı, önemli evraklarınızı ve ilaçlarınızı ayrı bir çantada kendi yanınızda taşımanızı öneriyoruz. Gerisini biz hallederiz.

Hangi ilçede olduğunuzu aşağıdaki listeden seçip o bölgeye özel bilgileri okuyabilir ya da doğrudan [iletişim sayfamızdan](/iletisim/) bize ulaşabilirsiniz.

## Taşınmadan önce sizin yapabilecekleriniz

Birkaç küçük hazırlık taşınma gününü epey kısaltıyor:

- Kullanmadığınız eşyaları önceden ayırın. Taşınmayacak her parça hem süreyi hem fiyatı düşürür.
- Buzdolabını bir gece önce boşaltıp kapağını açık bırakın, derin dondurucunun buzu çözülsün.
- Çamaşır makinesinin suyunu boşaltın; mümkünse taşıma vidasını takın.
- Yeni evin anahtarını, otopark ve asansör bilgisini taşınma gününden önce netleştirin.
- Perde, avize ve televizyon askısı gibi duvara bağlı şeylerin sökülüp sökülmeyeceğini bize baştan söyleyin.

Bunları yapamadıysanız da sorun değil. Söylemeniz yeterli, ekibimiz o işleri de üstlenir.""",
    },
    "about": {
        "crumb": "Hakkımızda",
        "title": "Hakkımızda | Kardeşlerim Nakliyat Serdivan, Sakarya",
        "desc": "Kardeşlerim Nakliyat'ı tanıyın: Serdivan Yazlık'taki ekibimiz, çalışma şeklimiz ve Sakarya genelinde taşımacılıkta nelere dikkat ettiğimiz.",
        "h1": "Biz kimiz, <span>nasıl çalışıyoruz?</span>",
        "lead": "Serdivan'da yerleşik bir nakliyat ekibiyiz. Kendi aracımız, kendi ustalarımız ve Sakarya'yı sokak sokak bilen bir ekiple çalışıyoruz.",
        "body": """## Serdivan'da, Plevne Caddesi'ndeyiz

Kardeşlerim Nakliyat'ın adresi Serdivan Yazlık Mahallesi, Plevne Caddesi No:27. Burası hem Adapazarı merkezine hem de otoyol bağlantısına yakın. Sabah işe çıktığımızda Sakarya'nın hangi ilçesine gideceksek yolumuz kısa oluyor.

Bizi arayan biriyle konuşan kişi, taşınma günü kapınıza gelen ekibin içinde de oluyor. Telefonda söylenen bir şeyin kamyona yüklenirken unutulmasını istemiyoruz. Hangi dolabın kapağı gevşek, hangi koli kırılacak eşya dolu, bunları başından beri biliyoruz.

## İşi nasıl yapıyoruz?

Her taşınmaya bir liste ile başlıyoruz. Odaları tek tek dolaşıyor, büyük parçaları sayıyoruz. Sökülecek mobilyaları, özel paketleme isteyen eşyaları ve apartmanın durumunu not alıyoruz. Bu liste aynı zamanda fiyatın da dayanağı oluyor.

Taşınma sabahı ekip, bütün malzemeyle birlikte geliyor. Önce yerleri ve kapı kasalarını koruyoruz. Sonra paketlemeye geçiyoruz. Yükleme bittiğinde eski evi bir kez daha dolaşıp unutulan bir şey kalmadığını sizinle birlikte kontrol ediyoruz.

Yeni evde iş bitmiyor. Yatakları kuruyor, dolapları yerine oturtuyor, kolileri ait oldukları odalara bırakıyoruz. İsterseniz boş kolileri de geri alıyoruz.

## Neye önem veriyoruz?

Bize göre iyi bir taşınmanın üç şartı var. Söylenen saatte gelmek, konuşulan işi eksiksiz yapmak ve eşyayı kendi eşyamız gibi taşımak. Kulağa basit geliyor ama çoğu şikayet bu üçünden birinden çıkıyor.

Eşya taşırken bir şey çizilir ya da kırılırsa bunu saklamıyoruz. Yükleme ve boşaltma sırasında fark ettiğimiz her şeyi size hemen söylüyoruz, nasıl telafi edeceğimizi birlikte konuşuyoruz.

Bir de komşularınızı düşünüyoruz. Apartman girişini uzun süre kapatmamaya, merdivenleri kirletmemeye ve gürültüyü makul saatlerde tutmaya dikkat ediyoruz. Site yönetimlerinin istediği saat aralıklarına da uyuyoruz.

## Kimlere taşıma yapıyoruz?

Müşterilerimizin çoğu Sakarya'da bir evden başka bir eve geçen aileler. Bunun yanında Sakarya Üniversitesi'ne gelen ya da mezun olup ayrılan öğrenciler, tayini çıkan memurlar, Serdivan ve Adapazarı'ndaki ofisler ve dükkanlar da sık çalıştığımız kişiler arasında.

Yazın Karasu ve Kocaali'deki yazlıklara, kışın şehir merkezine dönüş taşımaları da yapıyoruz. Yaşlı bir yakınınızı yanınıza alıyorsanız, eşyasını onun evinden toplayıp sizin evinize yerleştirmeyi de üstleniyoruz.

## Bize nasıl ulaşırsınız?

En hızlı yol telefon ve WhatsApp. Eşyalarınızın birkaç fotoğrafını gönderirseniz konuşma çok daha kısa sürüyor. Adres ve harita bilgisi için [iletişim sayfamıza](/iletisim/), yaptığımız işlerin ayrıntısı için [hizmetler sayfamıza](/hizmetler/) bakabilirsiniz.

## Bir taşınma günü bizde nasıl geçer?

Sabah genellikle sekiz gibi kapınızdayız. Önce ekip başı sizinle evi kısaca dolaşıyor, neyin nereye gideceğini, nelerin özel ilgi istediğini bir kez daha konuşuyor. Sonra herkes işine geçiyor: biri mutfağa, ikisi yatak odalarına, biri söküme.

Öğleye doğru yükleme başlıyor. Kamyonun içi de bir düzen istiyor; sağlam ve ağır parçalar alta, kırılacaklar üste ve yanlara. Yükleme bittiğinde eski evde son bir tur atıyoruz. Dolap içleri, balkon, kiler. Unutulan bir şey kalmadığından emin olunca yola çıkıyoruz.

Yeni evde boşaltma, yüklemeye göre daha hızlı ilerliyor. Akşam olmadan yataklar kurulu, mutfak kolileri tezgahın yanında oluyor. İlk geceyi rahat geçirmeniz bizim için işin bittiği an.""",
    },
    "services": {
        "crumb": "Hizmetler",
        "title": "Nakliyat Hizmetlerimiz | Evden Eve, Ofis, Asansörlü Taşıma",
        "desc": "Evden eve nakliyat, şehirler arası taşıma, ofis taşıma, asansörlü taşıma, eşya depolama ve parça eşya taşıma. Sakarya geneli, Serdivan çıkışlı.",
        "h1": "Nakliyat <span>hizmetlerimiz</span>",
        "lead": "Tek bir buzdolabından komple bir ofise kadar; Sakarya içinde ve Sakarya dışına yaptığımız taşımaların hepsi bu sayfada.",
        "body": """Aşağıda yaptığımız işleri tek tek anlattık. Çoğu taşıma bunların birkaçını birlikte içeriyor. Örneğin Serdivan'daki bir 4. kat daireden İstanbul'a taşınan bir aile için hem paketleme, hem asansörlü taşıma, hem de şehirler arası nakliyat yapıyoruz. Hangisine ihtiyacınız olduğundan emin değilseniz arayın, birlikte karar verelim.""",
        "outro": """## Fiyatlar nasıl belirleniyor?

Her hizmette fiyatı eşyanın miktarına, kat ve asansör durumuna, ve mesafeye bakarak veriyoruz. Telefonda konuştuktan ya da fotoğrafları gördükten sonra fiyatı söylüyoruz. Eşya listesini baştan netleştirdiğimiz için taşınma günü sürpriz yaşanmıyor.

Hizmet verdiğimiz ilçelerin listesi aşağıda. İlçenize özel bilgiler için ilgili sayfaya göz atabilirsiniz.""",
    },
    "contact": {
        "crumb": "İletişim",
        "title": "İletişim | Kardeşlerim Nakliyat, Yazlık Serdivan Sakarya",
        "desc": "Kardeşlerim Nakliyat iletişim: Yazlık Mah. Plevne Cd. No:27 D:2, 54130 Serdivan/Sakarya. Telefon ve WhatsApp ile fiyat alın, keşif randevusu ayarlayın.",
        "h1": "Bize <span>ulaşın</span>",
        "lead": "Telefonla arayın ya da WhatsApp'tan yazın. Eşyalarınızın fotoğraflarını gönderirseniz fiyatı daha hızlı çıkarıyoruz.",
        "body": """## Adresimiz

Yazlık Mahallesi, Plevne Caddesi No:27 Daire:2, 54130 Serdivan/Sakarya. Serdivan'ın merkezine ve Adapazarı'na birkaç dakikalık mesafedeyiz. Uğramak isterseniz önceden arayın; ekibimiz gün içinde çoğu zaman sahada oluyor.

## Fiyat almanın en kısa yolu

Telefonda bize şu bilgileri verirseniz fiyatı genellikle aynı gün söyleyebiliyoruz:

- Şu anki adresiniz ve taşınacağınız yer (ilçe ya da il yeterli)
- Evin büyüklüğü: kaç oda, hangi kat, bina asansörü var mı
- Büyük parçalar: gardırop, koltuk takımı, beyaz eşya, vitrin gibi
- Paketlemeyi bizim mi yapmamızı istediğiniz
- Düşündüğünüz taşınma tarihi

WhatsApp'tan her odanın bir iki fotoğrafını göndermeniz de çok işe yarıyor. Fotoğraflara bakıp neyin sökülmesi gerektiğini, kaç kişilik ekip ve hangi boyutta araç lazım olduğunu görebiliyoruz.

## Yerinde keşif

Eşya çoksa ya da binada özel bir durum varsa (dar merdiven, asansöre sığmayan mobilya, araç yaklaşamayan sokak gibi) gelip yerinde bakmayı tercih ediyoruz. Keşif ücretsiz ve 15-20 dakika sürüyor. Serdivan, Adapazarı, Erenler ve Arifiye'de çoğu zaman aynı gün ya da ertesi gün gelebiliyoruz. Uzak ilçeler için uygun bir günü birlikte ayarlıyoruz.

## Taşınma tarihini ne zaman bildirmeli?

Hafta içi taşımalar için birkaç gün önce haber vermeniz genellikle yeterli. Ay sonları, hafta sonları ve okulların kapandığı haziran sonu en yoğun dönemler. Bu tarihlerde taşınacaksanız bir iki hafta önceden yer ayırtmanızı öneriyoruz. Şehirler arası taşımalarda da erken haber vermek, aracı sadece size ayırmamızı kolaylaştırıyor.

## Hangi ilçelere geliyoruz?

Sakarya'nın 16 ilçesinin tamamına gidiyoruz. Aşağıdaki listeden ilçenizi seçerek o bölgedeki taşımalarla ilgili ayrıntıları okuyabilirsiniz. Hizmetlerin tamamını görmek için [hizmetler sayfamıza](/hizmetler/) bakabilirsiniz.

## WhatsApp'tan fotoğraf gönderirken

Fotoğraflar ne kadar net olursa fiyat da o kadar doğru çıkıyor. Birkaç öneri:

- Her odayı kapıdan, geniş açıyla bir kez çekin.
- Gardırop ve vitrin gibi büyük parçaların içi doluysa kapağı açık bir fotoğraf ekleyin.
- Bina girişini, merdiven boşluğunu ve evin önündeki sokağı da gösterin.
- Bodrum, kiler ya da balkonda taşınacak eşya varsa onları unutmayın.

Fotoğraflara baktıktan sonra genellikle kısa bir telefonla eksikleri tamamlıyor, ardından fiyatı iletiyoruz.

## Taşınma günü

Ekibimiz konuştuğumuz saatte, bütün malzemesiyle kapınızda oluyor. Sizden tek isteğimiz, eski ve yeni evde birinin bulunması. Eşyaların nereye konacağını o kişiye sorarak yerleştiriyoruz.""",
    },
}
