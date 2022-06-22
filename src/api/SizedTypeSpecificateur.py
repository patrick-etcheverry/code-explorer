from src.api.BlocSimple import BlocSimple

##@class SizedTypeSpecificateur(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets SizedTypeSpecificateur d'un code, comme les "unsigned int" par exemple.
class SizedTypeSpecificateur(BlocSimple):


    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe SizedTypeSpecificateur.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSizedTypeSpecificateurs.append(self)



