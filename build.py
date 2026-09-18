#!/usr/bin/env python3
"""Genera index.html a partir de los datos de abajo. Ejecutar: python3 build.py"""
from html import escape

PERSONAS = 9
FECHA_PRECIOS = "18 de septiembre de 2026"

VUELOS = dict(
    ruta="Bogotá (BOG) a Cali (CLO)", sub="Ida y vuelta, por persona. Vistos en Google Flights el 18 de septiembre de 2026.",
    items=[
        dict(aerolinea="Wingo", sale="7:10", llega="8:18", dur="1 h 8 min", precio=366425,
             notas=["Directo", "Solo artículo personal, sin equipaje de mano", "Billetes separados: ida y vuelta se compran aparte"]),
        dict(aerolinea="JetSMART", sale="5:05", llega="6:19", dur="1 h 14 min", precio=393790,
             notas=["Directo", "Solo artículo personal, sin equipaje de mano", "Un solo billete"]),
        dict(aerolinea="LATAM", sale="14:05", llega="15:15", dur="1 h 10 min", precio=394390,
             notas=["Directo", "Solo artículo personal, sin equipaje de mano", "Billetes separados: ida y vuelta se compran aparte"]),
    ])
VUELO_MIN = min(v["precio"] for v in VUELOS["items"])
VUELO_MAX = max(v["precio"] for v in VUELOS["items"])

CIUDAD = dict(
    id="ciudad", titulo="En la ciudad", sub="28 de diciembre al 1 de enero · 4 noches",
    noches=4, check_in="2026-12-28", check_out="2027-01-01",
    resumen=[("Más barata", "Casa en Granada"), ("Más reseñas", "Luxury 502"), ("Más camas y baños", "Casa Alba")],
    items=[
        dict(slug="casa-granada", corto="Granada", rank="Precio más bajo · Descuento vigente",
             nombre="Casa en Granada cerca a dining & nightlife", lugar="Casa en el barrio Granada, Cali",
             precio=3769071, antes=4177299, cap=10, hab=3, camas=5, banos="2,5", nota="4,89", resenas=18,
             tags=[("Favorito entre huéspedes", "fav"), ("Superanfitriona", ""), ("Cancelación gratuita", "")],
             pro="La más barata de la ciudad, en Granada, la zona de restaurantes y rumba. Superanfitriona con 8 años.",
             con="Solo 5 camas para 9 personas: al menos 4 tendrían que compartir cama. 2,5 baños para todos.",
             host="Anfitriona: Samilis · Superanfitriona · 8 años en Airbnb",
             barrio=dict(nombre="Granada", texto=[
                 "Es la zona gastronómica de Cali: en pocas cuadras, sobre la Avenida 9N y sus alrededores, se concentran restaurantes, cafés, bares y boutiques. Es el barrio para salir a comer y a tomar algo sin coger taxi.",
                 "Queda al norte del centro, a unos 10 minutos a pie del Boulevard del Río y del barrio El Peñón, y a unos 10 minutos en carro del centro comercial Chipichape.",
                 "De noche hay mucho movimiento, sobre todo en fin de año. Es de las zonas más seguras para caminar, aunque conviene volver por las calles principales."]),
             url="https://www.airbnb.com/rooms/1678538745581343486"),
        dict(slug="casa-alba", corto="Casa Alba", rank="Más habitaciones y baños",
             nombre="Casa Alba - San Antonio", lugar="Casa en San Antonio, Cali",
             precio=4197491, antes=None, cap=12, hab=5, camas=6, banos="5", nota="4,8", resenas=5,
             tags=[("Aire acondicionado", ""), ("Barrio histórico", ""), ("Cancelación gratuita", "")],
             pro="5 habitaciones y 5 baños, la mejor distribución para 9. San Antonio es el barrio más pintoresco y se camina a todo.",
             con="Solo 5 reseñas. 6 camas para 9, así que 3 comparten.",
             host="Anfitriona: Alba · 3 años en Airbnb",
             barrio=dict(nombre="San Antonio", texto=[
                 "Es el barrio colonial de Cali, en una loma con casas de colores, calles empinadas y la iglesia de San Antonio en la cima, con el mejor mirador de la ciudad para ver el atardecer.",
                 "Tiene cafés, restaurantes pequeños, teatros y tiendas de artesanías. Bajando la loma se llega caminando al centro histórico, a la Plaza de Cayzedo y a La Ermita, y en 15 minutos a El Peñón. La Loma de la Cruz, con su mercado artesanal, queda al lado.",
                 "Es la zona más turística y con más ambiente bohemio. Las calles principales son tranquilas, pero de noche es mejor no alejarse hacia los bordes del barrio."]),
             url="https://www.airbnb.com/rooms/1063628642244199346"),
        dict(slug="luxury-502", corto="Luxury 502", rank="Más reseñas · Descuento vigente",
             nombre="Luxury apartamento en Cali 502", lugar="Apartamento dúplex en Cali",
             precio=6111968, antes=6774509, cap=9, hab=4, camas=5, banos="2,5", nota="4,95", resenas=110,
             tags=[("Favorito entre huéspedes", "fav"), ("Piscina compartida", ""), ("Dos pisos", "")],
             pro="El más probado: 110 reseñas con 4,95. Acabados modernos y anfitrión profesional.",
             con="Casi el doble que Granada. Cabe exactamente 9, con 5 camas, y no muestra cancelación gratuita.",
             host="Anfitrión: Zenya Host · 2 años en Airbnb",
             barrio=dict(nombre="Sur de Cali", texto=[
                 "Según la descripción del anuncio queda cerca del centro comercial Unicentro y de Holguines Trade Center, en el sur de la ciudad, una zona residencial y de estrato alto, con edificios con piscina y portería.",
                 "Es cómodo para ir a Pance y al río, y tiene supermercados y centros comerciales a mano, pero para salir a comer o a rumbear hay que coger taxi: Granada y San Antonio quedan a 25 o 30 minutos en carro.",
                 "Es la opción más tranquila y segura de las tres, a cambio de estar lejos del ambiente."]),
             url="https://www.airbnb.com/rooms/1134995105818917390"),
    ])

