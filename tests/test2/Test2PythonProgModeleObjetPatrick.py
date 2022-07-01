import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme


p = Programme("tests/test2/essai.cpp")

#Affichage du nombre de Boucles For contenu dans "essai.cpp"
print(len(p.getStructuresFor()))


print("---------------------------------")


#Affiche "OK" si la première Boucle du code est un For, "Non" sinon.
if p.getStructuresIterative()[0].getType() == "BoucleFor":
  print("OK")
else:
  print("Non")


print("---------------------------------")


#Affiche "OK" si la condition de la Boucle While du code est identique à celle mise en paramètre et "Non" sinon.
if p.getStructuresWhile()[0].verifCondition("i < 3") == True:
  print("OK")
else:
  print("Non")


print("---------------------------------")


