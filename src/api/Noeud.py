##
#@class Noeud
#@brief Base de toutes choses dans le programme, elle encapsule un "node" de Tree-Sitter.
class Noeud:

    ##Structure de données de la classe "Noeud" constituée d'un ensemble de clés.
    #lesCles = set()
    
    #ici on va utiliser la structure lesCles attaché au prgramme p
    
    ##Structure de données qui permet de récupérer le "Noeud" associé à une clé.
    
    #ici on va utiliser la structure mondictCles attaché au programme p
    #mondictCles = {}

    ##
    #@fn get_laCle(leNode)
    #@brief Renvoie une clé qui contient les coordonnées du Noeud passé en paramètre sous la forme : XX-YY_WW-ZZ.\n
    #Avec : 
    #- XX correspondant au début de la ligne du Noeud
    #- YY à la fin de la ligne
    #- WW au début de la colonne
    #- ZZ à la fin de la colonne
    #@param leNode : Correspond au Noeud dont on veut obtenir la clé.
    def get_laCle(leNode):
        x1 = leNode.start_point[0]
        y1 = leNode.start_point[1]
        x2 =  leNode.end_point[0]
        y2 = leNode.end_point[1]
        laCle = str(x1) + "-" + str(y1) + "_"+str(x2) + "-" + str(y2)
        return laCle


    
    ##
    #@fn __init__(nodeTreesitter, leBloc)
    #@brief Constructeur de la classe Noeud.
    #@param nodeTreesitter : Correspond à un Node de Tree-Sitter à qui on va associer une clé
    #@param leBloc : Bloc qui va être associé à cet objet Noeud.
    def __init__(self, nodeTreesitter, leBloc, dansprog):
        self.node = nodeTreesitter
        self.bloc = leBloc
        #on cree l'element du dictionnaire qui va permettre d'associer un Node au sens tree-sitter à une clé
        maCle = Noeud.get_laCle(nodeTreesitter)
        dansprog.lesCles.add(maCle)
        dansprog.mondictCles[maCle] = self 


  