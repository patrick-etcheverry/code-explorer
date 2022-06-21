from src.api.BlocSimple import BlocSimple

##@class Type(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Type d'un code, comme "int" ou "string" par exemple.
class Type(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Type.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesTypes.append(self)


    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getTypes()[2].getType() \n \n
    #Résultat possible : \n \n
    #'Type'
    def getType(self):
        return self.getTypeBloc()