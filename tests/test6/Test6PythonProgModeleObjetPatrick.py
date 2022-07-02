import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

# TEST SUR LES PARAMETRES


p = Programme("tests/test6/essai.cpp")

print("---------------------------------")


# Affiche le nombre de paramètres d'un sous-programme
print ()
for elem in p.chercheBlocsControleNonComposes():
    print(elem.getLocalisation())



print("---------------------------------")








