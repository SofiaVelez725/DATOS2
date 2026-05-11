import heapq
import math
from itertools import permutations, combinations




DESTINOS = {
    "Bali, Indonesia": {
        "intereses": ["playa", "cultura", "relax", "naturaleza", "arte"],
        "clima": "tropical",
        "epoca": [4, 5, 6, 7, 8, 9],
        "costo_dia": 60,
        "duracion_ideal": 7,
        "coordenadas": (-8.34, 115.09),
        "descripcion": "Isla de los dioses con templos, arrozales y playas paradisíacas"
    },
    "París, Francia": {
        "intereses": ["arte", "cultura", "gastronomia", "historia", "lujo"],
        "clima": "templado",
        "epoca": [4, 5, 6, 9, 10],
        "costo_dia": 200,
        "duracion_ideal": 5,
        "coordenadas": (48.85, 2.35),
        "descripcion": "La ciudad del amor, arte y alta gastronomía"
    },
    "Machu Picchu, Perú": {
        "intereses": ["historia", "aventura", "naturaleza", "cultura"],
        "clima": "templado",
        "epoca": [5, 6, 7, 8, 9],
        "costo_dia": 80,
        "duracion_ideal": 3,
        "coordenadas": (-13.16, -72.54),
        "descripcion": "Ciudad inca en las cimas de los Andes peruanos"
    },
    "Tokio, Japón": {
        "intereses": ["cultura", "gastronomia", "arte", "historia", "familia"],
        "clima": "templado",
        "epoca": [3, 4, 10, 11],
        "costo_dia": 150,
        "duracion_ideal": 7,
        "coordenadas": (35.68, 139.69),
        "descripcion": "Metrópolis futurista con tradición milenaria"
    },
    "Santorini, Grecia": {
        "intereses": ["playa", "relax", "lujo", "gastronomia", "historia"],
        "clima": "mediterraneo",
        "epoca": [5, 6, 7, 8, 9],
        "costo_dia": 180,
        "duracion_ideal": 5,
        "coordenadas": (36.39, 25.46),
        "descripcion": "Volcánica isla con vistas únicas al Mar Egeo"
    },
    "Safari Kenia": {
        "intereses": ["naturaleza", "aventura", "familia"],
        "clima": "tropical",
        "epoca": [1, 2, 6, 7, 8, 9, 10],
        "costo_dia": 250,
        "duracion_ideal": 7,
        "coordenadas": (-1.28, 36.82),
        "descripcion": "Vida salvaje africana en su estado más puro"
    },
    "Nueva York, EE.UU.": {
        "intereses": ["arte", "cultura", "gastronomia", "historia", "lujo"],
        "clima": "templado",
        "epoca": [4, 5, 6, 9, 10],
        "costo_dia": 250,
        "duracion_ideal": 5,
        "coordenadas": (40.71, -74.00),
        "descripcion": "La ciudad que nunca duerme, capital cultural del mundo"
    },
    "Maldivas": {
        "intereses": ["playa", "relax", "lujo", "naturaleza"],
        "clima": "tropical",
        "epoca": [11, 12, 1, 2, 3, 4],
        "costo_dia": 400,
        "duracion_ideal": 7,
        "coordenadas": (3.20, 73.22),
        "descripcion": "Atolones de ensueño con bungalows sobre el agua"
    },
    "Roma, Italia": {
        "intereses": ["historia", "arte", "gastronomia", "cultura"],
        "clima": "mediterraneo",
        "epoca": [4, 5, 6, 9, 10],
        "costo_dia": 160,
        "duracion_ideal": 5,
        "coordenadas": (41.90, 12.49),
        "descripcion": "La ciudad eterna, cuna de la civilización occidental"
    },
    "Patagonia, Argentina": {
        "intereses": ["naturaleza", "aventura", "relax"],
        "clima": "frio",
        "epoca": [11, 12, 1, 2, 3],
        "costo_dia": 100,
        "duracion_ideal": 7,
        "coordenadas": (-49.33, -73.00),
        "descripcion": "Glaciares, montañas y paisajes vírgenes del fin del mundo"
    },
    "Dubái, EAU": {
        "intereses": ["lujo", "cultura", "gastronomia", "arte"],
        "clima": "desertico",
        "epoca": [10, 11, 12, 1, 2, 3],
        "costo_dia": 300,
        "duracion_ideal": 4,
        "coordenadas": (25.20, 55.27),
        "descripcion": "Ciudad del futuro en medio del desierto árabe"
    },
    "Barcelona, España": {
        "intereses": ["arte", "playa", "gastronomia", "historia", "cultura"],
        "clima": "mediterraneo",
        "epoca": [4, 5, 6, 9, 10],
        "costo_dia": 140,
        "duracion_ideal": 5,
        "coordenadas": (41.39, 2.15),
        "descripcion": "Gaudí, tapas y el Mediterráneo en una sola ciudad"
    },
    "Isla de Pascua, Chile": {
        "intereses": ["historia", "aventura", "naturaleza", "cultura"],
        "clima": "templado",
        "epoca": [1, 2, 3, 10, 11, 12],
        "costo_dia": 150,
        "duracion_ideal": 4,
        "coordenadas": (-27.11, -109.35),
        "descripcion": "Misterio milenario de los Moai en el Pacífico Sur"
    },
    "Ámsterdam, Holanda": {
        "intereses": ["arte", "historia", "cultura", "gastronomia"],
        "clima": "templado",
        "epoca": [4, 5, 6, 7, 8],
        "costo_dia": 170,
        "duracion_ideal": 4,
        "coordenadas": (52.37, 4.89),
        "descripcion": "Canales, museos y bicicletas en la capital de los Países Bajos"
    },
    "Costa Rica": {
        "intereses": ["naturaleza", "aventura", "playa", "familia"],
        "clima": "tropical",
        "epoca": [12, 1, 2, 3, 4],
        "costo_dia": 100,
        "duracion_ideal": 7,
        "coordenadas": (9.75, -83.75),
        "descripcion": "Biodiversidad, volcanes y playas del Pacífico"
    },
    "Marrakech, Marruecos": {
        "intereses": ["cultura", "historia", "gastronomia", "arte"],
        "clima": "desertico",
        "epoca": [3, 4, 5, 9, 10, 11],
        "costo_dia": 70,
        "duracion_ideal": 4,
        "coordenadas": (31.63, -8.00),
        "descripcion": "Zócalos coloridos, medinas y encanto árabe-bereber"
    },
    "Islandia": {
        "intereses": ["naturaleza", "aventura", "relax"],
        "clima": "polar",
        "epoca": [6, 7, 8],
        "costo_dia": 200,
        "duracion_ideal": 7,
        "coordenadas": (64.96, -19.02),
        "descripcion": "Aurora boreal, géiseres y paisajes volcánicos"
    },
    "Bangkok, Tailandia": {
        "intereses": ["cultura", "gastronomia", "historia", "arte", "familia"],
        "clima": "tropical",
        "epoca": [11, 12, 1, 2, 3],
        "costo_dia": 60,
        "duracion_ideal": 5,
        "coordenadas": (13.75, 100.52),
        "descripcion": "Templos dorados, mercados flotantes y street food"
    },
    "Venecia, Italia": {
        "intereses": ["historia", "arte", "cultura", "romantico"],
        "clima": "mediterraneo",
        "epoca": [3, 4, 5, 9, 10],
        "costo_dia": 190,
        "duracion_ideal": 3,
        "coordenadas": (45.44, 12.33),
        "descripcion": "Ciudad flotante única en el mundo, patrimonio UNESCO"
    },
    "Río de Janeiro, Brasil": {
        "intereses": ["playa", "cultura", "aventura", "gastronomia", "familia"],
        "clima": "tropical",
        "epoca": [12, 1, 2, 3],
        "costo_dia": 90,
        "duracion_ideal": 5,
        "coordenadas": (-22.91, -43.17),
        "descripcion": "Ciudad maravillosa entre montañas y el Atlántico"
    },
    "Cartagena, Colombia": {
        "intereses": ["historia", "playa", "cultura", "gastronomia", "relax"],
        "clima": "tropical",
        "epoca": [12, 1, 2, 3, 4],
        "costo_dia": 70,
        "duracion_ideal": 4,
        "coordenadas": (10.39, -75.51),
        "descripcion": "Ciudad amurallada colonial en el Caribe colombiano"
    },
    "Praga, República Checa": {
        "intereses": ["historia", "arte", "cultura", "gastronomia"],
        "clima": "templado",
        "epoca": [4, 5, 6, 9, 10],
        "costo_dia": 100,
        "duracion_ideal": 4,
        "coordenadas": (50.08, 14.44),
        "descripcion": "Cuentos de hadas medievales a orillas del Moldava"
    },
    "Sydney, Australia": {
        "intereses": ["playa", "cultura", "aventura", "gastronomia", "familia"],
        "clima": "templado",
        "epoca": [10, 11, 12, 1, 2, 3],
        "costo_dia": 180,
        "duracion_ideal": 5,
        "coordenadas": (-33.87, 151.21),
        "descripcion": "Opera House, playas y vida cosmopolita en el Pacífico Sur"
    },
    "Petra, Jordania": {
        "intereses": ["historia", "aventura", "cultura"],
        "clima": "desertico",
        "epoca": [3, 4, 10, 11],
        "costo_dia": 80,
        "duracion_ideal": 2,
        "coordenadas": (30.33, 35.44),
        "descripcion": "Ciudad rosa tallada en roca por los nabateos"
    },
    "Seúl, Corea del Sur": {
        "intereses": ["cultura", "gastronomia", "historia", "arte", "familia"],
        "clima": "templado",
        "epoca": [3, 4, 5, 9, 10],
        "costo_dia": 100,
        "duracion_ideal": 5,
        "coordenadas": (37.57, 126.98),
        "descripcion": "K-pop, palacios Joseon y gastronomía de clase mundial"
    },
    "Phuket, Tailandia": {
        "intereses": ["playa", "relax", "aventura", "gastronomia"],
        "clima": "tropical",
        "epoca": [11, 12, 1, 2, 3, 4],
        "costo_dia": 70,
        "duracion_ideal": 7,
        "coordenadas": (7.88, 98.39),
        "descripcion": "Playas blancas y aguas turquesas en el Índico"
    },
    "Cusco, Perú": {
        "intereses": ["historia", "cultura", "aventura", "arte"],
        "clima": "templado",
        "epoca": [5, 6, 7, 8, 9],
        "costo_dia": 60,
        "duracion_ideal": 4,
        "coordenadas": (-13.53, -71.97),
        "descripcion": "Navel del mundo inca, puerta a Machu Picchu"
    },
    "Lisboa, Portugal": {
        "intereses": ["historia", "cultura", "gastronomia", "arte", "playa"],
        "clima": "mediterraneo",
        "epoca": [4, 5, 6, 9, 10],
        "costo_dia": 110,
        "duracion_ideal": 4,
        "coordenadas": (38.72, -9.14),
        "descripcion": "Fado, pastéis de nata y tranvías por las siete colinas"
    },
    "Zúrich, Suiza": {
        "intereses": ["lujo", "naturaleza", "gastronomia", "cultura"],
        "clima": "templado",
        "epoca": [6, 7, 8, 12],
        "costo_dia": 300,
        "duracion_ideal": 3,
        "coordenadas": (47.38, 8.54),
        "descripcion": "Capital financiera rodeada de Alpes y lagos cristalinos"
    },
    "Cancún, México": {
        "intereses": ["playa", "relax", "aventura", "historia", "familia"],
        "clima": "tropical",
        "epoca": [12, 1, 2, 3, 4, 5],
        "costo_dia": 120,
        "duracion_ideal": 7,
        "coordenadas": (21.16, -86.85),
        "descripcion": "Riviera Maya, cenotes y ruinas mayas en el Caribe"
    },
    "Ciudad de México": {
        "intereses": ["historia", "gastronomia", "arte", "cultura"],
        "clima": "templado",
        "epoca": [3, 4, 10, 11, 12],
        "costo_dia": 70,
        "duracion_ideal": 5,
        "coordenadas": (19.43, -99.13),
        "descripcion": "Aztecas, murales de Rivera y gastronomía patrimonio UNESCO"
    },
    "Viena, Austria": {
        "intereses": ["arte", "historia", "cultura", "gastronomia", "lujo"],
        "clima": "templado",
        "epoca": [4, 5, 6, 9, 10],
        "costo_dia": 150,
        "duracion_ideal": 4,
        "coordenadas": (48.21, 16.37),
        "descripcion": "Palacios imperiales, ópera y Sachertorte"
    },
    "Nairobi, Kenia": {
        "intereses": ["aventura", "naturaleza", "cultura"],
        "clima": "tropical",
        "epoca": [1, 2, 6, 7, 8, 9],
        "costo_dia": 80,
        "duracion_ideal": 3,
        "coordenadas": (-1.29, 36.82),
        "descripcion": "Puerta de entrada a los safaris africanos"
    },
    "Fiordos de Noruega": {
        "intereses": ["naturaleza", "aventura", "relax"],
        "clima": "frio",
        "epoca": [5, 6, 7, 8],
        "costo_dia": 220,
        "duracion_ideal": 7,
        "coordenadas": (61.00, 6.00),
        "descripcion": "Paisajes escandinávos de postal con fiordos y cascadas"
    },
    "Angkor Wat, Camboya": {
        "intereses": ["historia", "cultura", "aventura", "naturaleza"],
        "clima": "tropical",
        "epoca": [11, 12, 1, 2, 3],
        "costo_dia": 50,
        "duracion_ideal": 3,
        "coordenadas": (13.41, 103.87),
        "descripcion": "El mayor templo religioso del mundo entre la selva"
    },
    "Hawái, EE.UU.": {
        "intereses": ["playa", "naturaleza", "aventura", "relax", "familia"],
        "clima": "tropical",
        "epoca": [4, 5, 9, 10],
        "costo_dia": 250,
        "duracion_ideal": 7,
        "coordenadas": (20.80, -156.33),
        "descripcion": "Volcanes activos, surf y aloha en el Pacífico"
    },
    "Medellín, Colombia": {
        "intereses": ["cultura", "aventura", "gastronomia", "historia", "naturaleza"],
        "clima": "templado",
        "epoca": [1, 2, 3, 7, 8],
        "costo_dia": 50,
        "duracion_ideal": 4,
        "coordenadas": (6.25, -75.56),
        "descripcion": "Ciudad de la eterna primavera, innovadora y vibrante"
    },
    "Estambul, Turquía": {
        "intereses": ["historia", "cultura", "gastronomia", "arte"],
        "clima": "mediterraneo",
        "epoca": [4, 5, 9, 10],
        "costo_dia": 90,
        "duracion_ideal": 5,
        "coordenadas": (41.01, 28.97),
        "descripcion": "Puente entre Europa y Asia, mezquitas y bazares"
    },
    "Galápagos, Ecuador": {
        "intereses": ["naturaleza", "aventura", "ciencia"],
        "clima": "tropical",
        "epoca": [6, 7, 8, 9, 10, 11],
        "costo_dia": 200,
        "duracion_ideal": 7,
        "coordenadas": (-0.95, -90.96),
        "descripcion": "Paraíso de la biodiversidad que inspiró a Darwin"
    },
    "Florencia, Italia": {
        "intereses": ["arte", "historia", "gastronomia", "cultura"],
        "clima": "mediterraneo",
        "epoca": [4, 5, 6, 9, 10],
        "costo_dia": 160,
        "duracion_ideal": 4,
        "coordenadas": (43.77, 11.25),
        "descripcion": "Cuna del Renacimiento, David de Miguel Ángel y Uffizi"
    },
    "Queenstown, Nueva Zelanda": {
        "intereses": ["aventura", "naturaleza", "relax"],
        "clima": "templado",
        "epoca": [11, 12, 1, 2, 3],
        "costo_dia": 180,
        "duracion_ideal": 5,
        "coordenadas": (-45.03, 168.66),
        "descripcion": "Capital mundial del aventura extrema entre fiordos"
    },
    "Sahara, Marruecos": {
        "intereses": ["aventura", "naturaleza", "cultura"],
        "clima": "desertico",
        "epoca": [10, 11, 12, 1, 2, 3],
        "costo_dia": 80,
        "duracion_ideal": 3,
        "coordenadas": (31.00, -4.00),
        "descripcion": "Mar de dunas y cielos estrellados en el mayor desierto"
    },
    "Kyoto, Japón": {
        "intereses": ["historia", "cultura", "arte", "naturaleza"],
        "clima": "templado",
        "epoca": [3, 4, 10, 11],
        "costo_dia": 120,
        "duracion_ideal": 5,
        "coordenadas": (35.01, 135.77),
        "descripcion": "Geishas, templos zen y cerezos en flor"
    },
    "Bogotá, Colombia": {
        "intereses": ["historia", "arte", "cultura", "gastronomia"],
        "clima": "templado",
        "epoca": [12, 1, 2, 6, 7],
        "costo_dia": 50,
        "duracion_ideal": 3,
        "coordenadas": (4.71, -74.07),
        "descripcion": "Museos, historia precolombina y gastronomía en la sabana"
    },
    "Cinque Terre, Italia": {
        "intereses": ["playa", "naturaleza", "gastronomia", "relax"],
        "clima": "mediterraneo",
        "epoca": [5, 6, 7, 8, 9],
        "costo_dia": 140,
        "duracion_ideal": 3,
        "coordenadas": (44.12, 9.72),
        "descripcion": "Cinco aldeas de colores en los acantilados ligures"
    },
    "Seychelles": {
        "intereses": ["playa", "naturaleza", "relax", "lujo"],
        "clima": "tropical",
        "epoca": [4, 5, 10, 11],
        "costo_dia": 350,
        "duracion_ideal": 7,
        "coordenadas": (-4.68, 55.49),
        "descripcion": "Playas de granito rosado y tortugas gigantes"
    },
    "Buenos Aires, Argentina": {
        "intereses": ["cultura", "gastronomia", "arte", "historia", "familia"],
        "clima": "templado",
        "epoca": [10, 11, 12, 3, 4],
        "costo_dia": 60,
        "duracion_ideal": 5,
        "coordenadas": (-34.60, -58.38),
        "descripcion": "Tango, asado y arquitectura europea en el Río de la Plata"
    },
    "Cappadocia, Turquía": {
        "intereses": ["historia", "aventura", "naturaleza", "cultura"],
        "clima": "desertico",
        "epoca": [4, 5, 9, 10],
        "costo_dia": 80,
        "duracion_ideal": 3,
        "coordenadas": (38.64, 34.82),
        "descripcion": "Globos aerostáticos sobre paisajes lunares y ciudades subterráneas"
    },
    "Dubrovnik, Croacia": {
        "intereses": ["historia", "playa", "cultura", "gastronomia"],
        "clima": "mediterraneo",
        "epoca": [5, 6, 9, 10],
        "costo_dia": 130,
        "duracion_ideal": 4,
        "coordenadas": (42.65, 18.09),
        "descripcion": "Perla del Adriático, murallas medievales y aguas cristalinas"
    },
    "Mumbai, India": {
        "intereses": ["cultura", "gastronomia", "historia", "arte"],
        "clima": "tropical",
        "epoca": [10, 11, 12, 1, 2, 3],
        "costo_dia": 50,
        "duracion_ideal": 4,
        "coordenadas": (19.08, 72.88),
        "descripcion": "Ciudad de Bollywood, contrastes y sabores intensos"
    },
    "Zanzibar, Tanzania": {
        "intereses": ["playa", "historia", "cultura", "relax", "naturaleza"],
        "clima": "tropical",
        "epoca": [6, 7, 8, 9, 12, 1, 2],
        "costo_dia": 90,
        "duracion_ideal": 6,
        "coordenadas": (-6.16, 39.20),
        "descripcion": "Isla de especias con playas infinitas en el Índico"
    },
}


