from src.api.Bloc import Bloc
from src.api.ListeOrdonnee import ListeOrdonnee
from src.api.tree_sitter_utilities import getCle
#from src.api.BlocSimple import BlocSimple
#from src.api.BlocStructure import BlocStructure



##@brief Classe héritant de Bloc, elle contient des objets composés de plusieurs BlocSimple.
class BlocCompose(Bloc):
  


    ##
    #@fn __init__( lenodeTreeSitter, progObjetPatrick)
    #@brief Constructeur de la classe BlocCompose.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.lesBlocs=[]
        self.lesBlocs=ListeOrdonnee(getCle)

        #rajoute par nods pour pouvoir récupérer par getNext tous les blocs composant d'un bloc compose
        #self.bloccompose_iter=iter(self.lesBlocs)

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
        return self.lesBlocs 

     ##
    #@fn traiteBlocs()
    #@brief Applique de maniere recursive la fonction passee en paramètre à chaque bloc simple du bloc compose considere  la liste de tous les Blocs sous forme d'un ensemble.
    #@param fonction : fonction a appliquer quand on trouve un bloc compose
    def traiteBlocs(self, fonction):
        for e in self.getBlocs():
            if isinstance(e, BlocCompose):
                fonction(e.getType())
                e.traiteBlocs(fonction)
            else:
                fonction(e)
    '''
    ##
    #@fn chercheIdentificateur()
    #@brief Applique de maniere recursive la fonction passee en paramètre à chaque bloc simple du bloc compose considere  la liste de tous les Blocs sous forme d'un ensemble.
    #@param nomIdentificateur : nom de l'identificateur cherche
   
    def chercheTracesIdentificateur(self, nomIdentificateur):
        leresultat=ListeOrdonnee(getCle)
        for e in self.getBlocs():
            if isinstance(e, BlocSimple):
                try:
                    if e.getIdentificateur()==nomIdentificateur:
                        leresultat.append(e)        
                except Exception:
                    pass
            elif isinstance(e, BlocStructure):
                pass

        return leresultat    

    '''        
