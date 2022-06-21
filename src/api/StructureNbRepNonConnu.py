from src.api.StructureIterative import StructureIterative


##@class StructureNbRepNonConnu(StructureIterative)
#@brief Classe héritant de StructureIterative, elle contient tous les objets StructureNbRepNonConnu d'un code.
class StructureNbRepNonConnu(StructureIterative):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe StructureNbRepNonConnu.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresNbRepNonConnu.append(self)

    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getStructuresNbRepNonConnu()[2].getType() \n \n
    #Résultat possible : \n \n
    #'StructureNbRepNonConnu', 'StructureFor', 'StructureWhile', 'StructureDoWhile'
    def getType(self):
        return self.getTypeBloc()