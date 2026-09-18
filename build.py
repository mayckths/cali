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
    id="ciudad", titulo="En la ciudad", fechas="28 dic a 1 ene",
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
    id="finca", titulo="Finca", fechas="1 a 3 ene",
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
             url="https://www.airbnb.com/rooms/1511142141665799976"),
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
        cards += f'''
      <li class="flight">
        <div class="ftop">
          <div class="times"><strong>{v["sale"]}</strong><span class="arrow">→</span><strong>{v["llega"]}</strong>
            <span class="codes">BOG a CLO · {escape(v["dur"])}</span></div>
          <div class="fprice"><strong>{cop(v["precio"])}</strong><span>ida y vuelta, por persona</span></div>
        </div>
        <div class="airline">{escape(v["aerolinea"])}</div>
      </li>'''
    return f'''
    <details class="leg" id="vuelos">
      <summary>
        <span class="leg-head"><span class="dot c-vuelos"></span><span class="leg-title">Vuelos</span></span>
        <span class="chips">
          <span class="chip c-vuelos">{cop(VUELO_MIN)} a {cop(VUELO_MAX)} por persona</span>
          <span class="chip">BOG → CLO</span>
          <span class="chip">{len(VUELOS["items"])} aerolíneas</span>
        </span>
      </summary>
      <ol class="flights">{cards}
      </ol>
      <p class="note">{escape(VUELOS["sub"])}</p>
    </details>'''


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
          {btn}
        </div>
      </li>'''


def leg(l):
    res = "".join(f'<div><span>{escape(a)}</span><strong>{escape(b)}</strong></div>' for a, b in l["resumen"])
    cards = "".join(card(i + 1, it, l) for i, it in enumerate(l["items"]))
    return f'''
    <details class="leg" id="{l["id"]}">
      <summary>
        <span class="leg-head"><span class="dot c-{l["id"]}"></span><span class="leg-title">{escape(l["titulo"])}</span></span>
        <span class="chips">
          <span class="chip c-{l["id"]}">Desde {cop(min(i["precio"] for i in l["items"]) / PERSONAS)} por persona</span>
          <span class="chip">{escape(l["fechas"])}</span>
          <span class="chip">{l["noches"]} noches</span>
          <span class="chip">{len(l["items"])} opciones</span>
        </span>
      </summary>
      <div class="summary">{res}</div>
      <ol class="cards">{cards}
      </ol>
    </details>'''


CSS = """
    :root {
      --bg: #f7f7f5; --card: #ffffff; --fg: #1c1c1c; --muted: #6b6b6b; --line: #e5e5e2;
      --accent: #2563eb; --accent-fg: #ffffff; --accent-bg: #eff4ff;
      --good: #15803d; --good-bg: #ecfdf3; --warn: #b45309; --warn-bg: #fff7ed; --tag-bg: #f1f1ef;

    }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: var(--fg);
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; line-height: 1.5; }
    .wrap { max-width: 720px; margin: 0 auto; padding: 16px 16px 64px; }
    .hero { position: relative; border-radius: 20px; overflow: hidden; height: clamp(260px, 70vw, 380px); background: #1c2a3a; }
    .hero img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .hero-text { position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: flex-end; padding: 20px;
      background: linear-gradient(to top, rgba(0,0,0,0.78) 0%, rgba(0,0,0,0.35) 50%, rgba(0,0,0,0) 100%); color: #fff; }
    .hero-kicker { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.9; }
    .hero h1 { font-size: clamp(2.4rem, 10vw, 4rem); margin: 0; line-height: 1; letter-spacing: -0.03em; }
    .hero p { margin: 4px 0 0; font-size: 1.05rem; opacity: 0.95; }
    .intro { font-size: 0.9rem; color: var(--muted); margin: 16px 0 0; }
    .total { margin-top: 16px; background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 16px 18px; }
    .total-label { display: block; font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; }
    .total-range { display: block; font-size: clamp(1.4rem, 6vw, 1.9rem); letter-spacing: -0.02em; margin: 2px 0 4px; }
    .total-sub { display: block; font-size: 0.85rem; color: var(--muted); margin-bottom: 10px; }
    .chips { display: flex; flex-wrap: wrap; gap: 6px; }
    .chip { background: var(--tag-bg); color: var(--fg); border-radius: 999px; padding: 4px 10px; font-size: 0.8rem; font-weight: 500; white-space: nowrap; }
    .chip.c-vuelos, .chip.c-ciudad, .chip.c-finca { background: var(--accent-bg); color: var(--accent); font-weight: 600; }
    .dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; flex: none; background: var(--accent); }
    .leg-head { display: flex; align-items: center; gap: 10px; }
    .note { font-size: 0.85rem; color: var(--muted); margin: 12px 0 0; }
    section.leg, details.leg { margin-top: 24px; }
    details.leg { background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 0 16px; }
    details.leg > summary { list-style: none; cursor: pointer; padding: 16px 0; display: flex; flex-direction: column; gap: 10px; position: relative; }
    details.leg { border-left: 4px solid var(--accent); }
    details.leg > summary::-webkit-details-marker { display: none; }
    details.leg > summary::after { content: "+"; position: absolute; right: 0; top: 14px; font-size: 1.6rem; line-height: 1; color: var(--muted); }
    details.leg[open] > summary::after { content: "–"; }
    details.leg[open] > summary { border-bottom: 1px solid var(--line); margin-bottom: 14px; }
    details.leg > *:last-child { padding-bottom: 16px; }
    .leg-title { font-size: 1.4rem; font-weight: 700; letter-spacing: -0.01em; display: block; padding-right: 32px; }
    .leg-sub { color: var(--muted); margin: 8px 0 8px; display: block; font-size: 0.9rem; }
    details.leg .cards { margin-bottom: 4px; }
    details.leg .card { background: var(--bg); }
    details.leg .flight { background: var(--bg); }
    details.leg .summary div { background: var(--bg); }
    .summary { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 0 0 16px; }
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
      white-space: normal; color: var(--fg); }
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

def rango():
    c_min = min(i["precio"] for i in CIUDAD["items"]) / PERSONAS
    c_max = max(i["precio"] for i in CIUDAD["items"]) / PERSONAS
    f_min = min(i["precio"] for i in FINCA["items"]) / PERSONAS
    f_max = max(i["precio"] for i in FINCA["items"]) / PERSONAS
    t_min = VUELO_MIN + c_min + f_min
    t_max = VUELO_MAX + c_max + f_max
    return f'''
    <section class="total" aria-label="Total por persona">
      <span class="total-label">Total por persona, vuelos y estadía</span>
      <strong class="total-range">{cop(t_min)} a {cop(t_max)}</strong>
      <span class="total-sub">Vuelo ida y vuelta, {CIUDAD["noches"]} noches en la ciudad y {FINCA["noches"]} en finca, dividido entre {PERSONAS}.</span>
      <div class="chips">
        <span class="chip c-vuelos">Vuelo {cop(VUELO_MIN)} a {cop(VUELO_MAX)}</span>
        <span class="chip c-ciudad">Ciudad {cop(c_min)} a {cop(c_max)}</span>
        <span class="chip c-finca">Finca {cop(f_min)} a {cop(f_max)}</span>
      </div>
    </section>'''


HTML = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="color-scheme" content="light">
  <title>Cali, fin de año</title>
  <meta name="description" content="Comparación de alojamientos en Airbnb para el viaje a Cali del 28 de diciembre al 3 de enero, {PERSONAS} personas.">
  <style>{CSS}  </style>
</head>
<body>
  <div class="wrap">
    <header class="hero">
      <img src="img/cali.jpg" alt="Iglesia La Ermita y el centro de Cali" width="1200" height="653">
      <div class="hero-text">
        <span class="hero-kicker">Fin de año · {PERSONAS} personas</span>
        <h1>Cali</h1>
        <p>28 de diciembre al 3 de enero</p>
      </div>
    </header>
    <p class="intro">Opciones en Airbnb para los dos tramos del viaje, ordenadas por precio dentro de cada tramo. Ninguna pide pago hoy. Precios en COP tal como aparecían el {FECHA_PRECIOS}; pueden cambiar. Los botones abren Airbnb con las fechas y las {PERSONAS} personas ya puestas.</p>
{rango()}
{vuelos()}
{leg(CIUDAD)}
{leg(FINCA)}
    <footer>
      <a href="https://github.com/mayckths/cali">Editar en GitHub</a>
    </footer>
  </div>
</body>
</html>
'''

open("index.html", "w").write(HTML)
print("index.html generado:", len(HTML), "bytes")
