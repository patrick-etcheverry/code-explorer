import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

p = Programme("fichiers/etudiant001.cpp")


print()

print("                on affiche le code parsé")
print("                ------------------------")


print(p.codeSource)
print()
os.system("pause")
print()
print()




#Pour recuperer le texte associé à un objet pour lequel on a une classe dans le modèle OBjet de Patrick
#print("Exemple1 :" + str(list(p.lesBouclesFor)[0]))

#Pour recuperer le texte d'un element qui a été défini par une méthode setXXX
#print("Exemple2 : " + str(list(p.lesBouclesFor)[0].getInit()))

#Pour recupérer tous les objets instanciés et accéder à leur type
print()
print()
print("                on affiche le type de tous les blocs de code récupérés")
print("                ------------------------------------------------------")


for i,o in enumerate(list(p.lesBlocs)):
  print("A l'indice "+ str(i)+ " ==> "+ str(o) + ":" + str(type(o)))
print()
print()
print()
#On va regarder ce qu'il se passe pour une boucle
os.system("pause")
print()
print()


print("                on s'interesse aux boucles For du programme")
print("                ----------------------------------------")
print()

for o in p.lesBouclesFor:
  print("==> "+ str(o) + ":" + str(type(o)))
  init=o.getInit()
  cond=o.getCondition()
  pas=o.getPas()
  trt=o.getBlocTrt()
  print ("         init="+str(init)+ " et cond="+str(cond)+ " et pas="+str(pas)+" et trt="+str(trt))
  #on va regarder ce qu'il se passe pour init
  #print ("                  - init :"+ str(init["bloc"]))
  print("             => init :"+ str(init))
  print("                      ident = "+ str(init.getIdentificateur()))
  print("                      expr = "+ str(init.getExpression()))
  
  print("             => condition :")
  print("                      cond a detailler= "+str(cond))
  print("                      expr Gauche= "+str(cond.getGauche()))
  print("                      expr operateur= "+str(cond.getOperateur()))
  print("                      expr Droite= "+str(cond.getDroite()))
  
  
  print("             => update :"+ str(pas))
'''

  print("                      gauche= "+str(pas.getIdentificateur()))
  if type(pas)=="expression_update":
    print("operateur= "+str(pas.getOperateur()))
  else:
    print("                      droite= "+str(pas.getExpression()))
    print("                           detail droite= ")
    print("                               expr gauche = "+ str(pas.getExpression().getGauche()))
    print("                               operateur = "+ str(pas.getExpression().getOperateur()))
    print("                               expr droite = "+ str(pas.getExpression().getDroite()))
'''
os.system("pause")
print()
print()



  
  
print("                on s'intéresse aux blocs composés")
print("                ----------------------------------")
for i, b in enumerate(list(p.lesBlocsComposes)):
  print(str(b))
  print("bloc à l'index : " + str(i) + " ===> nombre de blocs composant le bloc : "+ str(len (b.lesBlocs)))
  print ("détail des blocs = ... ")
  for j, bb in enumerate(b.lesBlocs):
    print("      => bloc "+ str(j) + " : "+str(bb) )
  print()
print()
print("FIN pour p")





p2 = Programme("fichiers/essai.cpp")


#on compare p1 et p2
print("on compare p et p2")
print("longueur des blocs de p : "+str(len(p.lesBlocs)))
print("longueur des blocs de p2 : "+str(len(p2.lesBlocs)))
print
for x in p.lesBlocs:
  trouve=False
  for y in p2.lesBlocs:
    if x.getLocalisation() == y.getLocalisation():
      print("OK pour :"+x.getValeur())
      trouve=True
      break
  if not trouve:
    print("Non trouvé : "+x.getValeur())













  #print (len(p.lesBlocs)) 


# serialisation
'''
desti='.'
monfichier="dumpModeleObjetPatrick"
chemin_final=pathlib.Path(desti, monfichier)
with open(chemin_final, 'wb') as fp:
  pickle.dump(p, fp)
  fp.close()        
'''
