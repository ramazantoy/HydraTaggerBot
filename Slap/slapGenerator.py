import random


class SlapGenerator:
    def __init__(self):
        self.slapMessages = [
            "bir tokat attı 👋",
            "sert bir tokat indirdi 🖐️💥",
            "acımasızca tokatladı 😡✋",
            "hafifçe tokatladı 🤏",
            "şaplak attı 👏",
            "okkalı bir tokat yapıştırdı 💪👋",
            "eline ne geçtiyse fırlattı 🤾‍♂️💨",
            "suratına bir yumruk indirdi 👊💢",
            "kulağının dibinde alkış yaptı 👏😵",
            "ensesine bir şaplak indirdi ✋😲",
            "kafasına bir fiske vurdu 🤏😅",
            "ayağına bastı 🦶😣",
            "sırtına bir tekme attı 🦵💨",
            "gıdıkladı 🤗😂",
            "burnunu sıktı 👃✊",
            "saçını çekti 💇‍♂️😫",
            "kolunu çimdikledi ✌️😖",
            "omzuna vurdu 💁‍♂️😯",
            "suratına pasta fırlattı 🎂💨",
            "üzerine su döktü 💦😲",
            "kulağına fısıldadı 🗣️👂",
            "gözlerini kapatıp korkuttu 🙈😱",
            "sırtına buz koydu 🧊😨",
            "kafasına şapka geçirdi 🧢😵",
            "ayakkabı bağcıklarını bağladı 👞🤔",
            "koltuk altını gıdıkladı 🤗😂",
            "burnuna çiçek tuttu 🌸🤧",
            "kulağına üfledi 💨👂",
            "alnına fiske attı 🤏😳",
            "parmağını şaklattı 👌😲",
            "eline sıcak çay döktü ☕💦",
            "kafasına kitap kapattı 📚😵",
            "ayak bileğini burktu 🦶😖",
            "saçına sakız yapıştırdı 🍬😱",
            "gözüne fener tuttu 🔦👀",
            "kulağına megafonla bağırdı 📢😵",
            "sırtına buz küpü koydu 🧊😨",
            "yüzüne krem sürdü 🧴😌",
            "kafasına kova geçirdi 🪣😵",
            "eline ıslak çorap giydirdi 🧦💦",
            "burnuna mandal taktı 🤏👃",
            "ağzına limon sıktı 🍋😖",
            "saçını elektrikle statikledi ⚡💇",
            "kulağına sümük üfledi 🤧💨",
            "gözüne su fışkırttı 💦👁️",
            "kafasına yastık fırlattı 🛏️💨",
            "ayağına lego bastırdı 🧱😫",
            "sırtına kedi attı 🐱😲",
            "yüzüne ayna tuttu 🪞😳",
            "eline yapışkan sürdü 🖐️😅",
            "burnuna tüy üfledi 🪶💨",
            "kulağına buz koydu 🧊👂",
            "gözüne konfeti patlattı 🎉👀",
            "kafasına balon patlattı 🎈💥",
            "ayağını gıdıkladı 🦶😂",
            "sırtına sülük yapıştırdı 🐛😨",
            "yüzüne köpük fışkırttı 🧼💦",
            "eline fare kapanı kapattırdı 🐁😱",
            "burnuna biber çekti 🌶️🤧",
            "kulağına zil çaldı 🔔👂",
            "gözüne makyaj yaptı 💄👁️",
            "kafasına yumurta kırdı 🥚💥",
            "ayağına buz torbası koydu 🧊🦶",
            "sırtına sıcak su torbası yapıştırdı 🔥💧",
            "yüzüne un üfledi 🌬️😶",
            "eline elektrikli çarpan sıktırdı ⚡🖐️",
            "burnuna nane koklatıp hapşırttı 🌿🤧",
            "kulağına fısıldayıp ürpertti 🗣️😨",
            "gözüne gözlük taktı 👓😎",
            "kafasına peruk yapıştırdı 💇‍♀️😅",
            "ayağına ağırlık bağladı 🏋️‍♂️🦶",
            "sırtına buz kayağı yaptırdı 🏂🧊",
            "yüzüne maske yapıştırdı 🎭😷",
            "eline yapay örümcek koydu 🕷️😱",
            "burnuna tütsü üfledi 💨👃",
            "kulağına kulaklık takıp yüksek sesle müzik açtı 🎧🎵",
            "gözüne dürbünle baktı 🔭👀",
            "kafasına şemsiye açtı ☂️😳",
            "ayağına paten taktı ⛸️🦶",
            "sırtına sırt çantası astı 🎒😮",
            "yüzüne ahtapot yapıştırdı 🐙😨",
            "eline ıslak boya sürdü 🎨💦",
            "burnuna çiçek tozu üfledi 🌺🤧",
            "kulağına kulak tıkacı tıktı 🧱👂",
            "gözüne teleskop dayadı 🔭👁️",
            "kafasına karpuz kabuğu geçirdi 🍉😵",
            "ayağına kurbağa koydu 🐸🦶",
            "sırtına kaktüs yapıştırdı 🌵😖",
            "yüzüne tıraş köpüğü sıktı 🧔💦",
            "eline erimiş dondurma döktü 🍦💧",
            "burnuna karanfil soktu 🌺👃",
            "kulağına saat kurdu ⏰👂",
            "gözüne büyüteç tuttu 🔍👀",
            "kafasına küvet geçirdi 🛁😵",
            "ayağına kum döktü 🏖️🦶",
            "sırtına buz kaydırağı yaptı 🧊🛝",
            "yüzüne akvaryum geçirdi 🐠😳",
            "eline elektrikli süpürge tuttu 🧹💨",
            "burnuna çorap koklatıp bayılttı 🧦😵",
            "kulağına vuvuzela çaldı 📯😫",
            "gözüne lazer pointer tuttu 🚨👀",
            "kafasına kamera yerleştirdi 📹🤔",
            "ayağına kestane kabuğu bastırdı 🌰😖",
            "sırtına kedi tırmaladı 🐱😾",
            "yüzüne sarımsak sürdü 🧄😖",
            "eline ateş böceği koydu 🐞✨",
            "burnuna nane şekeri soktu 🍬👃",
            "kulağına su kaçırdı 💦👂",
            "gözüne rüzgar üfledi 💨👁️",
            "kafasına küçük bir kuş kondurdu 🐦😳",
            "ayağına kum torbası bağladı 🏋️‍♂️🦶",
            "sırtına boya rulosu sürdü 🎨🖌️",
            "yüzüne pizza yapıştırdı 🍕😋",
            "eline cımbız verdi 🤏😅",
            "burnuna çikolata sürdü 🍫👃",
            "kulağına saz çaldı 🎸👂",
            "gözüne gökkuşağı yansıttı 🌈👀",
            "kafasına küçük bir ufo indirdi 🛸😲",
            "ayağına kurbağa balçığı sürdü 🐸💩",
            "sırtına buz kırığı attı 🧊💥",
            "yüzüne tüy yelpazesi salladı 🪶💨",
            "eline elektrikli çırpıcı tutuşturdu 🔌🥄",
            "burnuna tarçın üfledi 🌰💨",
            "kulağına deniz kabuğu dayadı 🐚👂",
            "gözüne sabun köpüğü üfledi 🧼💭",
            "kafasına küçük bir helikopter indirdi 🚁😵",
            "ayağına kaktüs dikeni batırdı 🌵😖",
            "sırtına sıcak kum torbası koydu 🏖️🔥",
            "yüzüne ıspanak macunu sürdü 🥬😖",
            "eline elektrikli diş fırçası tutuşturdu 🪥⚡",
            "burnuna lavanta kokusu püskürttü 💐💨",
            "kulağına küçük bir zil taktı 🔔👂",
            "gözüne disco ışıkları tuttu 🕺💡",
            "kafasına minik bir UFO kondurdu 🛸👽",
            "ayağına küçük bir yengeç yapıştırdı 🦀🦶",
            "sırtına elektrikli masaj aleti dayadı 🔌💆",
            "yüzüne küçük bir ahtapot yapıştırdı 🐙😨",
            "eline mıknatıs tutuşturdu 🧲🖐️",
            "burnuna nane esansı püskürttü 🌿💨"
        ]

    def getRandomSlapMessage(self):
        return random.choice(self.slapMessages)