def distancia_km(coord1, coord2):
    R = 6371
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))


def calcular_peso(origen, destino, prioridad="mixto"):
    dist = distancia_km(DESTINOS[origen]["coordenadas"], DESTINOS[destino]["coordenadas"])
    costo = DESTINOS[destino]["costo_dia"] * DESTINOS[destino]["duracion_ideal"]
    duracion = DESTINOS[destino]["duracion_ideal"]

    if prioridad == "distancia":
        return dist * 0.6 + (costo / 500) * 0.25 + (duracion / 7) * 0.15
    elif prioridad == "costo":
        return (dist / 1000) * 0.25 + costo * 0.6 + (duracion / 7) * 0.15
    elif prioridad == "tiempo":
        return (dist / 1000) * 0.25 + (costo / 500) * 0.15 + duracion * 0.6
    else:  # mixto: equilibrio general
        return (dist / 1000) * 0.4 + (costo / 500) * 0.4 + (duracion / 7) * 0.2

##grafo 
def construir_grafo(destinos_validos, prioridad="mixto"):
    grafo = {d: {} for d in destinos_validos}
    for i, origen in enumerate(destinos_validos):
        for destino in destinos_validos:
            if origen != destino:
                grafo[origen][destino] = calcular_peso(origen, destino, prioridad)
    return grafo


