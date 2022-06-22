from src.api.Expression import Expression
from src.api.BlocSimple import BlocSimple

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

##@class ExpressionUnaire(Expression)
#@brief Classe héritant de Expression, elle contient tous les objets ExpressionUnaire d'un code, par exemple : while("!estTrie").
class ExpressionUnaire(Expression):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ExpressionUnaire.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesExpressionsUnaires.append(self)


    ##
    #@fn setArgument(node)
    #@brief Défini le noeud en tant qu'Argument.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setArgument(self, node):
        self.argument = {} 
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.argument["bloc"]=leBloc
        else:
            logger.debug("!!!!!!! Bloc inexistant pour Argument")
        self.argument["node"] = node
    
    ##
    #@fn getArgument()
    #@brief Retourne tous les Arguments sous forme d'une structure de données.
    def getArgument(self):
        return self.argument["bloc"]

    ##
    #@fn setOperateur(node)
    #@brief Défini le noeud en tant qu'Operateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setOperateur(self, node):
        self.operateur = {} 
        leBloc = BlocSimple(node, self.prog)
        if not leBloc == None:
            self.operateur["bloc"]=leBloc
        else:
            logger.debug("!!!!!!! Bloc inexistant pour operateur" + str(node))
        self.operateur["node"] = node
    
    ##
    #@fn getOperateur()
    #@brief Retourne tous les Operateurs sous forme d'une structure de données.
    def getOperateur(self):
        return self.operateur["bloc"]

