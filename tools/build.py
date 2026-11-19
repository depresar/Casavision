#!/usr/bin/env python3
"""Builds the CASAVISION static mock-up.

Outputs (repo root):
  index.html                 home page
  <slug>.html                one page per project
  .artifact/index.html       the home page without the document wrapper (for claude.ai Artifact publishing)

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

SERVICES = ["Interior Design", "Creative & Design Direction", "Branding & Brand Strategy", "Consultancy"]

# ---------------------------------------------------------------- projects
P = [
    dict(
        slug="fragments-de-paris", key="fragments", name="Fragments de Paris",
        kind="Residential interior", where="Paris", scope="Interior design, styling",
        words=["timeless", "balance", "monochrome", "opulent"],
        quote="Beauty is not decoration.",
        short="A Paris apartment designed as proof that some cities live inside you before you ever arrive. Every surface treats beauty as a way of taking the world seriously.",
        brief="There are cities that live inside you before you ever arrive. Paris is one of them, and this apartment was designed to feel like the proof.",
        idea="We believe that the most extraordinary spaces are not designed. They are distilled, from memory, from longing, from the courage to choose depth over novelty.",
        mood="An invitation to live fully inside a vision of life that refuses to be ordinary: classical mouldings, quiet light, ivory and walnut, one gesture of opulence per room.",
        result="Here, every surface carries the quiet conviction that beauty is not decoration, but a way of taking the world seriously.",
        hero="cover.jpg", wordimg="living.jpg",
        moodboard=[("m7.jpg", ""), ("m2.jpg", ""), ("m9.png", "cut"), ("m3.jpg", ""), ("m4.jpg", ""), ("m1.jpg", ""), ("m5.jpg", ""), ("m6.jpg", ""), ("m8.jpg", ""), ("m10.png", "cut")],
        gallery=[("living.jpg", "Living room", "w-left"), ("living-detail.jpg", "Living room, detail", "w-small-r"),
                 ("kitchen-sketch.jpg", "Kitchen, sketch", "w-half-l"), ("kitchen.jpg", "Kitchen, visualisation", "w-half-r"),
                 ("bedroom.jpg", "Bedroom", "w-full"), ("bathroom.jpg", "Bathroom", "w-mid")],
        notes={},
    ),
    dict(
        slug="the-hold", key="hold", name="The Hold",
        kind="Specialty coffee shop", where="Dubai", scope="Concept, interior design",
        words=["stillness", "desert", "spirit", "oasis"],
        quote="Where the desert taught us to be still and the coffee gave us a reason to stay.",
        short="A specialty coffee space that takes the Arabian desert as its design language. Sky pressed into blue panels, earth warmed into walnut, steel at the centre.",
        brief="A conceptual proposal for a specialty coffee space in Dubai, developed as an independent design study. The Hold takes the Arabian desert as its primary design language, as philosophy rather than reference.",
        idea="The patience of the Arabian desert meets the precision of craft. A café designed around one radical idea: in Dubai, stillness is the greatest luxury of all.",
        mood="Sand in motion, mirrored steel, walnut, a single blue sky. The board collects the textures of waiting and the ritual of a slow cup.",
        result="The desert holds its silence for a thousand years. We asked what a café would feel like if it held the same quality of stillness.",
        hero="cover.jpg", wordimg="seating.jpg",
        moodboard=[("m6.jpg", ""), ("m2.jpg", ""), ("m9.png", "cut"), ("m1.jpg", "mult"), ("m5.jpg", ""), ("m3.jpg", ""), ("m4.jpg", ""), ("m8.jpg", "")],
        gallery=[("island.jpg", "Coffee island", "w-left"), ("seating.jpg", "Seating area", "w-small-r"),
                 ("bar-detail.jpg", "Brew bar, detail", "w-small-l"), ("@note", "", ""),
                 ("bar.jpg", "Coffee island and bar", "w-full")],
        notes={"@note": "Three forces hold it together: the sky pressed into blue panels above you, the earth warmed into walnut around you, and the steel at the centre that transforms the raw into the essential."},
    ),
    dict(
        slug="confesso-milano", key="confesso", name="Confesso Milano",
        kind="Hair salon", where="Milanese concept", scope="Naming, concept, interior design",
        words=["lightweight", "elegance", "exchanging", "freedom"],
        quote="Safe place to be yourself.",
        short="Naming, concept and interior for a hair salon inspired by Milanese beauty culture: a social destination where beauty, comfort and connection coexist.",
        brief="Inspired by Milanese lifestyle and beauty culture, we developed a full concept including the naming and interior design of the space.",
        idea="The project transforms the traditional hair salon into a contemporary social sanctuary: a place to talk, laugh, share stories and experience transformation through beauty.",
        mood="Openness, comfort and authenticity. Arches, terrazzo, burnished metal, warm plaster and the women who make a salon a meeting place.",
        result="A destination where everyone feels free to express their identity and leave feeling confident.",
        hero="cover.jpg", wordimg="station.jpg",
        moodboard=[("m4.jpg", ""), ("m2.jpg", ""), ("m8.png", "cut"), ("m6.jpg", ""), ("m5.jpg", ""), ("m1.jpg", ""), ("m7.jpg", ""), ("m3.jpg", ""), ("m9.png", "cut")],
        gallery=[("reception.jpg", "Entrance and reception", "w-full"),
                 ("plan.jpg", "Floor plan", "w-small-l"), ("materials.jpg", "Materials", "w-small-r"),
                 ("@note", "", ""),
                 ("station.jpg", "Hair styling station", "w-small-l"), ("washing.jpg", "Washing area", "w-right")],
        notes={"@note": "Every surface was chosen as a love letter to Milan: its terrazzo floors, its burnished metals, its earth-toned plasters. Materials that age with grace and make a room feel like it has always belonged to the people inside it."},
    ),
    dict(
        slug="velvet-meadow", key="velvet", name="Velvet Meadow",
        kind="Spring / Summer event for Flabelus", where="Castello di Reschio, Umbria", scope="Event concept, styling, activation",
        words=["weightless", "energy", "wildflowers", "emotion"],
        quote="Colour is not chosen but discovered.",
        short="A countryside brunch for the Spring/Summer launch of Flabelus, born from one image: a woman walking barefoot through a field in full bloom.",
        brief="For the Spring/Summer launch of Flabelus, we created a countryside brunch at Castello di Reschio. The concept was born from a single image: a woman walking barefoot through a field in full bloom, unhurried, unbothered, completely herself.",
        idea="This is the world Flabelus lives in: colour is discovered, comfort is a conviction, and every step feels like the ground is giving back.",
        mood="Velvet Meadow is rooted in the kind of beauty that cannot be arranged: wild, saturated and alive. Every image here is a fragment of a single feeling.",
        result="The particular freedom of a woman who has stopped trying to be careful and started trying to be present. This is not a mood. This is a manifesto.",
        hero="cover.jpg", wordimg="table.jpg",
        moodboard=[("m5.jpg", ""), ("m4.jpg", ""), ("m7.png", "cut"), ("m3.jpg", ""), ("m6.jpg", ""), ("m2.jpg", ""), ("m1.jpg", "mult")],
        gallery=[("long-table.jpg", "The long table", "w-left"), ("table.jpg", "Stripes and wildflowers", "w-small-r"),
                 ("@note", "", ""),
                 ("workshop.jpg", "Glassware painting workshop", "w-small-l"), ("photomoment.jpg", "Photomoment area", "w-right")],
        notes={"@note": "Tables dressed in bold stripes and crowned with wildflowers, set in the middle of a living, breathing meadow, as if the celebration had always belonged to the earth. Guests paint their own glassware: a playful moment to create, connect and bloom together."},
    ),
    dict(
        slug="sliceit", key="slice", name="SLICEit",
        kind="Pizza pop-up", where="Dubai", scope="Concept, naming, identity, pop-up design",
        words=["young", "bold", "diverse", "contemporary"],
        quote="Just the good part.",
        short="A pizza pop-up with its own identity: one perfect slice, from a window, in under a minute. New York state of mind wrapped in Italian soul.",
        brief="SLICEit was born from the most honest craving in the world: a single, perfect slice, hot from a wood-fired oven, eaten standing up, no occasion required.",
        idea="In a city that does everything at scale, we asked a different question: what if the best pizza in Dubai came in one piece, from a window, in under a minute?",
        mood="Fire, steel, and a slice that speaks for itself. Every detail is turned up: the red is redder, the crust is louder.",
        result="Designed to be remembered after a single visit. This is not fast food. This is fast confidence.",
        hero="cover.jpg", wordimg="box.jpg",
        moodboard=[("m4.jpg", ""), ("m1.jpg", ""), ("m8.png", "cut"), ("m6.jpg", ""), ("m7.jpg", ""), ("m3.jpg", ""), ("m5.jpg", ""), ("m2.jpg", "")],
        gallery=[("front.jpg", "Front view", "w-left"), ("box.jpg", "Packaging", "w-small-r"),
                 ("d1.jpg", "Identity in use", "w-small-l"), ("@note", "", ""),
                 ("d2.jpg", "Slice wrap", "w-small-l"), ("side.jpg", "Side view", "w-right")],
        notes={"@note": "Bold red on white, a logotype with personality to spare, and product shots so unapologetic they make you hungry before you finish looking. The identity was built to stop people mid-scroll and mid-street."},
    ),
    dict(
        slug="sensorial-dive", key="sensorial", name="Sensorial Dive",
        kind="Fragrance pop-up for Gucci", where="Immersive pop-up", scope="Concept, spatial design, experience",
        words=["water flow", "reflection", "botanical", "structural"],
        quote="How deep are you willing to go?",
        short="A fragrance pop-up for Gucci built around one question: what if a fragrance were not something you wore, but somewhere you went?",
        brief="Sensorial Dive was born from a single question: what if a fragrance were not something you wore, but somewhere you went?",
        idea="A corridor that pulls you forward, a light that beckons from the end, a room that blooms open like a secret. An immersive world built around the most intimate thing Gucci makes, and you are the one diving in.",
        mood="The references move between the botanical and the surreal: water flow and structural glass, reflection and dissolution, the precision of a bottle and the abandon of a garden in full bloom.",
        result="Nature here is not decoration, it is architecture. Purple bleeds into pink bleeds into the memory of a scent you cannot name but have always known.",
        hero="cover.jpg", wordimg="corridor.jpg",
        moodboard=[("m1.jpg", ""), ("m3.jpg", ""), ("m6.jpg", ""), ("m2.jpg", ""), ("m5.jpg", ""), ("m4.jpg", ""), ("m7.png", "cut")],
        gallery=[("room.jpg", "Fragrance room", "w-left"), ("corridor.jpg", "The Deep Reveal", "w-small-r"),
                 ("@note", "", ""),
                 ("diagram.jpg", "Spatial concept", "w-full"), ("plan.jpg", "Pavilion and floor plan", "w-mid")],
        notes={"@note": "A digital screen of nature, water and Gucci aesthetic. A botanical plinth for each fragrance, with a bespoke floral arrangement that mirrors its notes. And at the corridor's end, a beckoning purple light that invites guests to submerge themselves in the brand's story."},
    ),
]
BY = {p["key"]: p for p in P}


def img(p, f):
    return f"assets/img/{p['key']}/{f}"


# ---------------------------------------------------------------- partials
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Raleway:wght@300;400;500;600&display=swap">'


def head(title, desc, artifact=False):
    meta = (f'<title>{E(title)}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            f'<meta name="description" content="{E(desc)}">\n{FONTS}\n<link rel="stylesheet" href="assets/css/site.css">\n'
            f'<link rel="icon" href="assets/brand/monogram.png">')
    if artifact:
        return meta + "\n"
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'{meta}\n</head>\n<body>\n')


def header(home):
    h = "#" if home else "index.html#"
    return f'''<div class="curtain" aria-hidden="true"><img src="assets/brand/monogram.png" alt=""></div>
<header class="hdr wrap">
  <div class="grid">
    <a class="brand" href="{'#top' if home else 'index.html'}" {'' if home else 'data-go'} aria-label="CASAVISION, home"><img src="assets/brand/monogram.png" alt=""><b>CASAVISION</b></a>
    <span class="hdr-loc label">Dubai, UAE</span>
    <a class="hdr-cta label" href="{h}contact">Tell us about your project</a>
    <a class="hdr-wa label" href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
    <button class="hdr-menu label" type="button" data-menu-open aria-controls="menu" aria-expanded="false"><span class="burger" aria-hidden="true"><span></span><span></span></span>Menu</button>
  </div>
</header>
'''


def menu(home):
    h = "#" if home else "index.html#"
    go = "" if home else " data-go"
    items = [
        ("Home", "#top" if home else "index.html", "assets/img/home/cave.jpg", "CASAVISION, creative atelier", ""),
        ("About", f"{h}about", "assets/img/fragments/living.jpg", "Philosophy and values",
         f'<a href="{h}approach"{go}>How we work</a><a href="{h}beliefs"{go}>What we believe in</a>'),
        ("Services", f"{h}services", "assets/img/confesso/reception.jpg", "Four disciplines, one team",
         "".join(f'<a href="{h}services"{go}>{E(s)}</a>' for s in SERVICES)),
        ("Projects", f"{h}projects", "assets/img/velvet/long-table.jpg", "Six stories from the portfolio",
         "".join(f'<a href="{p["slug"]}.html" data-go>{E(p["name"])}</a>' for p in P)),
        ("Contact", f"{h}contact", "assets/img/hold/island.jpg", "Tell us about your project", ""),
    ]
    nav = "\n".join(
        f'''      <div class="mn-item" data-cap="{E(cap)}"><a class="mn-link" href="{href}"{go if href.startswith('index') else ''}>{E(t)}</a><div class="mn-sub">{sub}</div></div>'''
        for t, href, im, cap, sub in items)
    imgs = "".join(f'<img src="{im}" alt=""{" class=\"is-on\"" if i == 0 else ""} loading="lazy">' for i, (t, href, im, cap, sub) in enumerate(items))
    return f'''<div class="menu" id="menu" aria-hidden="true">
  <div class="menu-scrim" data-menu-close></div>
  <div class="menu-panel wrap" role="dialog" aria-modal="true" aria-label="Menu">
    <div class="menu-top grid">
      <a class="brand" href="{'#top' if home else 'index.html'}"{go}><img src="assets/brand/monogram.png" alt=""><b>CASAVISION</b></a>
      <button class="menu-close label" type="button" data-menu-close>Close <span class="x" aria-hidden="true"></span></button>
    </div>
    <div class="menu-body grid">
      <nav class="menu-nav" aria-label="Main">
{nav}
      </nav>
      <figure class="menu-preview" aria-hidden="true">{imgs}<figcaption class="label">CASAVISION, creative atelier</figcaption></figure>
    </div>
    <div class="menu-info grid">
      <div><span class="label">Write to us</span><a href="mailto:{EMAIL}">{EMAIL}</a><span>{PHONE}</span></div>
      <div><span class="label">Socials</span><a href="{IG}">Instagram</a><a href="{LI}">LinkedIn</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
      <div><span class="label">Studio</span><span>CASAVISION L.L.C-FZ</span><span>Dubai, United Arab Emirates</span></div>
      <div class="mi-cta"><span class="label">New project</span><a class="btn" href="{h}contact"{go}>Tell us about your project</a></div>
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
      <div class="fc-1"><p>Creative atelier for spaces, brands and moments. Dubai, UAE and international.</p></div>
      <div class="fc-2"><span class="label">Menu</span><a href="{'#top' if home else 'index.html'}"{go}>Home</a><a href="{h}about"{go}>About</a><a href="{h}services"{go}>Services</a><a href="{h}projects"{go}>Projects</a><a href="{h}contact"{go}>Contact</a></div>
      <div class="fc-3"><span class="label">Services</span>{''.join(f'<a href="{h}services"{go}>{E(s)}</a>' for s in SERVICES)}</div>
      <div class="fc-4"><span class="label">Socials</span><a href="{IG}">Instagram</a><a href="{LI}">LinkedIn</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
      <div class="fc-5"><span class="label">Contact</span><a href="mailto:{EMAIL}">{EMAIL}</a><span>{PHONE}</span></div>
    </div>
  </div>
  <div class="ftr-mark" aria-hidden="true"><div class="blurmark" data-fit="0.98" data-focus="26" data-focus-min="0">CASAVISION</div></div>
  <div class="wrap"><div class="ftr-base"><span>© <span data-year>2026</span> CASAVISION Creative Atelier L.L.C-FZ</span><a href="#">Privacy policy</a><span>Dubai, UAE</span></div></div>
</footer>
<script src="assets/js/site.js"></script>
'''


def case_meta(p, n, desc=True, extra_cls=""):
    words = " · ".join(p["words"])
    d = f'<p class="cm-desc" data-r style="--d:.1s">{E(p["short"])}</p>' if desc else ""
    return f'''<div class="cm-cat label" data-r><span class="cm-num mute">{n:02d} / 06</span>{E(p["kind"])}</div>
        {d}
        <div class="cm-head" data-r style="--d:.15s"><h3 class="cm-title"><a href="{p["slug"]}.html" data-go>{E(p["name"])}</a></h3><span class="cm-words">{E(words)}</span></div>
        <a class="cm-link more" href="{p["slug"]}.html" data-go data-r style="--d:.2s">View project <i></i></a>
        <div class="cm-loc" data-r style="--d:.25s">{E(p["where"])}</div>'''


# ---------------------------------------------------------------- home
def home(artifact=False):
    f, h_, c, v, s, g = (BY[k] for k in ("fragments", "hold", "confesso", "velvet", "slice", "sensorial"))
    services_html = []
    seen = {
        "Interior Design": "Fragments de Paris, The Hold, Confesso Milano",
        "Creative & Design Direction": "Velvet Meadow, Sensorial Dive",
        "Branding & Brand Strategy": "SLICEit, Confesso Milano",
        "Consultancy": "Alongside every project",
    }
    svc_data = [
        ("Interior Design", "Spaces lived, felt, and remembered.",
         "We design interiors that go beyond aesthetics, beginning with listening to the brief, the building and the people who will inhabit it. The result is always specific, never generic.",
         ["Residential", "HoReCa", "Retail & commercial"]),
        ("Creative & Design Direction", "Vision before execution. Always.",
         "Concept, visual language and styling for spaces, pop-ups, activations and events. For clients who need a point of view before they need a floor plan.",
         ["Concept development", "Styling", "Pop-ups", "Activations", "Events"]),
        ("Branding & Brand Strategy", "Whole from the first day.",
         "For brands that are just appearing: concept, naming, positioning and identity, so the brand is coherent from day one and ready for its first space.",
         ["Concept", "Naming", "Positioning", "Identity"]),
        ("Consultancy", "Clarity is the rarest luxury.",
         "For clients who need more than execution: strategy, project management and space planning, with the human insight that only comes from experience.",
         ["Client advisory", "Strategy", "Project management", "Space planning"]),
    ]
    for i, (name, line, body, tags) in enumerate(svc_data):
        services_html.append(f'''      <div class="svc{' is-open' if i == 0 else ''}" data-r>
        <button class="svc-row grid" type="button" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="svc-{i}">
          <span class="svc-tag label">Seen in: {E(seen[name])}</span>
          <span class="svc-name">{E(name)}</span>
          <span class="svc-line">{E(line)}</span>
          <span class="svc-plus" aria-hidden="true"></span>
        </button>
        <div class="svc-body" id="svc-{i}"><div><div class="svc-inner grid">
          <p>{E(body)}</p>
          <div class="svc-tags">{''.join(f'<span>{E(t)}</span>' for t in tags)}</div>
          <a class="more" href="#contact" data-service="{E(name)}">Discuss a project <i></i></a>
        </div></div></div>
      </div>''')

    steps = [
        ("Conversation", "We start by listening: who you are, what you are launching and who it is for."),
        ("Research", "We study the audience, the client, the brand and the market. The design follows these findings."),
        ("Concept", "One strong idea and a story that belongs to this project only."),
        ("Moodboard", "Images, materials and the key words of the concept, like stillness, desert, oasis."),
        ("Design", "Space, identity and visualisations developed around that one idea."),
        ("Realisation", "We stay with the project through to the opening, the event or the first point of sale."),
    ]
    beliefs = [
        ("Human First", "Every brief begins not with dimensions, but with understanding who will live inside the work. People are not the audience. They are the origin."),
        ("Collective Intelligence", "The atelier is a meeting point. Designers, clients, artisans and collaborators think together, because the best ideas are never the product of a single mind."),
        ("Cultural Depth", "Rooted in Italian design culture, we draw from history and craft, not from trends. Our work is grounded, but never static."),
        ("Conviction in Detail", "Nothing in a CASAVISION project is accidental. Every material, every object, every line is a position taken."),
        ("Vision for Longevity", "We design for the people who will inhabit a space in twenty years, not just the ones who commission it today."),
        ("Warmth & Rigour", "The care of a home and the precision of an atelier, always together. Emotion and craft are the same thing, seen differently."),
    ]
    chips = SERVICES + ["Not sure yet"]

    body = f'''{header(True)}{menu(True)}
<main id="top">

  <!-- HERO -->
  <section class="hero" data-tone="dark">
    <div class="hero-media"><video autoplay muted loop playsinline preload="auto" poster="assets/video/hero-poster.jpg"><source src="assets/video/hero.mp4" type="video/mp4"></video></div>
    <div class="hero-in wrap">
      <div class="grid hero-top">
        <div class="hero-lead">
          <span class="label" data-r>Creative atelier <span class="sq gold"></span> Dubai, UAE</span>
          <p data-r style="--d:.15s">We design spaces, brands and moments that say something.</p>
        </div>
        <ul class="hero-list" data-r style="--d:.3s">{''.join(f'<li>{E(x)}</li>' for x in SERVICES)}</ul>
      </div>
      <div class="grid hero-bottom">
        <div class="hero-scroll label" data-r style="--d:.5s"><i></i>Scroll</div>
        <a class="hero-card" href="{f['slug']}.html" data-go data-r style="--d:.45s">
          <span class="hc-txt"><span class="label mute">Featured</span><span class="hc-title">{E(f['name'])}</span><span>{E(f['kind'])}, {E(f['where'])}</span><span class="more">View project <i></i></span></span>
          <span class="hc-img"><img src="{img(f, 'living.jpg')}" alt="Living room of the Fragments de Paris apartment"></span>
        </a>
        <h1 class="masthead" data-r style="--d:.25s"><span class="mh-word" data-fit="1">CASAVISION</span><span class="mh-sub">Creative atelier</span></h1>
      </div>
    </div>
  </section>

  <!-- ABOUT -->
  <section class="intro tone-light" id="about" data-tone="light">
    <div class="blurmark" aria-hidden="true" data-focus="22" data-focus-min="9">CASAVISION</div>
    <div class="wrap">
      <div class="grid intro-head">
        <span class="label" data-r>About the atelier</span>
        <p class="intro-statement" data-r style="--d:.1s">Every project begins with a conversation and <em>one strong idea</em>. That idea runs through everything: the space, the brand, the event.</p>
      </div>
      <div class="grid intro-cols">
        <p class="ic-a" data-r>CASAVISION is a creative atelier based in Dubai, working across the UAE and internationally. We bring an Italian design sensibility: the kind that respects the past, understands the present and builds for what comes next.</p>
        <p class="ic-b" data-r style="--d:.1s">Each project starts with research into the audience, the client, the brand and the market. The design follows those findings rather than trends or ready-made templates.</p>
        <a class="ic-c more" href="#approach" data-r style="--d:.2s">How we work <i></i></a>
      </div>
      <div class="grid facts">
        <div class="fact" data-r><b>One team</b><p>Brand, space and activation are led by one team, so everything speaks the same language.</p></div>
        <div class="fact" data-r style="--d:.1s"><b>From name to first store</b><p>We can take a brand from the first idea and its name to the first point of sale.</p></div>
        <div class="fact" data-r style="--d:.2s"><b>Made from scratch</b><p>Every concept is written for one client and one story. No typical solutions.</p></div>
      </div>
    </div>
  </section>

  <!-- PROJECTS -->
  <section id="projects" class="tone-dark" data-tone="dark">
    <div class="wrap works-head">
      <div class="grid sec-head">
        <span class="label" data-r>Selected works</span>
        <h2 data-r style="--d:.1s">Projects told as <em>stories</em></h2>
        <p data-r style="--d:.2s">Every project here began as a conversation. Each case shows how we think, from the brief and the moodboard to the finished space.</p>
      </div>
    </div>
  </section>

  <!-- 01 wide image -->
  <article class="case case-a tone-light" data-tone="light">
    <div class="wrap">
      <a class="media" href="{f['slug']}.html" data-go data-r="img" aria-label="{E(f['name'])}"><img src="{img(f, 'bedroom.jpg')}" alt="Bedroom with classical mouldings in the Fragments de Paris apartment" loading="lazy"></a>
      <div class="grid cm">
        {case_meta(f, 1)}
      </div>
    </div>
  </article>

  <!-- 02 image right, concept words over it -->
  <article class="case case-b tone-dark" data-tone="dark">
    <div class="wrap">
      <div class="grid cb-stage">
        <a class="media" href="{h_['slug']}.html" data-go data-r="img" aria-label="{E(h_['name'])}"><img src="{img(h_, 'island.jpg')}" alt="Steel coffee island under a blue stone canopy" loading="lazy"></a>
        <div class="cb-words" aria-hidden="true"><span data-r="word">stillness</span><span data-r="word" style="--d:.25s">desert</span><span data-r="word" style="--d:.5s">oasis</span></div>
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
        <a class="media cc-1" href="{c['slug']}.html" data-go data-r="img" aria-label="{E(c['name'])}"><img src="{img(c, 'cover.jpg')}" alt="Two women talking in the salon" loading="lazy"></a>
        <a class="media cc-2" href="{c['slug']}.html" data-go data-r="img" style="--d:.2s" aria-label="{E(c['name'])}, washing area"><img src="{img(c, 'washing.jpg')}" alt="Washing area under a marble arch" loading="lazy"></a>
        <div class="cc-txt" data-r>
          <p class="cc-quote">“{E(c['quote'])}”</p>
          <p>{E(c['short'])}</p>
        </div>
        <div class="cc-head">
          <div class="cm-head" data-r><span class="label"><span class="mute">03 / 06</span> <span class="sq gold"></span>{E(c['kind'])}</span><h3 class="cm-title"><a href="{c['slug']}.html" data-go>{E(c['name'])}</a></h3><span class="cm-words">{E(' · '.join(c['words']))}</span></div>
          <a class="cm-link more" href="{c['slug']}.html" data-go data-r style="--d:.1s">View project <i></i></a>
          <div class="cm-loc" data-r style="--d:.15s">{E(c['where'])}</div>
        </div>
      </div>
    </div>
  </article>

  <!-- 04 full-screen colour band -->
  <article class="case case-d tone-sky" data-tone="light">
    <div class="wrap">
      <div class="grid cd">
        <a class="media cd-1" href="{v['slug']}.html" data-go data-r="img" aria-label="{E(v['name'])}" data-par="0.06"><img src="{img(v, 'cover.jpg')}" alt="Women in a field of wildflowers" loading="lazy"></a>
        <a class="media cd-2" href="{v['slug']}.html" data-go data-r="img" style="--d:.2s" aria-label="{E(v['name'])}, photomoment"><img src="{img(v, 'photomoment.jpg')}" alt="Mirrored photomoment installation in the meadow" loading="lazy"></a>
        <h3 class="cd-title" data-r="word" style="--d:.3s"><a href="{v['slug']}.html" data-go>Velvet<em>Meadow</em></a></h3>
        <img class="cd-flower" src="{img(v, 'm7.png')}" alt="" aria-hidden="true" data-par="-0.18" loading="lazy">
      </div>
      <div class="grid cm">
        <div class="cm-cat label" data-r><span class="cm-num mute">04 / 06</span>{E(v['kind'])}</div>
        <p class="cm-desc" data-r style="--d:.1s">{E(v['short'])}</p>
        <div class="cm-head" data-r style="--d:.15s"><span class="cm-words">{E(' · '.join(v['words']))}</span></div>
        <a class="cm-link more" href="{v['slug']}.html" data-go data-r style="--d:.2s">View project <i></i></a>
        <div class="cm-loc" data-r style="--d:.25s">{E(v['where'])}</div>
      </div>
    </div>
  </article>

  <!-- 05 two images, showroom rhythm -->
  <article class="case case-e tone-dark" data-tone="dark">
    <div class="wrap">
      <div class="grid ce">
        <a class="media ce-1" href="{s['slug']}.html" data-go data-r="img" aria-label="{E(s['name'])}"><img src="{img(s, 'box.jpg')}" alt="SLICEit pizza boxes on a steel chair" loading="lazy"></a>
        <a class="media ce-2" href="{s['slug']}.html" data-go data-r="img" style="--d:.2s" aria-label="{E(s['name'])}, front view"><img src="{img(s, 'front.jpg')}" alt="Front view of the SLICEit pop-up window" loading="lazy"></a>
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
        <a class="media cf-1" href="{g['slug']}.html" data-go data-r="img" aria-label="{E(g['name'])}"><img src="{img(g, 'room.jpg')}" alt="Pink fragrance room with a botanical plinth" loading="lazy"></a>
        <div class="cf-side">
          <div data-r><span class="label"><span class="mute">06 / 06</span> <span class="sq gold"></span>{E(g['kind'])}</span><p class="cm-desc" style="margin-top:22px">{E(g['short'])}</p></div>
          <div class="cf-bottom" data-r style="--d:.15s">
            <h3 class="cm-title"><a href="{g['slug']}.html" data-go>{E(g['name'])}</a></h3>
            <span class="cm-words">{E(' · '.join(g['words']))}</span>
            <div class="cf-row"><a class="more" href="{g['slug']}.html" data-go>View project <i></i></a><span class="label mute">{E(g['where'])}</span></div>
          </div>
        </div>
      </div>
    </div>
  </article>

  <section class="nda tone-dark" data-tone="dark">
    <div class="wrap"><div class="grid">
      <p data-r>The full portfolio is shared on request. Some projects are under NDA or were made in collaboration.</p>
      <a class="btn" href="#contact" data-r style="--d:.1s">Request the portfolio</a>
    </div></div>
  </section>

  <!-- SERVICES -->
  <section class="services tone-ink" id="services" data-tone="dark">
    <div class="wrap">
      <div class="grid sec-head">
        <span class="label" data-r>Services</span>
        <h2 data-r style="--d:.1s">Four disciplines, <em>one language</em></h2>
        <p data-r style="--d:.2s">Prices are not published: every project is calculated individually, on request.</p>
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
        <span class="label" data-r>How we work</span>
        <h2 data-r style="--d:.1s">From a conversation to the <em>first opening</em></h2>
        <p data-r style="--d:.2s">You should see how we think, not only the pictures. Every case on this site follows the same path.</p>
      </div>
      <ol class="steps">
{chr(10).join(f'        <li class="step" data-r style="--d:{i*0.08:.2f}s"><span class="step-n">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d) in enumerate(steps))}
      </ol>
    </div>
  </section>

  <!-- BELIEFS -->
  <section class="beliefs tone-dark" id="beliefs" data-tone="dark">
    <div class="wrap">
      <div class="grid sec-head">
        <span class="label" data-r>What we believe in</span>
        <h2 data-r style="--d:.1s">Design is not what you see. <em>It is what you feel inside it.</em></h2>
      </div>
      <div class="bel-grid">
{chr(10).join(f'        <div class="bel" data-r style="--d:{(i%3)*0.1:.1f}s"><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i, (t, d) in enumerate(beliefs))}
      </div>
      <p class="motto" data-r="word">Design by people. For people. Built to last.</p>
    </div>
  </section>

  <!-- CONTACT -->
  <section class="contact tone-light" id="contact" data-tone="light">
    <div class="wrap"><div class="grid ct">
      <div class="ct-left">
        <span class="label" data-r>Contact</span>
        <h2 data-r style="--d:.1s">Tell us about <em>your project</em></h2>
        <p data-r style="--d:.15s">A few words about your brand, space or event are enough to start. We reply with questions and the next steps.</p>
        <div class="ct-lines" data-r style="--d:.2s">
          <div class="ct-line"><span class="label">Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
          <div class="ct-line"><span class="label">Phone</span><span>{PHONE}</span></div>
          <div class="ct-line"><span class="label">Studio</span><span>Dubai, United Arab Emirates</span></div>
        </div>
        <div class="ct-quick" data-r style="--d:.25s"><a class="btn solid" href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a class="btn" href="{IG}">Instagram</a><a class="btn" href="{LI}">LinkedIn</a></div>
      </div>
      <form class="form" id="brief" novalidate data-r style="--d:.15s">
        <div class="f-row">
          <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" placeholder="Your name" required></div>
          <div class="field"><label for="f-brand">Brand or company</label><input id="f-brand" name="brand" autocomplete="organization" placeholder="Brand name"></div>
        </div>
        <div class="f-row">
          <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" placeholder="you@brand.com" required></div>
          <div class="field"><label for="f-phone">Phone or WhatsApp</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder="+971"></div>
        </div>
        <fieldset>
          <legend class="f-legend">Service</legend>
          <div class="chips">{''.join(f'<label class="chip"><input type="radio" name="service" id="f-svc-{i}" value="{E(x)}"{" checked" if i == len(chips)-1 else ""}><span>{E(x)}</span></label>' for i, x in enumerate(chips))}</div>
        </fieldset>
        <div class="field"><label for="f-msg">About the project</label><textarea id="f-msg" name="message" rows="3" placeholder="What are you launching, where and when?"></textarea></div>
        <div class="f-foot"><p class="f-note">By sending the form you agree to the privacy policy.</p><button class="btn solid" type="submit">Send request</button></div>
        <p class="f-done" role="status">Thank you. Your request is with us, and we will be in touch soon.</p>
      </form>
    </div></div>
  </section>
</main>
{footer(True)}'''
    title = "CASAVISION Creative Atelier"
    desc = "Creative atelier from Dubai: interior design, creative direction, branding and consultancy."
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
    k = p["key"]
    words = "".join(f'<div class="pw-word">{E(w)}</div>' for w in p["words"])
    mood = []
    for j, (src, cls) in enumerate(p["moodboard"]):
        dl, dt, dw = DESK[j]
        ml, mt, mw = MOB[j]
        mood.append(f'<figure class="pm-item {cls}" style="--l:{dl}%;--t:{dt}%;--w:{dw}%;--ml:{ml}%;--mt:{mt}%;--mw:{mw}%;z-index:{1 + (j % 3)}"><img src="{img(p, src)}" alt="" loading="lazy"></figure>')
    for j, w in enumerate(p["words"]):
        dl, dt = WDESK[j]
        ml, mt = WMOB[j]
        mood.append(f'<span class="pm-word" style="--l:{dl}%;--t:{dt}%;--ml:{ml}%;--mt:{mt}%">{E(w)}</span>')
    gal = []
    for src, cap, cls in p["gallery"]:
        if src.startswith("@"):
            gal.append(f'<p class="pg-note" data-r>{E(p["notes"][src])}</p>')
        else:
            gal.append(f'<figure class="pg-item {cls}"><div class="media" data-r="img"><img src="{img(p, src)}" alt="{E(p["name"])}: {E(cap)}" loading="lazy"></div><figcaption><span class="label">{E(cap)}</span><span class="mute">{E(p["name"])}</span></figcaption></figure>')
    location_block = f'<div><span class="label">Location</span><span>{E(p["where"])}</span></div>'
    body = f'''{header(False)}{menu(False)}
<main id="top">
  <section class="p-hero tone-light" data-tone="light">
    <div class="wrap"><div class="grid">
      <div class="media ph-img" data-r="img"><img src="{img(p, p['hero'])}" alt="{E(p['name'])}"></div>
      <div class="ph-txt">
        <a class="ph-back label" href="index.html#projects" data-go data-r><i></i>All projects</a>
        <div style="display:grid;gap:28px">
          <span class="label" data-r><span class="mute">{i+1:02d} / 06</span> <span class="sq gold"></span>{E(p['kind'])}</span>
          <h1 class="ph-title" data-r style="--d:.1s">{E(p['name'])}</h1>
          <p class="ph-quote" data-r style="--d:.2s">“{E(p['quote'])}”</p>
        </div>
        <div class="ph-meta" data-r style="--d:.3s">
          <div><span class="label">Project</span><span>{E(p['kind'])}</span></div>
          {location_block}
          <div><span class="label">Scope</span><span>{E(p['scope'])}</span></div>
          <div><span class="label">Concept words</span><span class="it">{E(', '.join(p['words']))}</span></div>
        </div>
      </div>
    </div></div>
  </section>

  <section class="p-story tone-dark" data-tone="dark">
    <div class="wrap"><div class="grid ps">
      <div class="ps-block" data-r><span class="label">01 <span class="sq gold"></span>The brief</span><p>{E(p['brief'])}</p></div>
      <div class="ps-block" data-r style="--d:.15s"><span class="label">02 <span class="sq gold"></span>The idea</span><p>{E(p['idea'])}</p></div>
    </div></div>
  </section>

  <section class="p-words tone-dark" data-tone="dark" aria-label="Concept words">
    <div class="pw-stage">
      <div class="media pw-img"><img src="{img(p, p['wordimg'])}" alt="" loading="lazy"></div>
      {words}
      <span class="pw-count label">1 / {len(p['words'])}</span>
      <span class="pw-hint label mute">03 <span class="sq gold"></span>Concept words</span>
    </div>
  </section>

  <section class="p-mood tone-light" data-tone="light" aria-label="Moodboard">
    <div class="pm-stage">
      <div class="pm-head wrap"><div class="grid"><span class="label">04 <span class="sq gold"></span>Moodboard</span><p>{E(p['mood'])}</p></div></div>
      <div class="pm-board">
        {chr(10).join('        ' + m for m in mood)}
      </div>
    </div>
  </section>

  <section class="p-gallery tone-light" data-tone="light">
    <div class="wrap">
      <div class="grid sec-head" style="margin-bottom:clamp(56px,7vw,110px)"><span class="label" data-r>05 <span class="sq gold"></span>Visualisations</span><h2 data-r style="--d:.1s">The space, <em>room by room</em></h2></div>
      <div class="grid pg">
{chr(10).join('        ' + x for x in gal)}
      </div>
    </div>
  </section>

  <section class="p-result tone-dark" data-tone="dark">
    <div class="blurmark" aria-hidden="true" data-fit="1">{E(p['name'].upper())}</div>
    <div class="wrap"><div class="grid"><span class="label">06 <span class="sq gold"></span>The result</span><blockquote data-r>{E(p['result'])}</blockquote></div></div>
  </section>

  <section class="p-cta tone-light" data-tone="light">
    <div class="wrap"><div class="grid">
      <h2 data-r>Want a concept <em>for your brand?</em></h2>
      <div class="pc-side" data-r style="--d:.15s"><p>Tell us about the project: what you are launching, where and when. Prices are calculated individually.</p><a class="btn solid" href="index.html#contact" data-go>Tell us about your project</a></div>
    </div></div>
  </section>

  <a class="p-next" href="{nxt['slug']}.html" data-go data-tone="dark">
    <img src="{img(nxt, nxt['hero'])}" alt="" loading="lazy">
    <span class="pn-in wrap"><span class="label">Next project <span class="sq"></span>{E(nxt['kind'])}</span><span class="pn-title">{E(nxt['name'])}</span><span class="more">Open the story <i></i></span></span>
  </a>
</main>
{footer(False)}</body>
</html>
'''
    css = ('<style>.pm-item{left:var(--l);top:var(--t);width:var(--w)}.pm-word{left:var(--l);top:var(--t)}'
           '@media (max-width:760px){.pm-item{left:var(--ml);top:var(--mt);width:var(--mw)}.pm-word{left:var(--ml);top:var(--mt)}}</style>\n')
    return head(f"{p['name']} · CASAVISION", p["short"]) + css + body


def main():
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(home())
    for i, p in enumerate(P):
        with open(os.path.join(ROOT, p["slug"] + ".html"), "w", encoding="utf-8") as fh:
            fh.write(project(i))
    os.makedirs(os.path.join(ROOT, ".artifact"), exist_ok=True)
    with open(os.path.join(ROOT, ".artifact", "index.html"), "w", encoding="utf-8") as fh:
        fh.write(home(artifact=True))
    print("built", 2 + len(P), "files")


if __name__ == "__main__":
    main()