FINCA = dict(
    id="finca", titulo="Finca", sub="1 al 3 de enero · 2 noches",
    noches=2, check_in="2027-01-01", check_out="2027-01-03",
    resumen=[("Más barata", "Villa Campestre"), ("Mejor calificada", "Finca de recreo Dapa"), ("Más camas", "Green Jay Dapa")],
    items=[
        dict(slug="villa-campestre", corto="Villa Campestre", rank="Precio más bajo",
             nombre="Espectacular Villa Campestre", lugar="Villa en Jamundí",
             precio=1982098, antes=None, cap=13, hab=4, camas=7, banos="4,5", nota="4,58", resenas=12,
             tags=[("Piscina", ""), ("Jacuzzi", ""), ("Llegada autónoma", ""), ("Cancelación gratuita", "")],
             pro="La más barata y la que más reseñas tiene entre las fincas. Piscina grande y jacuzzi.",
             con="7 camas para 9: dos comparten. La calificación es la más baja del grupo.",
             host="Anfitriona: Yamile · 8 años en Airbnb",
             url="https://www.airbnb.com/rooms/33601199"),
        dict(slug="green-jay-dapa", corto="Green Jay", rank="Descuento vigente",
             nombre="Green Jay Dapa", lugar="Alojamiento en Dapa",
             precio=2024000, antes=2530000, cap=15, hab=5, camas=14, banos="6", nota=None, resenas=2,
             tags=[("Piscina", ""), ("Jacuzzi", ""), ("Brasero", ""), ("Parrilla", ""), ("Cancelación gratuita", "")],
             pro="Sobra espacio: 14 camas y 6 baños para 9 personas. Clima fresco en Dapa.",
             con="Anfitrión con solo 8 meses y 2 reseñas, aún sin calificación pública. Mayor incertidumbre.",
             host="Anfitrión: Nicolas · 8 meses en Airbnb",
             url=None, buscar="https://www.airbnb.com/s/Dapa--Colombia/homes?query=Green%20Jay%20Dapa"),
        dict(slug="saladito-meralva", corto="Meralva", rank="Mejor nota, pocas reseñas",
             nombre="Cali Saladito descanso 10 pax jacuzzi Meralva", lugar="Chalet en El Saladito, Cali",
             precio=2058563, antes=None, cap=10, hab=5, camas=10, banos="4,5", nota="5,0", resenas=3,
             tags=[("Jacuzzi", ""), ("Bosque de niebla", ""), ("Cancelación gratuita", "")],
             pro="Calificación perfecta, anfitriona con 8 años y una cama por persona. 5 habitaciones.",
             con="No tiene piscina, solo jacuzzi. El Saladito es zona de montaña, más fría.",
             host="Anfitriona: Maria · 8 años en Airbnb",
             url="https://www.airbnb.com/rooms/28667828"),
        dict(slug="dagua-km26", corto="Dagua km 26", rank="Descuento vigente",
             nombre="Casa de campo con piscina y sauna km 26 vía al mar", lugar="Cabaña en Dagua",
             precio=2070000, antes=2290000, cap=10, hab=4, camas=10, banos="3", nota="4,8", resenas=5,
             tags=[("Piscina", ""), ("Sauna", ""), ("Terraza", ""), ("Cancelación gratuita", "")],
             pro="Buena calificación, piscina con vista, sauna y una cama por persona. Precio con descuento.",
             con="Solo 3 baños para 9. Queda en la vía al mar, a unos 40 minutos de Cali.",
             host="Anfitrión: Ivan Dario · 2 años en Airbnb",
             url="https://www.airbnb.com/rooms/1262351601757843663"),
        dict(slug="finca-el-jardin", corto="El Jardín Pance", rank="Más cerca de la ciudad",
             nombre="Finca El Jardín Pance-Cali", lugar="Casa de campo en La Voragine, Pance",
             precio=2422959, antes=None, cap=10, hab=3, camas=10, banos="3", nota="4,67", resenas=3,
             tags=[("Piscina", ""), ("Brasero", ""), ("Parrilla", ""), ("Cafetera", ""), ("Cancelación gratuita", "")],
             pro="Pance es la zona más cercana a Cali de las seis, con piscina grande y zona de parrilla.",
             con="Solo 3 habitaciones y 3 baños para 9. Más cara que las cuatro anteriores.",
             host="Anfitriona: Vicky · 2 años en Airbnb",
             url="https://www.airbnb.com/rooms/1243578139140209598"),
        dict(slug="finca-recreo-dapa", corto="Finca Dapa", rank="Mejor calificación",
             nombre="Finca de recreo Dapa Cali jacuzzi 4 habitaciones", lugar="Casa de campo en Dapa, Yumbo",
             precio=3547177, antes=None, cap=11, hab=4, camas=8, banos="3", nota="4,92", resenas=24,
             tags=[("Favorito entre huéspedes", "fav"), ("Jacuzzi", ""), ("Cocina al aire libre", ""), ("Brasero", ""), ("Parrilla", ""), ("Cancelación gratuita", "")],
             pro="La finca más confiable: 4,92 con 24 reseñas y sello de favorito. Casa colonial muy cuidada.",
             con="Cuesta un 75 % más que las demás fincas. No menciona piscina, solo jacuzzi. 8 camas para 9.",
             host="Anfitrión: Danny · 3 años en Airbnb",
             url="https://www.airbnb.com/rooms/897636893265667568"),
    ])


