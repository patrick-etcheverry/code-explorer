from src.api.ConditionBoucle import ConditionBoucle
from src.api.tree_sitter_utilities import splited

##@class ConditionBoucle(Condition)
#@brief Classe héritant de Condition, elle contient tous les objets ConditionArret d'un code.
class ConditionArret(ConditionBoucle):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ConditionArret.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesConditionsArret.append(self)


