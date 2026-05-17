import numpy as np
import matplotlib.pyplot as plt

# ── Données : coordonnées des quartiers de Nouakchott ──────
points = {
    'Depot':      (0, 0),
    'Arafat':     (3, 4),
    'Sebkha':     (-2, 3),
    'El Mina':    (-4, 1),
    'Dar Naim':   (2, -3),
    'Teyarett':   (4, -1),
    'Toujounine': (-1, -4)
}

demandes = {
    'Arafat': 300,
    'Sebkha': 200,
    'El Mina': 250,
    'Dar Naim': 150,
    'Teyarett': 180,
    'Toujounine': 220
}

CAPACITE = 1000  # litres par camion

# ── Calcul de distance ─────────────────────────────────────
def distance(a, b):
    x1, y1 = points[a]
    x2, y2 = points[b]
    return round(np.sqrt((x2-x1)**2 + (y2-y1)**2), 2)

# ── Heuristique greedy ─────────────────────────────────────
def vrp_greedy():
    non_visites = list(demandes.keys())
    tournees = []

    while non_visites:
        tournee = ['Depot']
        charge = 0
        current = 'Depot'

        while non_visites:
            # Clients accessibles sans dépasser la capacité
            accessibles = [
                c for c in non_visites
                if charge + demandes[c] <= CAPACITE
            ]
            if not accessibles:
                break
            # Choisir le plus proche
            voisin = min(accessibles,
                         key=lambda c: distance(current, c))
            tournee.append(voisin)
            charge += demandes[voisin]
            non_visites.remove(voisin)
            current = voisin

        tournee.append('Depot')
        tournees.append((tournee, charge))

    return tournees

tournees = vrp_greedy()

# ── Affichage des tournées ─────────────────────────────────
print(f"Capacité camion : {CAPACITE} L\n")
dist_totale = 0
for i, (tournee, charge) in enumerate(tournees):
    dist = sum(distance(tournee[j], tournee[j+1])
               for j in range(len(tournee)-1))
    dist_totale += dist
    print(f"Tournée {i+1} : {' → '.join(tournee)}")
    print(f"  Charge : {charge} L | Distance : {dist} km\n")
print(f"Distance totale : {round(dist_totale, 2)} km")

# ── Visualisation ──────────────────────────────────────────
couleurs = ['blue', 'red', 'green', 'orange']
plt.figure(figsize=(8, 8))

# Tracer les points
for nom, (x, y) in points.items():
    if nom == 'Depot':
        plt.plot(x, y, 'ks', markersize=14)
        plt.annotate(f"  {nom}", (x, y), fontsize=11, fontweight='bold')
    else:
        plt.plot(x, y, 'ko', markersize=10)
        plt.annotate(f"  {nom}\n  ({demandes[nom]}L)",
                     (x, y), fontsize=9)

# Tracer les tournées
for i, (tournee, _) in enumerate(tournees):
    couleur = couleurs[i % len(couleurs)]
    for j in range(len(tournee)-1):
        x1, y1 = points[tournee[j]]
        x2, y2 = points[tournee[j+1]]
        plt.annotate("", xy=(x2, y2), xytext=(x1, y1),
                     arrowprops=dict(arrowstyle="->",
                                     color=couleur, lw=2))

plt.title("VRP — Distribution d'eau à Nouakchott", fontsize=13)
plt.grid(True)
plt.savefig("vrp_graph.png", dpi=150)
plt.show()