def cop(n):
    return "$" + f"{round(n):,}".replace(",", ".")


def barrio(it):
    b = it.get("barrio")
    if not b:
        return ""
    ps = "".join(f"<p>{escape(t)}</p>" for t in b["texto"])
    return f'<details class="barrio"><summary>Sobre el barrio: {escape(b["nombre"])}</summary>{ps}</details>'


def vuelos():
    cards = ""
    for v in VUELOS["items"]:
        notas = "".join(f"<li>{escape(n)}</li>" for n in v["notas"])
        cards += f'''
      <li class="flight">
        <div class="ftop">
          <div class="times"><strong>{v["sale"]}</strong><span class="arrow">→</span><strong>{v["llega"]}</strong>
            <span class="codes">BOG a CLO · {escape(v["dur"])}</span></div>
          <div class="fprice"><strong>{cop(v["precio"])}</strong><span>ida y vuelta, por persona</span></div>
        </div>
        <div class="airline">{escape(v["aerolinea"])}</div>
        <ul class="fnotes">{notas}</ul>
      </li>'''
    return f'''
    <section class="leg" aria-labelledby="vuelos">
      <h2 class="leg-title" id="vuelos">Vuelos</h2>
      <p class="leg-sub">{escape(VUELOS["ruta"])}. {escape(VUELOS["sub"])}</p>
      <div class="summary two">
        <div><span>Rango por persona</span><strong>{cop(VUELO_MIN)} a {cop(VUELO_MAX)}</strong></div>
        <div><span>Aerolíneas</span><strong>{", ".join(v["aerolinea"] for v in VUELOS["items"])}</strong></div>
      </div>
      <ol class="flights">{cards}
      </ol>
      <p class="note">Ninguna tarifa incluye maleta de mano en cabina, solo un artículo personal. Sumar la maleta puede cambiar cuál es la más barata.</p>
    </section>'''


