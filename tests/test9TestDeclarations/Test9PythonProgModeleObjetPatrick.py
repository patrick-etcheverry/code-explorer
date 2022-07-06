import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

# TEST SUR LES PARAMETRES


p = Programme("tests/test9TestDeclarations/essai.cpp")

print("---------------------------------")
for x in p.getSousProgrammeAt(1).getDeclarations():
    print(x.getValeur())
    print (x.getValeur()+" / "+x.getType().getValeur()+ " :: "+x.getIdentificateur().getValeur()+ " : " + str(x.getExpression()))

print("---------------------------------")

a=p.getSousProgrammeAt(1)
print(a.getDeclaration().getValeur()) #ici on recupere la declaration du sous programme
print (a.getDeclaration().getTypeLong())
print (a.getDeclaration().getType())  #type de la valeur retournée dans la declaration du sous-programme
print (a.getDeclaration().getIdentificateur())  #Identificateur de la declaration du sous-programme


print("Pb : on ne recupère pas pour l'instant les paramètres de la declaration")
#print(a.getDeclaration().getDeclaration())


print (a.getParametres())  #Liste des parametres (de la definition) du sous-programme
print ("Le type du premier parametre est " + str(a.getParametres()[0].getType()))  #Type du premier parametre (de la definition) du sous-programme
#print (a.getBlocTrt())  #Bloc de traitement du sous-programme
print (a.getBlocTrt().getBlocAt(2))  #3ème bloc du Bloc de traitement du sous-programme
print("---------------------------------")