def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}
    visitados = set()
    heap = [(0, inicio)]

    while heap:
        dist_actual, nodo_actual = heapq.heappop(heap)
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)
        for vecino, peso in grafo[nodo_actual].items():
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                predecesores[vecino] = nodo_actual
                heapq.heappush(heap, (nueva_dist, vecino))

    return distancias, predecesores


def calcular_longitud_ruta(ruta, grafo):
    return sum(grafo[ruta[i]][ruta[i+1]] for i in range(len(ruta) - 1))


def seleccionar_destinos_por_vecindad(destinos_validos, grafo, max_destinos=8):
    if len(destinos_validos) <= max_destinos:
        return destinos_validos

    puntajes = []
    for origen in destinos_validos:
        vecinos = sorted(grafo[origen][destino] for destino in destinos_validos if destino != origen)
        puntajes.append((sum(vecinos[:min(4, len(vecinos))]), origen))

    puntajes.sort()
    return [destino for _, destino in puntajes[:max_destinos]]


def encontrar_ruta_optima_5(destinos_validos, prioridad="mixto", max_dias=None, inicio_fijo=None):
    if len(destinos_validos) < 5:
        return destinos_validos, 0

    grafo = construir_grafo(destinos_validos, prioridad)
    mejor_ruta = None
    mejor_costo = float('inf')

    if inicio_fijo:
        if inicio_fijo not in destinos_validos:
            return None, float('inf')
        otros = [d for d in destinos_validos if d != inicio_fijo]
        candidatos = sorted(otros, key=lambda d: grafo[inicio_fijo][d])[:8]

        for subset in combinations(candidatos, 4):
            for perm in permutations(subset):
                ruta = [inicio_fijo] + list(perm)
                dias_ruta = sum(DESTINOS[d]["duracion_ideal"] for d in ruta)
                if max_dias is not None and dias_ruta > max_dias:
                    continue
                costo_total = calcular_longitud_ruta(ruta, grafo)
                if costo_total < mejor_costo:
                    mejor_costo = costo_total
                    mejor_ruta = ruta

        return mejor_ruta, mejor_costo

    candidatos = destinos_validos
    if len(destinos_validos) > 8:
        candidatos = seleccionar_destinos_por_vecindad(destinos_validos, grafo, max_destinos=8)

    for subset in combinations(candidatos, 5):
        for perm in permutations(subset):
            ruta = list(perm)
            dias_ruta = sum(DESTINOS[d]["duracion_ideal"] for d in ruta)
            if max_dias is not None and dias_ruta > max_dias:
                continue
            costo_total = calcular_longitud_ruta(ruta, grafo)
            if costo_total < mejor_costo:
                mejor_costo = costo_total
                mejor_ruta = ruta

    return mejor_ruta, mejor_costo


