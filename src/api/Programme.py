from tree_sitter import Language, Parser
from src.api.tree_sitter_utilities import getCle
from src.api.ListeOrdonnee import ListeOrdonnee
from src.api.BlocCompose import BlocCompose
from src.api.StructureIterative import StructureIterative
from src.api.StructureIf import StructureIf
from src.api.StructureSwitch import StructureSwitch



from src.api.BlocStructure import BlocStructure
from src.api.Noeud import Noeud
import sys
import os
from importlib import import_module

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 


##@brief Base de tout, la classe Programme contient tous les Blocs.
class Programme(BlocStructure):  
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
        ##Conteneur de tous les Blocs Structures
        self.lesBlocsStructures = ListeOrdonnee(getCle)
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
        self.lesStructuresIteratives = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Conditions If (EX : if())
        self.lesStructuresIf = ListeOrdonnee(getCle)
        ##Conteneur de tous les Switchs (EX : switch())
        self.lesStructuresSwitch = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Fonctions 
        self.lesFunctions = ListeOrdonnee(getCle)
        ##Conteneur de toutes les Déclarations de sous-programme (EX : void triParNomCroissant(Etudiant tab[], unsigned int nbCases);
        self.lesProcedures = ListeOrdonnee(getCle)
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
        ##Conteneur de toutes les Parametres If (EX : i < 20)
        self.lesParametres = ListeOrdonnee(getCle)
        ##Conteneur de toutes les structures de controle
        self.lesStructuresControle = ListeOrdonnee(getCle)

        #on rajoute aux blocs structures
        super().__init__(self.TreeNode, self)

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
    #@fn chercheBlocsControleNonComposes()
    #@brief Retourne une liste Ordonnee de tous les blocs non composes dans les structures de controle d'un programme? Renvoie une liste vide s'il n'y en a pas
    def chercheBlocsControleNonComposes(self):
        lesBlocs=ListeOrdonnee(getCle)
        for s in self.lesStructuresControle:
            result=s.chercheBlocsNonComposes()
            for elem in result:
                lesBlocs.append(elem)
        return lesBlocs
    
    ##
    #@fn chercheTracesIdentificateur(valeur, danslebloc)
    #@brief Retourne la liste de tous les blocs dasn lesquelles cette valeur d'identificateur est référencée. Renvoie une liste vide si la valeur d'identificateur n'apparaît pas dans le bloc passé en paramètre
    #@param nomIdentificateur : nom de l'identificateur cherché
    #@param danslebloc : bloc dans lequel chercher l'identificateur
    def chercheTracesIdentificateur(self, nomIdentificateur, danslebloc):
        leresultat=ListeOrdonnee(getCle)
        for id in self.getIdentificateurs():
            if id.getIdentificateur().getValeur()==nomIdentificateur:
                if danslebloc.inBloc(id):
                    leresultat.append(id)
        return leresultat


        '''
        leresultat=ListeOrdonnee(getCle)
        if isinstance(danslebloc, BlocCompose):
            for e in danslebloc.getBlocs():
                res=e.chercheTracesIdentificateur(nomIdentificateur)
                leresultat.append(res)
        elif isinstance(danslebloc, StructureIterative):
            for e in danslebloc.getBlocTrt().getBlocs():
                res=e.chercheTracesIdentificateur(nomIdentificateur)
                leresultat.append(res)
        elif isinstance(danslebloc, StructureIf):
            for e in danslebloc.getBlocAlors().getBlocs():
                res=e.chercheTracesIdentificateur(nomIdentificateur)
                leresultat.append(res)
            for e in danslebloc.getBlocSinon().getBlocs():
                res=e.chercheTracesIdentificateur(nomIdentificateur)
                leresultat.append(res)
        elif isinstance(danslebloc, StructureSwitch):
            pass
        '''        
                


