import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

p = Programme("tests/test3/essai.cpp")

print("---------------------------------")


#Affiche "OK" si la condition de ces deux If sont égales, "Non" sinon.
condition1 = p.lesConditionsIf[0].getCondition().getValeur()
condition2 = p.lesConditionsIf[1].getCondition().getValeur()

if condition1 == condition2:
    print("OK")
else:
    print("Non")


print("---------------------------------")


#Affiche "OK" si la condition choisie est une Expression Binaire, "Non" sinon.
if p.getConditionsIf()[0].getCondition().getTypeString() == "binary_expression":
    print("OK")
else:
    print("Non")


print("---------------------------------")


#Affiche "OK" si la condition choisie est un If avec des accolades ou un If avec une seule instruction.
#"compound_statement" pour un corps classique et "expression_statement" pour un If avec une seule instruction.
if p.getConditionsIf()[0].getBlocAlors().getTypeString() == "compound_statement":
    print("OK")
else:
    print("Non")


print("---------------------------------")