import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

p = Programme("tests/test2/essai.cpp")

print(p.getBoucles().next().getType())
print("---------------------------------")


#Affichage du nombre de Boucles For contenu dans "mainProf.cpp"
print(len(p.getBouclesFor()))


print("---------------------------------")


#Affiche "OK" si la première Boucle du code est un For, "Non" sinon.
if p.getBoucles()[0].getTypeString() == "for_statement":
  print("OK")
else:
  print("Non")


print("---------------------------------")


#Affiche "OK" si la condition de la Boucle While du code est identique à celle que j'ai mise en paramètre et "Non" sinon.
if p.getBouclesWhile()[0].verifCondition("i < 3") == True:
  print("OK")
else:
  print("Non")


print("---------------------------------")


