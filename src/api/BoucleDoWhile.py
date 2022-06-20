from src.api.StructureNbRepNonConnu import StructureNbRepNonConnu
import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

##@class BoucleDoWhile(Boucle)
#@brief Classe héritant de Boucle, elle contient tous les objets BoucleDoWhile d'un code.
class BoucleDoWhile(StructureNbRepNonConnu):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe BoucleDoWhile.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBouclesDoWhile.append(self)


    ##
    #@fn setBlocTrt(node)
    #@brief Défini le noeud en tant que Bloc de Traitements.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocTrt(self, node):
        self.bloctrt = {}
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.bloctrt["bloc"] = leBloc
        else:
            pass
            logger.debug("!!!!!!! Pb sur BoucleWhile: Noeud inexistant sur bloctrt")        
        self.bloctrt["node"] = node
        #self.bloctrt["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesBouclesDoWhile[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle DoWhile du programme
    #\n\n Résultat potentiel : { int toto = 3 }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]


    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'une Boucle DoWhile.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.condition["bloc"] = leBloc
        else:
            pass
            logger.debug("!!!!!!! Pb sur BoucleWhile: Noeud inexistant sur condition")
        self.condition["node"] = node
        #self.condition["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getCondition()
    #@brief Retourne tous les Conditions de Boucle DoWhile sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesBouclesDoWhile[0].getCondition().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle DoWhile du programme
    #\n\n Résultat potentiel : compteur < 20
    def getCondition(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.condition["node"])
        return self.condition["bloc"]
    
  