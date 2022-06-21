from src.api.BlocSimple import BlocSimple

##@class Sous_Programme(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Sous_Programme d'un code.         
class SousProgramme(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Sous_Programme.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSousProgrammes.append(self)

    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getSousProgrammes()[2].getType() \n \n
    #Résultat possible : \n \n
    #'SousProgramme', 'Function'
    def getType(self):
        return self.getTypeBloc()
