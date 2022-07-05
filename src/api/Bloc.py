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

    '''
    #deprecated
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
        
    #deprecated
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
    '''
   
    
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
    #@fn getBlocs()
    #@brief Retourne tous les Blocs
    def getBlocs(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesBlocs
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result

    ##
    #@fn getBlocAt(pos)
    #@brief Retourne le Bloc correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBlocAt(self, pos):
        candidats=self.getBlocs()
        try:
            res=candidats[pos]
        except:
            return False
        return res
    



    ##
    #@fn getBlocsSimples()
    #@brief Retourne tous les Blocs Simples
    def getBlocsSimples(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesBlocsSimples
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getBlocSimpleAt(pos)
    #@brief Retourne le BlocSimple correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBlocSimpleAt(self, pos):
        candidats=self.getBlocsSimples()
        try:
            res=candidats[pos]
        except:
            return False
        return res
    




    ##
    #@fn getBlocsComposes()
    #@brief Retourne tous les Blocs Composés
    def getBlocsComposes(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesBlocsComposes
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getBlocComposeAt(pos)
    #@brief Retourne le BlocCompose correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBlocComposeAt(self, pos):
        candidats=self.getBlocsComposes()
        try:
            res=candidats[pos]
        except:
            return False
        return res
##
    #@fn getBlocsStructures()
    #@brief Retourne tous les Blocs Structures
    def getBlocsStructures(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesBlocsStructures
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getBlocStructureAt(pos)
    #@brief Retourne le BlocStructure correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBlocStructureAt(self, pos):
        candidats=self.getBlocsStructures()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getCommentaires()
    #@brief Retourne tous les Commentaires
    def getCommentaires(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesCommentaires
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getBlocComposeAt(pos)
    #@brief Retourne le Commentaire correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getCommentaireAt(self, pos):
        candidats=self.getCommentaires()
        try:
            res=candidats[pos]
        except:
            return False
        return res



    ##
    #@fn getTypesQualificateurs()
    #@brief Retourne tous les Type Qualificateur comme "const"
    def getTypesQualificateurs(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesTypesQualificateurs
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getBlocComposeAt(pos)
    #@brief Retourne le Type Qualificateur correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getTypeQualificateurAt(self, pos):
        candidats=self.getTypesQualificateurs()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getTypes()
    #@brief Retourne tous les Types de variables initialisés (int, string, ...)
    def getTypes(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesTypes
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getTypeAt(pos)
    #@brief Retourne le Type correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getTypeAt(self, pos):
        candidats=self.getTypes()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    #Issu de programme et deplacé dans la classe Bloc

    ##
    #@fn getIdentificateurs()
    #@brief Retourne tous les Identificateurs comme les noms de variables par exemple
    def getIdentificateurs(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesIdentificateurs
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getIdentificateurAt(pos)
    #@brief Retourne l'Identificateur correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getIdentificateurAt(self, pos):
        candidats=self.getIdentificateurs()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getDeclarations()
    #@brief Retourne toutes les Déclarations (int i = 0)
    def getDeclarations(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesDeclarations
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getDeclarationAt(pos)
    #@brief Retourne la Déclaration correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getDeclarationAt(self, pos):
        candidats=self.getDeclarations()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getAffectations()
    #@brief Retourne toutes les Affectations (i = i + 1)
    def getAffectations(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesAffectations
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result

    ##
    #@fn getAffectationAt(pos)
    #@brief Retourne l'Affectation correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getAffectationAt(self, pos):
        candidats=self.getAffectations()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getExpressions()
    #@brief Retourne toutes les Expressions (2 * 3)
    def getExpressions(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesExpressions
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result

    ##
    #@fn getExpressionAt(pos)
    #@brief Retourne l'Expression correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionAt(self, pos):
        candidats=self.getExpressions()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getBreaks()
    #@brief Retourne tous les Breaks (break;)
    def getInstructionsBreak(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesInstructionsBreak
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getBreakAt(pos)
    #@brief Retourne le Break correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getInstructionBreakAt(self, pos):
        candidats=self.getInstructionsBreak()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getReturns()
    #@brief Retourne tous les Return (return 0;)
    def getReturns(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesIntructionsReturn
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result

    ##
    #@fn getReturnAt(pos)
    #@brief Retourne le Return correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getReturnAt(self, pos):
        candidats=self.getReturns()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getExpressionsParenthesees()
    #@brief Retourne toutes les Expressions Parenthesées ( (i < 4) )
    def getExpressionsParenthesees(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesExpressionsParenthesees
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getExpressionParentheseeAt(pos)
    #@brief Retourne l'Expression Parenthesée correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionParentheseeAt(self, pos):
        candidats=self.getExpressionsParenthesees()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getExpressionsUnaires()
    #@brief Retourne toutes les Expressions Unaires (!estTriee)
    def getExpressionsUnaires(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesExpressionsUnaires
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getExpressionUnaireAt(pos)
    #@brief Retourne l'Expression Unaire correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionUnaireAt(self, pos):
        candidats=self.getExpressionsUnaires()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getExpressionsBinaires()
    #@brief Retourne toutes les Expressions Binaires ( compteur < 20 )
    def getExpressionsBinaires(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesExpressionsBinaires
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getExpressionBinaireAt(pos)
    #@brief Retourne l'Expression Binaire correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionBinaireAt(self, pos):
        candidats=self.getExpressionsBinaires()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getExpressionsBinairesSimples()
    #@brief Retourne toutes les Expressions Binaires Simples
    def getExpressionsBinairesSimples(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesExpressionsBinairesSimples
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getExpressionBinaireSimple(pos)
    #@brief Retourne l'Expression Binaire Simple correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionBinaireSimpleAt(self, pos):
        candidats=self.getExpressionsBinairesSimples()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getExpressionsBinairesComposees()
    #@brief Retourne toutes les Expressions Binaires Composées 
    def getExpressionsBinairesComposees(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesExpressionsComposees
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
##
    #@fn getExpressionBinaireComposeeAt(pos)
    #@brief Retourne l'Expression Binaire Composée correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionBinaireComposeeAt(self, pos):
        candidats=self.getExpressionsBinairesComposees()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getLiterals()
    #@brief Retourne tous les Litéraux ( 4 )
    def getLiterals(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesLiterals
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getLiteralAt(pos)
    #@brief Retourne le Litéral correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getLiteralAt(self, pos):
        candidats=self.getLiterals()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getExpressionsUpdates()
    #@brief Retourne toutes les Expressions Updates (i++)
    def getExpressionsUpdates(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesExpressionsUpdate
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getExpressionUpdateAt(pos)
    #@brief Retourne l'Expression Update Composée correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionUpdateAt(self, pos):
        candidats=self.getExpressionsUpdates()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getEntrees()
    #@brief Retourne toutes les Entrées
    def getEntrees(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesEntrees
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getEntreeAt(pos)
    #@brief Retourne l'Entrée correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getEntreeAt(self, pos):
        candidats=self.getEntrees()
        try:
            res=candidats[pos]
        except:
            return False
        return res

    ##
    #@fn getSorties()
    #@brief Retourne toutes les Sorties
    def getSorties(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesSorties
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getSortieAt(pos)
    #@brief Retourne la Sortie correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getSortieAt(self, pos):
        candidats=self.getSorties()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getStructuresWhile()
    #@brief Retourne toutes les Structures While ( while() { } )
    def getStructuresWhile(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesStructuresWhile
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getStructureWhileAt(pos)
    #@brief Retourne la Structure While correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureWhileAt(self, pos):
        candidats=self.getStructuresWhile()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getStructuresDoWhile()
    #@brief Retourne toutes les Structures Do While ( do { } while() )
    def getStructuresDoWhile(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesStructuresDoWhile
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getStructureDoWhileAt(pos)
    #@brief Retourne la Structure Do While correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureDoWhileAt(self, pos):
        candidats=self.getStructuresDoWhile()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getStructuresFor()
    #@brief Retourne toutes les Structures For ( for( ; ; ) { } )
    def getStructuresFor(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesStructuresFor
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getStructureForAt(pos)
    #@brief Retourne la Structure For correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureForAt(self, pos):
        candidats=self.getStructuresFor()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getStructuresNbRepConnu()
    #@brief Retourne toutes les Structures à nombres de répétitions connues
    def getStructuresNbRepConnu(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesStructuresNbRepConnu
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getStructureNbRepConnuAt(pos)
    #@brief Retourne la Structure à nombre de répétitions connues correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureNbRepConnuAt(self, pos):
        candidats=self.getStructuresNbRepConnu()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getStructuresNbRepNonConnu()
    #@brief Retourne toutes les Structures à nombres de répétitions inconnues
    def getStructuresNbRepNonConnu(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesStructuresNbRepNonConnu
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getStructureNbRepNonConnuAt(pos)
    #@brief Retourne la Structure à nombre de répétitions inconnues correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureNbRepNonConnuAt(self, pos):
        candidats=self.getStructuresNbRepNonConnu()
        try:
            res=candidats[pos]
        except:
            return False
        return res


    '''
    ##
    #@fn getStructuresIterative()
    #@brief Retourne toutes les Boucles
    def getStructuresIteratives(self):
        return self.lesStructuresIteratives
    ##
    #@fn getStructureIterativeAt(pos)
    #@brief Retourne la Boucle correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureIterativeAt(self, pos):
        try:
            return self.lesStructuresIteratives[pos]
        except:
            return False

    '''



    '''
    ##
    #@fn getStructuresIf()
    #@brief Retourne toutes les Structure If ( if() { } )
    def getStructuresIf(self):
        lesStructuresIf=self.prog.lesStructuresIf
        
        return self.lesStructuresIf
    ##
    #@fn getStructureIfAt(pos)
    #@brief Retourne la Structure If correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureIfAt(self, pos):
        try:
            return self.lesStructuresIf[pos]
        except:
            return False
    '''

    def getStructuresIf(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesStructuresIf
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result

    def getStructureIfAt(self, pos):
        candidats=self.getStructuresIf()
        try:
            res=candidats[pos]
        except:
            return False
        return res



    def getStructuresIteratives(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesStructuresIteratives
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result

    def getStructureIterativeAt(self, pos):
        candidats=self.getStructuresIteratives()
        try:
            res=candidats[pos]
        except:
            return False
        return res


    ##
    #@fn getStructuresSwitch()
    #@brief Retourne tous les Switchs ( switch() { } )
    def getStructuresSwitch(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesStructuresSwitch
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getStructureSwitchAt(pos)
    #@brief Retourne le Swtich correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureSwitchAt(self, pos):
        candidats=self.getStructuresSwitch()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getFunctions()
    #@brief Retourne toutes les Fonctions ( bool estCroissante() { } )
    def getFunctions(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesFunctions
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getFunctionAt(pos)
    #@brief Retourne la Fonction correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getFunctionAt(self, pos):
        candidats=self.getFunctions()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getSousProgrammes()
    #@brief Retourne tous les Sous-Programmes
    
    def getSousProgrammes(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesSousProgrammes
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
        
    ##
    #@fn getSousProgrammeAt(pos)
    #@brief Retourne le Sous-Programme correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    
    def getSousProgrammeAt(self, pos):
        candidats=self.getSousProgrammes()
        try:
            res=candidats[pos]
        except:
            return False
        return res


    ##
    #@fn getStructuresConditionelles()
    #@brief Retourne toutes les Structures Conditionnelles
    def getStructuresConditionelles(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesStructuresConditionnelles
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getStructureConditionelleAt(pos)
    #@brief Retourne la Structure Conditionnelle correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureConditionelleAt(self, pos):
        candidats=self.getStructuresConditionelles()
        try:
            res=candidats[pos]
        except:
            return False
        return res




    ##
    #@fn getConditions()
    #@brief Retourne toutes les Conditions
    def getConditions(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesConditions
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getConditionAt(pos)
    #@brief Retourne la condition correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionAt(self, pos):
        candidats=self.getConditions()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getConditionsBoucle()
    #@brief Retourne toutes les ConditionBoucle
    def getConditionsBoucle(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesConditionsBoucle
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getConditionBoucleAt(pos)
    #@brief Retourne la ConditionBoucle correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionBoucleAt(self, pos):
        candidats=self.getConditionsBoucle()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getConditionsContinuation()
    #@brief Retourne toutes les ConditionsContinuation
    def getConditionsContinuation(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesConditionsContinuation
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getConditionAt(pos)
    #@brief Retourne la ConditionContinuation correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionContinuationAt(self, pos):
        candidats=self.getConditionsContinuation()
        try:
            res=candidats[pos]
        except:
            return False
        return res



    ##
    #@fn getConditionsArret()
    #@brief Retourne toutes les ConditionsArret
    def getConditionsArret(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesConditionsArret
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getConditionArretAt(pos)
    #@brief Retourne la ConditionArret correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionArretAt(self, pos):
        candidats=self.getConditionsArret()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getConditionsIf()
    #@brief Retourne toutes les ConditionsArret
    def getConditionsIf(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesConditionsIf
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getConditionIfAt(pos)
    #@brief Retourne la ConditionIf correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionIfAt(self, pos):
        candidats=self.getConditionsIf()
        try:
            res=candidats[pos]
        except:
            return False
        return res





    ##
    #@fn getConditionsSwitch()
    #@brief Retourne toutes les ConditionsArret
    def getConditionsSwitch(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesConditionsSwitch
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getConditionSwitchAt(pos)
    #@brief Retourne la ConditionSwitch correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionSwitchAt(self, pos):
        candidats=self.getConditionsSwitch()
        try:
            res=candidats[pos]
        except:
            return False
        return res

    ##
    #@fn getProcedures()
    #@brief Retourne toutes les Procédures
    def getProcedures(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesProcedures
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getProcedureAt(pos)
    #@brief Retourne la Procédure correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getProcedureAt(self, pos):
        candidats=self.getProcedures()
        try:
            res=candidats[pos]
        except:
            return False
        return res


    ##
    #@fn getParametres()
    #@brief Retourne toutes les Parametres
    def getParametres(self):
        result=ListeOrdonnee(getCle)
        candidats=self.prog.lesParametres
        for c in candidats:
            if self.inBloc(c):
                result.append(c)
        return result
    ##
    #@fn getParametreAt(pos)
    #@brief Retourne le Parametre correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getParametreAt(self, pos):
        candidats=self.getParametres()
        try:
            res=candidats[pos]
        except:
            return False
        return res
