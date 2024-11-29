import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

p = Programme("tests/test3/essai.cpp")

print("---------------------------------")


#Affiche "OK" si la condition de ces deux If sont égales, "Non" sinon.
condition1 = p.lesStructuresIf[0].getCondition().getValeur()
condition2 = p.lesStructuresIf[1].getCondition().getValeur()

if condition1 == condition2:
    print("OK")
else:
    print("Non")


print("---------------------------------")


#Affiche "OK" si la condition choisie est une Expression Binaire, "Non" sinon.
if p.getStructuresIf()[0].getCondition().getType() == "ExpressionBinaire":
    print("OK")
else:
    print("Non")


print("---------------------------------")


#Affiche "OK" si la condition choisie est un If avec des accolades ou un If avec une seule instruction.
#"compound_statement" pour un corps classique et "expression_statement" pour un If avec une seule instruction.
if p.getStructureIfAt(0).getBlocAlors().getType() == "BlocCompose":
    print("OK")
else:
    print("Non")


