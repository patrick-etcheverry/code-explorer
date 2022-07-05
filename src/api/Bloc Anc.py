from sqlalchemy import true
from src.api.Noeud import Noeud
from src.api.tree_sitter_utilities import recupereTexteDansSource
from src.api.tree_sitter_utilities import getCle
from src.api.ListeOrdonnee import ListeOrdonnee
        
import inspect

##@brief Structure de données de plus haut niveau à laquelle on associe la gestion du Noeud.
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
            self.noeud = progObjetPatrick.mondictCles[cleNoeud]
           #On récupère le noeud
        else:
            self.noeud = Noeud(lenodeTreeSitter, self, progObjetPatrick)  #On cree l'objet Noeud
        
        self.blocParent = None
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
    #@fn getLigneDebut()
    #@brief Retourne la position de la première ligne du Bloc.
    def getLigneDebut(self):
        ligneDebut = self.noeud.node.start_point[0]
        return  ligneDebut
    
    ##
    #@fn getLigneFin()
    #@brief Retourne la position de la dernière ligne du Bloc.
    def getLigneFin(self):
        ligneFin = self.noeud.node.end_point[0]
        return ligneFin

    ##
    #@fn getColonneDebut()
    #@brief Retourne la position du premier caractère de la première ligne du Bloc.
    def getColonneDebut(self):
        colonneDebut = self.noeud.node.start_point[1]
        return colonneDebut
    
    ##
    #@fn getColonneFin()
    #@brief Retourne la position du dernier caractère de la dernière ligne du Bloc.
    def getColonneFin(self):
        colonneFin = self.noeud.node.end_point[1]
        return colonneFin

##
    #@fn getLocalisation()
    #@brief Retourne la position d'un Bloc sous la forme : [(ligneDebut, colonneDebut) (ligneFin, colonneFin)].
    def getLocalisation(self):
        x1=self.getLigneDebut()
        y1=self.getColonneDebut()
        x2=self.getLigneFin()
        y2=self.getColonneFin()
        return "[(" + str(x1) + ", " + str(y1) + ") (" + str(x2) + ", " + str(y2) + ")]"


    ##
    #@fn inBloc()
    #@brief Retourne True ou False selon que lebloc apparait ou pas à l'interieur du bloc constitué par self
    #@param lebloc : bloc dont on cherche à déterminer la position par rapport à self
    def inBloc(self, lebloc):
        if lebloc.getLigneDebut() >= self.getLigneDebut() and lebloc.getColonneDebut() >= self.getColonneDebut(): 
            if lebloc.getLigneFin() < self.getLigneFin():
                return true
            elif lebloc.getLigneFin() == self.getLigneFin() and lebloc.getColonneFin() <= self.getColonneFin():
                return True
            else:
                return False
        else:
            return False  


    def getBlocFromAt(self, lamethode, valeur):
        result=ListeOrdonnee(getCle)
        appel_methode='self.prog.'+ lamethode + '(' + str(valeur) + ')'
        candidats=eval(appel_methode)
        if candidats:
            for c in candidats:
                if self.inBloc(c):
                    result.append(c)
            try:
                res=result[valeur]
            except:
                return False
            return res
        else:
            return False
        

    def getBlocsFrom(self, lamethode):
        result=ListeOrdonnee(getCle)
        appel_methode='self.prog.'+ lamethode + '()'
        candidats=eval(appel_methode)
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    
    def getStructureIfAt(self, val):
        nom_methode = inspect.currentframe().f_code.co_name
        return self.getBlocFromAt(nom_methode, val)
    
    def getStructuresIf(self):
        nom_methode = inspect.currentframe().f_code.co_name
        #print Bloc.__name__
        return self.getBlocsFrom(nom_methode)

    def getStructureIterativeAt(self, val):
        nom_methode = inspect.currentframe().f_code.co_name
        return self.getBlocFromAt(nom_methode, val)
    
    def getStructuresIteratives(self):
        nom_methode = inspect.currentframe().f_code.co_name
        #print Bloc.__name__
        return self.getBlocsFrom(nom_methode)    
    
    '''
    def getStructuresIf(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.getStructuresIteratives()
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    

    def getStructureIterativeAt(self, val):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.getStructuresIteratives()
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        try:
            res=result[val]
        except:
            return False
        return res
    '''
    ##
    #@fn getType()
    #@brief Retourne le nom court du type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getBlocs()[2].getType() \n \n
    #Résultats possibles : \n \n
    #'Identificateur', 'Commentaire', 'Literal', 'TypeQualificateur', 'SizedTypeSpecificateur', 'Identificateur', 'Expression', 'ExpressionUnaire'
    #'ExpressionBinaire', 'ExpressionUpdate', 'ExpressionParenthesee', 'Function', 'Affectation', 'Declaration', 'BlocCompose', 'StructureIf'
    #'StructureSwitch', 'StructureFor', 'StructureWhile', 'StructureDoWhile', 'InstructionReturn', 'InstructionBreak' ...
    def getType(self):
        letype=type(self)
        tab=str(letype).split('.')
        val=tab[len(tab)-1][:-2]
        return val

    ##
    #@fn getTypeLong()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getBlocs()[2].getType() \n \n
    #Résultats possibles : \n \n
    #'src.api.Identificateur', 'src.api.Commentaire', 'src.api.Literal', 'TypeQualificateur', 'SizedTypeSpecificateur', 'Identificateur', 'Expression', 'ExpressionUnaire'
    #'src.api.ExpressionBinaire', 'src.api.ExpressionUpdate', 'src.api.ExpressionParenthesee', 'Function', 'Affectation', 'Declaration', 'BlocCompose', 'StructureIf'
    #'src.api.StructureSwitch', 'src.api.StructureFor', 'StructureWhile', 'StructureDoWhile', 'InstructionReturn', 'InstructionBreak' ...
    def getTypeLong(self):
        return type(self)
        
    ##
    #@fn getParent()
    #@brief Retourne le Bloc parent d'un Bloc. \n
    #Exemple : Dans l'instruction "for(int i; i < 20; i++) { }", le parent de "i < 20" est "for(int i; i < 20; i++) { }"
    def getParent(self):
        return self.blocParent