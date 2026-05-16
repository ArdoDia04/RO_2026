from pulp import *

# On crée le problème : on veut MAXIMISER
prob = LpProblem("Simplexe", LpMaximize)

# Les deux variables : x1 et x2, toutes les deux >= 0
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

# Fonction objectif : maximiser 3x1 + 4x2
prob += 3*x1 + 4*x2

# Contraintes
prob += x1 + 2*x2 <= 8   # Contrainte 1
prob += 3*x1 + x2  <= 9  # Contrainte 2

# Résoudre
prob.solve(PULP_CBC_CMD(msg=0))

# Afficher les résultats
print(f"x1 = {value(x1)}")
print(f"x2 = {value(x2)}")
print(f"z  = {value(prob.objective)}")