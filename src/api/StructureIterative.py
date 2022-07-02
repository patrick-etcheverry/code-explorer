from src.api.StructureControle import StructureControle
from src.api.tree_sitter_utilities import splited

##@brief Classe héritant de BlocCompose, elle contient tous les objets StructureIterative d'un code.
class StructureIterative(StructureControle):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe StructureIterative.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresIterative.append(self)

    ##
    #@fn natureBoucle(indexBoucle, programme)
    #@brief Retourne True si la Boucle a un nombre de répétitions connues et False sinon.
    #\n Exemple d'utilisation : \n
    #- toto = p.lesBoucles[0].natureBoucle()
    #\n \n Résultat potentiel : False
    def natureBoucle(self): 
        verdict = self.noeud.node.type
        if verdict == "for_statement":
            return True
        if verdict == "while_statement" or "do_statement":
            return False


    ##
    #@fn verifCondition(condition)
    #@brief Retourne True si la condition de la Boucle dans le code est identique à la condition donnée en paramètre et False sinon.
    #@param condition Chaîne de caractères correspondant à la condition que l'on souhaite vérifier.
    #\n Exemple d'utilisation : \n
    #- p.lesBoucles[0].verifCondition("i < 3")
    #\n \n Résultat potentiel : True
    def verifCondition(self, condition):
        conditionParametre = splited(condition)
        conditionCode = splited(self.getCondition().getValeur())
        if conditionParametre == conditionCode:
            return True
        else:
            return False

    def chercheBlocsNonComposes(self):
        lesBlocsSimples=[]
        if self.getBlocTrt().getType()!="BlocCompose":
            lesBlocsSimples.append(self.getBlocTrt())
        return lesBlocsSimples

