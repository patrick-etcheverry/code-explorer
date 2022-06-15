from src.api.BlocSimple import BlocSimple

##@class Literal(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets litéral d'un code.
class Literal(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Literal.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesLiteral.append(self)
        #self.prog.lesLiteral.sort(key=getCle)
    