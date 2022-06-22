from src.api.BlocSimple import BlocSimple


##@brief Classe héritant de BlocSimple, elle contient tous les objets Type d'un code, comme "int" ou "string" par exemple.
class Type(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Type.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesTypes.append(self)


