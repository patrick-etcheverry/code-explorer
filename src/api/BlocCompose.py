from src.api.Bloc import Bloc



##@class BlocCompose(Bloc)
#@brief Classe héritant de Bloc, elle contient des objets composés de plusieurs Blocs Simples.


class BlocCompose(Bloc):

    ##
    #@fn __init__( lenodeTreeSitter, progObjetPatrick)
    #@brief Constructeur de la classe BlocCompose.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        self.lesBlocs=[]
        progObjetPatrick.lesBlocsComposes.append(self)# Surcharge de progObjetPatrick en le définissant en BlocComposee
        #self.prog.lesBlocsComposes.sort(key=getCle)
        
        #il faudrait aussi rattacher les blocs inclus dans ce bloc à ce bloc compose
        #voir Modèle papier de Patrick pour comprendre les liens à établir. On le fera quand tous les objets de base seront créés
        # car sinon on peut en oublier 
    
    
    ##
    #@fn ajouteBloc(bloc)
    #@brief Ajoute un Bloc à la liste des Blocs du programme.
    #@param bloc : Bloc que l'on souhaite ajouter
    def ajouteBloc(self, bloc):
        self.lesBlocs.append(bloc)

    ##
    #@fn getBlocs()
    #@brief Renvoie la liste de tous les Blocs sous forme d'un ensemble.
    def getBlocs(self):
        return self.lesBlocs() 
