from src.api.BlocSimple import BlocSimple



##@brief Classe héritant de BlocSimple, elle contient tous les objets Commentaire d'un code.
class Commentaire(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Commentaire.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesCommentaires.append(self)
        #self.prog.lesCommentaires.sort(key=getCle)
    