def calcular_stats_ruta(ruta):
    costo_total = sum(DESTINOS[d]["costo_dia"] * DESTINOS[d]["duracion_ideal"] for d in ruta)
    dias_totales = sum(DESTINOS[d]["duracion_ideal"] for d in ruta)
    distancia_total = sum(
        distancia_km(DESTINOS[ruta[i]]["coordenadas"], DESTINOS[ruta[i+1]]["coordenadas"])
        for i in range(len(ruta)-1)
    )
    return costo_total, dias_totales, int(distancia_total)



def pedir_opcion(prompt, opciones):
    print(prompt)
    for i, op in enumerate(opciones, 1):
        print(f"  {i}. {op}")
    while True:
        try:
            sel = int(input("  Tu elección: ").strip())
            if 1 <= sel <= len(opciones):
                return opciones[sel - 1]
        except ValueError:
            pass
        print("  Por favor ingresa un número válido.")


def pedir_rango(prompt, minimo, maximo):
    while True:
        try:
            val = float(input(f"  {prompt} ({minimo}–{maximo}): ").strip())
            if minimo <= val <= maximo:
                return val
        except ValueError:
            pass
        print(f"  Ingresa un número entre {minimo} y {maximo}.")


def pedir_mes():
    meses = [
        "Enero","Febrero","Marzo","Abril","Mayo","Junio",
        "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
    ]
    return pedir_opcion("¿En qué mes viajarás?", meses)


