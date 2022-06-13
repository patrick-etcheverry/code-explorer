from tree_sitter import Language, Parser
#from tree_sitter_utilities import RecupereObjetsLiteral, RecupereObjetsExpressionBinaire, RecupereObjetsExpressionParenthesee, RecupereObjetsExpressionUnaire, RecupereObjetsIdentificateur, RecupereObjetsAffectation, RecupereObjetsDeclaration, RecupereObjetsBlocCompose
from ModeleObjetPatrick import Programme, Noeud
from ModeleObjetPatrick_helper import creeObjets
#import pickle
#import pathlib
import os 




Language.build_library(
  # Store the library in the `build` directory
  'build/my-languages.so',

  # Include one or more languages
  [
    'src/languages/tree-sitter-java',
    'src/languages/tree-sitter-python',
    'src/languages/tree-sitter-javascript',
    'src/languages/tree-sitter-c',
    'src/languages/tree-sitter-cpp'
  ]
)

#JS_LANGUAGE = Language('build/my-languages.so', 'javascript')
#PY_LANGUAGE = Language('build/my-languages.so', 'python')
#JAVA_LANGUAGE= Language('build/my-languages.so', 'java')
#C_LANGUAGE = Language('build/my-languages.so', 'c')
CPP_LANGUAGE= Language('build/my-languages.so', 'cpp')

parser = Parser()
parser.set_language(CPP_LANGUAGE)


f=open("src/essai.cpp", encoding='utf-8')
blob = f.read()
splitted_code = blob.split("\n")

#print(blob)  #pour afficher le fichier source qui vient d'etre lu
#print(splitted_code) #pour afficher la liste qui a été fabriquée à partir du texte 
tree=parser.parse(bytes(blob.encode('utf-8')))

root_node=tree.root_node
#print("tree = ",root_node.sexp())

'''
liste_Literal=RecupereObjetsLiteral(root_node)
liste_ExpressionBinaire=RecupereObjetsExpressionBinaire(root_node)
liste_ExpressionParenthesee=RecupereObjetsExpressionParenthesee(root_node)
liste_ExpressionUnaire=RecupereObjetsExpressionUnaire(root_node)
liste_Identificateur=RecupereObjetsIdentificateur(root_node)
liste_BlocCompose=RecupereObjetsBlocCompose(root_node)

#liste_Declaration=RecupereObjetsDeclaration(root_node) #Comme ils ont des composants, seront declares autrement 
#liste_Affectation=RecupereObjetsAffectation(root_node) #Comme ils ont des composants, seront declares autrement 

'''

print()









p=Programme(splitted_code, root_node, CPP_LANGUAGE)


#on cree les objets de base du programme
p.creeObjets()

 
print()
print(p.lesBlocs.next().getValeur())
#Traitement des expressions
#p.creeObjets_expressionsUnaires(liste_ExpressionUnaire)
#p.creeObjets_expressionsparenthesees()


#p.creeObjets_expressionsBinairesSimples()
#p.creeObjets_expressionsBinairesComposees()
#p.creeObjets_expressionsBinaires(liste_ExpressionBinaire)


#p.creeObjets_expressions()

#print("                on affiche les clés connues")
#print("                ------------------------")


#for c in Noeud.getensCles():
#  print(c)


#p.creeObjets_declarations(liste_Declaration)
#p.creeObjets_affectations(liste_Affectation)

#p.creeObjet_types()

#On peut maintenant créer les premiers objets exploitant ces objets de base



#p.creeObjets_conditions()


#Une fois que les instructions simples sont connues du modele objet de Patrick, on peut créer les objets référencant ces objets 
#p.creeObjets_blocscomposes()
#puis il faut créer des relations
#p.creeObjets_relationsBlocs()




#--------
#partie test du modèle objet produit
#--------
#pour appeler la méthode getText() de Bloc pour la premiere instance des instructions de type Update
#la transfo en liste du set est obligatoire pour pouvoir accéder aux elements individuels
#Attention l'ordre dans cette liste est aleatoire

print("                on affiche le code parsé")
print("                ------------------------")


print(splitted_code)
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





p2=Programme(splitted_code, root_node, CPP_LANGUAGE)
#on cree les objets de base du programme
p2.creeObjets()

#on compare p1 et p2
print("on compare p et p2")
print("longueur des blocs de p : "+str(len(p.lesBlocs)))
print("longueur des blocs de p2 : "+str(len(p2.lesBlocs)))
print
for x in p.lesBlocs:
  trouve=False
  for y in p2.lesBlocs:
    if x.getPosition() == y.getPosition():
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
