from src.api.StructureConditionnelle import StructureConditionnelle
import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 


##@class StructureIf(StructureConditionnelle)
#@brief Classe héritant de StructureConditionnelle, elle contient toutes les Strucutures sous forme de If d'un code.         
class StructureIf(StructureConditionnelle):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ConditionIf.
    #Exemple de récupération d'une Structure If : p.getStructuresIf[0] \n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Structure If du programme
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresIf.append(self)

    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'une Structure If.
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
    
    ##
    #@fn getCondition()
    #@brief Retourne tous les Structures de If sous forme d'une structure de données.
    #Exemple d'utilisation : p.getStructuresIf[0].getCondition().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Structure If du programme
    #\n\n Résultat potentiel : i < 20
    def getCondition(self):
        return self.condition["bloc"]
    

    ##
    #@fn setBlocTrt(node)
    #@brief Défini le noeud en tant que Bloc de Traitements.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocAlors(self, node):
        self.blocalors={} 
        
        lebloc=self.prog.cherche(node)
        if not lebloc==None:
            self.blocalors["bloc"]=lebloc
        else:
            pass
            logger.debug("!!!!!!! Pb sur If: Bloc inexistant pour blocalors dans if")
        self.blocalors["node"]=node
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.
    #Exemple d'utilisation : p.getStructuresIf[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Structure If du programme
    #\n\n Résultat potentiel : { int toto = 4; }
    def getBlocAlors(self):
        return self.blocalors["bloc"]


    ##
    #@fn setBlocSinon(node)
    #@brief Défini le noeud en tant que Bloc de Traitements Else.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocSinon(self, node):
        self.blocsinon={} 
        if node==None:
            self.blocsinon["bloc"]=False
        else:
            lebloc=self.prog.cherche(node)
            if not lebloc==None:
                self.blocsinon["bloc"]=lebloc
            else:
                pass
                logger.debug("!!!!!!! Pb sur If: Bloc inexistant pour bloc sinon dans if")
        self.blocsinon["node"]=node



    ##
    #@fn getBlocSinon()
    #@brief Retourne tous les Blocs de Traitements Else sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesConditionsIf[0].getBlocSinon().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition If du programme
    #\n\n Résultat potentiel : { int toto = 4; }
    def getBlocSinon(self):
        return self.blocsinon["bloc"]



