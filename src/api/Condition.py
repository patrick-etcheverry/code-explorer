from src.api.BlocSimple import BlocSimple
from src.api.tree_sitter_utilities import splited

##@class Condition(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Conditions d'un code.
class Condition(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Condition.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesConditions.append(self)


    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getConditions()[2].getType() \n \n
    #Résultat possible : \n \n
    #'Condition', 'ConditionContinuation', 'ConditionArret', 'ConditionBoucle', 'ConditionIf', 'ConditionSwitch' 
    def getType(self):
        return self.getTypeBloc()