from src.api.Expression import Expression
from src.api.BlocSimple import BlocSimple

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

##@class ExpressionBinaire(Expression)
#@brief Classe héritant de Expression, elle contient tous les objets ExpressionBinaire d'un code, par exemple : while("compteur < 20").
class ExpressionBinaire(Expression):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ExpressionBinaire.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        
        self.prog=progObjetPatrick

        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesExpressionsBinaires.append(self)

    ##
    #@fn setGauche(node)
    #@brief Défini le noeud en tant qu'élement de Gauche.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setGauche(self, node):
        self.gauche = {} 
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.gauche["bloc"] = leBloc
        else:
            logger.debug("!!!!!!! Bloc inexistant pour Gauche")
        self.gauche["node"] = node

    ##
    #@fn getGauche()
    #@brief Retourne tous les éléments de Gauche sous forme d'une structure de données.
    def getGauche(self):
        return self.gauche["bloc"]

    ##
    #@fn setOperateur(node)
    #@brief Défini le noeud en tant qu'Operateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setOperateur(self, node):
        self.operateur = {}
        leBloc = BlocSimple(node, self.prog) 
        if not leBloc == None:
            self.operateur["bloc"] = leBloc
        else:
            logger.debug("!!!!!!! Bloc inexistant pour Operateur" + str(node))
        self.operateur["node"] = node

    ##
    #@fn getOperateur()
    #@brief Retourne tous les Operateurs sous forme d'une structure de données.
    def getOperateur(self):
        return self.operateur["bloc"]

    ##
    #@fn setDroite(node)
    #@brief Défini le noeud en tant qu'élement de Droite.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setDroite(self, node):
        self.droite = {} 
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.droite["bloc"] = leBloc
        else:
            logger.debug("!!!!!!! Bloc inexistant pour Droite")
        self.droite["node"] = node

    ##
    #@fn getDroite()
    #@brief Retourne tous les éléments de Droite sous forme d'une structure de données.
    def getDroite(self):
        return self.droite["bloc"]
