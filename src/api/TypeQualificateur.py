from src.api.BlocSimple import BlocSimple

##@class TypeQualificateur(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets TypeQualificateur d'un code, comme les constantes par exemple.
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



    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getTypesQualificateurs()[2].getType() \n \n
    #Résultat possible : \n \n
    #'TypeQualificateur'
    def getType(self):
        return self.getTypeBloc()