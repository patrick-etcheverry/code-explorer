from src.api.StructureControle import StructureControle



##@brief Classe héritant de BlocCompose, elle contient toutes les StructureConditionnelle d'un code, par exemple ( if() { } ).         
class StructureConditionnelle(StructureControle):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe StructureConditionnelle.
    #Exemple de récupération d'une Structure Conditionnelle : p.getStructuresConditionelles[0] \n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Structure Conditionnelle du programme
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresConditionelles.append(self)

    


