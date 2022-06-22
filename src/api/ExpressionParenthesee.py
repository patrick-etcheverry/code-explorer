from src.api.Expression import Expression

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 



##@brief Classe héritant de Expression, elle contient tous les objets ExpressionParenthesee d'un code, par exemple : for (int i = 1; i <= "(nbCases - 2)""; i++).
class ExpressionParenthesee(Expression):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ExpressionParenthesee.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesExpressionsParenthesees.append(self)

    ##
    #@fn setExpression(node)
    #@brief Défini le noeud en tant qu'Expression.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setExpression(self, node):
        self.expression = {} 
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.expression["bloc"]=leBloc
        else:
            logger.debug("!!!!!!! Bloc inexistant pour Expression dans expr parenth")
        self.expression["node"] = node
    
    ##
    #@fn getExpression()
    #@brief Retourne toutes les Expressions sous forme d'une structure de données.
    def getExpression(self):
        return self.expression


