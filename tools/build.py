#!/usr/bin/env python3
"""Builds the CASAVISION static mock-up in two languages.

Outputs (repo root):
  index.html, <slug>.html            English
  ru/index.html, ru/<slug>.html      Russian
  .artifact/index.html               English home without the document wrapper (claude.ai Artifact)

Run:  python3 tools/build.py
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape

PHONE = "+971 50 306 5789"
WA = "https://wa.me/971503065789"
EMAIL = "casavisiondxb@gmail.com"
IG = "#"   # TODO: Instagram link from the client
LI = "#"   # TODO: LinkedIn link from the client

LANG = "en"
R = ""      # relative prefix to the site root ("" for EN, "../" for RU)


def t(en, ru):
    return ru if LANG == "ru" else en


def tr(d, k):
    """project field in the current language"""
    return d.get(k + "_ru", d[k]) if LANG == "ru" else d[k]


def services():
    return [t("Interior Design", "Дизайн интерьеров"),
            t("Creative & Design Direction", "Креативная дирекция и дизайн"),
            t("Branding & Brand Strategy", "Брендинг и бренд-стратегия"),
            t("Consultancy", "Консалтинг")]


# ---------------------------------------------------------------- projects
P = [
    dict(
        slug="fragments-de-paris", key="fragments", name="Fragments de Paris",
        kind="Residential interior", kind_ru="Жилой интерьер",
        where="Paris", where_ru="Париж",
        scope="Interior design, styling", scope_ru="Дизайн интерьера, стайлинг",
        words=["timeless", "balance", "monochrome", "opulent"], words_ru=["вне времени", "баланс", "монохром", "роскошь"],
        quote="Beauty is not decoration.", quote_ru="Красота — это не декор.",
        short="A Paris apartment designed as proof that some cities live inside you before you ever arrive. Every surface treats beauty as a way of taking the world seriously.",
        short_ru="Парижская квартира как доказательство того, что некоторые города живут в тебе ещё до приезда. Каждая поверхность относится к красоте как к способу серьёзно смотреть на мир.",
        brief="There are cities that live inside you before you ever arrive. Paris is one of them, and this apartment was designed to feel like the proof.",
        brief_ru="Есть города, которые живут внутри тебя ещё до того, как ты туда приедешь. Париж — один из них, и эта квартира задумана как доказательство.",
        idea="We believe that the most extraordinary spaces are not designed. They are distilled, from memory, from longing, from the courage to choose depth over novelty.",
        idea_ru="Мы верим, что самые удивительные пространства не проектируют, а дистиллируют: из памяти, из тоски, из смелости выбрать глубину вместо новизны.",
        mood="An invitation to live fully inside a vision of life that refuses to be ordinary: classical mouldings, quiet light, ivory and walnut, one gesture of opulence per room.",
        mood_ru="Приглашение жить внутри видения, которое отказывается быть обычным: классическая лепнина, тихий свет, слоновая кость и орех, один жест роскоши в каждой комнате.",
        result="Here, every surface carries the quiet conviction that beauty is not decoration, but a way of taking the world seriously.",
        result_ru="Каждая поверхность здесь несёт тихую уверенность: красота — не декор, а способ серьёзно относиться к миру.",
        hero="cover.jpg", wordimg="living.jpg",
        moodboard=[("m7.jpg", ""), ("m2.jpg", ""), ("m9.png", "cut"), ("m3.jpg", ""), ("m4.jpg", ""), ("m1.jpg", ""), ("m5.jpg", ""), ("m6.jpg", ""), ("m8.jpg", ""), ("m10.png", "cut")],
        gallery=[("living.jpg", "Living room", "Гостиная", "w-left"), ("living-detail.jpg", "Living room, detail", "Гостиная, деталь", "w-small-r"),
                 ("kitchen-sketch.jpg", "Kitchen, sketch", "Кухня, скетч", "w-half-l"), ("kitchen.jpg", "Kitchen, visualisation", "Кухня, визуализация", "w-half-r"),
                 ("bedroom.jpg", "Bedroom", "Спальня", "w-full"), ("bathroom.jpg", "Bathroom", "Ванная", "w-mid")],
        note=None,
    ),
    dict(
        slug="the-hold", key="hold", name="The Hold",
        kind="Specialty coffee shop", kind_ru="Спешелти-кофейня",
        where="Dubai", where_ru="Дубай",
        scope="Concept, interior design", scope_ru="Концепция, дизайн интерьера",
        words=["stillness", "desert", "spirit", "oasis"], words_ru=["тишина", "пустыня", "дух", "оазис"],
        quote="Where the desert taught us to be still and the coffee gave us a reason to stay.",
        quote_ru="Пустыня научила нас тишине, а кофе дал причину остаться.",
        short="A specialty coffee space that takes the Arabian desert as its design language. Sky pressed into blue panels, earth warmed into walnut, steel at the centre.",
        short_ru="Спешелти-кофейня, где языком дизайна стала Аравийская пустыня. Небо в голубых панелях, земля в тёплом орехе, сталь в центре.",
        brief="A conceptual proposal for a specialty coffee space in Dubai, developed as an independent design study. The Hold takes the Arabian desert as its primary design language, as philosophy rather than reference.",
        brief_ru="Концептуальное предложение спешелти-кофейни в Дубае, созданное как самостоятельное дизайн-исследование. The Hold берёт Аравийскую пустыню главным языком дизайна: как философию, а не как референс.",
        idea="The patience of the Arabian desert meets the precision of craft. A café designed around one radical idea: in Dubai, stillness is the greatest luxury of all.",
        idea_ru="Терпение Аравийской пустыни встречается с точностью ремесла. Кофейня построена вокруг одной радикальной идеи: в Дубае тишина — главная роскошь.",
        mood="Sand in motion, mirrored steel, walnut, a single blue sky. The board collects the textures of waiting and the ritual of a slow cup.",
        mood_ru="Песок в движении, зеркальная сталь, орех, одно голубое небо. Мудборд собирает фактуры ожидания и ритуал медленной чашки.",
        result="The desert holds its silence for a thousand years. We asked what a café would feel like if it held the same quality of stillness.",
        result_ru="Пустыня хранит тишину тысячу лет. Мы спросили себя, какой была бы кофейня, если бы в ней была та же тишина.",
        hero="cover.jpg", wordimg="seating.jpg",
        moodboard=[("m6.jpg", ""), ("m2.jpg", ""), ("m9.png", "cut"), ("m1.jpg", "mult"), ("m5.jpg", ""), ("m3.jpg", ""), ("m4.jpg", ""), ("m8.jpg", "")],
        gallery=[("island.jpg", "Coffee island", "Кофейный остров", "w-left"), ("seating.jpg", "Seating area", "Зона посадки", "w-small-r"),
                 ("bar-detail.jpg", "Brew bar, detail", "Брю-бар, деталь", "w-small-l"), ("@note", "", "", ""),
                 ("bar.jpg", "Coffee island and bar", "Кофейный остров и бар", "w-full")],
        note="Three forces hold it together: the sky pressed into blue panels above you, the earth warmed into walnut around you, and the steel at the centre that transforms the raw into the essential.",
        note_ru="Всё держат три силы: небо, вжатое в голубые панели над головой, земля, согретая в орехе вокруг, и сталь в центре, которая превращает сырое в главное.",
    ),
    dict(
        slug="confesso-milano", key="confesso", name="Confesso Milano",
        kind="Hair salon", kind_ru="Салон красоты",
        where="Milanese concept", where_ru="Миланская концепция",
        scope="Naming, concept, interior design", scope_ru="Нейминг, концепция, дизайн интерьера",
        words=["lightweight", "elegance", "exchanging", "freedom"], words_ru=["лёгкость", "элегантность", "общение", "свобода"],
        quote="Safe place to be yourself.", quote_ru="Место, где можно быть собой.",
        short="Naming, concept and interior for a hair salon inspired by Milanese beauty culture: a social destination where beauty, comfort and connection coexist.",
        short_ru="Нейминг, концепция и интерьер салона, вдохновлённого миланской бьюти-культурой: место встречи, где красота, комфорт и общение существуют вместе.",
        brief="Inspired by Milanese lifestyle and beauty culture, we developed a full concept including the naming and interior design of the space.",
        brief_ru="Вдохновившись миланским образом жизни и бьюти-культурой, мы разработали полную концепцию салона, включая нейминг и дизайн интерьера.",
        idea="The project transforms the traditional hair salon into a contemporary social sanctuary: a place to talk, laugh, share stories and experience transformation through beauty.",
        idea_ru="Проект превращает традиционный салон в современное социальное пространство: сюда приходят поговорить, посмеяться, поделиться историями и измениться через красоту.",
        mood="Openness, comfort and authenticity. Arches, terrazzo, burnished metal, warm plaster and the women who make a salon a meeting place.",
        mood_ru="Открытость, комфорт и подлинность. Арки, терраццо, состаренный металл, тёплая штукатурка и женщины, которые делают салон местом встречи.",
        result="A destination where everyone feels free to express their identity and leave feeling confident.",
        result_ru="Место, где каждый может свободно выражать себя и уходить с уверенностью.",
        hero="cover.jpg", wordimg="station.jpg",
        moodboard=[("m4.jpg", ""), ("m2.jpg", ""), ("m8.png", "cut"), ("m6.jpg", ""), ("m5.jpg", ""), ("m1.jpg", ""), ("m7.jpg", ""), ("m3.jpg", ""), ("m9.png", "cut")],
        gallery=[("reception.jpg", "Entrance and reception", "Вход и ресепшен", "w-full"),
                 ("plan.jpg", "Floor plan", "План", "w-small-l"), ("materials.jpg", "Materials", "Материалы", "w-small-r"),
                 ("@note", "", "", ""),
                 ("station.jpg", "Hair styling station", "Рабочее место стилиста", "w-small-l"), ("washing.jpg", "Washing area", "Зона мойки", "w-right")],
        note="Every surface was chosen as a love letter to Milan: its terrazzo floors, its burnished metals, its earth-toned plasters. Materials that age with grace and make a room feel like it has always belonged to the people inside it.",
        note_ru="Каждая поверхность выбрана как признание в любви Милану: полы из терраццо, состаренный металл, штукатурка землистых оттенков. Материалы красиво стареют, и комната ощущается так, будто всегда принадлежала людям внутри.",
    ),
    dict(
        slug="velvet-meadow", key="velvet", name="Velvet Meadow",
        kind="Spring / Summer event for Flabelus", kind_ru="Весенне-летний ивент для Flabelus",
        where="Castello di Reschio, Umbria", where_ru="Кастелло ди Решио, Умбрия",
        scope="Event concept, styling, activation", scope_ru="Концепция ивента, стайлинг, активация",
        words=["weightless", "energy", "wildflowers", "emotion"], words_ru=["невесомость", "энергия", "полевые цветы", "эмоция"],
        quote="Colour is not chosen but discovered.", quote_ru="Цвет не выбирают, его находят.",
        short="A countryside brunch for the Spring/Summer launch of Flabelus, born from one image: a woman walking barefoot through a field in full bloom.",
        short_ru="Загородный бранч для весенне-летнего запуска Flabelus, родившийся из одного образа: женщина идёт босиком по цветущему полю.",
        brief="For the Spring/Summer launch of Flabelus, we created a countryside brunch at Castello di Reschio. The concept was born from a single image: a woman walking barefoot through a field in full bloom, unhurried, unbothered, completely herself.",
        brief_ru="Для весенне-летнего запуска Flabelus мы придумали загородный бранч в Castello di Reschio. Концепция родилась из одного образа: женщина идёт босиком по цветущему полю, неспешно, безмятежно, оставаясь собой.",
        idea="This is the world Flabelus lives in: colour is discovered, comfort is a conviction, and every step feels like the ground is giving back.",
        idea_ru="Это мир, в котором живёт Flabelus: цвет находят, а не выбирают, комфорт — это убеждение, а каждый шаг ощущается так, будто земля отвечает тебе.",
        mood="Velvet Meadow is rooted in the kind of beauty that cannot be arranged: wild, saturated and alive. Every image here is a fragment of a single feeling.",
        mood_ru="Velvet Meadow — о красоте, которую нельзя расставить: дикой, насыщенной, живой. Каждый образ здесь — фрагмент одного чувства.",
        result="The particular freedom of a woman who has stopped trying to be careful and started trying to be present. This is not a mood. This is a manifesto.",
        result_ru="Особая свобода женщины, которая перестала стараться быть осторожной и начала быть здесь и сейчас. Это не настроение. Это манифест.",
        hero="cover.jpg", wordimg="table.jpg",
        moodboard=[("m5.jpg", ""), ("m4.jpg", ""), ("m7.png", "cut"), ("m3.jpg", ""), ("m6.jpg", ""), ("m2.jpg", ""), ("m1.jpg", "mult")],
        gallery=[("long-table.jpg", "The long table", "Длинный стол", "w-left"), ("table.jpg", "Stripes and wildflowers", "Полоски и полевые цветы", "w-small-r"),
                 ("@note", "", "", ""),
                 ("workshop.jpg", "Glassware painting workshop", "Мастер-класс по росписи бокалов", "w-small-l"), ("photomoment.jpg", "Photomoment area", "Фотозона", "w-right")],
        note="Tables dressed in bold stripes and crowned with wildflowers, set in the middle of a living, breathing meadow, as if the celebration had always belonged to the earth. Guests paint their own glassware: a playful moment to create, connect and bloom together.",
        note_ru="Столы в смелую полоску, украшенные полевыми цветами, посреди живого, дышащего луга, будто праздник всегда принадлежал земле. Гости сами расписывают бокалы: игривый момент, чтобы творить, общаться и расцветать вместе.",
    ),
    dict(
        slug="sliceit", key="slice", name="SLICEit",
        kind="Pizza pop-up", kind_ru="Поп-ап пиццерии",
        where="Dubai", where_ru="Дубай",
        scope="Concept, naming, identity, pop-up design", scope_ru="Концепция, нейминг, айдентика, дизайн поп-апа",
        words=["young", "bold", "diverse", "contemporary"], words_ru=["молодость", "смелость", "разнообразие", "современность"],
        quote="Just the good part.", quote_ru="Только самое вкусное.",
        short="A pizza pop-up with its own identity: one perfect slice, from a window, in under a minute. New York state of mind wrapped in Italian soul.",
        short_ru="Поп-ап пиццерии со своей айдентикой: один идеальный кусок, из окна, меньше чем за минуту. Нью-йоркский характер с итальянской душой.",
        brief="SLICEit was born from the most honest craving in the world: a single, perfect slice, hot from a wood-fired oven, eaten standing up, no occasion required.",
        brief_ru="SLICEit родился из самого честного желания в мире: один идеальный кусок пиццы из дровяной печи, который едят стоя, без всякого повода.",
        idea="In a city that does everything at scale, we asked a different question: what if the best pizza in Dubai came in one piece, from a window, in under a minute?",
        idea_ru="В городе, где всё делают с размахом, мы задали другой вопрос: что, если лучшая пицца в Дубае будет одним куском, из окна, меньше чем за минуту?",
        mood="Fire, steel, and a slice that speaks for itself. Every detail is turned up: the red is redder, the crust is louder.",
        mood_ru="Огонь, сталь и кусок, который говорит сам за себя. Каждая деталь на максимуме: красный краснее, корочка громче.",
        result="Designed to be remembered after a single visit. This is not fast food. This is fast confidence.",
        result_ru="Сделано, чтобы запомниться после первого визита. Это не фастфуд. Это быстрая уверенность.",
        hero="cover.jpg", wordimg="box.jpg",
        moodboard=[("m4.jpg", ""), ("m1.jpg", ""), ("m8.png", "cut"), ("m6.jpg", ""), ("m7.jpg", ""), ("m3.jpg", ""), ("m5.jpg", ""), ("m2.jpg", "")],
        gallery=[("front.jpg", "Front view", "Вид спереди", "w-left"), ("box.jpg", "Packaging", "Упаковка", "w-small-r"),
                 ("d1.jpg", "Identity in use", "Айдентика в деле", "w-small-l"), ("@note", "", "", ""),
                 ("d2.jpg", "Slice wrap", "Обёртка для куска", "w-small-l"), ("side.jpg", "Side view", "Вид сбоку", "w-right")],
        note="Bold red on white, a logotype with personality to spare, and product shots so unapologetic they make you hungry before you finish looking. The identity was built to stop people mid-scroll and mid-street.",
        note_ru="Смелый красный на белом, логотип с характером и фотографии продукта, от которых хочется есть ещё до конца просмотра. Айдентика сделана так, чтобы останавливать людей и в ленте, и на улице.",
    ),
    dict(
        slug="sensorial-dive", key="sensorial", name="Sensorial Dive",
        kind="Fragrance pop-up for Gucci", kind_ru="Парфюмерный поп-ап для Gucci",
        where="Immersive pop-up", where_ru="Иммерсивный поп-ап",
        scope="Concept, spatial design, experience", scope_ru="Концепция, пространство, опыт",
        words=["water flow", "reflection", "botanical", "structural"], words_ru=["поток воды", "отражение", "ботаника", "структура"],
        quote="How deep are you willing to go?", quote_ru="Насколько глубоко вы готовы погрузиться?",
        short="A fragrance pop-up for Gucci built around one question: what if a fragrance were not something you wore, but somewhere you went?",
        short_ru="Парфюмерный поп-ап для Gucci, построенный вокруг одного вопроса: что, если аромат — это не то, что носят, а место, куда приходят?",
        brief="Sensorial Dive was born from a single question: what if a fragrance were not something you wore, but somewhere you went?",
        brief_ru="Sensorial Dive родился из одного вопроса: что, если аромат — это не то, что носят, а место, куда приходят?",
        idea="A corridor that pulls you forward, a light that beckons from the end, a room that blooms open like a secret. An immersive world built around the most intimate thing Gucci makes, and you are the one diving in.",
        idea_ru="Коридор, который тянет вперёд, свет, который манит из глубины, комната, раскрывающаяся как секрет. Иммерсивный мир вокруг самого личного, что делает Gucci, и погружаетесь в него вы.",
        mood="The references move between the botanical and the surreal: water flow and structural glass, reflection and dissolution, the precision of a bottle and the abandon of a garden in full bloom.",
        mood_ru="Референсы движутся между ботаникой и сюрреализмом: поток воды и структурное стекло, отражение и растворение, точность флакона и свобода сада в полном цвету.",
        result="Nature here is not decoration, it is architecture. Purple bleeds into pink bleeds into the memory of a scent you cannot name but have always known.",
        result_ru="Природа здесь — не декор, а архитектура. Фиолетовый перетекает в розовый, а розовый — в память об аромате, который не можешь назвать, но знал всегда.",
        hero="cover.jpg", wordimg="corridor.jpg",
        moodboard=[("m1.jpg", ""), ("m3.jpg", ""), ("m6.jpg", ""), ("m2.jpg", ""), ("m5.jpg", ""), ("m4.jpg", ""), ("m7.png", "cut")],
        gallery=[("room.jpg", "Fragrance room", "Комната ароматов", "w-left"), ("corridor.jpg", "The Deep Reveal", "Финальный коридор", "w-small-r"),
                 ("@note", "", "", ""),
                 ("diagram.jpg", "Spatial concept", "Пространственная концепция", "w-full"), ("plan.jpg", "Pavilion", "Павильон", "w-mid")],
        note="A digital screen of nature, water and Gucci aesthetic. A botanical plinth for each fragrance, with a bespoke floral arrangement that mirrors its notes. And at the corridor's end, a beckoning purple light that invites guests to submerge themselves in the brand's story.",
        note_ru="Цифровой экран с природой, водой и эстетикой Gucci. Ботанический подиум для каждого аромата с авторской флористикой по его нотам. А в конце коридора манящий фиолетовый свет, приглашающий погрузиться в историю бренда.",
    ),
]
BY = {p["key"]: p for p in P}


def img(p, f):
    return f"{R}assets/img/{p['key']}/{f}"


def home_href():
    return "index.html"


def other_lang(page):
    """link to the same page in the other language"""
    return f"../{page}" if LANG == "ru" else f"ru/{page}"


# ---------------------------------------------------------------- partials
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Raleway:wght@300;400;500;600&display=swap">')


def head(title, desc, artifact=False, extra=""):
    meta = (f'<title>{E(title)}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            f'<meta name="description" content="{E(desc)}">\n{FONTS}\n<link rel="stylesheet" href="{R}assets/css/site.css">\n'
            f'<link rel="icon" href="{R}assets/brand/monogram.png">\n{extra}')
    if artifact:
        return meta + "\n"
    return (f'<!doctype html>\n<html lang="{LANG}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'{meta}\n</head>\n<body>\n')


def preloader():
    return f'''<div class="preloader" aria-hidden="true">
  <div class="pl-in">
    <span class="pl-mono"></span>
    <span class="pl-logo"></span>
    <span class="pl-bar"><i></i></span>
    <span class="pl-meta label"><span>{t("Dubai, UAE", "Дубай, ОАЭ")}</span><span class="pl-num">0</span></span>
  </div>
</div>
<div class="curtain" aria-hidden="true"><span class="pl-mono"></span></div>
'''


def lang_switch(page):
    en_cls = ' class="is-on"' if LANG == "en" else ""
    ru_cls = ' class="is-on"' if LANG == "ru" else ""
    en_href = page if LANG == "en" else f"../{page}"
    ru_href = f"ru/{page}" if LANG == "en" else page
    return f'<span class="lang label"><a href="{en_href}"{en_cls} lang="en" data-go>EN</a><a href="{ru_href}"{ru_cls} lang="ru" data-go>RU</a></span>'


def header(home, page):
    h = "#" if home else "index.html#"
    return f'''{preloader()}<header class="hdr wrap">
  <div class="grid">
    <a class="brand" href="{'#top' if home else 'index.html'}"{'' if home else ' data-go'} aria-label="CASAVISION"><span class="mono"></span><span class="logo"></span></a>
    <span class="hdr-loc label">{t("Dubai, UAE", "Дубай, ОАЭ")}</span>
    <a class="hdr-cta label" href="{h}contact">{t("Tell us about your project", "Обсудить проект")}</a>
    <a class="hdr-wa label" href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
    <span class="hdr-lang">{lang_switch(page)}</span>
    <button class="hdr-menu label" type="button" data-menu-open aria-controls="menu" aria-expanded="false"><span class="burger" aria-hidden="true"><span></span><span></span></span>{t("Menu", "Меню")}</button>
  </div>
</header>
'''


def menu(home, page):
    h = "#" if home else "index.html#"
    go = "" if home else " data-go"
    items = [
        (t("Home", "Главная"), "#top" if home else "index.html", "assets/img/home/cave.jpg", t("CASAVISION, creative atelier", "CASAVISION, креативное ателье"), ""),
        (t("About", "О нас"), f"{h}about", "assets/img/fragments/living.jpg", t("Philosophy and values", "Философия и ценности"),
         f'<a href="{h}approach"{go}>{t("How we work", "Как мы работаем")}</a><a href="{h}beliefs"{go}>{t("What we believe in", "Наши ценности")}</a>'),
        (t("Services", "Услуги"), f"{h}services", "assets/img/confesso/reception.jpg", t("Four disciplines, one team", "Четыре направления, одна команда"),
         "".join(f'<a href="{h}services"{go}>{E(s)}</a>' for s in services())),
        (t("Projects", "Проекты"), f"{h}projects", "assets/img/velvet/long-table.jpg", t("Six stories from the portfolio", "Шесть историй из портфолио"),
         "".join(f'<a href="{p["slug"]}.html" data-go>{E(p["name"])}</a>' for p in P)),
        (t("Contact", "Контакты"), f"{h}contact", "assets/img/hold/island.jpg", t("Tell us about your project", "Расскажите о своём проекте"), ""),
    ]
    nav = "\n".join(
        f'''      <div class="mn-item" data-cap="{E(cap)}"><a class="mn-link" href="{href}"{go if href.startswith('index') else ''}>{E(tt)}</a><div class="mn-sub">{sub}</div></div>'''
        for tt, href, im, cap, sub in items)
    imgs = "".join(f'<img src="{R}{im}" alt=""{" class=\"is-on\"" if i == 0 else ""} loading="lazy">' for i, (tt, href, im, cap, sub) in enumerate(items))
    return f'''<div class="menu" id="menu" aria-hidden="true">
  <div class="menu-panel wrap" role="dialog" aria-modal="true" aria-label="{t('Menu', 'Меню')}">
    <div class="menu-top grid">
      <a class="brand" href="{'#top' if home else 'index.html'}"{go} aria-label="CASAVISION"><span class="mono"></span><span class="logo"></span></a>
      <span class="menu-lang">{lang_switch(page)}</span>
      <button class="menu-close label" type="button" data-menu-close>{t("Close", "Закрыть")} <span class="x" aria-hidden="true"></span></button>
    </div>
    <div class="menu-body grid">
      <nav class="menu-nav" aria-label="{t('Main', 'Основное')}">
{nav}
      </nav>
      <figure class="menu-preview" aria-hidden="true">{imgs}<figcaption class="label">{items[0][3]}</figcaption></figure>
    </div>
    <div class="menu-info grid">
      <div><span class="label">{t("Write to us", "Написать нам")}</span><a href="mailto:{EMAIL}">{EMAIL}</a><span>{PHONE}</span></div>
      <div><span class="label">{t("Socials", "Соцсети")}</span><a href="{IG}">Instagram</a><a href="{LI}">LinkedIn</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
      <div><span class="label">{t("Studio", "Студия")}</span><span>CASAVISION L.L.C-FZ</span><span>{t("Dubai, United Arab Emirates", "Дубай, Объединённые Арабские Эмираты")}</span></div>
      <div class="mi-cta"><span class="label">{t("New project", "Новый проект")}</span><a class="btn" href="{h}contact"{go}>{t("Tell us about your project", "Обсудить проект")} <i></i></a></div>
    </div>
  </div>
</div>
'''


def footer(home):
    h = "#" if home else "index.html#"
    go = "" if home else " data-go"
    return f'''<footer class="ftr tone-ink" data-tone="dark">
  <div class="wrap">
    <div class="grid ftr-cols">
      <div class="fc-1"><p>{t("Creative atelier for spaces, brands and moments. Dubai, UAE and international.", "Креативное ателье пространств, брендов и событий. Дубай, ОАЭ и международные проекты.")}</p></div>
      <div class="fc-2"><span class="label">{t("Menu", "Меню")}</span><a href="{'#top' if home else 'index.html'}"{go}>{t("Home", "Главная")}</a><a href="{h}about"{go}>{t("About", "О нас")}</a><a href="{h}services"{go}>{t("Services", "Услуги")}</a><a href="{h}projects"{go}>{t("Projects", "Проекты")}</a><a href="{h}contact"{go}>{t("Contact", "Контакты")}</a></div>
      <div class="fc-3"><span class="label">{t("Services", "Услуги")}</span>{''.join(f'<a href="{h}services"{go}>{E(s)}</a>' for s in services())}</div>
      <div class="fc-4"><span class="label">{t("Socials", "Соцсети")}</span><a href="{IG}">Instagram</a><a href="{LI}">LinkedIn</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
      <div class="fc-5"><span class="label">{t("Contact", "Контакты")}</span><a href="mailto:{EMAIL}">{EMAIL}</a><span>{PHONE}</span></div>
    </div>
    <div class="ftr-mark" aria-hidden="true"><div class="blurmark" data-fit="1" data-focus="0.16" data-focus-min="0.035">CASAVISION</div></div>
    <div class="ftr-base"><span>© <span data-year>2026</span> CASAVISION Creative Atelier L.L.C-FZ</span><a href="#">{t("Privacy policy", "Политика конфиденциальности")}</a><span>{t("Dubai, UAE", "Дубай, ОАЭ")}</span></div>
  </div>
</footer>
<script src="{R}assets/js/site.js"></script>
'''


def btn(href, label, extra=""):
    return f'<a class="more{(" " + extra) if extra else ""}" href="{href}" data-go>{label} <i></i></a>'


def case_meta(p, n):
    words = " · ".join(tr(p, "words"))
    vp = t("View project", "Смотреть проект")
    return f'''<div class="cm-cat label" data-r><span class="cm-num mute">{n:02d} / 06</span>{E(tr(p, "kind"))}</div>
        <p class="cm-desc" data-r style="--d:.1s">{E(tr(p, "short"))}</p>
        <div class="cm-head" data-r style="--d:.15s"><h3 class="cm-title"><a href="{p["slug"]}.html" data-go>{E(p["name"])}</a></h3><span class="cm-words">{E(words)}</span></div>
        <div class="cm-link" data-r style="--d:.2s">{btn(p["slug"] + ".html", vp)}</div>
        <div class="cm-loc" data-r style="--d:.25s">{E(tr(p, "where"))}</div>'''


# ---------------------------------------------------------------- home
def home(artifact=False):
    f, h_, c, v, s, g = (BY[k] for k in ("fragments", "hold", "confesso", "velvet", "slice", "sensorial"))
    vp = t("View project", "Смотреть проект")
    sv = services()
    seen = [t("Fragments de Paris, The Hold, Confesso Milano", "Fragments de Paris, The Hold, Confesso Milano"),
            t("Velvet Meadow, Sensorial Dive", "Velvet Meadow, Sensorial Dive"),
            t("SLICEit, Confesso Milano", "SLICEit, Confesso Milano"),
            t("Alongside every project", "В каждом проекте")]
    svc_data = [
        (t("Spaces lived, felt, and remembered.", "Пространства, которые проживают, чувствуют и помнят."),
         t("We design interiors that go beyond aesthetics, beginning with listening to the brief, the building and the people who will inhabit it. The result is always specific, never generic.",
           "Проектируем интерьеры, которые больше, чем эстетика. Начинаем с того, что слушаем бриф, здание и людей, которые будут там жить. Результат всегда конкретный, никогда не типовой."),
         [t("Residential", "Жилые интерьеры"), "HoReCa", t("Retail & commercial", "Ритейл и коммерция")]),
        (t("Vision before execution. Always.", "Сначала видение, потом исполнение."),
         t("Concept, visual language and styling for spaces, pop-ups, activations and events. For clients who need a point of view before they need a floor plan.",
           "Концепция, визуальный язык и стайлинг для пространств, поп-апов, активаций и ивентов. Для тех, кому сначала нужна точка зрения, а уже потом планировка."),
         [t("Concept development", "Разработка концепции"), t("Styling", "Стайлинг"), t("Pop-ups", "Поп-апы"), t("Activations", "Активации"), t("Events", "Ивенты")]),
        (t("Whole from the first day.", "Цельный с первого дня."),
         t("For brands that are just appearing: concept, naming, positioning and identity, so the brand is coherent from day one and ready for its first space.",
           "Для брендов, которые только появляются: концепция, нейминг, позиционирование и айдентика, чтобы бренд был цельным с первого дня и готовым к своему первому пространству."),
         [t("Concept", "Концепция"), t("Naming", "Нейминг"), t("Positioning", "Позиционирование"), t("Identity", "Айдентика")]),
        (t("Clarity is the rarest luxury.", "Ясность — самая редкая роскошь."),
         t("For clients who need more than execution: strategy, project management and space planning, with the human insight that only comes from experience.",
           "Для тех, кому нужно больше, чем исполнение: стратегия, управление проектом и планировка, с пониманием людей, которое приходит только с опытом."),
         [t("Client advisory", "Консультации"), t("Strategy", "Стратегия"), t("Project management", "Управление проектом"), t("Space planning", "Планировка")]),
    ]
    services_html = []
    for i, (line, body, tags) in enumerate(svc_data):
        name = sv[i]
        services_html.append(f'''      <div class="svc{' is-open' if i == 0 else ''}" data-r>
        <button class="svc-row grid" type="button" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="svc-{i}">
          <span class="svc-tag label">{t("Seen in", "В проектах")}: {E(seen[i])}</span>
          <span class="svc-name">{E(name)}</span>
          <span class="svc-line">{E(line)}</span>
          <span class="svc-plus" aria-hidden="true"></span>
        </button>
        <div class="svc-body" id="svc-{i}"><div><div class="svc-inner grid">
          <p>{E(body)}</p>
          <div class="svc-tags">{''.join(f'<span>{E(x)}</span>' for x in tags)}</div>
          <div class="svc-cta"><a class="more" href="#contact" data-service="{i}">{t("Discuss a project", "Обсудить проект")} <i></i></a></div>
        </div></div></div>
      </div>''')

    steps = [
        (t("Conversation", "Разговор"), t("We start by listening: who you are, what you are launching and who it is for.", "Слушаем: кто вы, что запускаете и для кого.")),
        (t("Research", "Исследование"), t("We study the audience, the client, the brand and the market. The design follows these findings.", "Изучаем аудиторию, клиента, бренд и рынок. Дизайн следует этим выводам.")),
        (t("Concept", "Концепция"), t("One strong idea and a story that belongs to this project only.", "Одна сильная идея и история, которая принадлежит только этому проекту.")),
        (t("Moodboard", "Мудборд"), t("Images, materials and the key words of the concept, like stillness, desert, oasis.", "Образы, материалы и ключевые слова концепции: тишина, пустыня, оазис.")),
        (t("Design", "Дизайн"), t("Space, identity and visualisations developed around that one idea.", "Пространство, айдентика и визуализации вокруг этой одной идеи.")),
        (t("Realisation", "Реализация"), t("We stay with the project through to the opening, the event or the first point of sale.", "Ведём проект до открытия, события или первой точки продаж.")),
    ]
    beliefs = [
        (t("Human First", "Человек прежде всего"), t("Every brief begins not with dimensions, but with understanding who will live inside the work. People are not the audience. They are the origin.",
                                                    "Каждый бриф начинается не с размеров, а с понимания того, кто будет жить внутри. Люди — не аудитория. Они — начало.")),
        (t("Collective Intelligence", "Коллективный разум"), t("The atelier is a meeting point. Designers, clients, artisans and collaborators think together, because the best ideas are never the product of a single mind.",
                                                             "Ателье — место встречи. Дизайнеры, клиенты, мастера и партнёры думают вместе, потому что лучшие идеи не рождаются в одной голове.")),
        (t("Cultural Depth", "Культурная глубина"), t("Rooted in Italian design culture, we draw from history and craft, not from trends. Our work is grounded, but never static.",
                                                    "Мы опираемся на итальянскую культуру дизайна, историю и ремесло, а не на тренды. Наша работа укоренена, но не статична.")),
        (t("Conviction in Detail", "Убеждённость в деталях"), t("Nothing in a CASAVISION project is accidental. Every material, every object, every line is a position taken.",
                                                               "В проекте CASAVISION нет ничего случайного. Каждый материал, предмет и линия — это занятая позиция.")),
        (t("Vision for Longevity", "Взгляд на десятилетия"), t("We design for the people who will inhabit a space in twenty years, not just the ones who commission it today.",
                                                             "Проектируем для тех, кто будет жить в пространстве через двадцать лет, а не только для тех, кто заказывает его сегодня.")),
        (t("Warmth & Rigour", "Тепло и точность"), t("The care of a home and the precision of an atelier, always together. Emotion and craft are the same thing, seen differently.",
                                                   "Забота дома и точность ателье, всегда вместе. Эмоция и ремесло — одно и то же, увиденное по-разному.")),
    ]
    chips = sv + [t("Not sure yet", "Пока не знаю")]
    hw = tr(h_, "words")

    body = f'''{header(True, "index.html")}{menu(True, "index.html")}
<main id="top">

  <!-- HERO -->
  <section class="hero" data-tone="dark">
    <div class="hero-media"><video autoplay muted loop playsinline preload="auto" poster="{R}assets/video/hero-poster.jpg"><source src="{R}assets/video/hero.mp4" type="video/mp4" media="(min-width: 761px)"><source src="{R}assets/video/hero-720.mp4" type="video/mp4"></video></div>
    <div class="hero-in wrap">
      <div class="grid hero-top">
        <div class="hero-lead">
          <span class="label" data-r>{t("Creative atelier", "Креативное ателье")} <span class="sq gold"></span> {t("Dubai, UAE", "Дубай, ОАЭ")}</span>
          <p data-r style="--d:.15s">{t("We design spaces, brands and moments that say something.", "Создаём пространства, бренды и события, которым есть что сказать.")}</p>
        </div>
        <ul class="hero-list" data-r style="--d:.3s">{''.join(f'<li>{E(x)}</li>' for x in sv)}</ul>
      </div>
      <div class="grid hero-bottom">
        <a class="hero-card" href="{f['slug']}.html" data-go data-r style="--d:.45s">
          <span class="hc-txt"><span class="label mute">{t("Featured", "Избранное")}</span><span class="hc-title">{E(f['name'])}</span><span>{E(tr(f, 'kind'))}, {E(tr(f, 'where'))}</span><span class="more">{vp} <i></i></span></span>
          <span class="hc-img"><img src="{img(f, 'living.jpg')}" alt="{t('Living room of the Fragments de Paris apartment', 'Гостиная квартиры Fragments de Paris')}"></span>
        </a>
        <h1 class="masthead" data-r style="--d:.25s"><span class="mh-word" data-fit="1" data-fit-h="0.24">CASAVISION</span><span class="mh-sub">Creative atelier</span></h1>
      </div>
    </div>
  </section>

  <!-- ABOUT -->
  <section class="intro tone-light" id="about" data-tone="light">
    <div class="blurmark" aria-hidden="true" data-shadow>CASAVISION</div>
    <div class="wrap">
      <div class="grid intro-head">
        <span class="label" data-r>{t("About the atelier", "Об ателье")}</span>
        <p class="intro-statement" data-haze>{t("Every project begins with a conversation and <em>one strong idea</em>. That idea runs through everything: the space, the brand, the event.",
                                                "Каждый проект начинается с разговора и <em>одной сильной идеи</em>. Дальше она проходит через всё: пространство, бренд, событие.")}</p>
      </div>
      <div class="grid intro-cols">
        <p class="ic-a" data-haze>{t("CASAVISION is a creative atelier based in Dubai, working across the UAE and internationally. We bring an Italian design sensibility: the kind that respects the past, understands the present and builds for what comes next.",
                                    "CASAVISION — креативное ателье из Дубая. Работаем в ОАЭ и за их пределами. Привносим итальянское чувство дизайна: уважение к прошлому, понимание настоящего и взгляд в будущее.")}</p>
        <p class="ic-b" data-haze>{t("Each project starts with research into the audience, the client, the brand and the market. The design follows those findings rather than trends or ready-made templates.",
                                    "Каждый проект начинается с анализа аудитории, клиента, бренда и рынка. Дизайн строится на этих выводах, а не на трендах и готовых шаблонах.")}</p>
        <div class="ic-c" data-r style="--d:.2s"><a class="more" href="#approach">{t("How we work", "Как мы работаем")} <i></i></a></div>
      </div>
      <div class="grid facts">
        <div class="fact" data-r><b>{t("One team", "Одна команда")}</b><p>{t("Brand, space and activation are led by one team, so everything speaks the same language.", "Бренд, пространство и активацию ведёт одна команда, поэтому всё говорит на одном языке.")}</p></div>
        <div class="fact" data-r style="--d:.1s"><b>{t("From name to first store", "От названия до первой точки")}</b><p>{t("We can take a brand from the first idea and its name to the first point of sale.", "Можем провести бренд с нуля: от идеи и нейминга до первой точки продаж.")}</p></div>
        <div class="fact" data-r style="--d:.2s"><b>{t("Made from scratch", "Всё с нуля")}</b><p>{t("Every concept is written for one client and one story. No typical solutions.", "Каждая концепция пишется под одного клиента и одну историю. Без типовых решений.")}</p></div>
      </div>
    </div>
  </section>

  <!-- PROJECTS -->
  <section id="projects" class="tone-dark" data-tone="dark">
    <div class="wrap works-head">
      <div class="grid sec-head">
        <span class="label" data-r>{t("Selected works", "Избранные проекты")}</span>
        <h2 data-r style="--d:.1s">{t("Projects told as <em>stories</em>", "Проекты как <em>истории</em>")}</h2>
        <p data-r style="--d:.2s">{t("Every project here began as a conversation. Each case shows how we think, from the brief and the moodboard to the finished space.", "Каждый проект здесь начался с разговора. В кейсах видно, как мы думаем: от брифа и мудборда до готового пространства.")}</p>
      </div>
    </div>
  </section>

  <!-- 01 wide image -->
  <article class="case case-a tone-light" data-tone="light">
    <div class="wrap">
      <a class="media" href="{f['slug']}.html" data-go data-r="img" aria-label="{E(f['name'])}"><img src="{img(f, 'bedroom.jpg')}" alt="{t('Bedroom with classical mouldings', 'Спальня с классической лепниной')}" loading="lazy"></a>
      <div class="grid cm">
        {case_meta(f, 1)}
      </div>
    </div>
  </article>

  <!-- 02 image right, concept words over it -->
  <article class="case case-b tone-dark" data-tone="dark">
    <div class="wrap">
      <div class="grid cb-stage">
        <a class="media" href="{h_['slug']}.html" data-go data-r="img" aria-label="{E(h_['name'])}"><img src="{img(h_, 'island.jpg')}" alt="{t('Steel coffee island under a blue stone canopy', 'Стальной кофейный остров под голубым каменным козырьком')}" loading="lazy"></a>
        <div class="cb-words" aria-hidden="true"><span data-r="word">{E(hw[0])}</span><span data-r="word" style="--d:.25s">{E(hw[1])}</span><span data-r="word" style="--d:.5s">{E(hw[3])}</span></div>
      </div>
      <div class="grid cm">
        {case_meta(h_, 2)}
      </div>
    </div>
  </article>

  <!-- 03 two images, different places -->
  <article class="case case-c tone-light" data-tone="light">
    <div class="wrap">
      <div class="grid cc">
        <a class="media cc-1" href="{c['slug']}.html" data-go data-r="img" aria-label="{E(c['name'])}"><img src="{img(c, 'cover.jpg')}" alt="{t('Two women talking in the salon', 'Две женщины разговаривают в салоне')}" loading="lazy"></a>
        <a class="media cc-2" href="{c['slug']}.html" data-go data-r="img" style="--d:.2s" aria-label="{E(c['name'])}"><img src="{img(c, 'washing.jpg')}" alt="{t('Washing area under a marble arch', 'Зона мойки под мраморной аркой')}" loading="lazy"></a>
        <div class="cc-txt" data-r>
          <p class="cc-quote">“{E(tr(c, 'quote'))}”</p>
          <p>{E(tr(c, 'short'))}</p>
        </div>
        <div class="cc-head">
          <div class="cm-head" data-r><span class="label"><span class="mute">03 / 06</span> <span class="sq gold"></span>{E(tr(c, 'kind'))}</span><h3 class="cm-title"><a href="{c['slug']}.html" data-go>{E(c['name'])}</a></h3><span class="cm-words">{E(' · '.join(tr(c, 'words')))}</span></div>
          <div class="cm-link" data-r style="--d:.1s">{btn(c['slug'] + '.html', vp)}</div>
          <div class="cm-loc" data-r style="--d:.15s">{E(tr(c, 'where'))}</div>
        </div>
      </div>
    </div>
  </article>

  <!-- 04 full-screen colour band -->
  <article class="case case-d tone-sky" data-tone="light">
    <div class="wrap">
      <div class="grid cd">
        <a class="media cd-1" href="{v['slug']}.html" data-go data-r="img" aria-label="{E(v['name'])}" data-par="0.06"><img src="{img(v, 'cover.jpg')}" alt="{t('Women in a field of wildflowers', 'Девушки в поле полевых цветов')}" loading="lazy"></a>
        <a class="media cd-2" href="{v['slug']}.html" data-go data-r="img" style="--d:.2s" aria-label="{E(v['name'])}"><img src="{img(v, 'photomoment.jpg')}" alt="{t('Mirrored photomoment installation in the meadow', 'Зеркальная фотозона посреди луга')}" loading="lazy"></a>
        <h3 class="cd-title" data-r="word" style="--d:.3s"><a href="{v['slug']}.html" data-go>Velvet<em>Meadow</em></a></h3>
        <img class="cd-flower" src="{img(v, 'm7.png')}" alt="" aria-hidden="true" data-par="-0.18" loading="lazy">
      </div>
      <div class="grid cm">
        <div class="cm-cat label" data-r><span class="cm-num mute">04 / 06</span>{E(tr(v, 'kind'))}</div>
        <p class="cm-desc" data-r style="--d:.1s">{E(tr(v, 'short'))}</p>
        <div class="cm-head" data-r style="--d:.15s"><span class="cm-words">{E(' · '.join(tr(v, 'words')))}</span></div>
        <div class="cm-link" data-r style="--d:.2s">{btn(v['slug'] + '.html', vp)}</div>
        <div class="cm-loc" data-r style="--d:.25s">{E(tr(v, 'where'))}</div>
      </div>
    </div>
  </article>

  <!-- 05 two images, showroom rhythm -->
  <article class="case case-e tone-dark" data-tone="dark">
    <div class="wrap">
      <div class="grid ce">
        <a class="media ce-1" href="{s['slug']}.html" data-go data-r="img" aria-label="{E(s['name'])}"><img src="{img(s, 'box.jpg')}" alt="{t('SLICEit pizza boxes on a steel chair', 'Коробки SLICEit на стальном стуле')}" loading="lazy"></a>
        <a class="media ce-2" href="{s['slug']}.html" data-go data-r="img" style="--d:.2s" aria-label="{E(s['name'])}"><img src="{img(s, 'front.jpg')}" alt="{t('Front view of the SLICEit pop-up window', 'Окно поп-апа SLICEit')}" loading="lazy"></a>
      </div>
      <div class="grid cm">
        {case_meta(s, 5)}
      </div>
    </div>
  </article>

  <!-- 06 image left, text right -->
  <article class="case case-f tone-light" data-tone="light">
    <div class="wrap">
      <div class="grid cf">
        <a class="media cf-1" href="{g['slug']}.html" data-go data-r="img" aria-label="{E(g['name'])}"><img src="{img(g, 'room.jpg')}" alt="{t('Pink fragrance room with a botanical plinth', 'Розовая комната ароматов с ботаническим подиумом')}" loading="lazy"></a>
        <div class="cf-side">
          <div data-r><span class="label"><span class="mute">06 / 06</span> <span class="sq gold"></span>{E(tr(g, 'kind'))}</span><p class="cm-desc" style="margin-top:22px">{E(tr(g, 'short'))}</p></div>
          <div class="cf-bottom" data-r style="--d:.15s">
            <h3 class="cm-title"><a href="{g['slug']}.html" data-go>{E(g['name'])}</a></h3>
            <span class="cm-words">{E(' · '.join(tr(g, 'words')))}</span>
            <div class="cf-row">{btn(g['slug'] + '.html', vp)}<span class="label mute">{E(tr(g, 'where'))}</span></div>
          </div>
        </div>
      </div>
    </div>
  </article>

  <!-- SERVICES -->
  <section class="services tone-ink" id="services" data-tone="dark">
    <div class="wrap">
      <div class="grid sec-head">
        <span class="label" data-r>{t("Services", "Услуги")}</span>
        <h2 data-r style="--d:.1s">{t("Four disciplines, <em>one language</em>", "Четыре направления, <em>один язык</em>")}</h2>
        <p data-r style="--d:.2s">{t("Prices are not published: every project is calculated individually, on request.", "Цены не публикуем: каждый проект считаем индивидуально, по запросу.")}</p>
      </div>
      <div class="svc-list">
{chr(10).join(services_html)}
      </div>
    </div>
  </section>

  <!-- APPROACH -->
  <section class="approach tone-light" id="approach" data-tone="light">
    <div class="wrap">
      <div class="grid sec-head">
        <span class="label" data-r>{t("How we work", "Как мы работаем")}</span>
        <h2 data-r style="--d:.1s">{t("From a conversation to the <em>first opening</em>", "От разговора до <em>первого открытия</em>")}</h2>
        <p data-r style="--d:.2s">{t("You should see how we think, not only the pictures. Every case on this site follows the same path.", "Важно показать, как мы думаем, а не только картинки. Каждый кейс на сайте проходит этот путь.")}</p>
      </div>
      <ol class="steps">
{chr(10).join(f'        <li class="step" data-r style="--d:{i*0.08:.2f}s"><span class="step-n">{i+1:02d}</span><h3>{E(a)}</h3><p>{E(b)}</p></li>' for i, (a, b) in enumerate(steps))}
      </ol>
    </div>
  </section>

  <!-- BELIEFS -->
  <section class="beliefs tone-dark" id="beliefs" data-tone="dark">
    <div class="wrap">
      <div class="grid sec-head">
        <span class="label" data-r>{t("What we believe in", "Во что мы верим")}</span>
        <h2 data-r style="--d:.1s">{t("Design is not what you see. <em>It is what you feel inside it.</em>", "Дизайн — это не то, что вы видите. <em>Это то, что вы чувствуете внутри.</em>")}</h2>
      </div>
      <div class="bel-grid">
{chr(10).join(f'        <div class="bel" data-r style="--d:{(i%3)*0.1:.1f}s"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for i, (a, b) in enumerate(beliefs))}
      </div>
      <p class="motto" data-r="word">{t("Design by people. For people. Built to last.", "Дизайн от людей. Для людей. На годы вперёд.")}</p>
    </div>
  </section>

  <!-- CONTACT -->
  <section class="contact tone-light" id="contact" data-tone="light">
    <div class="wrap"><div class="grid ct">
      <div class="ct-left">
        <span class="label" data-r>{t("Contact", "Контакты")}</span>
        <h2 data-r style="--d:.1s">{t("Tell us about <em>your project</em>", "Расскажите о <em>своём проекте</em>")}</h2>
        <p data-r style="--d:.15s">{t("A few words about your brand, space or event are enough to start. We reply with questions and the next steps.", "Чтобы начать, достаточно пары слов о бренде, пространстве или событии. Мы ответим с вопросами и следующими шагами.")}</p>
        <div class="ct-lines" data-r style="--d:.2s">
          <div class="ct-line"><span class="label">{t("Email", "Почта")}</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
          <div class="ct-line"><span class="label">{t("Phone", "Телефон")}</span><span>{PHONE}</span></div>
          <div class="ct-line"><span class="label">{t("Studio", "Студия")}</span><span>{t("Dubai, United Arab Emirates", "Дубай, ОАЭ")}</span></div>
        </div>
        <div class="ct-quick" data-r style="--d:.25s"><a class="btn solid" href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a class="btn" href="{IG}">Instagram</a><a class="btn" href="{LI}">LinkedIn</a></div>
      </div>
      <form class="form" id="brief" novalidate data-r style="--d:.15s">
        <div class="f-row">
          <div class="field"><label for="f-name">{t("Name", "Имя")}</label><input id="f-name" name="name" autocomplete="name" placeholder="{t('Your name', 'Как вас зовут')}" required></div>
          <div class="field"><label for="f-brand">{t("Brand or company", "Бренд или компания")}</label><input id="f-brand" name="brand" autocomplete="organization" placeholder="{t('Brand name', 'Название бренда')}"></div>
        </div>
        <div class="f-row">
          <div class="field"><label for="f-email">{t("Email", "Почта")}</label><input id="f-email" name="email" type="email" autocomplete="email" placeholder="you@brand.com" required></div>
          <div class="field"><label for="f-phone">{t("Phone or WhatsApp", "Телефон или WhatsApp")}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder="+971"></div>
        </div>
        <fieldset>
          <legend class="f-legend">{t("Service", "Услуга")}</legend>
          <div class="chips">{''.join(f'<label class="chip"><input type="radio" name="service" id="f-svc-{i}" value="{i}"{" checked" if i == len(chips)-1 else ""}><span>{E(x)}</span></label>' for i, x in enumerate(chips))}</div>
        </fieldset>
        <div class="field"><label for="f-msg">{t("About the project", "О проекте")}</label><textarea id="f-msg" name="message" rows="3" placeholder="{t('What are you launching, where and when?', 'Что запускаете, где и когда?')}"></textarea></div>
        <div class="f-foot"><p class="f-note">{t("By sending the form you agree to the privacy policy.", "Отправляя форму, вы соглашаетесь с политикой конфиденциальности.")}</p><button class="btn solid" type="submit">{t("Send request", "Отправить заявку")} <i></i></button></div>
        <p class="f-done" role="status">{t("Thank you. Your request is with us, and we will be in touch soon.", "Спасибо! Заявка у нас, скоро свяжемся с вами.")}</p>
      </form>
    </div></div>
  </section>
</main>
{footer(True)}'''
    title = t("CASAVISION Creative Atelier", "CASAVISION — креативное ателье")
    desc = t("Creative atelier from Dubai: interior design, creative direction, branding and consultancy.",
             "Креативное ателье из Дубая: дизайн интерьеров, креативная дирекция, брендинг и консалтинг.")
    out = head(title, desc, artifact) + body
    if not artifact:
        out += "</body>\n</html>\n"
    return out


# ---------------------------------------------------------------- project page
DESK = [(0, 6, 15), (17, 0, 18), (37, 10, 17), (56, 0, 15), (73, 4, 19), (3, 50, 17), (23, 44, 19), (45, 52, 16), (64, 46, 20), (86, 50, 13)]
MOB = [(0, 2, 34), (33, 6, 32), (66, 0, 34), (2, 33, 32), (35, 30, 32), (68, 34, 32), (0, 64, 34), (34, 62, 32), (66, 66, 34), (40, 86, 26)]
WDESK = [(18, -9), (79, 41), (2, 42), (47, 95)]
WMOB = [(34, -6), (66, 56), (0, 28), (36, 96)]


def project(i):
    p = P[i]
    nxt = P[(i + 1) % len(P)]
    words_l = tr(p, "words")
    words = "".join(f'<div class="pw-word">{E(w)}</div>' for w in words_l)
    mood = []
    for j, (src, cls) in enumerate(p["moodboard"]):
        dl, dt, dw = DESK[j]
        ml, mt, mw = MOB[j]
        mood.append(f'<figure class="pm-item {cls}" style="--l:{dl}%;--t:{dt}%;--w:{dw}%;--ml:{ml}%;--mt:{mt}%;--mw:{mw}%;z-index:{1 + (j % 3)}"><img src="{img(p, src)}" alt="" loading="lazy"></figure>')
    for j, w in enumerate(words_l):
        dl, dt = WDESK[j]
        ml, mt = WMOB[j]
        mood.append(f'<span class="pm-word" style="--l:{dl}%;--t:{dt}%;--ml:{ml}%;--mt:{mt}%">{E(w)}</span>')
    gal = []
    for src, cap_en, cap_ru, cls in p["gallery"]:
        if src.startswith("@"):
            gal.append(f'<p class="pg-note" data-haze>{E(tr(p, "note"))}</p>')
        else:
            cap = t(cap_en, cap_ru)
            gal.append(f'<figure class="pg-item {cls}"><div class="media" data-r="img"><img src="{img(p, src)}" alt="{E(p["name"])}: {E(cap)}" loading="lazy"></div><figcaption><span class="label">{E(cap)}</span><span class="mute">{E(p["name"])}</span></figcaption></figure>')
    page = p["slug"] + ".html"
    body = f'''{header(False, page)}{menu(False, page)}
<main id="top">
  <section class="p-hero tone-light" data-tone="light">
    <div class="wrap"><div class="grid">
      <div class="media ph-img" data-r="img"><img src="{img(p, p['hero'])}" alt="{E(p['name'])}"></div>
      <div class="ph-txt">
        <div data-r><a class="more back" href="index.html#projects" data-go><i></i> {t("All projects", "Все проекты")}</a></div>
        <div style="display:grid;gap:28px">
          <span class="label" data-r><span class="mute">{i+1:02d} / 06</span> <span class="sq gold"></span>{E(tr(p, 'kind'))}</span>
          <h1 class="ph-title" data-r style="--d:.1s">{E(p['name'])}</h1>
          <p class="ph-quote" data-r style="--d:.2s">“{E(tr(p, 'quote'))}”</p>
        </div>
        <div class="ph-meta" data-r style="--d:.3s">
          <div><span class="label">{t("Project", "Проект")}</span><span>{E(tr(p, 'kind'))}</span></div>
          <div><span class="label">{t("Location", "Локация")}</span><span>{E(tr(p, 'where'))}</span></div>
          <div><span class="label">{t("Scope", "Что сделали")}</span><span>{E(tr(p, 'scope'))}</span></div>
          <div><span class="label">{t("Concept words", "Слова концепции")}</span><span class="it">{E(', '.join(words_l))}</span></div>
        </div>
      </div>
    </div></div>
  </section>

  <section class="p-story tone-dark" data-tone="dark">
    <div class="wrap"><div class="grid ps">
      <div class="ps-block"><span class="label" data-r>01 <span class="sq gold"></span>{t("The brief", "Задача")}</span><p data-haze>{E(tr(p, 'brief'))}</p></div>
      <div class="ps-block"><span class="label" data-r style="--d:.15s">02 <span class="sq gold"></span>{t("The idea", "Идея")}</span><p data-haze>{E(tr(p, 'idea'))}</p></div>
    </div></div>
  </section>

  <section class="p-words tone-dark" data-tone="dark" aria-label="{t('Concept words', 'Слова концепции')}">
    <div class="pw-stage">
      <div class="media pw-img"><img src="{img(p, p['wordimg'])}" alt="" loading="lazy"></div>
      {words}
      <span class="pw-count label">1 / {len(words_l)}</span>
      <span class="pw-hint label mute">03 <span class="sq gold"></span>{t("Concept words", "Слова концепции")}</span>
    </div>
  </section>

  <section class="p-mood tone-light" data-tone="light" aria-label="{t('Moodboard', 'Мудборд')}">
    <div class="pm-stage">
      <div class="pm-head wrap"><div class="grid"><span class="label">04 <span class="sq gold"></span>{t("Moodboard", "Мудборд")}</span><p>{E(tr(p, 'mood'))}</p></div></div>
      <div class="pm-board">
{chr(10).join('        ' + m for m in mood)}
      </div>
    </div>
  </section>

  <section class="p-gallery tone-light" data-tone="light">
    <div class="wrap">
      <div class="grid sec-head" style="margin-bottom:clamp(56px,7vw,110px)"><span class="label" data-r>05 <span class="sq gold"></span>{t("Visualisations", "Визуализации")}</span><h2 data-r style="--d:.1s">{t("From concept <em>to space</em>", "От концепции <em>к пространству</em>")}</h2></div>
      <div class="grid pg">
{chr(10).join('        ' + x for x in gal)}
      </div>
    </div>
  </section>

  <section class="p-result tone-dark" data-tone="dark">
    <div class="blurmark" aria-hidden="true" data-fit="1" data-par="-0.3">{E(p['name'].upper())}</div>
    <div class="wrap"><div class="grid"><span class="label">06 <span class="sq gold"></span>{t("The result", "Результат")}</span><blockquote data-haze>{E(tr(p, 'result'))}</blockquote></div></div>
  </section>

  <section class="p-cta tone-light" data-tone="light">
    <div class="wrap"><div class="grid">
      <h2 data-r>{t("Want a concept <em>for your brand?</em>", "Хотите концепцию <em>для своего бренда?</em>")}</h2>
      <div class="pc-side" data-r style="--d:.15s"><p>{t("Tell us about the project: what you are launching, where and when. Prices are calculated individually.", "Расскажите о проекте: что запускаете, где и когда. Стоимость считаем индивидуально.")}</p><div><a class="btn solid" href="index.html#contact" data-go>{t("Tell us about your project", "Обсудить проект")} <i></i></a></div></div>
    </div></div>
  </section>

  <a class="p-next" href="{nxt['slug']}.html" data-go data-tone="dark">
    <img src="{img(nxt, nxt['hero'])}" alt="" loading="lazy">
    <span class="pn-in wrap"><span class="label">{t("Next project", "Следующий проект")} <span class="sq"></span>{E(tr(nxt, 'kind'))}</span><span class="pn-title">{E(nxt['name'])}</span><span><span class="more">{t("Open the story", "Открыть историю")} <i></i></span></span></span>
  </a>
</main>
{footer(False)}</body>
</html>
'''
    css = ('<style>.pm-item{left:var(--l);top:var(--t);width:var(--w)}.pm-word{left:var(--l);top:var(--t)}'
           '@media (max-width:760px){.pm-item{left:var(--ml);top:var(--mt);width:var(--mw)}.pm-word{left:var(--ml);top:var(--mt)}}</style>\n')
    return head(f"{p['name']} · CASAVISION", tr(p, "short"), extra=css) + body


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    global LANG, R
    n = 0
    for lang, prefix, outdir in (("en", "", ROOT), ("ru", "../", os.path.join(ROOT, "ru"))):
        LANG, R = lang, prefix
        write(os.path.join(outdir, "index.html"), home()); n += 1
        for i, p in enumerate(P):
            write(os.path.join(outdir, p["slug"] + ".html"), project(i)); n += 1
    LANG, R = "en", ""
    write(os.path.join(ROOT, ".artifact", "index.html"), home(artifact=True)); n += 1
    print("built", n, "files")


if __name__ == "__main__":
    main()
