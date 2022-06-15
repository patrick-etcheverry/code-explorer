from src.api.BlocSimple import BlocSimple

##@class Entree(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Entree d'un code, par exemple : i = "i + 1".      
class Entree(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Entree.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        
        progObjetPatrick.lesEntrees.append(self)