def filtrar_destinos_modo1(interes, presupuesto_dia, clima, mes_num, dias_disponibles):
    validos = []
    for nombre, datos in DESTINOS.items():
        if interes not in datos["intereses"]:
            continue
        if datos["costo_dia"] > presupuesto_dia:
            continue
        if clima and datos["clima"] != clima:
            continue
        if mes_num not in datos["epoca"]:
            continue
        if datos["duracion_ideal"] > dias_disponibles:
            continue
        validos.append(nombre)
    return validos


def obtener_condicion_desde_base(destino_base, atributo):
    base = DESTINOS[destino_base]
    if atributo == "intereses":
        return atributo, base["intereses"]
    elif atributo == "clima":
        return atributo, base["clima"]
    elif atributo == "mes":
        return atributo, base["epoca"]
    elif atributo == "costo_dia":
        return atributo, base["costo_dia"]
    elif atributo == "duracion_ideal":
        return atributo, base["duracion_ideal"]
    return atributo, None


def filtrar_destinos_modo2(destino_base, condicion1, condicion2):
    validos = [destino_base]
    for nombre, datos in DESTINOS.items():
        if nombre == destino_base:
            continue
        if cumple_condicion_atributo(datos, condicion1) and cumple_condicion_atributo(datos, condicion2):
            validos.append(nombre)
    return list(dict.fromkeys(validos))



