from src.api.Boucle import Boucle


##@class BoucleNbRepConnu(Boucle)
#@brief Classe héritant de Boucle, elle contient tous les objets BoucleNbRepConnu d'un code.
class BoucleNbRepConnu(Boucle):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe BoucleNbRepConnu.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBouclesNbRepConnu.append(self)

