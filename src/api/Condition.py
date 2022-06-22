from src.api.BlocSimple import BlocSimple
from src.api.tree_sitter_utilities import splited


##@brief Classe héritant de BlocSimple, elle contient tous les objets Condition d'un code.
class Condition(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Condition.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesConditions.append(self)


