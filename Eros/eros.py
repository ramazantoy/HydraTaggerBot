import random

class ErosGenerator:
    def __init__(self):
        self.eros_messages = {
            (0, 20): [
                "Böyle aşkın ızdırabına, olmaz bu iş 🥲",
                "Aşk dediğin nane limon gibidir, acı ama ferahlatır 😅",
                "Bu ilişki, buz üstünde dans etmeye benziyor 🥶",
                "Aşk kuşu değil, kargalar uçuşuyor sanki 🐦",
                "Cupid'in oku hedefi ıska geçmiş gibi 🏹😬",
                "Bu ilişki, sıcak çöle düşen bir buz küpü gibi 🏜️❄️",
                "Aşk treni raydan çıkmış durumda 🚂💔",
                "İlişkiniz, yağmurda ıslanan kedi yavrusu gibi üzgün görünüyor 😿",
                "Aşk ateşiniz, sönmüş bir volkan gibi 🌋❄️",
                "Bu ilişki, tuzsuz yemek gibi biraz tatsız 🍲😕",
                "Aşkınız, kırık bir gitar teli gibi ahenksiz 🎸💔",
                "İlişkiniz, çölde susuz kalmış bir kaktüs gibi 🌵💧",
                "Aşk bahçenizde sadece dikenler büyüyor gibi 🥀",
                "Bu ilişki, kapalı bir hava gibi bunaltıcı ☁️😓",
                "Aşkınız, sönmüş bir mum gibi ışıltısını kaybetmiş 🕯️😔",
                "İlişkiniz, bozuk bir saat gibi ilerlemiyor ⏰🚫",
                "Bu aşk, yapboz gibi ama eksik parçalar var 🧩❓",
                "Aşkınız, kırık bir ayna gibi parçalanmış görünüyor 🪞💔",
                "İlişkiniz, eskimiş bir ayakkabı gibi rahat değil 👞😖",
                "Bu aşk hikayesi, mutlu sona ulaşamayan bir film gibi 🎬🚫"
            ],
            (21, 50): [
                "Bi çay içmelisiniz bence 🙃🥰",
                "Potansiyel var, biraz çaba ile yoluna girebilir 💪",
                "Orta şekerli bir ilişki, ne fazla tatlı ne de tatsız. Daha iyi olacak🍬",
                "Fırında pişen bir aşk, biraz daha pişerse lezzetlenecek 🥘",
                "İlişkiniz puzzle gibi, birkaç parça daha ekleyin tamamlanacak 🧩",
                "Aşkınız, yeni filizlenen bir tohum gibi bakım bekliyor 🌱",
                "İlişkiniz, ılık bir çay gibi, ne çok sıcak ne de soğuk ☕️",
                "Aşk bahçeniz sulanmayı bekleyen çiçekler gibi 🌼💦",
                "Bu ilişki, yeni öğrenilen bir dans gibi, pratikle güzelleşecek 💃🕺",
                "Aşkınız, güneşi bekleyen bir güneş paneli gibi ☀️🔋",
                "İlişkiniz, beslenmeyi bekleyen sevimli bir yavru kedi gibi 🐱🍼",
                "Bu aşk, mayalanmayı bekleyen bir hamur gibi 🥖⏳",
                "Aşkınız, ağır ağır demlenen bir çay gibi 🍵⏳",
                "İlişkiniz, yavaş yavaş olgunlaşan bir meyve gibi 🍎🌳",
                "Bu ilişki, sabırla örülen bir atkı gibi, emek istiyor 🧣✨",
                "Aşkınız, yeni yazılmaya başlanan bir kitap gibi, devamı gelecek 📚✍️",
                "İlişkiniz, yavaş yavaş ısınan bir motor gibi 😅🚗💨",
                "Bu aşk, sessiz sedasız büyüyen bir ağaç gibi 🌳😌",
                "Aşkınız, zamanla güzelleşen bir şarap gibi 🍷⏳",
                "İlişkiniz, kademe kademe yükselen bir merdiven gibi 🪜🆙"
            ],
            (51, 75): [
                "Güzel gidiyor, devam edin böyle 😊",
                "Aşk kuşları cıvıl cıvıl ötüyor 🐦❤️",
                "Bu ilişkinin aroması harika, devam edin 🌺",
                "Kalpler aynı ritimde atıyor gibi görünüyor 💓",
                "Yıldızlar sizin için parlıyor, romantizm havada 🌟",
                "Aşkınız, tam kıvamında pişmiş bir yemek gibi lezzetli 🍲😋",
                "İlişkiniz, uyumlu bir dans eden çift gibi 💃🕺",
                "Bu aşk, güneşli bir yaz günü kadar ısıtıcı ☀️😊",
                "Aşkınız, sakin bir göl gibi huzur veriyor 🏞️😌",
                "İlişkiniz, tatlı bir melodi gibi kulağa hoş geliyor 🎵💖",
                "Bu aşk, tam olgunlaşmış bir meyve gibi tatlı 🍑😍",
                "Aşkınız, rüzgârla savrulan tohumlar gibi hayat dolu 🌱💨",
                "İlişkiniz, sağlam temelli bir ev gibi güven veriyor 🏠💪",
                "Bu aşk, okyanusta usulca ilerleyen bir gemi gibi 🚢🌊",
                "Aşkınız, rengarenk bir gökkuşağı gibi göz alıcı 🌈😮",
                "İlişkiniz, uyumlu çalan bir orkestra gibi 🎻🎺",
                "Bu aşk, doğanın uyumu gibi mükemmel görünüyor 🏞️✨",
                "Aşkınız, karanlıkta parlayan bir ateş böceği gibi 🐞✨",
                "İlişkiniz, sabah güneşi gibi içinizi ısıtıyor 🌅😊",
                "Bu aşk, çiçek açmış bir bahar dalı gibi umut dolu 🌸🌿"
            ],
            (76, 100): [
                "Aşkınız destanlara konu olacak cinsten 📚❤️",
                "Cupid sizin için fazla mesai yapıyor 🏹😍",
                "Bu ne güzel aşk böyle, gözlerim kamaştı ✨",
                "Aşkınızın ateşi Güneş'i bile kıskandırıyor 🌞❤️",
                "Siz birbiriniz için yaratılmışsınız resmen 👩‍❤️‍👨",
                "İlişkiniz, masallardaki prenses ve prens gibi kusursuz 👑💖",
                "Aşkınız, galaksiler arası bir yolculuk gibi sonsuz 🚀🌌",
                "Bu ilişki, en güzel şiirin dizeleri gibi ahenkli 📜💕",
                "Aşkınız, çağlayan bir şelale gibi coşkulu ve güçlü 🏞️💪",
                "İlişkiniz, en tatlı rüyanın gerçeğe dönüşmüş hali 💤😍",
                "Bu aşk, iki kalbin mükemmel senfonisi gibi 🎵❤️",
                "Aşkınız, zamanı durduracak kadar etkileyici ⏱️😮",
                "İlişkiniz, en parlak yıldızdan bile daha ışıltılı ⭐✨",
                "Bu aşk, derin bir okyanus gibi sonsuz ve gizemli 🌊💙",
                "Aşkınız, en güzel tablonun ana teması gibi 🎨😍",
                "İlişkiniz, mükemmel uyumlu bir dans gibi 💃🕺",
                "Bu aşk, tüm zorlukları aşan bir süper kahraman gibi 🦸‍♀️🦸‍♂️",
                "Aşkınız, en lezzetli tatlıdan bile daha tatlı 🍰😋",
                "İlişkiniz, sonsuzluğa uzanan bir yol gibi 🛤️♾️",
                "Bu aşk, tüm evrenin merkezi gibi güçlü bir çekim yaratıyor 🌍🧲"
            ]
        }

    def get_random_message(self, rate):
        for range_tuple, messages in self.eros_messages.items():
            if range_tuple[0] <= rate <= range_tuple[1]:
                return random.choice(messages)
        return "Aşk her zaman bir sürprizdir 💖"