from src.api.BlocSimple import BlocSimple


##@brief Classe héritant de BlocSimple, elle contient tous les objets TypeQualificateur d'un code, comme les constantes par exemple.
class TypeQualificateur(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe TypeQualificateur.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesTypesQualificateurs.append(self)
        #progObjetPatrick.lesTypesQualificateurs.append(self)