def cumple_condicion_atributo(datos, condicion):
    atributo, valor = condicion
    if atributo == "intereses":
        comunes = set(valor) & set(datos["intereses"])
        return len(comunes) >= 2
    elif atributo == "clima":
        similares = {
            "tropical": ["tropical"],
            "mediterraneo": ["mediterraneo", "templado"],
            "templado": ["templado", "mediterraneo"],
            "desertico": ["desertico"],
            "frio": ["frio", "polar"],
            "polar": ["polar", "frio"]
        }
        return datos["clima"] in similares.get(valor, [valor])
    elif atributo == "mes":
        return len(set(valor) & set(datos["epoca"])) >= 1
    elif atributo == "costo_dia":
        rango = max(10, valor * 0.2)
        return abs(datos["costo_dia"] - valor) <= rango
    elif atributo == "duracion_ideal":
        return abs(datos["duracion_ideal"] - valor) <= 2
    return False


MESES_NOMBRES = [
    "","Enero","Febrero","Marzo","Abril","Mayo","Junio",
    "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
]

def imprimir_ruta(ruta, modo_label=""):
    costo, dias, dist = calcular_stats_ruta(ruta)

    print("\n")
    print(f"  RUTA TURÍSTICA ÓPTIMA  {modo_label}")
    print(f"  Días totales:     {dias} días")
    print(f"  Presupuesto estimado: ${costo:,} USD")
    print(f"  Distancia total:  {dist:,} km")
    print("─"*65)

    dia_acum = 1
    for paso, destino in enumerate(ruta, 1):
        d = DESTINOS[destino]
        epocas = ", ".join(MESES_NOMBRES[m] for m in d["epoca"][:3])
        costo_dest = d["costo_dia"] * d["duracion_ideal"]

        print(f"\n  PARADA {paso}/5  -  {destino}")
        print(f"  {d['descripcion']}")
        print(f"  Días {dia_acum}-{dia_acum + d['duracion_ideal'] - 1} "
              f"({d['duracion_ideal']} días)   Costo aproximado: ${costo_dest:,} USD")
        print(f"  Intereses: {', '.join(d['intereses'][:4])}")
        print(f"  Clima: {d['clima'].capitalize()}   Mejor época: {epocas}{'...' if len(d['epoca']) > 3 else ''}")
        if paso < 5:
            sig = ruta[paso]
            km = int(distancia_km(d["coordenadas"], DESTINOS[sig]["coordenadas"]))
            print(f"       {km:,} km hasta {sig}")

        dia_acum += d["duracion_ideal"]



