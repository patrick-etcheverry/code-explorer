from src.api.BlocSimple import BlocSimple


##@class StructureConditionnelle(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient toutes les Strucutures Conditionnelles d'un code, par exemple ( if() { } ).         
class StructureConditionnelle(BlocSimple):
    
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


    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getStructuresConditionnelles()[2].getType() \n \n
    #Résultat possible : \n \n
    #'StructureConditionnelle', 'StructureIf', 'StructureSwitch'
    def getType(self):
        return self.getTypeBloc()