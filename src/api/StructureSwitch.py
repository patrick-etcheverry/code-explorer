from src.api.StructureConditionnelle import StructureConditionnelle

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

##@class StructureSwitch(StructureConditionnelle)
#@brief Classe héritant de StructureConditionnelle, elle contient toutes les Strucutures sous forme de Switch d'un code.         
class StructureSwitch(StructureConditionnelle):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Switch.
    #Exemple de récupération d'une Switch : p.lesSwitchs)[0] \n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Premier Switch du programme
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresSwitchs.append(self)

    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'un Switch.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.condition["bloc"] = leBloc
        else:
            pass
            logger.debug("!!!!!!! Pb sur ConditionIf: Noeud inexistant sur condition")
        self.condition["node"] = node
        #self.condition["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getCondition()
    #@brief Retourne tous les Conditions des Switchs sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesSwitchs[0].getCondition().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition d'un Switch du programme
    #\n\n Résultat potentiel : i < 20
    def getCondition(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.condition["node"])
        return self.condition["bloc"]
    

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
            logger.debug("!!!!!!! Pb sur ConditionIf: Noeud inexistant sur bloctrt")        
        self.bloctrt["node"] = node
        #self.bloctrt["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesSwitchs[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition d'un Switch du programme
    #\n\n Résultat potentiel : { int toto = 4; }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]


    ##
    #@fn setCase(node)
    #@brief Défini le noeud en tant que Cas de Switch.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setCase(self, node):
        self.case = {}
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.case["bloc"] = leBloc
        else:
            pass
            logger.debug("!!!!!!! Pb sur Switch: Noeud inexistant sur case")        
        self.case["node"] = node
        #self.case["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getCase()
    #@brief Retourne tous les Cas sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesSwitchs[0].getCase().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition d'un Switch du programme
    #\n\n Résultat potentiel : { int toto = 4; }
    #@warning Non fonctionnel pour l'instant
    def getCase(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.case["node"])
        return self.case["bloc"]