def card(i, it, leg):
    was = f'<span class="was">{cop(it["antes"])}</span>' if it.get("antes") else ""
    nota = (f'★ {it["nota"]} <span class="n">({it["resenas"]} reseñas)</span>' if it["nota"]
            else f'★ Sin calificación <span class="n">({it["resenas"]} reseñas)</span>')
    tags = "".join(f'<span class="tag {c}">{escape(t)}</span>' for t, c in it["tags"])
    if it.get("url"):
        q = f'?check_in={leg["check_in"]}&check_out={leg["check_out"]}&adults={PERSONAS}'
        btn = f'<a class="btn" href="{it["url"]}{q}" target="_blank" rel="noopener">Ver en Airbnb</a>'
    else:
        btn = (f'<a class="btn ghost" href="{it["buscar"]}" target="_blank" rel="noopener">Buscar en Airbnb</a>'
               f'<p class="pend">Enlace exacto pendiente. Búsqueda por nombre mientras tanto.</p>')
    return f'''
      <li class="card" id="{it["slug"]}">
        <a class="photo" href="{it.get("url") or it["buscar"]}" target="_blank" rel="noopener">
          <img src="img/{it["slug"]}.jpg" alt="Foto de {escape(it["nombre"])}" loading="lazy" width="900" height="429">
        </a>
        <div class="body">
          <div class="top">
            <div>
              <div class="rank">#{i} · {escape(it["rank"])}</div>
              <h3>{escape(it["nombre"])}</h3>
              <p class="place">{escape(it["lugar"])}</p>
            </div>
            <div class="price">
              {was}
              <span class="total">{cop(it["precio"])}</span>
              <span class="night">{cop(it["precio"] / leg["noches"])} por noche</span>
            </div>
          </div>
          <p class="each"><span>Cada uno paga</span><strong>{cop(it["precio"] / PERSONAS)}</strong><small>entre {PERSONAS}, por {leg["noches"]} noches</small></p>
          <ul class="facts">
            <li>{it["cap"]} huéspedes</li><li>{it["hab"]} habitaciones</li><li>{it["camas"]} camas</li><li>{it["banos"]} baños</li>
            <li class="rating">{nota}</li>
          </ul>
          <div class="tags">{tags}</div>
          {barrio(it)}
          <p class="pro">{escape(it["pro"])}</p>
          <p class="con">{escape(it["con"])}</p>
          <p class="host">{escape(it["host"])}</p>
          {btn}
        </div>
      </li>'''


def leg(l):
    res = "".join(f'<div><span>{escape(a)}</span><strong>{escape(b)}</strong></div>' for a, b in l["resumen"])
    cards = "".join(card(i + 1, it, l) for i, it in enumerate(l["items"]))
    return f'''
    <section class="leg" aria-labelledby="{l["id"]}">
      <h2 class="leg-title" id="{l["id"]}">{escape(l["titulo"])}</h2>
      <p class="leg-sub">{escape(l["sub"])}</p>
      <div class="summary">{res}</div>
      <ol class="cards">{cards}
      </ol>
    </section>'''


