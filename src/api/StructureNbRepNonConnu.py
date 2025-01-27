from src.api.StructureIterative import StructureIterative



##@brief Classe héritant de StructureIterative, elle contient tous les objets StructureNbRepNonConnu d'un code.
class StructureNbRepNonConnu(StructureIterative):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe StructureNbRepNonConnu.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresNbRepNonConnu.append(self)

