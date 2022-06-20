from src.api.StructureIterative import StructureIterative


##@class StructureNbRepConnu(Boucle)
#@brief Classe héritant de Boucle, elle contient tous les objets StructureNbRepConnu d'un code.
class StructureNbRepConnu(StructureIterative):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe StructureNbRepConnu.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresNbRepConnu.append(self)

