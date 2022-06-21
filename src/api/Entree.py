from src.api.BlocSimple import BlocSimple

##@class Entree(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Entree d'un code, par exemple : i = "i + 1".      
class Entree(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Entree.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        
        progObjetPatrick.lesEntrees.append(self)



    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getEntrees()[2].getType() \n \n
    #Résultat possible : \n \n
    #'Entree'
    def getType(self):
        return self.getTypeBloc()