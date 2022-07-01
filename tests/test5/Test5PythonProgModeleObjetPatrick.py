import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

# TEST SUR LES PARAMETRES

p = Programme("tests/test5/essai.cpp")

print("---------------------------------")


# Affiche le nombre de paramètres d'un sous-programme
print(len(p.getSousProgrammeAt(1).getParametres()))


print("---------------------------------")


# Affiche le Type et le Nom de chacun des paramètres d'un sous-programme
for leParametre in p.getSousProgrammeAt(1).getParametres():
    leType = leParametre.getType().getValeur()
    leNom = leParametre.getIdentificateur().getValeur()

    laChaine = "Type : " + leType + " et Nom : " + leNom
    print(laChaine)


print("---------------------------------")








