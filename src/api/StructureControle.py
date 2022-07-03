#from src.api.BlocCompose import BlocCompose
from src.api.BlocStructure import BlocStructure

#from src.api.tree_sitter_utilities import getCle
#from src.api.ListeOrdonnee import ListeOrdonnee


class StructureControle(BlocStructure):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe StructureControle.
    #Exemple de récupération d'une Structure de Controle : p.getStructuresControle[0] \n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Structure Controle du programme
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresControle.append(self)

    
        


