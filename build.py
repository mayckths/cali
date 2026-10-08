#!/usr/bin/env python3
"""Genera index.html a partir de los datos de abajo. Ejecutar: python3 build.py"""
from html import escape

PERSONAS = 8
FECHA_PRECIOS = "18 de septiembre de 2026"

VUELOS = dict(
    ruta="Bogotá (BOG) a Cali (CLO)", sub="Ida y vuelta por persona, 28 de diciembre al 3 de enero. Vistos en Google Flights el 8 de octubre de 2026. Sin equipaje de mano.",
    items=[
        dict(aerolinea="Wingo", sale="0:00", llega="1:08", dur="1 h 8 min", precio=392775),
        dict(aerolinea="JetSMART", sale="5:05", llega="6:19", dur="1 h 14 min", precio=438060),
        dict(aerolinea="LATAM", sale="11:30", llega="12:40", dur="1 h 10 min", precio=439010),
    ])
VUELO_MIN = min(v["precio"] for v in VUELOS["items"])
VUELO_MAX = max(v["precio"] for v in VUELOS["items"])

CIUDAD = dict(
    id="ciudad", titulo="En la ciudad", fechas="28 dic a 1 ene",
    noches=4, check_in="2026-12-28", check_out="2027-01-01",
    resumen=[("Más barata", "Apto Jaime"), ("Mejor calificada", "Posada ABBA"), ("Más baños", "Posada ABBA")],
    items=[
        dict(slug="apto-jaime", corto="Apto Jaime", rank="Precio más bajo · Superanfitrión",
             nombre="Apartamento grande y cómodo - Cozy large apartment", lugar="Vivienda en Cali, cerca del centro y la Avenida 6N",
             precio=2826961, antes=None, cap=14, hab=3, camas=7, banos="2", nota="4,63", resenas=38,
             tags=[("Superanfitrión", ""), ("Zona de trabajo con wifi", ""), ("Cancelación gratuita", "")],
             pro="La más barata de la ciudad por lejos. Superanfitrión con 4 años y 38 reseñas, 7 camas para 8 y cancelación gratis hasta el 27 de diciembre.",
             con="Solo 2 baños para 8, y la calificación es la más baja de la ciudad. No menciona aire acondicionado.",
             barrio=dict(nombre="Norte, cerca de la Avenida 6N", texto=[
                 "El anuncio dice que está en el corazón de Cali, cerca del centro y de la Avenida 6N, la avenida que cruza el norte y conecta Granada, Chipichape y el centro.",
                 "Si queda sobre la 6N, Granada y su zona de restaurantes están a pocas cuadras a pie. Al abrir el anuncio en Airbnb, el mapa muestra la zona aproximada antes de reservar."]),
             url="https://www.airbnb.cl/rooms/876849081818118019?unique_share_id=561908c4-437e-4286-9436-9c5a097e3c69&viralityEntryPoint=1&s=76"),
        dict(slug="posada-abba", corto="Posada ABBA", rank="Mejor calificación",
             nombre="Posada Familiar ABBA. Casa al sur de Cali", lugar="Casa en el sur de Cali",
             precio=3953711, antes=None, cap=10, hab=5, camas=7, banos="4,5", nota="5,0", resenas=7,
             tags=[("Favorito entre huéspedes", "fav"), ("Aire acondicionado", ""), ("Cancelación gratuita", "")],
             pro="Calificación perfecta con 7 reseñas y sello de favorito. 5 habitaciones y 4,5 baños para 8: casi un baño por habitación.",
             con="7 camas para 8, una pareja comparte.",
             barrio=dict(nombre="Sur de Cali", texto=[
                 "El anuncio la ubica en el sur de Cali, la zona residencial de la ciudad: barrios de casas y conjuntos, con supermercados, centros comerciales como Unicentro y Jardín Plaza, y clínicas cerca.",
                 "Es la parte de la ciudad más cercana a Pance y al río, y queda bien conectada por la Autopista Sur y la Avenida Cañasgordas. Para ir a comer o a rumbear a Granada o San Antonio hay que coger taxi, unos 25 o 30 minutos.",
                 "Es una zona tranquila y segura para un grupo con carro, a cambio de estar lejos del ambiente del centro."]),
             url="https://www.airbnb.cl/rooms/989271767589296963?unique_share_id=7cf59e94-326d-4a00-b29f-0e7ffb0964de&viralityEntryPoint=1&s=76"),
    ])

