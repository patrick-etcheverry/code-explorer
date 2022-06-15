from src.api.Boucle import Boucle


##@class BoucleNbRepNonConnu(Boucle)
#@brief Classe héritant de Boucle, elle contient tous les objets BoucleNbRepNonConnu d'un code.
class BoucleNbRepNonConnu(Boucle):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe BoucleNbRepNonConnu.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBouclesNbRepNonConnu.append(self)

