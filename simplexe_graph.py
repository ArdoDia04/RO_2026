import numpy as np
import matplotlib.pyplot as plt

# ── Axes ──────────────────────────────────────────────────
x = np.linspace(0, 10, 400)

# ── Contraintes ───────────────────────────────────────────
# C1 : x1 + 2x2 <= 8  →  x2 = (8 - x1) / 2
c1 = (8 - x) / 2

# C2 : 3x1 + x2 <= 9  →  x2 = 9 - 3x1
c2 = 9 - 3*x

# ── Tracer les droites ────────────────────────────────────
plt.figure(figsize=(8, 6))
plt.plot(x, c1, label="C1 : x1 + 2x2 = 8", color="blue")
plt.plot(x, c2, label="C2 : 3x1 + x2 = 9", color="red")

# ── Zone faisable ─────────────────────────────────────────
y_faisable = np.minimum(c1, c2)
y_faisable = np.maximum(y_faisable, 0)
plt.fill_between(x, 0, y_faisable,
                 where=(y_faisable >= 0) & (x >= 0),
                 alpha=0.2, color="green",
                 label="Zone faisable")

# ── Solution optimale ─────────────────────────────────────
plt.plot(2, 3, 'ko', markersize=10, label="Optimal (x1=2, x2=3, z=18)")
plt.annotate("  (2, 3)\n  z = 18",
             xy=(2, 3), fontsize=11, color="black")

# ── Mise en forme ─────────────────────────────────────────
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Simplexe — Zone faisable et solution optimale")
plt.legend()
plt.grid(True)
plt.savefig("simplexe_graph.png", dpi=150)
plt.show()