import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

# TEST SUR LES PARAMETRES


p = Programme("tests/test5/essai.cpp")

print("---------------------------------")


# Affiche le nombre de paramètres d'un sous-programme
print(p.getSousProgrammes()[2].getBlocTrt().getBlocs().getNext())
print(len(p.getSousProgrammeAt(1).getParametres()))
b_compose=p.getSousProgrammeAt(2).getBlocTrt() #on s'interesse au bloc de trt du 3ème sous programme
for lebloc in b_compose.getBlocs():
    print(lebloc.getValeur())


print("---------------------------------")

b_compose.traiteBlocs(print)

# Affiche le Type et le Nom de chacun des paramètres d'un sous-programme
for leParametre in p.getSousProgrammeAt(1).getParametres():
    leType = leParametre.getType().getValeur()
    leNom = leParametre.getIdentificateur().getValeur()

    laChaine = "Type : " + leType + " et Nom : " + leNom
    print(laChaine)


print("---------------------------------")