## modo 1
def modo_1():
    print("\n")
    print("  MODO 1: Planificación por preferencias personales")
    print("─"*65)

    # Interés principala
    todos_intereses = sorted(set(
        i for d in DESTINOS.values() for i in d["intereses"]
    ))
    interes = pedir_opcion("\n¿Cuál es tu interés principal de viaje?", todos_intereses)

    # Presupuesto diario
    print("\nReferencia de presupuesto diario (USD):")
    presupuesto_dia = pedir_rango("¿Cuál es tu presupuesto máximo por dia?", 100, 500)

    # Clima preferido
    climas = ["tropical", "mediterraneo", "desertico", "templado", "frio", "polar", "Sin preferencia"]
    clima = pedir_opcion("\n¿Qué tipo de clima prefieres?", climas)

    # Época del año
    mes_nombre = pedir_mes()
    mes_num = MESES_NOMBRES.index(mes_nombre)

    # Tiempo disponible
    print("\nReferencia de tiempo:")
    dias_disponibles = int(pedir_rango("¿Cuántos días tienes disponibles en total?", 20, 60))

    # Prioridad de atributos
    prioridad = pedir_opcion(
        "\n¿Qué atributo debe tener mayor peso en la ruta?",
        ["distancia", "costo", "tiempo", "equilibrado"]
    )

    # Filtrar con presupuestos y tiempo estrictos
    validos = filtrar_destinos_modo1(interes, presupuesto_dia,
                                     clima if clima != "Sin preferencia" else None,
                                     mes_num, dias_disponibles)

    # Si con clima no hay suficientes, relajar solo el filtro de clima
    if len(validos) < 5:
        print(f"\n  Solo {len(validos)} destino(s) coinciden exactamente. Ampliando criterios de clima...")
        validos = filtrar_destinos_modo1(interes, presupuesto_dia, None, mes_num, dias_disponibles)

    if len(validos) < 5:
        print(f"\n  Solo {len(validos)} destinos disponibles con esos criterios. Buscando por interés y tiempo/presupuesto estrictos...")
        validos = [n for n, d in DESTINOS.items()
                   if interes in d["intereses"] and d["costo_dia"] <= presupuesto_dia
                   and d["duracion_ideal"] <= dias_disponibles and mes_num in d["epoca"]]

    if len(validos) < 5:
        print("\n  No hay suficientes destinos para generar una ruta de 5 paradas.")
        print(f"    Destinos encontrados: {', '.join(validos) if validos else 'ninguno'}")
        return

    print(f"\n  {len(validos)} destinos candidatos encontrados. Calculando ruta óptima...")

    ruta, _ = encontrar_ruta_optima_5(validos, prioridad, dias_disponibles)
    if not ruta:
        print("\n  No se encontró una ruta de 5 destinos que cumpla el límite de días.")
        return
    imprimir_ruta(ruta, "| MODO 1: Por Preferencias")



