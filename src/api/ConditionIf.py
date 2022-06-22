from src.api.Condition import Condition
from src.api.tree_sitter_utilities import splited

##@class ConditionIf(Condition)
#@brief Classe héritant de Condition, elle contient tous les objets ConditionIf d'un code.
class ConditionIf(Condition):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ConditionIf.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesConditionsIf.append(self)


