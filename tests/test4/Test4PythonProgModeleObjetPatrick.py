import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

# TEST SUR LES FONCTIONS ET LES PROCEDURES

p = Programme("tests/test4/essai.cpp")

print("---------------------------------")


# Affichage de la définition du premier sous-programme ainsi que sa déclaration
print(p.getSousProgrammeAt(1).getValeur()) # Indice 1, car le 0 étant le main
print(p.getSousProgrammeAt(1).getDeclaration().getValeur())


print("---------------------------------")


# Renvoie True si le premier sous-programme a été appelé et False sinon.
if p.getSousProgrammeAt(2).getAppel() != []:
    print(True)
else:
    print(False)


print("---------------------------------")


# Affiche la liste de tous les paramètres d'un sous-programme
for leParametre in p.getSousProgrammeAt(1).getParametres():
    print(leParametre)


print("---------------------------------")












