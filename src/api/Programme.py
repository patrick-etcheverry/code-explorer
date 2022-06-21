from tree_sitter import Language, Parser
from src.api.tree_sitter_utilities import getCle
from src.api.ListeOrdonnee import ListeOrdonnee


from src.api.Noeud import Noeud
import sys
import os
from importlib import import_module

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

##@class Programme
#@brief Base de tout, la classe Programme contient tous les Blocs.
class Programme:  
    ##
    #@fn __init__(liste_lignescode, arbre_TreeSitter, langage)
    #@brief Constructeur de la classe Programme.
    #@param liste_lignescode : Correspond au tableau contenant à chaque index toutes lignes du code que vous analysez
    #@param arbre_TreeSitter : Noeud principal du code que vous analysez
    #@param langage : Langage du code que vous analysez
    def __init__(self, cheminfichier):
        
        self.cheminfichier=cheminfichier
        
        Language.build_library(
        # Store the library in the `build` directory
        'build/my-languages.so',

        # Include one or more languages
        [
            'src/languages/tree-sitter-java',
            'src/languages/tree-sitter-python',
            'src/languages/tree-sitter-javascript',
            'src/languages/tree-sitter-c',
            'src/languages/tree-sitter-cpp'
        ]
        )  
          


        #JS_LANGUAGE = Language('build/my-languages.so', 'javascript')
        #PY_LANGUAGE = Language('build/my-languages.so', 'python')
        #JAVA_LANGUAGE= Language('build/my-languages.so', 'java')
        #C_LANGUAGE = Language('build/my-languages.so', 'c')
        
        # tester l'extension du fichier à parser
        #selon le cas
        nom, extension = os.path.splitext(cheminfichier)
        if extension==".c":
            self.LANGUAGE= Language('build/my-languages.so', 'c')
            self.helper="ModeleObjetPatrick_helperC"
        elif extension==".h":
            self.LANGUAGE= Language('build/my-languages.so', 'cpp')
            self.helper="ModeleObjetPatrick_helperCPP"
        elif extension==".cpp":
            self.LANGUAGE= Language('build/my-languages.so', 'cpp')
            self.helper="ModeleObjetPatrick_helperCPP"
        elif extension==".java":
            self.LANGUAGE= Language('build/my-languages.so', 'java')
            self.helper="ModeleObjetPatrick_helperJAVA"
        elif extension==".js":
            self.LANGUAGE = Language('build/my-languages.so', 'javascript')
            self.helper="ModeleObjetPatrick_helperJS"
        elif extension==".py":
            self.LANGUAGE = Language('build/my-languages.so', 'python')
            self.helper="ModeleObjetPatrick_helperJS"
        else:
            logger.debug("Attention, ce type de fichier n'a pas de parseur associé")
            sys.exit()
        #dans les cas où ca marche ...    
        parser = Parser()
        parser.set_language(self.LANGUAGE)

        moduleCreeObjets=import_module("src.helpers."+self.helper)
        
        
        lefichier=open(self.cheminfichier, encoding='utf-8')
        self.fichierSourceOri = lefichier.read()
        self.codeSource = self.fichierSourceOri.split("\n")
        #print(blob)  #pour afficher le fichier source qui vient d'etre lu
        #print(splitted_code) #pour afficher la liste qui a été fabriquée à partir du texte 
        tree=parser.parse(bytes(self.fichierSourceOri.encode('utf-8')))
        self.TreeNode=tree.root_node
        #print("tree = ",root_node.sexp())

        #ici References pour récuperer des infos sur les noeuds
        ##Conteneur de tous les Noeuds
        ## structures de données utilitaires à ne pas utiliser dans les programmes (à rendre privées)
        self.lesNoeuds =  {}
        self.mondictCles= {}
        ##Conteneur de toutes les Clés
        self.lesCles = set()


        #on utilise des set pour éviter les problemes de doublons
        ##Conteneur de tous les Blocs
        self.lesBlocs = ListeOrdonnee(getCle)
        ##Conteneur de tous les Blocs Simples
        self.lesBlocsSimples = ListeOrdonnee(getCle)
        ##Conteneur de tous les Blocs Composés
        self.lesBlocsComposes = ListeOrdonnee(getCle)
        ##Conteneur de tous les Commentaires (EX : /* */)
        self.lesCommentaires = ListeOrdonnee(getCle)
        ##Conteneur de tous les TypesQualificateurs (EX : const)
        self.lesTypesQualificateurs = ListeOrdonnee(getCle)
        ##Conteneur de tous les SizedTypeSpecificateurs (EX : unsigned int)
        self.lesSizedTypeSpecificateurs=ListeOrdonnee(getCle)
        ##Conteneur de tous les Types (EX : int)
        self.lesTypes = ListeOrdonnee(getCle)
        ##Conteneur de tous les Identificateurs (EX : Nom d'une variable)
        self.lesIdentificateurs = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Déclarations (EX : int toto)
        self.lesDeclarations = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Affectations (EX : toto = toto + 1)
        self.lesAffectations = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions (EX : cout << endl)
        self.lesExpressions = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Instructions Break (EX : break;)
        self.lesInstructionsBreak=ListeOrdonnee(getCle)
        ##Conteneur de toutes les Instructions Return (EX : return ();)
        self.lesInstructionsReturn=ListeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Parenthesées (EX : i <= "(nbCases - 2)")
        self.lesExpressionsParenthesees = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Unaires (EX : (!estTriee))
        self.lesExpressionsUnaires = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Binaires (EX : (compteur < 20))
        self.lesExpressionsBinaires = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Binaires Simples
        self.lesExpressionsBinairesSimples = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Binaires Composées
        self.lesExpressionsBinairesComposees = ListeOrdonnee(getCle)
        ##Conteneur de tous les Litéraux (EX : 3)
        self.lesLiteral = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Update (EX : i++)
        self.lesExpressionsUpdate = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Entrées (EX : toto = "titi + 1")
        self.lesEntrees = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Sorties (EX : "toto" = titi + 1)
        self.lesSorties = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Structures While (EX : while())
        self.lesStructuresWhile = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Structures DoWhile (EX : do{} while())
        self.lesStructuresDoWhile = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Structures For (EX : for( ; ; ))
        self.lesStructuresFor = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Structures avec un nombre de répétition connu (EX : for( ; ; ))
        self.lesStructuresNbRepConnu = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Structures avec un nombre de répétition inconnu (EX : while(), dowhile())
        self.lesStructuresNbRepNonConnu = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Structures Itératives (EX : for( ; ; ), while())
        self.lesStructuresIterative = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Conditions If (EX : if())
        self.lesStructuresIf = ListeOrdonnee(getCle)
        ##Conteneur de tous les Switchs (EX : switch())
        self.lesStructuresSwitch = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Conditions (EX : (!estTriee))
        self.lesFonctions = ListeOrdonnee(getCle)
        ##Conteneur de tous les Sous-Programmes (EX : function())
        self.lesSousProgrammes = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Structures Conditionelles If (EX : if() { })
        self.lesStructuresConditionelles = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Conditions If (EX : i < 20)
        self.lesConditions = ListeOrdonnee(getCle)
        ##Conteneur de toutes les ConditionBoucle If (EX : i < 20)
        self.lesConditionsBoucle = ListeOrdonnee(getCle)
        ##Conteneur de toutes les ConditionContinuation If (EX : i < 20)
        self.lesConditionsContinuation = ListeOrdonnee(getCle)
        ##Conteneur de toutes les ConditionArret If (EX : i < 20)
        self.lesConditionsArret = ListeOrdonnee(getCle)
        ##Conteneur de toutes les ConditionIf If (EX : i < 20)
        self.lesConditionsIf = ListeOrdonnee(getCle)
        ##Conteneur de toutes les ConditionSwitch If (EX : i < 20)
        self.lesConditionsSwitch = ListeOrdonnee(getCle)

        moduleCreeObjets.creeObjets(self)
        
        
    
    ##
    #@fn getdictNoeuds()
    #@brief Retourne la structure de données contenant tous les "Noeuds" associés à une clé. 
    def getdictNoeuds(self):
        return self.mondictCles
    

    ##
    #@fn getToutesLesCles()
    #@brief Retourne la structure de données contenant l'ensemble de toutes les clés.
    def getToutesLesCles(self):
        return self.lesCles


    ##
    #@fn cherche(node)
    #@brief Renvoie une instance de Noeud correspondant au node Tree-Sitter si elle existe, sinon elle renvoie "None"
    #@param node : Correspond au Noeud dont on veut savoir si sa clé existe déjà ou non.
    def chercheNoeud(self, node):
        laCleCherchee = Noeud.get_laCle(node)
        if laCleCherchee in self.getToutesLesCles():
            return self.getdictNoeuds()[laCleCherchee] # Si la clé existe, on récupère son noeud
        else:
            return None
    

    ##
    #@fn cherche(leNodeTreeSitter)
    #@brief Vérifie si un noeud existe déjà. A pour but d'éviter les doublons.
    #@param leNodeTreeSitter : Correspond à un Node de Tree-Sitter dont on veut vérifier s'il existe déjà dans le "Programme"
    def cherche(self, leNodeTreeSitter):
        leNoeud = self.chercheNoeud(leNodeTreeSitter)
        if not leNoeud is None:
            return leNoeud.bloc
        else: 
            return None

    #def prepareList(self, laliste):
    #    maliste=sorted(laliste, key=Noeud.get_laCle)
    #    return iter(maliste)





    ##
    #@fn getBlocs()
    #@brief Retourne tous les Blocs
    def getBlocs(self):
        return self.lesBlocs
    ##
    #@fn getBlocAt(pos)
    #@brief Retourne le Bloc correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBlocAt(self, pos):
        try:
            return self.lesBlocs[pos]
        except:
            return False
    



    ##
    #@fn getBlocsSimple()
    #@brief Retourne tous les Blocs Simples
    def getBlocsSimple(self):
        return self.lesBlocsSimples
    ##
    #@fn getBlocSimpleAt(pos)
    #@brief Retourne le BlocSimple correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBlocSimpleAt(self, pos):
        try:
            return self.lesBlocsSimples[pos]
        except:
            return False





    ##
    #@fn getBlocsCompose()
    #@brief Retourne tous les Blocs Composés
    def getBlocsCompose(self):
        return self.lesBlocsComposes
    ##
    #@fn getBlocComposeAt(pos)
    #@brief Retourne le BlocCompose correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBlocComposeAt(self, pos):
        try:
            return self.lesBlocsComposes[pos]
        except:
            return False





    ##
    #@fn getCommentaires()
    #@brief Retourne tous les Commentaires
    def getCommentaires(self):
        return self.lesCommentaires
    ##
    #@fn getBlocComposeAt(pos)
    #@brief Retourne le Commentaire correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getCommentaireAt(self, pos):
        try:
            return self.lesCommentaires[pos]
        except:
            return False





    ##
    #@fn getTypesQualificateurs()
    #@brief Retourne tous les Type Qualificateur comme "const"
    def getTypesQualificateurs(self):
        return self.lesTypesQualificateurs
    ##
    #@fn getBlocComposeAt(pos)
    #@brief Retourne le Type Qualificateur correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getTypeQualificateurAt(self, pos):
        try:
            return self.lesTypesQualificateurs[pos]
        except:
            return False





    ##
    #@fn getTypes()
    #@brief Retourne tous les Types de variables initialisés (int, string, ...)
    def getTypes(self):
        return self.lesTypes
    ##
    #@fn getTypeAt(pos)
    #@brief Retourne le Type correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getTypeAt(self, pos):
        try:
            return self.lesTypes[pos]
        except:
            return False





    ##
    #@fn getIdentificateurs()
    #@brief Retourne tous les Identificateurs comme les noms de variables par exemple
    def getIdentificateurs(self):
        return self.lesIdentificateurs
    ##
    #@fn getIdentificateurAt(pos)
    #@brief Retourne l'Identificateur correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getIdentificateurAt(self, pos):
        try:
            return self.lesIdentificateurs[pos]
        except:
            return False





    ##
    #@fn getDeclarations()
    #@brief Retourne toutes les Déclarations (int i = 0)
    def getDeclarations(self):
        return self.lesDeclarations
    ##
    #@fn getDeclarationAt(pos)
    #@brief Retourne la Déclaration correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getDeclarationAt(self, pos):
        try:
            return self.lesDeclarations[pos]
        except:
            return False





    ##
    #@fn getAffectations()
    #@brief Retourne toutes les Affectations (i = i + 1)
    def getAffectations(self):
        return self.lesAffectations
    ##
    #@fn getAffectationAt(pos)
    #@brief Retourne l'Affectation correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getAffectationAt(self, pos):
        try:
            return self.lesAffectations[pos]
        except:
            return False





    ##
    #@fn getExpressions()
    #@brief Retourne toutes les Expressions (2 * 3)
    def getExpressions(self):
        return self.lesExpressions
    ##
    #@fn getExpressionAt(pos)
    #@brief Retourne l'Expression correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionAt(self, pos):
        try:
            return self.lesExpressions[pos]
        except:
            return False





    ##
    #@fn getBreaks()
    #@brief Retourne tous les Breaks (break;)
    def getBreaks(self):
        return self.lesInstructionsBreak
    ##
    #@fn getBreakAt(pos)
    #@brief Retourne le Break correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBreakAt(self, pos):
        try:
            return self.lesInstructionsBreak[pos]
        except:
            return False





    ##
    #@fn getReturns()
    #@brief Retourne tous les Return (return 0;)
    def getReturns(self):
        return self.lesInstructionsReturn
    ##
    #@fn getReturnAt(pos)
    #@brief Retourne le Return correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getReturnAt(self, pos):
        try:
            return self.lesInstructionsReturn[pos]
        except:
            return False





    ##
    #@fn getExpressionsParenthesees()
    #@brief Retourne toutes les Expressions Parenthesées ( (i < 4) )
    def getExpressionsParenthesees(self):
        return self.lesExpressionsParenthesees
    ##
    #@fn getExpressionParentheseeAt(pos)
    #@brief Retourne l'Expression Parenthesée correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionParentheseeAt(self, pos):
        try:
            return self.lesExpressionsParenthesees[pos]
        except:
            return False





    ##
    #@fn getExpressionsUnaires()
    #@brief Retourne toutes les Expressions Unaires (!estTriee)
    def getExpressionsUnaires(self):
        return self.lesExpressionsUnaires
    ##
    #@fn getExpressionUnaireAt(pos)
    #@brief Retourne l'Expression Unaire correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionUnaireAt(self, pos):
        try:
            return self.lesExpressionsUnaires[pos]
        except:
            return False





    ##
    #@fn getExpressionsBinaires()
    #@brief Retourne toutes les Expressions Binaires ( compteur < 20 )
    def getExpressionsBinaires(self):
        return self.lesExpressionsBinaires
    ##
    #@fn getExpressionBinaireAt(pos)
    #@brief Retourne l'Expression Binaire correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionBinaireAt(self, pos):
        try:
            return self.lesExpressionsBinaires[pos]
        except:
            return False





    ##
    #@fn getExpressionsBinairesSimples()
    #@brief Retourne toutes les Expressions Binaires Simples
    def getExpressionsBinairesSimples(self):
        return self.lesExpressionsBinairesSimples
    ##
    #@fn getExpressionBinaireSimple(pos)
    #@brief Retourne l'Expression Binaire Simple correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionBinaireSimpleAt(self, pos):
        try:
            return self.lesExpressionsBinairesSimples[pos]
        except:
            return False





    ##
    #@fn getExpressionsBinairesComposees()
    #@brief Retourne toutes les Expressions Binaires Composées 
    def getExpressionsBinairesComposees(self):
        return self.lesExpressionsBinairesComposees
    ##
    #@fn getExpressionBinaireComposeeAt(pos)
    #@brief Retourne l'Expression Binaire Composée correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionBinaireComposeeAt(self, pos):
        try:
            return self.lesExpressionsBinairesComposees[pos]
        except:
            return False





    ##
    #@fn getLiterals()
    #@brief Retourne tous les Litéraux ( 4 )
    def getLiterals(self):
        return self.lesLiteral
    ##
    #@fn getLiteralAt(pos)
    #@brief Retourne le Litéral correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getLiteralAt(self, pos):
        try:
            return self.lesLiteral[pos]
        except:
            return False





    ##
    #@fn getExpressionsUpdates()
    #@brief Retourne toutes les Expressions Updates (i++)
    def getExpressionsUpdates(self):
        return self.lesExpressionsUpdate
    ##
    #@fn getExpressionUpdateAt(pos)
    #@brief Retourne l'Expression Update Composée correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getExpressionUpdateAt(self, pos):
        try:
            return self.lesExpressionsUpdate[pos]
        except:
            return False





    ##
    #@fn getEntrees()
    #@brief Retourne toutes les Entrées
    def getEntrees(self):
            return self.lesEntrees
    ##
    #@fn getEntreeAt(pos)
    #@brief Retourne l'Entrée correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getEntreeAt(self, pos):
        try:
            return self.lesEntrees[pos]
        except:
            return False





    ##
    #@fn getSorties()
    #@brief Retourne toutes les Sorties
    def getSorties(self):
        return self.lesSorties
    ##
    #@fn getSortieAt(pos)
    #@brief Retourne la Sortie correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getSortieAt(self, pos):
        try:
            return self.lesSorties[pos]
        except:
            return False





    ##
    #@fn getStructuresWhile()
    #@brief Retourne toutes les Structures While ( while() { } )
    def getStructuresWhile(self):
        return self.lesStructuresWhile
    ##
    #@fn getStructureWhileAt(pos)
    #@brief Retourne la Structure While correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureWhileAt(self, pos):
        try:
            return self.lesStructuresWhile[pos]
        except:
            return False





    ##
    #@fn getStructuresDoWhile()
    #@brief Retourne toutes les Structures Do While ( do { } while() )
    def getStructuresDoWhile(self):
        return self.lesStructuresDoWhile
    ##
    #@fn getStructureDoWhileAt(pos)
    #@brief Retourne la Structure Do While correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureDoWhileAt(self, pos):
        try:
            return self.lesStructuresDoWhile[pos]
        except:
            return False





    ##
    #@fn getStructuresFor()
    #@brief Retourne toutes les Structures For ( for( ; ; ) { } )
    def getStructuresFor(self):
        return self.lesStructuresFor
    ##
    #@fn getStructureForAt(pos)
    #@brief Retourne la Structure For correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureForAt(self, pos):
        try:
            return self.lesStructuresFor[pos]
        except:
            return False





    ##
    #@fn getStructuresNbRepConnu()
    #@brief Retourne toutes les Structures à nombres de répétitions connues
    def getStructuresNbRepConnu(self):
        return self.lesStructuresNbRepConnu
    ##
    #@fn getStructureNbRepConnuAt(pos)
    #@brief Retourne la Structure à nombre de répétitions connues correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureNbRepConnuAt(self, pos):
        try:
            return self.lesStructuresNbRepConnu[pos]
        except:
            return False





    ##
    #@fn getStructuresNbRepNonConnu()
    #@brief Retourne toutes les Structures à nombres de répétitions inconnues
    def getStructuresNbRepNonConnu(self):
        return self.lesStructuresNbRepNonConnu
    ##
    #@fn getStructureNbRepNonConnuAt(pos)
    #@brief Retourne la Structure à nombre de répétitions inconnues correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureNbRepNonConnuAt(self, pos):
        try:
            return self.lesStructuresNbRepNonConnu[pos]
        except:
            return False





    ##
    #@fn getStructuresIterative()
    #@brief Retourne toutes les Boucles
    def getStructuresIterative(self):
        return self.lesStructuresIterative
    ##
    #@fn getStructureIterativeAt(pos)
    #@brief Retourne la Boucle correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureIterativeAt(self, pos):
        try:
            return self.lesStructuresIterative[pos]
        except:
            return False






    ##
    #@fn getStructuresIf()
    #@brief Retourne toutes les Structure If ( if() { } )
    def getStructuresIf(self):
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


    ##
    #@fn getStructuresSwitch()
    #@brief Retourne tous les Switchs ( switch() { } )
    def getStructuresSwitch(self):
        return self.lesStructuresSwitch
    ##
    #@fn getStructureSwitchAt(pos)
    #@brief Retourne le Swtich correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureSwitchAt(self, pos):
        try:
            return self.lesStructuresSwitch[pos]
        except:
            return False





    ##
    #@fn getFonctions()
    #@brief Retourne toutes les Fonctions ( bool estCroissante() { } )
    def getFonctions(self):
        return self.lesFonctions
    ##
    #@fn getFonctionAt(pos)
    #@brief Retourne la Fonction correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getFonctionAt(self, pos):
        try:
            return self.lesFonctions[pos]
        except:
            return False





    ##
    #@fn getSousProgrammes()
    #@brief Retourne tous les Sous-Programmes
    def getSousProgrammes(self):
        return self.lesSousProgrammes
    ##
    #@fn getSousProgrammeAt(pos)
    #@brief Retourne le Sous-Programme correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getSousProgrammeAt(self, pos):
        try:
            return self.lesSousProgrammes[pos]
        except:
            return False


    ##
    #@fn getStructuresConditionelles()
    #@brief Retourne toutes les Structures Conditionnelles
    def getStructuresConditionelles(self):
        return self.lesStructuresConditionelles
    ##
    #@fn getStructureConditionelleAt(pos)
    #@brief Retourne la Structure Conditionnelle correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getStructureConditionelleAt(self, pos):
        try:
            return self.lesStructuresConditionelles[pos]
        except:
            return False
    




    ##
    #@fn getConditions()
    #@brief Retourne toutes les Conditions
    def getConditions(self):
        return self.lesConditions
    ##
    #@fn getConditionAt(pos)
    #@brief Retourne la condition correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionAt(self, pos):
        try:
            return self.lesConditions[pos]
        except:
            return False





    ##
    #@fn getConditionsBoucle()
    #@brief Retourne toutes les ConditionBoucle
    def getConditionsBoucle(self):
        return self.lesConditionsBoucle
    ##
    #@fn getConditionBoucleAt(pos)
    #@brief Retourne la ConditionBoucle correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionBoucleAt(self, pos):
        try:
            return self.lesConditionsBoucle[pos]
        except:
            return False





    ##
    #@fn getConditionsContinuation()
    #@brief Retourne toutes les ConditionsContinuation
    def getConditionsContinuation(self):
        return self.lesConditionsContinuation
    ##
    #@fn getConditionAt(pos)
    #@brief Retourne la ConditionContinuation correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionContinuationAt(self, pos):
        try:
            return self.lesConditionsContinuation[pos]
        except:
            return False




    ##
    #@fn getConditionsArret()
    #@brief Retourne toutes les ConditionsArret
    def getConditionsArret(self):
        return self.lesConditionsArret
    ##
    #@fn getConditionArretAt(pos)
    #@brief Retourne la ConditionArret correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionArretAt(self, pos):
        try:
            return self.lesConditionsArret[pos]
        except:
            return False





    ##
    #@fn getConditionsIf()
    #@brief Retourne toutes les ConditionsArret
    def getConditionsIf(self):
        return self.lesConditionsIf
    ##
    #@fn getConditionIfAt(pos)
    #@brief Retourne la ConditionIf correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionIfAt(self, pos):
        try:
            return self.lesConditionsIf[pos]
        except:
            return False





    ##
    #@fn getConditionsSwitch()
    #@brief Retourne toutes les ConditionsArret
    def getConditionsSwitch(self):
        return self.lesConditionsSwitch
    ##
    #@fn getConditionSwitchAt(pos)
    #@brief Retourne la ConditionSwitch correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionSwitchAt(self, pos):
        try:
            return self.lesConditionsSwitch[pos]
        except:
            return False