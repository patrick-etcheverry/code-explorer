from src.api.BlocSimple import BlocSimple

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

##@class Expression(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Affectations d'un code, par exemple : "toto = tab[i];".
class Expression(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Expression.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)

        progObjetPatrick.lesExpressions.append(self)

    def setExpression(self, node):
        self.expression={} 
        lebloc=self.prog.cherche(node)
        if not lebloc==None:
            self.expression["bloc"]=lebloc
        else:
            logger.debug("!!!!!!! Bloc inexistant pour setExpression dans expression")
        self.expression["node"]=node
    
    def getExpression(self):
        return self.expression["bloc"]


