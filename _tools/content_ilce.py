"""İlçe sayfaları (1/2). Kalan ilçeler content_ilce_b.py içinde.

Her ilçe: slug, name, title, desc, h1, lead, body, near (iç link verilecek komşu ilçe slug'ları).
"""
from content_ilce_b import ILCELER_B

ILCELER_A = [
    {
        "slug": "adapazari-evden-eve-nakliyat",
        "name": "Adapazarı",
        "title": "Adapazarı Evden Eve Nakliyat | Kardeşlerim Nakliyat",
        "desc": "Adapazarı'nda evden eve nakliyat: Tığcılar'dan Karaman'a, Çark Caddesi çevresinden Korucuk'a paketleme, asansörlü taşıma ve kurulum. Hemen fiyat alın.",
        "h1": "Adapazarı evden eve <span>nakliyat</span>",
        "lead": "Çarşının dar sokaklarından Karaman ve Korucuk'taki yeni sitelere kadar Adapazarı'nın her mahallesinde taşıma yapıyoruz.",
        "near": ["serdivan-evden-eve-nakliyat", "erenler-evden-eve-nakliyat", "arifiye-evden-eve-nakliyat", "sogutlu-evden-eve-nakliyat"],
        "body": """## Adapazarı'nda taşınmak neden biraz farklı?

Adapazarı, Sakarya'nın en kalabalık ilçesi ve bizim de en çok gidip geldiğimiz yer. Serdivan'daki adresimizden çıktıktan birkaç dakika sonra Çark Caddesi'ndeyiz. Bu yakınlık işimizi kolaylaştırıyor ama merkezde taşınmanın kendine has zorlukları var.

Tığcılar, Semerciler, Cumhuriyet ve Yağcılar gibi çarşıya yakın mahallelerde sokaklar dar, park yeri az. Kamyonu kapının önüne yanaştırmak her zaman mümkün olmuyor. Böyle durumlarda aracı en yakın uygun noktaya çekiyor, eşyayı oradan taşıyoruz. Gerekirse taşınma saatini trafiğin hafif olduğu sabah erken saatlere alıyoruz.

## Eski binalar, yeni siteler

1999 depreminden sonra şehrin bir kısmı yeniden yapıldı. Bugün Adapazarı'nda iki farklı yapı tipi yan yana duruyor. Bir yanda asansörsüz, dar merdivenli eski apartmanlar var. Öbür yanda Karaman, Korucuk ve Tepekum taraflarında asansörlü, otoparklı yeni siteler.

Eski binalarda üçüncü katın üstündeki taşımalarda çoğu zaman [dış cephe asansörü](/hizmetler/#asansorlu-tasima) kuruyoruz. Gardırop ve koltuk takımı merdivenden dönmüyorsa bunu zaten başka yolla çıkarmak zor. Yeni sitelerde ise mesele genellikle yönetim. Pek çok site, taşınma için önceden gün ve saat istiyor, bina asansörünün korumayla kullanılmasını şart koşuyor. Bu izni sizinle birlikte, taşınmadan birkaç gün önce alıyoruz.

## Mahalleler arasında taşıma

Adapazarı içinde taşınanların bir kısmı aslında birkaç sokak öteye gidiyor. Mithatpaşa'dan Hızırtepe'ye, Tekeler'den Karaman'a gibi kısa mesafelerde işin çoğu paketleme ve yükleme oluyor. Yol kısa olduğu için aynı gün içinde boşaltıp kurulumu da bitiriyoruz.

Çaybaşı ve Korucuk gibi merkeze biraz uzak, bahçeli evlerin olduğu yerlerde ise bahçe eşyası, odun, depo malzemesi gibi ek yükler çıkabiliyor. Bunları baştan konuşursak doğru boyutta araçla geliyoruz.

## Dükkan ve ofis taşımaları

Çarşıdaki dükkanlar ve Çark Caddesi çevresindeki ofisler için mesai saatleri dışında çalışıyoruz. Akşam kapanıştan sonra ya da pazar günü taşıyıp ertesi sabah açılışa yetiştiriyoruz. Raf sistemlerini söküp yeni yerde kurmak, kasa ve vitrin gibi hassas parçaları ayrıca sarmak işin bir parçası. Ayrıntılar için [ofis taşıma](/hizmetler/#ofis-tasima) bölümüne bakabilirsiniz.

## Adapazarı'ndan başka şehirlere

Adapazarı'ndan İstanbul'a ve Kocaeli'ye taşınma çok yaygın. Otoyola yakınlık sayesinde bu işleri çoğunlukla aynı gün yükleyip ertesi gün teslim ediyoruz. Ankara, Bursa ya da daha uzak iller için de [şehirler arası nakliyat](/hizmetler/#sehirler-arasi) yapıyoruz.

## Adapazarı için fiyat

Mahallenizi, kat bilgisini ve kabaca eşya miktarını söylemeniz yeterli. Adapazarı merkezde çoğu zaman aynı gün gelip yerinde bakabiliyoruz. Fotoğraf gönderirseniz telefonda da rakam verebiliyoruz.""",
    },
    {
        "slug": "serdivan-evden-eve-nakliyat",
        "name": "Serdivan",
        "title": "Serdivan Evden Eve Nakliyat | Yazlık, Kemalpaşa, Esentepe",
        "desc": "Serdivan merkezli nakliyat firmasıyız. Kemalpaşa, İstiklal, Arabacıalanı, Esentepe ve tüm Serdivan'da site taşıma, öğrenci evi ve parça eşya taşıma.",
        "h1": "Serdivan evden eve nakliyat: <span>kendi mahallemiz</span>",
        "lead": "Adresimiz Serdivan Yazlık'ta. Kemalpaşa'dan Esentepe'ye, Arabacıalanı'ndan Beşköprü'ye ilçenin her köşesine birkaç dakikada ulaşıyoruz.",
        "near": ["adapazari-evden-eve-nakliyat", "arifiye-evden-eve-nakliyat", "erenler-evden-eve-nakliyat", "sapanca-evden-eve-nakliyat"],
        "body": """## Serdivan bizim evimiz

Kardeşlerim Nakliyat'ın adresi Yazlık Mahallesi, Plevne Caddesi'nde. Yani Serdivan'da bir taşıma yaptığımızda kendi mahallemizde çalışıyoruz. Sokakları, site girişlerini ve hangi saatte hangi caddenin sıkıştığını iyi biliyoruz. Bu da taşınma gününü kısaltıyor.

Serdivan son yıllarda çok hızlı büyüdü. Kemalpaşa, İstiklal, Arabacıalanı ve Bahçelievler'de yüksek katlı siteler arka arkaya yükseldi. Kazımpaşa, Köprübaşı ve Beşköprü tarafında da yeni yapılar artıyor. Bu yüzden Serdivan'daki taşımaların büyük kısmı site içinden siteye oluyor.

## Site taşımalarında dikkat ettiklerimiz

Sitelerin çoğunda taşınma kuralları var. Genelde şunlar isteniyor:

- Yönetime önceden haber verip gün ve saat almak
- Bina asansörünün içini koruma malzemesiyle kaplamak
- Otopark ya da giriş önünde aracın duracağı yeri belirlemek
- Belirli saatlerden sonra gürültülü iş yapmamak

Bunların hepsini taşınmadan önce sizinle birlikte hallediyoruz. Asansör kabinine koruma panellerini biz getiriyoruz. Yüksek katlarda bina asansörüne sığmayan büyük parçalar için [dış cephe asansörü](/hizmetler/#asansorlu-tasima) kuruyoruz. Böylece hem süre kısalıyor hem de ortak alanlar yıpranmıyor.

## Öğrenci evleri ve Esentepe

Sakarya Üniversitesi'nin Esentepe Kampüsü Serdivan sınırları içinde. Her yaz ve eylül başında öğrenci evi taşımalarımız artıyor. Mezun olup memleketine dönen, yurttan eve çıkan ya da ev arkadaşı değiştiren öğrencilerle sık çalışıyoruz.

Öğrenci taşımalarında eşya az ama süre kısıtlı oluyor. Birkaç koli, bir yatak, bir çalışma masası için [parça eşya taşıma](/hizmetler/#parca-esya) çoğu zaman yeterli. Memleketine dönen öğrenciler için eşyayı paketleyip [şehirler arası](/hizmetler/#sehirler-arasi) gönderiyoruz. Ailelerin uzaktan organize ettiği taşımalarda süreci telefonla anlatıyor, fotoğraflarla bilgi veriyoruz.

## Serdivan'ın eski yüzü

Bütün Serdivan yeni sitelerden ibaret değil. Vatan, Otuziki Evler ve Selahiye gibi mahallelerde bahçeli, müstakil ya da iki üç katlı evler var. Meşeli ve Uzunköy tarafında köy evlerine de gidiyoruz. Bu evlerde genellikle eşya fazla, depo ve bodrum dolu oluyor. Bodrumdan çıkacak eşyaları önceden konuşursak doğru ekibi ve aracı getiriyoruz.

## Serdivan'dan Adapazarı'na

Serdivan ile Adapazarı arasında taşınanlar epey fazla. Mesafe kısa olduğu için böyle işleri aynı gün içinde bitiriyoruz. Sabah yükleme yapıyor, öğleden sonra yeni evde kurulumu tamamlıyoruz. Serdivan AVM çevresi ve ana caddelerdeki trafiği hesaba katıp saatleri buna göre ayarlıyoruz.

## Hemen yanınızdayız

Serdivan içindeyseniz keşif için çoğu zaman aynı gün gelebiliyoruz. Arayın, uygun bir saatte kapınızda olalım.""",
    },
    {
        "slug": "erenler-evden-eve-nakliyat",
        "name": "Erenler",
        "title": "Erenler Nakliyat | Evden Eve Taşıma, Bekirpaşa, Kozluk",
        "desc": "Erenler'de evden eve nakliyat ve parça eşya taşıma. Erenler merkez, Bekirpaşa, Hacıoğlu, Kozluk, Küpçüler ve Alancuma'ya Serdivan'dan hızlı ulaşım.",
        "h1": "Erenler'de <span>evden eve nakliyat</span>",
        "lead": "Erenler merkezdeki apartmanlardan Kozluk ve Alancuma'daki bahçeli evlere kadar ilçenin her yerine taşıma yapıyoruz.",
        "near": ["adapazari-evden-eve-nakliyat", "serdivan-evden-eve-nakliyat", "karapurcek-evden-eve-nakliyat", "hendek-evden-eve-nakliyat"],
        "body": """## Hem şehir hem köy

Erenler, Adapazarı'nın hemen doğusunda ve iki farklı yüzü olan bir ilçe. Merkeze yakın kısımlarda dört beş katlı apartmanlar, yeni yapılan siteler var. Biraz dışarı çıkınca bahçeli evler, tarlalar ve köy yolları başlıyor. Biz ikisinde de sık çalışıyoruz ve taşıma planını buna göre kuruyoruz.

Erenler merkez, Yeni Mahalle, Bekirpaşa ve Hacıoğlu tarafındaki taşımalar Adapazarı'ndaki işlere benziyor. Kat, asansör ve park yeri belirleyici oluyor. Kozluk, Küpçüler, Alancuma ve Kayalar tarafında ise işin rengi değişiyor. Evler daha geniş, eşya daha fazla. Bahçe takımı, kışlık odun, depo malzemesi gibi yükler de sık çıkıyor.

## Bahçeli evlerden taşınırken

Müstakil evlerden taşınanlar çoğu zaman eşya miktarını küçümsüyor. Oturma odası ve yatak odaları sayılınca liste kısa görünüyor. Sonra bodrum, çatı arası, kiler ve bahçe deposu açılıyor. Bu yüzden Erenler'deki müstakil ev taşımalarında genellikle önceden gelip yerinde bakıyoruz. Keşif sırasında şunlara bakıyoruz:

- Aracın bahçe kapısına kadar yaklaşıp yaklaşamayacağı
- Bodrum ve depoda ne kadar eşya olduğu
- Taşınmayacak, atılacak ya da bağışlanacak eşyalar
- Söküm isteyen büyük mobilyalar

Böylece taşınma günü sürpriz yaşamıyoruz. Doğru boyutta araçla ve yeterli kişiyle geliyoruz.

## Erenler'den merkeze, merkezden Erenler'e

Son yıllarda Adapazarı ve Serdivan'dan Erenler'e taşınan aileler arttı. Daha geniş ve bahçeli ev arayanlar bu tarafa yöneliyor. Tersine, çocukları okula başlayınca merkeze yakın bir apartmana geçenler de var. İki durumda da mesafe kısa olduğu için taşımayı tek günde bitiriyoruz.

Sabah eski evde paketleme ve yükleme yapıyoruz. Öğleden sonra yeni evde boşaltma ve kurulum. Akşama doğru yataklarınız kurulmuş, mutfak kolileri yerinde oluyor.

## İş yerleri ve atölyeler

Erenler'de sanayiye yakın bölgelerde küçük atölyeler ve depolar da var. Bunların taşınmasında makine, tezgah ve ağır malzeme çıkabiliyor. Ağır parçalar için ekstra ekip ve uygun ekipman getiriyoruz. Ofis ve iş yeri taşımaları hakkında [ofis taşıma](/hizmetler/#ofis-tasima) bölümünde daha fazla bilgi var.

## Tek parça taşıma

Erenler'den Adapazarı'na bir buzdolabı, Kozluk'tan Serdivan'a bir yatak odası takımı gibi tek parça işler için de geliyoruz. Bunun için [parça eşya taşıma](/hizmetler/#parca-esya) hizmetimiz var. Fotoğrafı WhatsApp'tan gönderirseniz fiyatı hemen söylüyoruz.

## Fiyat ve randevu

Erenler'in merkezine Serdivan'dan kısa sürede ulaşıyoruz. Keşif için arayın, çoğu zaman aynı gün ya da ertesi gün gelebiliyoruz.""",
    },
    {
        "slug": "arifiye-evden-eve-nakliyat",
        "name": "Arifiye",
        "title": "Arifiye Evden Eve Nakliyat | Hanlı, Neviye, Kirazca",
        "desc": "Arifiye'de evden eve nakliyat: Arifiye merkez, Hanlı, Neviye, Kirazca, Arifbey ve Mollaköy'de paketleme, taşıma ve kurulum. Serdivan'a komşu ekip.",
        "h1": "Arifiye evden eve <span>nakliyat</span>",
        "lead": "Arifiye, Serdivan'ın hemen yanı başında. Merkezdeki apartmanlardan Hanlı ve Kirazca'daki bahçeli evlere kadar her yere geliyoruz.",
        "near": ["serdivan-evden-eve-nakliyat", "sapanca-evden-eve-nakliyat", "adapazari-evden-eve-nakliyat", "geyve-evden-eve-nakliyat"],
        "body": """## Yol üstünde bir ilçe

Arifiye, Sakarya'nın kavşak noktalarından biri. Otoyol, D-100 ve demiryolu bu ilçeden geçiyor. Serdivan'daki adresimizden Arifiye merkeze kısa sürede varıyoruz. Bu yakınlık, keşfe gelmeyi ve taşınma gününü planlamayı kolaylaştırıyor.

Arifiye'deki taşımaların bir kısmı ilçe içinde oluyor. Bir kısmı ise Arifiye'den Serdivan ve Adapazarı'na ya da tersine. Otoyola yakın olduğu için İstanbul ve Kocaeli yönüne taşınanlar da çok. Hangisi olursa olsun yükleme ve boşaltmayı aynı gün içinde planlıyoruz.

## Mahalleden mahalleye

Arifiye merkezde, Fatih ve Arifbey taraflarında apartmanlar ağırlıkta. Bu binaların çoğu üç dört katlı ve bir kısmında asansör yok. Üst katlardan büyük eşya indirirken dar merdiven boşluğu sorun olabiliyor. Gardırop ve köşe takımı gibi parçalar dönmüyorsa [dış cephe asansörü](/hizmetler/#asansorlu-tasima) ile pencereden indiriyoruz.

Hanlı, Neviye, Kirazca, Mollaköy ve Karaabdülbaki gibi mahallelerde ise bahçeli ve müstakil evler fazla. Bu evlerde eşya genellikle daha çok oluyor. Kiler, bahçe deposu ve garajda biriken eşyayı da taşınma listesine eklemek gerekiyor. Burada önceden yapılan bir keşif, taşınma gününü çok rahatlatıyor.

## Yeni evlere taşınanlar

Arifiye'nin bazı bölgelerinde yeni konut projeleri yükseliyor. Yeni bir binaya ilk taşınanlar arasında olmak bazı küçük işleri de beraberinde getiriyor. Asansörün henüz tam devreye girmemiş olması, otopark girişinin bitmemiş olması ya da çevre yolunun kum ve mıcırla kaplı olması gibi. Bu durumlarda aracı ve ekibi buna göre seçiyor, gerekirse taşınmayı birkaç saat öne ya da sona alıyoruz.

## Paketleme ve kurulum

Paketlemeyi bize bırakmak isteyenler için tüm malzemeyi biz getiriyoruz. Mutfak eşyasını tek tek sarıyor, kıyafetleri askılı kolilere yerleştiriyor, mobilyaları battaniye ve streç filmle koruyoruz. Yeni evde yatakları ve dolapları kurup kolileri odalara dağıtıyoruz.

Paketleme ve malzemeler taşıma fiyatına dahil. Yine de bazı kolileri kendiniz hazırlamak isterseniz koli ve bant bırakabiliyoruz.

## Arifiye'den şehir dışına

Otoyola birkaç dakikalık mesafede olmak, Arifiye'den İstanbul ve Kocaeli'ye taşımayı kolaylaştırıyor. Bu yönlere taşınanların eşyasını genellikle sabah yükleyip aynı gün ya da ertesi sabah teslim ediyoruz. Daha uzak iller için [şehirler arası nakliyat](/hizmetler/#sehirler-arasi) sayfamıza göz atabilirsiniz.

## Arifiye için randevu

Mahallenizi ve eşya durumunu kısaca anlatın. Arifiye'de çoğu zaman aynı gün keşfe gelebiliyoruz.""",
    },
    {
        "slug": "akyazi-evden-eve-nakliyat",
        "name": "Akyazı",
        "title": "Akyazı Nakliyat | Evden Eve Taşıma, Kuzuluk, Dokurcun",
        "desc": "Akyazı'da evden eve nakliyat: Akyazı merkez, Konuralp, Gazipaşa, Altındere, Kuzuluk ve Dokurcun'a paketleme ve taşıma. Şehir içi ve şehirler arası.",
        "h1": "Akyazı'da <span>evden eve nakliyat</span>",
        "lead": "Akyazı merkezden Kuzuluk'a, Altındere'den Dokurcun'a kadar ilçenin her mahallesinde taşıma yapıyoruz.",
        "near": ["hendek-evden-eve-nakliyat", "karapurcek-evden-eve-nakliyat", "kocaali-evden-eve-nakliyat", "geyve-evden-eve-nakliyat"],
        "body": """## Geniş bir ilçe, farklı ihtiyaçlar

Akyazı, Sakarya'nın en geniş ilçelerinden biri. Merkezde apartmanlar ve çarşı, çevrede ise ovaya ve dağ eteklerine yayılmış köyler var. Bu yüzden Akyazı'daki taşımaları tek bir kalıba sokmak zor. Her işte önce adresin nerede olduğuna, araca nasıl ulaşılacağına bakıyoruz.

Akyazı merkezde Konuralp, Gazipaşa, Cumhuriyet, Fatih ve Yeni Mahalle taraflarında taşımalar genellikle apartmandan apartmana. Burada kat bilgisi, asansör ve park yeri önemli. Altındere ve Kuzuluk gibi biraz dışarıdaki mahallelerde ise müstakil evler, bahçeler ve daha fazla eşya bizi bekliyor.

## Kuzuluk ve kaplıca evleri

Kuzuluk, kaplıcalarıyla bilinen bir yer. Buradaki evlerin bir kısmı yıl boyu oturulan evler, bir kısmı ise hafta sonu ya da yaz için kullanılan ikinci konutlar. Bu ikinci evlerin taşımalarında genellikle tüm ev değil, birkaç oda eşya oluyor. Böyle işlerde [parça eşya taşıma](/hizmetler/#parca-esya) uygun bir seçenek.

İkinci evini satan ya da kiraya veren aileler, eşyanın bir kısmını asıl evlerine, bir kısmını başka bir adrese göndermek isteyebiliyor. Aynı gün iki ayrı adrese boşaltma yapmayı da planlayabiliyoruz. Bunu baştan söylemeniz yeterli.

## Dokurcun ve dağ köyleri

Dokurcun ve çevresindeki köylerde yollar dar ve virajlı olabiliyor. Kışın ve yağışlı günlerde bazı yollara büyük kamyonla çıkmak riskli. Bu durumlarda daha küçük bir araç kullanıyor ya da eşyayı uygun bir noktada aktarıyoruz. Taşınma tarihini belirlerken hava durumunu da hesaba katıyoruz.

Köy evlerinden taşınırken çoğu zaman yıllardır biriken eşyalar çıkıyor. Eski sandıklar, ahşap dolaplar, el işi örtüler... Bunların bazıları aile için çok değerli. Eski ahşap mobilyaları ekstra battaniye ile sarıyor, yükleme sırasında ayrı bir yere koyuyoruz.

## Akyazı'dan merkeze

Akyazı'dan Adapazarı ve Serdivan'a taşınanlar epey fazla. Çocuğu üniversiteyi kazanan, işi merkeze taşınan ya da yaşlı ebeveynlerinin yanına geçen aileler bunların başında. Mesafe yaklaşık yarım saatlik yol olduğu için taşımayı bir günde bitiriyoruz.

## Şehirler arası taşıma

Akyazı, D-100 ve otoyola yakın. İstanbul, Kocaeli ya da Düzce yönüne taşınanların eşyasını sabah yükleyip genellikle aynı gün teslim edebiliyoruz. Ankara ve daha uzak illere de gidiyoruz. Ayrıntılar için [şehirler arası nakliyat](/hizmetler/#sehirler-arasi) bölümüne bakabilirsiniz.

## Akyazı'dan arayanlar

Mahallenizi, evin tipini ve yaklaşık eşya miktarını söyleyin. Fotoğraf gönderirseniz telefonda fiyat çıkarabiliyoruz. Eşya fazlaysa uygun bir günde keşfe geliyoruz.""",
    },
    {
        "slug": "hendek-evden-eve-nakliyat",
        "name": "Hendek",
        "title": "Hendek Evden Eve Nakliyat | Hendek OSB, Başpınar, Kemaliye",
        "desc": "Hendek'te evden eve nakliyat ve ofis taşıma. Hendek merkez, Başpınar, Kemaliye, Rasimpaşa, Puna, Akova ve OSB çevresine paketleme ve taşıma.",
        "h1": "Hendek evden eve <span>nakliyat</span>",
        "lead": "Hendek merkezden OSB çevresine, Başpınar'dan Akova'ya kadar ilçenin her yerinde evden eve ve iş yeri taşıması yapıyoruz.",
        "near": ["akyazi-evden-eve-nakliyat", "erenler-evden-eve-nakliyat", "kaynarca-evden-eve-nakliyat", "kocaali-evden-eve-nakliyat"],
        "body": """## Sanayiyle büyüyen bir ilçe

Hendek son yıllarda organize sanayi bölgesiyle birlikte hızla büyüdü. Fabrikalarda çalışmak için başka şehirlerden gelen aileler, ilçeye yerleşen mühendisler ve teknik personel, Hendek'teki taşıma işlerinin önemli bir kısmını oluşturuyor. Bu yüzden Hendek'e hem şehir içi hem de şehirler arası taşıma için sık gidiyoruz.

Başka bir ilden Hendek'e gelen biri için ilk günler yoğun geçiyor. İş başlıyor, ev tutuluyor, eşya yolda. Biz eşyayı yükleme yapılan şehirden alıp Hendek'teki yeni eve kadar getiriyor, kurulumu da yapıyoruz. Böylece işe başlamadan önce ev oturulabilir hale geliyor.

## Merkez mahalleler

Hendek merkezde Başpınar, Kemaliye, Rasimpaşa, Yeni Mahalle ve Nuriye tarafında apartmanlar yoğun. Yeni yapılan sitelerin çoğu asansörlü. Eski binalarda ise merdiven taşıması gerekiyor. Üst katlarda ve büyük parçalarda [asansörlü taşıma](/hizmetler/#asansorlu-tasima) süreyi kısaltıyor.

Hendek'in merkez caddelerinde, özellikle hafta içi gündüz saatlerinde trafik ve park sorunu olabiliyor. Taşıma saatini buna göre planlıyoruz. Sabah erken yükleme yapmak çoğu zaman en rahatı oluyor.

## Puna, Akova ve köy yerleşimleri

Hendek'in merkezden uzak mahallelerinde, Puna ve Akova gibi yerlerde müstakil ve bahçeli evler fazla. Buralarda eşya genellikle daha çok oluyor ve ağır parçalar çıkabiliyor. Fındık bahçesi olan evlerde tarım aletleri, çuvallar ve depo malzemesi de taşınma listesine girebiliyor. Bunları önceden konuşursak doğru aracı getiriyoruz.

Köy yollarında büyük araçla ilerlemek her zaman mümkün olmuyor. Gerekirse küçük bir araçla aktarma yapıyoruz. Bu tür ayrıntıları keşif sırasında netleştiriyoruz.

## Fabrika ve ofis taşımaları

Hendek OSB çevresindeki firmaların ofis bölümleri ve idari birimleri için de taşıma yapıyoruz. Masa, dolap, dosya arşivi ve bilgisayar ekipmanını mesai dışında taşıyıp yeni yerde kuruyoruz. Üretim makineleri gibi özel ekipman gerektiren işler bizim alanımız dışında kalıyor, bunu baştan söylüyoruz. [Ofis taşıma](/hizmetler/#ofis-tasima) bölümünde nasıl çalıştığımızı anlattık.

## Hendek'ten şehir dışına

Hendek otoyola çok yakın. Buradan İstanbul, Kocaeli, Düzce, Bolu ve Ankara yönüne taşıma oldukça kolay. Fabrikada işi biten ve memleketine dönen çalışanların eşyasını da paketleyip gönderiyoruz. Şehirler arası işlerde teslim gününü baştan söylüyoruz.

## Hendek'ten arayanlar için

Hendek'in hangi mahallesinde olduğunuzu ve eşya miktarını söylemeniz yeterli. Fotoğraf gönderirseniz telefonda fiyat verebiliyoruz. Gerekirse gelip yerinde bakıyoruz.""",
    },
    {
        "slug": "karasu-evden-eve-nakliyat",
        "name": "Karasu",
        "title": "Karasu Nakliyat | Yazlık ve Evden Eve Taşıma, Sakarya",
        "desc": "Karasu'da evden eve nakliyat ve yazlık taşıma. Yalı, Aziziye, İncilli, Kurudere, Limandere ve sahildeki sitelere sezon başı ve sonu taşıma yapıyoruz.",
        "h1": "Karasu'da <span>yazlık ve ev taşıma</span>",
        "lead": "Sahildeki yazlık sitelerden Karasu merkezdeki apartmanlara kadar her yere geliyoruz. Sezon başı ve sonunda yoğun çalışıyoruz.",
        "near": ["kocaali-evden-eve-nakliyat", "kaynarca-evden-eve-nakliyat", "ferizli-evden-eve-nakliyat", "adapazari-evden-eve-nakliyat"],
        "body": """## Karasu'da iki tür taşıma

Karasu'da yaptığımız işler kabaca ikiye ayrılıyor. Bir yanda ilçede yıl boyu oturan aileler var. Onların taşımaları Sakarya'nın diğer ilçelerindekine benziyor. Öbür yanda sahildeki yazlıklar var. Bu evler genellikle İstanbul, Kocaeli ya da Adapazarı'nda oturan ailelerin ikinci konutları. Yazlık taşımaları ise kendi düzeni olan bir iş.

Yalı, Aziziye ve Karasu merkezde apartman taşımaları yapıyoruz. İncilli, Kurudere, Limandere, Tepetarla ve Darıçayırı tarafındaki sahil sitelerinde ise yazlık taşımaları ağırlıkta. Yassıgeçit ve iç kesimdeki köylerde de müstakil evlere gidiyoruz.

## Sezon başı ve sezon sonu

Mayıs sonu ve haziran başında yazlığa gidenler, eylül ve ekimde ise şehre dönenler bizi arıyor. Bu dönemlerde talep çok arttığı için birkaç hafta önceden tarih almanızı öneriyoruz. Özellikle hafta sonları çabuk doluyor.

Yazlık taşımalarında genellikle tüm ev değil, mevsimlik eşya taşınıyor. Birkaç koli, yatak takımları, bahçe mobilyası, belki bir buzdolabı ya da çamaşır makinesi. Bu tür işlerde [parça eşya taşıma](/hizmetler/#parca-esya) daha ekonomik oluyor. Komple yazlık boşaltma ya da yazlığı satıp eşyayı başka şehre götürme gibi büyük işlerde ise tam bir evden eve taşıma planlıyoruz.

## Deniz kenarında eşya

Sahile yakın evlerde nem ve tuzlu hava eşyaya iz bırakıyor. Kışın kapalı kalan yazlıklarda bazı mobilyalar ve kumaş eşyalar nem çekmiş olabiliyor. Taşırken bunlara dikkat ediyoruz. Nemli eşyayı kuru eşyayla aynı koliye koymuyor, ahşap parçaları streç filmle sıkıca sarmadan önce kurumuş olduklarından emin oluyoruz.

Sahil sitelerinin bir kısmında yollar kumlu ya da toprak. Bazı sitelere büyük kamyonla girmek mümkün olmuyor. Bu durumda aracı site girişine bırakıp eşyayı oradan taşıyoruz. Keşif ya da fotoğraf sırasında bunu baştan görmek işimizi kolaylaştırıyor.

## Kışın Karasu'da kalmak

Son yıllarda Karasu'ya yerleşip kışı da burada geçiren emekliler arttı. Bu ailelerin taşımaları genellikle büyük şehirden Karasu'ya, tam bir ev boyutunda oluyor. [Şehirler arası nakliyat](/hizmetler/#sehirler-arasi) ile eşyayı İstanbul ya da başka bir ilden alıp Karasu'daki yeni eve yerleştiriyoruz.

## Fiyat ve tarih

Karasu'nun hangi tarafında olduğunuzu, taşınacak eşyayı ve hedef adresi söyleyin. Sezon dönemlerinde mümkün olduğunca erken arayın.""",
    },
    {
        "slug": "kocaali-evden-eve-nakliyat",
        "name": "Kocaali",
        "title": "Kocaali Evden Eve Nakliyat | Yazlık Taşıma, Sakarya",
        "desc": "Kocaali'de evden eve nakliyat ve yazlık taşıma. Kocaali merkez, Yalı Mahallesi, Caferiye, Köşkdere ve çevre köylere paketleme ve taşıma yapıyoruz.",
        "h1": "Kocaali evden eve <span>nakliyat</span>",
        "lead": "Kocaali'nin sahil mahallelerinden fındık bahçeli köy evlerine kadar her adrese taşıma yapıyoruz.",
        "near": ["karasu-evden-eve-nakliyat", "kaynarca-evden-eve-nakliyat", "akyazi-evden-eve-nakliyat", "hendek-evden-eve-nakliyat"],
        "body": """## Sakin bir sahil ilçesi

Kocaali, Karasu'ya göre daha sakin ve daha küçük bir sahil ilçesi. Yazın nüfusu artıyor, kışın sessizleşiyor. Biz de Kocaali'ye en çok yaz başında ve sonbaharda gidiyoruz. Ama yıl boyunca burada oturan ailelerin taşımaları da işlerimizin önemli bir kısmı.

Kocaali merkez ve Yalı Mahallesi çevresinde apartmanlar ve yazlık siteler var. Caferiye, Köşkdere, Kirazlı ve Kadıköy gibi mahallelerde ise müstakil evler ağırlıkta. Akpınar ve iç kesimdeki köylerde fındık bahçeleri arasında dağınık evlere gidiyoruz.

## Yazlık eşyası

Yazlık taşımalarında genellikle mevsimlik eşya söz konusu. Yatak takımları, birkaç koli mutfak eşyası, bahçe sandalyeleri, belki bir buzdolabı. Bu tür işlerde tam bir kamyon yerine [parça eşya taşıma](/hizmetler/#parca-esya) daha uygun. Adapazarı, Serdivan ya da İstanbul'daki evinizden eşyayı alıp Kocaali'deki yazlığa bırakıyoruz. Sonbaharda da geri getiriyoruz.

Yazlık evini satan ya da kalıcı olarak Kocaali'ye yerleşen aileler için ise tam bir [evden eve nakliyat](/hizmetler/#evden-eve) planlıyoruz. Paketleme, söküm, taşıma ve kurulum dahil.

## Köy evlerinden taşınma

Kocaali'nin köylerinde evler genellikle geniş, depolar dolu oluyor. Fındık hasadında kullanılan aletler, çuvallar, kışlık odun ve yıllardır biriken eşyalar çıkabiliyor. Bunların hangisinin taşınacağını, hangisinin kalacağını önceden konuşursak doğru aracı ve ekibi getiriyoruz.

Köy yolları bazen dar ve eğimli. Yağmurlu günlerde toprak yollarda büyük araçla ilerlemek zorlaşıyor. Bu durumda daha küçük bir araç ya da aktarma ile çözüyoruz. Taşınma gününü belirlerken hava durumuna da bakıyoruz.

## Deniz havası ve eşya

Sahile yakın evlerde eşyalar nem çekebiliyor. Özellikle kışın kapalı kalan yazlıklarda yataklar, halılar ve ahşap mobilyalarda bunu görüyoruz. Taşırken nemli eşyayı ayrı tutuyor, ahşap parçaları kuru olduklarından emin olduktan sonra sarıyoruz. Bu küçük ayrıntı, yeni evde küf ve koku sorununu önlüyor.

## Kocaali'den şehir dışına

Kocaali'den İstanbul, Kocaeli ve Düzce yönüne taşıma oldukça kolay. Sahil yolu ve otoyol bağlantısıyla eşyayı çoğu zaman aynı gün teslim edebiliyoruz. Daha uzak iller için [şehirler arası nakliyat](/hizmetler/#sehirler-arasi) sayfamızda bilgi var.

## Yoğun dönemler

Haziran başı ve eylül sonu Kocaali'de en yoğun dönemler. Bu tarihlerde taşınacaksanız birkaç hafta önceden arayıp yer ayırtmanızı öneriyoruz. Diğer zamanlarda birkaç gün önceden haber vermeniz genellikle yeterli.""",
    },
]

ILCELER = ILCELER_A + ILCELER_B
