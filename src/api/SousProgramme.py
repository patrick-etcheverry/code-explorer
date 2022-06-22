from src.api.BlocSimple import BlocSimple


##@brief Classe héritant de BlocSimple, elle contient tous les objets SousProgramme d'un code.         
class SousProgramme(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Sous_Programme.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSousProgrammes.append(self)

