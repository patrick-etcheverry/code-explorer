from src.api.StructureNbRepNonConnu import StructureNbRepNonConnu
import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

##@brief Classe héritant de Boucle, elle contient tous les objets StructureWhile d'un code.
class StructureWhile(StructureNbRepNonConnu):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe StructureWhile.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresWhile.append(self)

    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'une Structure While.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setConditionContinuation(self, node):
        self.conditionContinuation = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.conditionContinuation["bloc"] = leBloc
        else:
            pass
            logger.debug("!!!!!!! Pb sur BoucleWhile: Noeud inexistant sur conditionContinuation")
        self.conditionContinuation["node"] = node
        #self.condition["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getConditionContinuation()
    #@brief Retourne tous les Conditions de Structure While sous forme d'une structure de données.
    #Exemple d'utilisation : p.getStructuresWhile[0].getConditionContinuation().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle While du programme
    #\n\n Résultat potentiel : compteur < 20
    def getConditionContinuation(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.condition["node"])
        return self.conditionContinuation["bloc"]
    




    ##
    #@fn setConditionArret(node)
    #@brief Défini le noeud en tant que Condition d'Arret.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setConditionsArret(self, listNode):

        self.conditionArret = []

        if listNode==None:
                    self.conditionArret = False

        else:
            for node in listNode:
                leBloc = self.prog.cherche(node)
                if not leBloc == None:
                    self.conditionArret.append(leBloc)
                else:
                    pass
                    logger.debug("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur conditionArret")
            #self.condition["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getConditionArret()
    #@brief Retourne toutes les Conditions d'Arrêts sous forme d'une liste.
    #Exemple d'utilisation : p.getStructuresWhile[0].getConditionArret()[0].getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Structure While du programme
    #\n\n Résultat potentiel : if () { break; }
    def getConditionsArret(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.condition["node"])
        return self.conditionArret




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
            logger.debug("!!!!!!! Pb sur StructureWhile: Noeud inexistant sur bloctrt")        
        self.bloctrt["node"] = node
        #self.bloctrt["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.*
    #Exemple d'utilisation : p.getStructuresWhile[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Structures While du programme
    #\n\n Résultat potentiel : { int toto = 3 }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]



