import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

# TEST SUR LES PARAMETRES


p = Programme("tests/test7Suivi_Identificateur/essai.cpp")

print("---------------------------------")


# Affiche le nombre de paramètres d'un sous-programme
print ()
for elem in p.chercheTracesIdentificateur("estTrie", p.getStructureWhileAt(0)):
    print(elem.getValeur()+':'+elem.getLocalisation()+"  _  "+elem.getParent().getValeur())




print("---------------------------------")








