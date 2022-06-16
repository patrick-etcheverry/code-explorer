from src.api.BlocSimple import BlocSimple

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

##@class Identificateur(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Identificateur d'un code, c'est-à-dire les noms des variables par exemple.

class Identificateur(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Identificateur.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesIdentificateurs.append(self)

    ##
    #@fn setIdentificateur(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):
        self.identificateur = {}
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.identificateur["bloc"] = leBloc
        else:
            pass
            logger.debug("!!!!!!! Bloc inexistant pour identificateur")

        self.identificateur["node"] = node
    
    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Identificateurs sous forme d'une structure de données.
    def getIdentificateur(self):
        return self.identificateur["bloc"]