CSS = """
    :root {
      --bg: #f7f7f5; --card: #ffffff; --fg: #1c1c1c; --muted: #6b6b6b; --line: #e5e5e2;
      --accent: #2563eb; --accent-fg: #ffffff; --accent-bg: #eff4ff;
      --good: #15803d; --good-bg: #ecfdf3; --warn: #b45309; --warn-bg: #fff7ed; --tag-bg: #f1f1ef;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #121212; --card: #1c1c1c; --fg: #f0f0f0; --muted: #9a9a9a; --line: #2c2c2c;
        --accent: #60a5fa; --accent-fg: #0b1220; --accent-bg: #16213a;
        --good: #4ade80; --good-bg: #14291b; --warn: #fbbf24; --warn-bg: #2b2210; --tag-bg: #262626;
      }
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: var(--fg);
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; line-height: 1.5; }
    .wrap { max-width: 720px; margin: 0 auto; padding: 32px 16px 64px; }
    header h1 { font-size: clamp(1.8rem, 6vw, 2.6rem); margin: 0 0 4px; letter-spacing: -0.02em; }
    header p { margin: 0; color: var(--muted); }
    .note { font-size: 0.85rem; color: var(--muted); margin: 12px 0 0; }
    section.leg { margin-top: 36px; }
    .leg-title { font-size: 1.4rem; margin: 0 0 2px; letter-spacing: -0.01em; }
    .leg-sub { color: var(--muted); margin: 0 0 8px; }
    .summary { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 12px 0 16px; }
    .summary div { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 12px; }
    .summary span { display: block; font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }
    .summary strong { display: block; font-size: 1.05rem; margin-top: 2px; }
    ol.cards { list-style: none; padding: 0; margin: 0; display: grid; gap: 20px; }
    .card { background: var(--card); border: 1px solid var(--line); border-radius: 16px; overflow: hidden; }
    .photo { display: block; aspect-ratio: 900 / 429; background: var(--tag-bg); }
    .photo img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .body { padding: 16px 18px 18px; }
    .top { display: flex; justify-content: space-between; gap: 12px; align-items: flex-start; }
    .rank { font-size: 0.8rem; color: var(--muted); font-weight: 600; }
    h3 { font-size: 1.15rem; margin: 2px 0 2px; line-height: 1.3; }
    .place { color: var(--muted); font-size: 0.95rem; margin: 0; }
    .price { text-align: right; white-space: nowrap; }
    .price .total { font-weight: 700; font-size: 1.1rem; display: block; }
    .price .was { color: var(--muted); text-decoration: line-through; font-size: 0.85rem; display: block; }
    .price .night { color: var(--muted); font-size: 0.8rem; display: block; }
    .each { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; margin: 12px 0 0;
      padding: 10px 12px; border-radius: 10px; background: var(--accent-bg); }
    .each span { color: var(--muted); font-size: 0.85rem; }
    .each strong { color: var(--accent); font-size: 1.25rem; }
    .each small { color: var(--muted); font-size: 0.8rem; margin-left: auto; }
    .tablewrap { overflow-x: auto; background: var(--card); border: 1px solid var(--line); border-radius: 12px; }
    table.combos { border-collapse: collapse; width: 100%; font-size: 0.9rem; }
    .combos th, .combos td { padding: 10px 8px; text-align: right; border-bottom: 1px solid var(--line); white-space: nowrap; }
    .combos th[scope="row"], .combos thead th:first-child { text-align: left; font-weight: 500;
      white-space: normal; color: var(--fg); }
    .combos thead th { font-size: 0.8rem; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.03em; }
    .combos tbody tr:last-child th, .combos tbody tr:last-child td { border-bottom: 0; }
    .combos td { font-weight: 600; color: var(--accent); font-variant-numeric: tabular-nums; }
    @media (max-width: 420px) { table.combos { font-size: 0.8rem; } .combos th, .combos td { padding: 9px 5px; } .combos thead th { font-size: 0.7rem; } }
    .facts { display: flex; flex-wrap: wrap; gap: 6px 14px; margin: 12px 0 10px; padding: 0; list-style: none; font-size: 0.95rem; }
    .facts li::before { content: "· "; color: var(--muted); }
    .facts li:first-child::before { content: ""; }
    .rating { font-weight: 600; }
    .rating .n { color: var(--muted); font-weight: 400; }
    .tags { display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 12px; }
    .tag { background: var(--tag-bg); border-radius: 999px; padding: 3px 10px; font-size: 0.8rem; }
    .tag.fav { background: var(--good-bg); color: var(--good); font-weight: 600; }
    .pro, .con { margin: 0; font-size: 0.9rem; padding: 8px 12px; border-radius: 10px; }
    .pro { background: var(--good-bg); color: var(--good); }
    .con { background: var(--warn-bg); color: var(--warn); margin-top: 6px; }
    .host { color: var(--muted); font-size: 0.85rem; margin: 12px 0 0; }
    .btn { display: block; text-align: center; margin-top: 14px; padding: 12px 16px; border-radius: 12px;
      background: var(--accent); color: var(--accent-fg); font-weight: 600; text-decoration: none; }
    .btn.ghost { background: transparent; color: var(--accent); border: 1px solid var(--accent); }
    .pend { margin: 6px 0 0; font-size: 0.8rem; color: var(--muted); text-align: center; }
    .summary.two { grid-template-columns: 1fr 1fr; }
    .summary.two strong { font-size: 0.95rem; }
    ol.flights { list-style: none; padding: 0; margin: 0; display: grid; gap: 12px; }
    .flight { background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 14px 16px; }
    .ftop { display: flex; justify-content: space-between; gap: 12px; align-items: flex-start; }
    .times strong { font-size: 1.25rem; }
    .times .arrow { color: var(--muted); margin: 0 8px; }
    .times .codes { display: block; color: var(--muted); font-size: 0.85rem; }
    .fprice { text-align: right; white-space: nowrap; }
    .fprice strong { display: block; color: var(--accent); font-size: 1.1rem; }
    .fprice span { display: block; color: var(--muted); font-size: 0.75rem; }
    .airline { font-weight: 600; margin-top: 8px; }
    .fnotes { margin: 6px 0 0; padding-left: 18px; color: var(--muted); font-size: 0.85rem; }
    .fnotes li { margin: 2px 0; }
    details.barrio { margin: 0 0 12px; border: 1px solid var(--line); border-radius: 10px; padding: 0 12px; }
    details.barrio summary { cursor: pointer; padding: 10px 0; font-weight: 600; font-size: 0.9rem; }
    details.barrio p { margin: 0 0 10px; font-size: 0.9rem; color: var(--fg); }
    details.barrio[open] summary { border-bottom: 1px solid var(--line); margin-bottom: 10px; }
    footer { margin-top: 32px; color: var(--muted); font-size: 0.85rem; text-align: center; }
    footer a { color: var(--accent); text-decoration: none; }
    @media (max-width: 480px) {
      .summary { grid-template-columns: 1fr 1fr; }
      .top { flex-direction: column; }
      .ftop { flex-direction: column; }
      .fprice { text-align: left; }
      .summary.two { grid-template-columns: 1fr; }
      .each small { margin-left: 0; width: 100%; }
      .price { text-align: left; }
    }
"""

