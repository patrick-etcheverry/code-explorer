from src.api.BlocSimple import BlocSimple


##@brief Classe héritant de BlocSimple, elle contient tous les objets Sortie d'un code, par exemple : "i" = i + 1.      
class Sortie(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Sortie.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSorties.append(self)