## modo 2
def modo_2():
    print("\n")
    print("  MODO 2: Planificación desde un destino específico")
    print("─"*65)

    nombres = sorted(DESTINOS.keys())
    print("\nDestinos disponibles:")
    for i, n in enumerate(nombres, 1):
        d = DESTINOS[n]
        print(f"  {i:>2}. {n}  (${d['costo_dia']}/día)")

    while True:
        try:
            sel = int(input("\n  Elige el número de tu destino principal: ").strip())
            if 1 <= sel <= len(nombres):
                destino_base = nombres[sel - 1]
                break
        except ValueError:
            pass
        print("  Número inválido.")

    base = DESTINOS[destino_base]
    print(f"\n  Seleccionaste: {destino_base}")
    print(f"  Intereses de este destino: {', '.join(base['intereses'])}")
    print(f"  Clima: {base['clima'].capitalize()} | Precio: ${base['costo_dia']}/día | Duración: {base['duracion_ideal']} días")
    epocas = ', '.join(MESES_NOMBRES[m] for m in base['epoca'][:3])
    print(f"  Meses óptimos: {epocas}{'...' if len(base['epoca']) > 3 else ''}")

    atributos = ["intereses", "clima", "mes", "costo_dia", "duracion_ideal"]
    attr1 = pedir_opcion(
        "\n¿Qué primer atributo quieres usar como condición de filtro?",
        atributos
    )
    attr2 = pedir_opcion(
        "\n¿Qué segundo atributo quieres usar como condición de filtro?",
        [a for a in atributos if a != attr1]
    )

    prioridad = pedir_opcion(
        "\n¿Qué atributo debe tener mayor peso en la ruta?",
        ["distancia", "costo", "tiempo", "equilibrado"]
    )

    condicion1 = obtener_condicion_desde_base(destino_base, attr1)
    condicion2 = obtener_condicion_desde_base(destino_base, attr2)
    validos = filtrar_destinos_modo2(destino_base, condicion1, condicion2)

    if len(validos) < 5:
        print(f"\n  Solo {len(validos)} destinos coinciden. Ampliando criterios con cualquiera de los dos atributos...")
        validos = [destino_base] + [
            n for n, d in DESTINOS.items()
            if n != destino_base and (
                cumple_condicion_atributo(d, condicion1) or
                cumple_condicion_atributo(d, condicion2)
            )
        ]

    if len(validos) < 5:
        print("\n  No hay suficientes destinos para generar una ruta de 5 paradas.")
        return

    print(f"\n  {len(validos)} destinos candidatos encontrados. Calculando ruta óptima...")

    mejor_ruta, _ = encontrar_ruta_optima_5(validos, prioridad, inicio_fijo=destino_base)
    if not mejor_ruta:
        print("\n  No se encontró una ruta válida de 5 destinos con estos criterios.")
        return
    imprimir_ruta(mejor_ruta, f"| MODO 2: Desde {destino_base}")


def main():
    print("\n")
    print("PLANIFICADOR DE RUTAS TURÍSTICAS")
    print(f"\n  Base de datos: {len(DESTINOS)} destinos turísticos en todo el mundo.")
    print("  La herramienta genera UNA RUTA de 5 destinos ordenados secuencialmente.")

    while True:
        print("\n")
        print("  Selecciona el modo de planificación:")
        print("  1. Por preferencias generales (interés, presupuesto, clima, época, tiempo)")
        print("  2. Desde un destino específico (selecciona destino + 2 atributos)")
        print("  3. Salir")
        print("─"*65)

        try:
            opcion = int(input("  Tu elección (1/2/3): ").strip())
        except ValueError:
            opcion = 0

        if opcion == 1:
            modo_1()
        elif opcion == 2:
            modo_2()
        elif opcion == 3:
            print("\n  ¡Buen viaje! Hasta pronto.\n")
            break
        else:
            print("  Opción inválida. Elige 1, 2 o 3.")

        continuar = input("\n  ¿Deseas planificar otra ruta? (s/n): ").strip().lower()
        if continuar != 's':
            print("\n  ¡Buen viaje! Hasta pronto.\n")
            break


if __name__ == "__main__":
    main()
