from src.api.BlocSimple import BlocSimple


##@class Commentaire(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets commentaires d'un code.
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
    

    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getCommentaires()[2].getType() \n \n
    #Résultat possible : \n \n
    #'Commentaire'
    def getType(self):
        return self.getTypeBloc()