def combos():
    cols = "".join(f'<th scope="col">{escape(c["corto"])}</th>' for c in CIUDAD["items"])
    rows = ""
    for f in FINCA["items"]:
        cells = "".join(f'<td>{cop((f["precio"] + c["precio"]) / PERSONAS)[1:]}</td>' for c in CIUDAD["items"])
        rows += f'<tr><th scope="row">{escape(f["corto"])}</th>{cells}</tr>'
    return f'''
    <section class="leg" aria-labelledby="total">
      <h2 class="leg-title" id="total">Cuánto paga cada uno en total</h2>
      <p class="leg-sub">Ciudad más finca, 6 noches, dividido entre {PERSONAS}. En pesos colombianos, sin vuelo. Filas: finca. Columnas: ciudad.</p>
      <div class="tablewrap">
        <table class="combos">
          <thead><tr><th scope="col">Finca / Ciudad</th>{cols}</tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
      <p class="note">Con el vuelo, suma entre {cop(VUELO_MIN)} y {cop(VUELO_MAX)} a cada casilla. La combinación más barata, Granada más Villa Campestre, queda entre {cop((CIUDAD["items"][0]["precio"] + FINCA["items"][0]["precio"]) / PERSONAS + VUELO_MIN)} y {cop((CIUDAD["items"][0]["precio"] + FINCA["items"][0]["precio"]) / PERSONAS + VUELO_MAX)} por persona.</p>
    </section>'''


HTML = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cali, fin de año</title>
  <meta name="description" content="Comparación de alojamientos en Airbnb para el viaje a Cali del 28 de diciembre al 3 de enero, {PERSONAS} personas.">
  <style>{CSS}  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>Cali, 28 de diciembre al 3 de enero</h1>
      <p>Somos {PERSONAS}. Opciones en Airbnb para los dos tramos del viaje, ordenadas por precio dentro de cada tramo. Ninguna pide pago hoy.</p>
      <p class="note">Precios en COP tal como aparecían en Airbnb el {FECHA_PRECIOS}. Pueden cambiar. El precio por persona divide el total entre {PERSONAS}. Los botones abren Airbnb con las fechas y las {PERSONAS} personas ya puestas.</p>
    </header>
{vuelos()}
{leg(CIUDAD)}
{leg(FINCA)}
{combos()}
    <footer>
      <a href="https://github.com/mayckths/cali">Editar en GitHub</a>
    </footer>
  </div>
</body>
</html>
'''

open("index.html", "w").write(HTML)
print("index.html generado:", len(HTML), "bytes")