FINCA = dict(
    id="finca", titulo="Finca", fechas="1 a 3 ene",
    noches=2, check_in="2027-01-01", check_out="2027-01-03",
    resumen=[("Calificación", "4,91 · 43 reseñas"), ("Piscina y jacuzzi", "3 baños"), ("Precio enero", "Confirmado")],
    items=[
        dict(slug="finca-angela", corto="Finca Angela", rank="Única opción disponible",
             nombre="Finca nueva encantadora con jacuzzi", lugar="Alojamiento vacacional en Rozo, Palmira",
             precio=2800000, antes=None, cap=8, hab=3, camas=4, banos="3", nota="4,91", resenas=43,
             tags=[("Favorito entre huéspedes", "fav"), ("Piscina", ""), ("Jacuzzi", ""), ("Brasero", ""), ("Cancelación gratuita", "")],
             pro="La finca más confiable: 4,91 con 43 reseñas, sello de favorito y anfitriona con 8 años. Piscina, jacuzzi y 3 baños. Precio confirmado para el 1 al 3 de enero con 8 personas.",
             con="Solo 4 camas para 8, así que todos comparten.",
             url="https://www.airbnb.cl/rooms/713793181158552706?unique_share_id=4c55635e-3083-4fd6-b81f-16170c3703dd&viralityEntryPoint=1&s=76"),
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
    if it["nota"]:
        nota = f'★ {it["nota"]}{it.get("escala", "")} <span class="n">({it["resenas"]} reseñas)</span>'
    elif it["resenas"]:
        nota = f'★ Sin calificación <span class="n">({it["resenas"]} reseñas)</span>'
    else:
        nota = '★ Aún sin reseñas'
    tags = "".join(f'<span class="tag {c}">{escape(t)}</span>' for t, c in it["tags"])
    plat = it.get("plataforma", "Airbnb")
    if it.get("url"):
        if plat == "Airbnb":
            sep = "&" if "?" in it["url"] else "?"
            q = f'{sep}adults={PERSONAS}&check_in={leg["check_in"]}&check_out={leg["check_out"]}'
        else:
            q = ""
        btn = f'<a class="btn" href="{it["url"]}{q}" target="_blank" rel="noopener">Ver en {plat}</a>'
    else:
        btn = (f'<a class="btn ghost" href="{it["buscar"]}" target="_blank" rel="noopener">Buscar en Airbnb</a>'
               f'<p class="pend">Enlace exacto pendiente. Búsqueda por nombre mientras tanto.</p>')
    return f'''
      <li class="card" id="{it["slug"]}">
        <a class="photo" href="{it["url"]}{q}" target="_blank" rel="noopener">
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
              <span class="total">{cop(it["precio"]) if it["precio"] else "Precio pendiente"}</span>
              {f'<span class="night">{escape(it["precio_nota"])}</span>' if it.get("precio_nota") else ''}
            </div>
          </div>
          {f'<p class="each"><span>Cada uno paga</span><strong>{cop(it["precio"] / PERSONAS)}</strong></p>' if it["precio"] else '<p class="each"><span>Cada uno paga</span><strong>por confirmar</strong></p>'}
          <ul class="facts">
            <li>{it["cap"]} huéspedes</li><li>{it["hab"]} {"apartamentos" if plat == "Booking" else "habitaciones"}</li>{f'<li>{it["camas"]} camas</li>' if it["camas"] else ''}<li>{it["banos"]} baños</li>
            <li class="rating">{nota}</li>
          </ul>
          <div class="tags">{tags}</div>
          {barrio(it)}
          <p class="pro">{escape(it["pro"])}</p>
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
          <span class="chip c-{l["id"]}">Desde {cop(min(i["precio"] for i in l["items"] if i["precio"]) / PERSONAS)} por persona</span>
          <span class="chip">{escape(l["fechas"])}</span>
          <span class="chip">{l["noches"]} noches</span>
          <span class="chip">{len(l["items"])} opciones</span>
        </span>
      </summary>
      <div class="summary">{res}</div>
      <ol class="cards">{cards}
      </ol>
      {('<p class="note">' + escape(l["aviso"]) + '</p>') if l.get("aviso") else ''}
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
    .grand { margin-top: 16px; background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 16px 18px; }
    .total-label { display: block; font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; }
    .total-range { display: block; font-size: clamp(1.4rem, 6vw, 1.9rem); letter-spacing: -0.02em; margin: 2px 0 4px; }
    .total-sub { display: block; font-size: 0.85rem; color: var(--muted); margin-bottom: 10px; }
    .picker { display: grid; gap: 10px; margin: 10px 0 14px; }
    .picker label { display: grid; gap: 4px; font-size: 0.8rem; color: var(--muted); }
    .picker select { width: 100%; font: inherit; font-size: 0.95rem; color: var(--fg); background: var(--bg);
      border: 1px solid var(--line); border-radius: 10px; padding: 10px 12px; -webkit-appearance: none; appearance: none;
      background-image: linear-gradient(45deg, transparent 50%, var(--muted) 50%), linear-gradient(135deg, var(--muted) 50%, transparent 50%);
      background-position: calc(100% - 18px) 50%, calc(100% - 12px) 50%; background-size: 6px 6px; background-repeat: no-repeat; padding-right: 34px; }
    .result { background: var(--accent-bg); border-radius: 12px; padding: 12px 14px; margin-bottom: 10px; }
    .result .total-range { color: var(--accent); margin-bottom: 2px; }
    .result .total-sub { margin-bottom: 0; }
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
    .price .night { white-space: normal; max-width: 220px; }
    .price .total { font-weight: 700; font-size: 1.1rem; display: block; }
    .price .was { color: var(--muted); text-decoration: line-through; font-size: 0.85rem; display: block; }
    .price .night { color: var(--muted); font-size: 0.8rem; display: block; }
    .each { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; margin: 12px 0 0;
      padding: 10px 12px; border-radius: 10px; background: var(--accent-bg); }
    .each span { color: var(--muted); font-size: 0.85rem; }
    .each strong { color: var(--accent); font-size: 1.25rem; }
    .each small { color: var(--muted); font-size: 0.8rem; margin-left: auto; }
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
    import json
    cp = [i["precio"] for i in CIUDAD["items"] if i["precio"]]
    fp = [i["precio"] for i in FINCA["items"] if i["precio"]]
    c_min, c_max = min(cp) / PERSONAS, max(cp) / PERSONAS
    f_min, f_max = min(fp) / PERSONAS, max(fp) / PERSONAS
    t_min = VUELO_MIN + c_min + f_min
    t_max = VUELO_MAX + c_max + f_max
    opt_c = "".join(f'<option value="{i["precio"]}">{escape(i["corto"])} · {cop(i["precio"] / PERSONAS)}</option>' for i in CIUDAD["items"] if i["precio"])
    opt_f = "".join(f'<option value="{i["precio"]}">{escape(i["corto"])} · {cop(i["precio"] / PERSONAS)}</option>' for i in FINCA["items"] if i["precio"])
    opt_v = "".join(f'<option value="{v["precio"]}">{escape(v["aerolinea"])} · {cop(v["precio"])}</option>' for v in VUELOS["items"])
    return f'''
    <section class="grand" aria-label="Calculadora por persona">
      <span class="total-label">Arma tu combinación</span>
      <div class="picker">
        <label><span>Casa en la ciudad</span><select id="selCiudad">{opt_c}</select></label>
        <label><span>Finca</span><select id="selFinca">{opt_f}</select></label>
        <label><span>Vuelo</span><select id="selVuelo">{opt_v}</select></label>
      </div>
      <div class="result">
        <span class="total-label">Cada uno paga, vuelo y estadía</span>
        <strong class="total-range" id="outTotal"></strong>
        <span class="total-sub" id="outDetalle"></span>
      </div>
      <span class="total-sub">Rango con todas las opciones: {cop(t_min)} a {cop(t_max)} por persona. Precios aproximados, los reales se ven en cada anuncio.</span>
    </section>
    <script>
      (function () {{
        var P = {PERSONAS};
        var sc = document.getElementById("selCiudad"), sf = document.getElementById("selFinca"), sv = document.getElementById("selVuelo");
        function cop(n) {{ return "$" + Math.round(n).toLocaleString("es-CO"); }}
        function calc() {{
          var c = +sc.value / P, f = +sf.value / P, v = +sv.value;
          document.getElementById("outTotal").textContent = cop(c + f + v);
          document.getElementById("outDetalle").textContent = "Ciudad " + cop(c) + " + finca " + cop(f) + " + vuelo " + cop(v) + ", dividido entre " + P + ".";
        }}
        [sc, sf, sv].forEach(function (el) {{ el.addEventListener("change", calc); }});
        calc();
      }})();
    </script>'''


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
    <p class="intro">Opciones en Airbnb para los dos tramos del viaje, ordenadas por precio dentro de cada tramo. Ninguna pide pago hoy. Precios en COP tal como aparecían el {FECHA_PRECIOS}; pueden cambiar. Los botones abren el anuncio con las fechas del tramo y las {PERSONAS} personas ya puestas.</p>
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
