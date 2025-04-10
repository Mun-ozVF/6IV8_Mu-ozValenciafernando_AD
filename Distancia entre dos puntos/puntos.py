import itertools
import math

# Definición de puntos
puntos = {
    'A': (2, 3),
    'B': (5, 4),
    'C': (1, 1),
    'D': (6, 7),
    'E': (3, 5),
    'F': (8, 2),
    'G': (4, 6),
    'H': (2, 1)
}

# Funciones de distancia
def euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def chebyshev(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

# Calcular distancias
distancias = []
for (nombre1, p1), (nombre2, p2) in itertools.combinations(puntos.items(), 2):
    distancias.append({
        'par': (nombre1, nombre2),
        'euclidiana': euclidiana(p1, p2),
        'manhattan': manhattan(p1, p2),
        'chebyshev': chebyshev(p1, p2)
    })

# Mostrar tabla con todas las distancias
print("Tabla de Distancias entre Puntos:\n")
print(f"{'Par':<10}{'Euclidiana':<15}{'Manhattan':<15}{'Chebyshev':<15}")
print("-" * 55)
for d in distancias:
    par = f"{d['par'][0]}-{d['par'][1]}"
    print(f"{par:<10}{d['euclidiana']:<15.2f}{d['manhattan']:<15}{d['chebyshev']:<15}")

# Función para encontrar extremos
def encontrar_extremos(distancias, tipo):
    min_dist = min(distancias, key=lambda d: d[tipo])
    max_dist = max(distancias, key=lambda d: d[tipo])
    return min_dist, max_dist

# Mostrar pares más cercanos y más lejanos por tipo de distancia
tipos = ['euclidiana', 'manhattan', 'chebyshev']
for tipo in tipos:
    min_d, max_d = encontrar_extremos(distancias, tipo)
    print(f"\n--- Distancia {tipo.capitalize()} ---")
    print(f"Par más cercano: {min_d['par']} con distancia {min_d[tipo]:.2f}")
    print(f"Par más lejano: {max_d['par']} con distancia {max_d[tipo]:.2f}")
