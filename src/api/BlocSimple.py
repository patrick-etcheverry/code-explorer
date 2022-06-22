from src.api.Bloc import Bloc



##@brief Classe héritant de Bloc, elle ne contient que les objets les plus basique d'un code.
class BlocSimple(Bloc):

    ##
    #@fn __init__(lenodeTreeSitter, progObjetPatrick)
    #@brief Constructeur de la classe BlocSimple.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBlocsSimples.append(self) # Surcharge de progObjetPatrick en le définissant en BlocSimple
        #self.prog.lesBlocsSimples.sort(key=getCle)

