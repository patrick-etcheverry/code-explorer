from src.api.BlocSimple import BlocSimple

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 



##@brief Classe héritant de BlocSimple, elle contient tous les Parametre de SousProgramme d'un code, comme "int" ou "string" par exemple.
class Parametre(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Type.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesParametres.append(self)



    ##
    #@fn setType(node)
    #@brief Défini le noeud en tant que Type.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setType(self, node):
        self.type = {}
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.type["bloc"] = leBloc
        else:
            pass
            logger.debug("!!!!!!! Bloc inexistant pour type")
        self.type["node"] = node
        #self.type["text"]=recupereTexteDansSource(self.prog.codeSource, nodeType)



    ##
    #@fn getType()
    #@brief Retourne tous les Types sous forme d'une structure de données.
    def getType(self):
        return self.type["bloc"]
    
    ##
    #@fn setTsetIdentificateurype(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):       
        self.identifiant = {}

        if node==None:
            self.identifiant["bloc"]=False
        else:
            lebloc=self.prog.cherche(node)
            if not lebloc==None:
                self.identifiant["bloc"]=lebloc
            else:
                pass
                logger.debug("!!!!!!! Pb sur If: Bloc inexistant pour identifiant dans Fonction")
        self.identifiant["node"]=node
    

    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Identificateur sous forme d'une structure de données.
    def getIdentificateur(self):