class ResultGenerator:
    def __init__(self):
        self.results = [
            "Oha! 😮",
            "Vay canına! 😲",
            "Bu acıtmış olmalı! 😖",
            "Aman aman! 😱",
            "Off! 😣",
            "Eyvah! 😨",
            "Ağzım açık kaldı! 😮",
            "İnanılmaz! 🤯",
            "Gözlerime inanamıyorum! 👀",
            "Bu beklenmedikti! 😳",
            "Şok oldum! 😵",
            "Herkes donakaldı! 😶",
            "Nefesim kesildi! 😮‍💨",
            "Kulağıma inanamadım! 👂😯",
            "Dünya durdu sanki! 🌍😲",
            "Zaman dondu gibi! ⏳😳",
            "Herkes kahkahaya boğuldu! 🤣",
            "Ortalık buz kesti! 🥶",
            "Görenler şaşkına döndü! 😵‍💫",
            "Kimse ne diyeceğini bilemedi! 🤐",
            "Bu görülmeye değerdi! 👀👌",
            "Tarihe geçecek bir an! 📜✍️",
            "Büyük bir gürültü koptu! 💥🔊",
            "Herkes nefesini tuttu! 😤",
            "Gök gürler gibi bir ses duyuldu! 🌩️",
            "Yer yerinden oynadı! 🌋",
            "Tüyler diken diken oldu! 😨",
            "Kalpler durdu bir an! 💓😱",
            "Zaman yavaşladı sanki! ⏳🐢",
            "Herkes donup kaldı! 🧊😶",
            "Bu nasıl mümkün olabilir? 😧",
            "Akıl almaz! 😵",
            "Bir an duraksadım! 😮",
            "Kulaklarıma inanamadım! 👂😲",
            "Herkes birbirine baktı! 👀",
            "Şok dalgası yayıldı! 🌊",
            "Ağzım açık kaldı! 😲",
            "Bunu beklemiyordum! 😧",
            "İmkansız! 😵",
            "Herkes sessiz kaldı! 🤫",
            "Bir fırtına koptu! 🌪️",
            "Yerinden zıpladım! 🕴️",
            "Korkutucu! 😨",
            "Sarsıcı bir olay! 😳",
            "Bu bir şaka olmalı! 😅",
            "Herkes donup kaldı! 😮",
            "Kalbim durdu sandım! 💓",
            "Bunu hayal bile edemezdim! 😲",
            "Herkes panikledi! 😱",
            "Bu çok tuhaftı! 😕",
            "Bir anlık sessizlik oldu! 🤐",
            "Herkes hayretle baktı! 👀",
            "Gerçek olamaz! 😵",
            "Şok etkisi yarattı! 💥",
            "Her şey bir anda değişti! 🔄",
            "Herkesin gözleri büyüdü! 😳",
            "Kimse bir şey söyleyemedi! 🤐",
            "Bu inanılmaz bir andı! 👌",
            "Her şey durdu sanki! ⏸️",
            "Kelimeler kifayetsiz kaldı! 🗣️",
            "Bir patlama oldu! 💥",
            "Nefesimi tuttum! 😮",
            "Bu beklenmedik bir andı! 😧",
            "Herkes birbirine baktı! 👀",
            "Bu bir mucizeydi! ✨",
            "Herkes şok oldu! 😱",
            "Bu gerçek olamaz! 😵",
            "Bu, inanılmaz bir olaydı! 😲",
            "Tüylerim diken diken oldu! 😨",
            "Kalbim hızla atmaya başladı! 💓",
            "Bu nasıl olabilir? 😧",
            "Herkes sessizleşti! 🤫",
            "Bu bir hayal mi? 😵",
            "Herkes durakladı! ⏸️",
            "Bir sessizlik oldu! 🤐",
            "Herkes şaşırdı! 😲",
            "Bu akıl almaz! 🤯",
            "Herkes panik içinde! 😱",
            "Bu, tarihe geçecek! 📜",
            "Bunu unutmam! 🧠",
            "Herkes dondu kaldı! 🧊",
            "Bu bir şaka mı? 😅",
            "Her şey değişti bir anda! 🔄",
            "Bu inanılmaz! 😧",
            "Bu beklenmedikti! 😲",
            "Herkes şaşkın! 😵",
            "Bu, akıl almaz! 😳",
            "Bu, gerçek olamaz! 😱",
            "Herkes sessiz kaldı! 🤫",
        ]

    def getRandomResult(self):
        return random.choice(self.results)




