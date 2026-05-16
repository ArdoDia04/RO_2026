import numpy as np
import matplotlib.pyplot as plt
import itertools

# ── Villes et coordonnées ──────────────────────────────────
villes = ['A', 'B', 'C', 'D', 'E']
coords = {
    'A': (0, 0),
    'B': (2, 4),
    'C': (5, 2),
    'D': (6, 5),
    'E': (3, 1)
}

# ── Calcul des distances ───────────────────────────────────
def distance(v1, v2):
    x1, y1 = coords[v1]
    x2, y2 = coords[v2]
    return round(np.sqrt((x2-x1)**2 + (y2-y1)**2), 2)

# ── Heuristique : Plus proche voisin ──────────────────────
def greedy_tsp(depart):
    non_visites = list(villes)
    non_visites.remove(depart)
    chemin = [depart]
    current = depart
    total = 0

    while non_visites:
        voisin = min(non_visites, key=lambda v: distance(current, v))
        total += distance(current, voisin)
        chemin.append(voisin)
        non_visites.remove(voisin)
        current = voisin

    # Retour au départ
    total += distance(current, depart)
    chemin.append(depart)
    return chemin, round(total, 2)

chemin, dist_greedy = greedy_tsp('A')
print(f"Chemin greedy : {' → '.join(chemin)}")
print(f"Distance greedy : {dist_greedy}")

# ── Solution exacte (brute-force) ─────────────────────────
def brute_force_tsp():
    autres = [v for v in villes if v != 'A']
    meilleur = None
    meilleure_dist = float('inf')

    for perm in itertools.permutations(autres):
        chemin = ['A'] + list(perm) + ['A']
        dist = sum(distance(chemin[i], chemin[i+1])
                   for i in range(len(chemin)-1))
        if dist < meilleure_dist:
            meilleure_dist = dist
            meilleur = chemin

    return meilleur, round(meilleure_dist, 2)

chemin_exact, dist_exact = brute_force_tsp()
print(f"\nChemin exact  : {' → '.join(chemin_exact)}")
print(f"Distance exacte : {dist_exact}")

# ── Visualisation ─────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

def tracer_chemin(ax, chemin, titre, couleur):
    for v, (x, y) in coords.items():
        ax.plot(x, y, 'ko', markersize=10)
        ax.annotate(f"  {v}", (x, y), fontsize=12)
    for i in range(len(chemin)-1):
        x1, y1 = coords[chemin[i]]
        x2, y2 = coords[chemin[i+1]]
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color=couleur, lw=2))
    ax.set_title(titre, fontsize=13)
    ax.grid(True)

tracer_chemin(axes[0], chemin, f"Greedy : {dist_greedy}", "blue")
tracer_chemin(axes[1], chemin_exact, f"Exact : {dist_exact}", "green")

plt.tight_layout()
plt.savefig("tsp_graph.png", dpi=150)
plt.show()