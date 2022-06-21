from src.api.Noeud import Noeud
from src.api.tree_sitter_utilities import recupereTexteDansSource

##@class Bloc 
#@brief Structure de données de plus haut niveau à laquelle on associe la gestion du Noeud.
#Un Bloc se limite à sa référence à un objet Noeud (qui lui même fait référence à un node de Tressitter).
class Bloc:
    ##
    #@fn __init__(lenodeTreeSitter, progObjetPatrick)
    #@brief Constructeur de la classe Bloc.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        #Cette partie permet d'éviter de créer inutilement des instances de noeuds
        cleNoeud = Noeud.get_laCle(lenodeTreeSitter) # cleNoeud contient les coordonnées du Bloc
        if cleNoeud in progObjetPatrick.lesCles:
            self.noeud = progObjetPatrick.mondictCles[cleNoeud]   #On récupère le noeud
        else:
            self.noeud = Noeud(lenodeTreeSitter, self, progObjetPatrick)  #On cree l'objet Noeud
        
        self.prog = progObjetPatrick
        self.prog.lesBlocs.append(self) #Ajoute à progObjetPatrick le Bloc que l'on vient de créer
        #self.prog.lesBlocs.sort(key=getCle)  #on maintient trié
        #self.prog.lesBlocs.sort(key=getattr(self, 'getCle'))
        #bisect.insort_left( self.prog.lesBlocs, self, key=Noeud.get_laCle)

    ##
    #@fn __str__()
    #@brief Renvoie le texte correspondant à un objet Noeud. Diffère de la fonction str() de base de Python.
    def __str__(self):
        val = recupereTexteDansSource(self.prog.codeSource, self.noeud.node)
        return val       


    ##
    #@fn getValeur()
    #@brief Récupère la valeur d'un Bloc.
    def getValeur(self):
        return self.__str__()    

    ##
    #@fn getLocalisation()
    #@brief Retourne la position d'un Bloc sous la forme : [(ligneDebut, colonneDebut) (ligneFin, colonneFin)].
    def getLocalisation(self):
        x1=self.noeud.node.start_point[0]
        y1=self.noeud.node.start_point[1]
        x2=self.noeud.node.end_point[0]
        y2=self.noeud.node.end_point[1]
        return "[(" + str(x1) + ", " + str(x2) + ") (" + str(y1) + ", " + str(y2) + ")]"


    ##
    #@fn getLigneDebut()
    #@brief Retourne la position de la première ligne du Bloc.
    def getLigneDebut(self):
        ligneDebut = self.noeud.node.start_point[0]
        return  ligneDebut
    
    ##
    #@fn getLigneFin()
    #@brief Retourne la position de la dernière ligne du Bloc.
    def getLigneFin(self):
        ligneFin = self.noeud.node.start_point[1]
        return ligneFin

    ##
    #@fn getColonneDebut()
    #@brief Retourne la position du premier caractère de la première ligne du Bloc.
    def getColonneDebut(self):
        colonneDebut = self.noeud.node.end_point[0]
        return colonneDebut
    
    ##
    #@fn getColonneFin()
    #@brief Retourne la position du dernier caractère de la dernière ligne du Bloc.
    def getColonneFin(self):
        colonneFin = self.noeud.node.end_point[1]
        return colonneFin

    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getBlocs()[2].getType() \n \n
    #Résultats possibles : \n \n
    #'Identificateur', 'Commentaire', 'Literal', 'TypeQualificateur', 'SizedTypeSpecificateur', 'Identificateur', 'Expression', 'ExpressionUnaire'
    #'ExpressionBinaire', 'ExpressionUpdate', 'ExpressionParenthesee', 'Function', 'Affectation', 'Declaration', 'BlocCompose', 'StructureIf'
    #'StructureSwitch', 'StructureFor', 'StructureWhile', 'StructureDoWhile', 'InstructionReturn', 'InstructionBreak' ...
    def getTypeBloc(self):
        letype=type(self)
        tab=str(letype).split('.')
        val=tab[len(tab)-1][:-2]
        return val
        #return type(self)

    