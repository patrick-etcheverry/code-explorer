##
#@file ModeleObjetPatrick.py
#Fichier contenant les classes du programme
#@author NODENOT Thierry
#@date 06/2022
#@version 0.0.1 Alpha
#

from sqlalchemy import false, true
from tree_sitter_utilities import splited, traverse, extraireByType, extraireByName, cherche, recupereNoeud, recupereTexteDansSource
#import bisect


class listeOrdonnee(list):
    def __init__(self, cletri):  #on lui passe le critère de tri
        super().__init__()
        self.laCleTri=cletri
        self.iterListe=iter(self)
    
    def append(self, val):
        super().append(val)
        self.sort(key=self.laCleTri)

    def next(self):
        return next(self.iterListe)


    

#a déplacer
def getCle(bloc):
    x1=bloc.noeud.node.start_point[0]
    y1=bloc.noeud.node.start_point[1]
    x2=bloc.noeud.node.end_point[0]
    y2=bloc.noeud.node.end_point[1]      
    return (x1, y1, x2, y2)


##
#@class Noeud
#@brief Base de toutes choses dans le programme, elle encapsule un "node" de Tree-Sitter.
class Noeud:

    ##Structure de données de la classe "Noeud" constituée d'un ensemble de clés.
    #lesCles = set()
    
    #ici on va utiliser la structure lesCles attaché au prgramme p
    
    ##Structure de données qui permet de récupérer le "Noeud" associé à une clé.
    
    #ici on va utiliser la structure mondictCles attaché au programme p
    #mondictCles = {}

    ##
    #@fn get_laCle(leNode)
    #@brief Renvoie une clé qui contient les coordonnées du Noeud passé en paramètre sous la forme : XX-YY_WW-ZZ.\n
    #Avec : 
    #- XX correspondant au début de la ligne du Noeud
    #- YY à la fin de la ligne
    #- WW au début de la colonne
    #- ZZ à la fin de la colonne
    #@param leNode : Correspond au Noeud dont on veut obtenir la clé.
    def get_laCle(leNode):
        x1 = leNode.start_point[0]
        y1 = leNode.start_point[1]
        x2 =  leNode.end_point[0]
        y2 = leNode.end_point[1]
        laCle = str(x1) + "-" + str(y1) + "_"+str(x2) + "-" + str(y2)
        return laCle


    
    ##
    #@fn __init__(nodeTreesitter, leBloc)
    #@brief Constructeur de la classe Noeud.
    #@param nodeTreesitter : Correspond à un Node de Tree-Sitter à qui on va associer une clé
    #@param leBloc : Bloc qui va être associé à cet objet Noeud.
    def __init__(self, nodeTreesitter, leBloc, dansprog):
        self.node = nodeTreesitter
        self.bloc = leBloc
        #on cree l'element du dictionnaire qui va permettre d'associer un Node au sens tree-sitter à une clé
        maCle = Noeud.get_laCle(nodeTreesitter)
        dansprog.lesCles.add(maCle)
        dansprog.mondictCles[maCle] = self 
    

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
    #@fn getTypeBloc()
    #@brief Retourne le type du Bloc.
    def getType(self):
        return type(self)


    def getTypeString(self):
        return self.noeud.node.type.__str__()

    
##@class BlocSimple(Bloc)
#@brief Classe héritant de Bloc, elle ne contient que les objets les plus basique d'un code.
class BlocSimple(Bloc):

    ##
    #@fn __init__(lenodeTreeSitter, progObjetPatrick)
    #@brief Constructeur de la classe BlocSimple.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBlocsSimples.append(self) # Surcharge de progObjetPatrick en le définissant en BlocSimple
        #self.prog.lesBlocsSimples.sort(key=getCle)

##@class BlocCompose(Bloc)
#@brief Classe héritant de Bloc, elle contient des objets composés de plusieurs Blocs Simples.
class BlocCompose(Bloc):

    ##
    #@fn __init__( lenodeTreeSitter, progObjetPatrick)
    #@brief Constructeur de la classe BlocCompose.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        self.lesBlocs=[]
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
        return self.lesBlocs() 


##@class Commentaire(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets commentaires d'un code.
class Commentaire(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Commentaire.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesCommentaires.append(self)
        #self.prog.lesCommentaires.sort(key=getCle)
        


##@class Literal(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets litéral d'un code.
class Literal(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Literal.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesLiteral.append(self)
        #self.prog.lesLiteral.sort(key=getCle)
        
    


##@class InstructionBreak(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient toutes instruction Break d'un code.
class InstructionBreak(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe InstructionBreak.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesInstructionsBreak.append(self)
        #self.prog.lesInstructionsBreak.sort(key=getCle)
        


##@class InstructionReturn(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient toutes instruction Return d'un code.
class InstructionReturn(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe InstructionReturn.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesInstructionsReturn.append(self)
        #self.prog.lesInstructionsReturn.sort(key=getCle)
        



##@class TypeQualificateur(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets TypeQualificateur d'un code, comme les constantes par exemple.
class TypeQualificateur(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe TypeQualificateur.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesTypesQualificateurs.append(self)
        #progObjetPatrick.lesTypesQualificateurs.append(self)


##@class SizedTypeSpecificateur(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets SizedTypeSpecificateur d'un code, comme les "unsigned int" par exemple.
class SizedTypeSpecificateur(BlocSimple):


    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe SizedTypeSpecificateur.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSizedTypeSpecificateurs.append(self)



##@class Type(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Type d'un code, comme "int" ou "string" par exemple.
class Type(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Type.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesTypes.append(self)

##@class Identificateur(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Identificateur d'un code, c'est-à-dire les noms des variables par exemple.
class Identificateur(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Identificateur.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesIdentificateurs.append(self)

    ##
    #@fn setIdentificateur(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):
        self.identificateur = {}
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.identificateur["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Bloc inexistant pour identificateur")

        self.identificateur["node"] = node
    
    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Identificateurs sous forme d'une structure de données.
    def getIdentificateur(self):
        return self.identificateur["bloc"]
           

##@class Declaration(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Declaration d'un code, par exemple : "int i = 2;".
class Declaration(BlocSimple):  

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Declaration.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter,  progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesDeclarations.append(self)
    

    ##
    #@fn setType(node)
    #@brief Défini le noeud en tant que Type.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setType(self, node):
        self.type = {}
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.type["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Bloc inexistant pour type")
        self.type["node"] = node
        #self.type["text"]=recupereTexteDansSource(self.prog.codeSource, nodeType)


    ##
    #@fn getType()
    #@brief Retourne tous les Types sous forme d'une structure de données.
    def getType(self):
        return self.type["bloc"]
    
    ##
    #@fn setTsetIdentificateurype(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):       
        self.identificateur = {}

        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.identificateur["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Bloc inexistant pour identificateur")
        self.identificateur["node"] = node
    

    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Identificateur sous forme d'une structure de données.
    def getIdentificateur(self):
        return self.identificateur["bloc"]
    

    ##
    #@fn setValeurExpression(node)
    #@brief Défini le noeud en tant que ValeurExpression.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setValeurExpression(self, node):
        self.valeur={}
        if node==None:
            self.valeur["bloc"]=None
        else:
            lebloc=self.prog.cherche(node)
            if not lebloc==None:
                self.valeur["bloc"]=lebloc
            else:
                pass
                print("!!!!!!! Bloc inexistant pour setvaleurexpression")
        self.valeur["node"]=node
    
    ##
    #@fn getExpression()
    #@brief Retourne toutes les Expressions sous forme d'une structure de données.
    def getExpression(self):
        return self.valeur["bloc"]
    
    ##
    #@fn setDeclaration(node)
    #@brief Défini le noeud en tant que Declaration.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setDeclaration(self, node):
        self.declaration = {}
        leBloc = BlocSimple(node, self.prog)
        if not leBloc == None:
            self.declaration["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Bloc inexistant pour setDeclaration")
        self.declaration["node"] = node


    ##
    #@fn getDeclaration()
    #@brief Retourne toutes les Declarations sous forme d'une structure de données.
    def getDeclaration(self):
        return self.declaration["bloc"]
    
##@class ExpressionUpdate(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets ExpressionUpdate d'un code, par exemple : "i++".
class ExpressionUpdate(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ExpressionUpdate.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesExpressionsUpdate.append(self)

    ##
    #@fn setIdentificateur(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):
        self.identificateur={}
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.identificateur["bloc"] = leBloc
        else:
            print("!!!!!!! Bloc inexistant pour setIdentificateur de ExpressionUpdate")
        self.identificateur["node"] = node

    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Identificateurs sous forme d'une structure de données.
    def getIdentificateur(self):
        return self.identificateur["bloc"]

    ##
    #@fn setOperateur(node)
    #@brief Défini le noeud en tant qu'Operateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setOperateur(self, node):
        self.operateur = {}

        leBloc = BlocSimple(node, self.prog)
        if not leBloc == None:
            self.operateur["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Bloc inexistant pour setOperateur de ExpressionUpdate")
        self.operateur["node"] = node

    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Operateurs sous forme d'une structure de données.
    def getOperateur(self):
        return self.operateur["bloc"]
        #self.identifier["text"] = recupereTexteDansSource(self.prog.codeSource, node)



##@class Affectation(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Affectations d'un code, par exemple : "i = i + 1".
class Affectation(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Affectation.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesAffectations.append(self)
    
    ##
    #@fn setIdentificateur(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):
        self.identifier = {}
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.identifier["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Bloc inexistant pour identificateur")
        self.identifier["node"] = node
        #self.identifier["text"] = recupereTexteDansSource(self.prog.codeSource, node)


    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Identificateurs sous forme d'une structure de données.
    def getIdentificateur(self):
        return self.identifier["bloc"]


    ##
    #@fn setExpression(node)
    #@brief Défini le noeud en tant qu'Expression.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setExpression(self, node):
        self.expression = {} 
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.expression["bloc"] = leBloc
        else:
            print("!!!!!!! Bloc inexistant pour expression dans Affectation")
        self.expression["node"] = node
        #self.expression["text"]=recupereTexteDansSource(self.prog.codeSource, node)   
    

    ##
    #@fn getExpression()
    #@brief Retourne toutes les Expressions sous forme d'une structure de données.
    def getExpression(self):
        return self.expression["bloc"]


      ##
    #@fn setOperateur(node)
    #@brief Défini le noeud en tant qu'Operateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setOperateur(self, node):
        self.operateur = {}

        leBloc = BlocSimple(node, self.prog)
        if not leBloc == None:
            self.operateur["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Bloc inexistant pour setOperateur de Affectation")
        self.operateur["node"] = node

    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Operateurs sous forme d'une structure de données.
    def getOperateur(self):
        return self.operateur["bloc"]
        #self.identifier["text"] = recupereTexteDansSource(self.prog.codeSource, node)


##@class Expression(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Affectations d'un code, par exemple : "toto = tab[i];".
class Expression(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Expression.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)

        progObjetPatrick.lesExpressions.append(self)

    def setExpression(self, node):
        self.expression={} 
        lebloc=self.prog.cherche(node)
        if not lebloc==None:
            self.expression["bloc"]=lebloc
        else:
            print("!!!!!!! Bloc inexistant pour setExpression dans expression")
        self.expression["node"]=node
    
    def getExpression(self):
        return self.expression["bloc"]


##@class ExpressionParenthesee(Expression)
#@brief Classe héritant de Expression, elle contient tous les objets ExpressionParenthesee d'un code, par exemple : for (int i = 1; i <= "(nbCases - 2)""; i++).
class ExpressionParenthesee(Expression):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ExpressionParenthesee.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesExpressionsParenthesees.append(self)

    ##
    #@fn setExpression(node)
    #@brief Défini le noeud en tant qu'Expression.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setExpression(self, node):
        self.expression = {} 
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.expression["bloc"]=leBloc
        else:
            print("!!!!!!! Bloc inexistant pour Expression dans expr parenth")
        self.expression["node"] = node
    
    ##
    #@fn getExpression()
    #@brief Retourne toutes les Expressions sous forme d'une structure de données.
    def getExpression(self):
        return self.expression

##@class ExpressionUnaire(Expression)
#@brief Classe héritant de Expression, elle contient tous les objets ExpressionUnaire d'un code, par exemple : while("!estTrie").
class ExpressionUnaire(Expression):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ExpressionUnaire.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesExpressionsUnaires.append(self)


    ##
    #@fn setArgument(node)
    #@brief Défini le noeud en tant qu'Argument.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setArgument(self, node):
        self.argument = {} 
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.argument["bloc"]=leBloc
        else:
            print("!!!!!!! Bloc inexistant pour Argument")
        self.argument["node"] = node
    
    ##
    #@fn getArgument()
    #@brief Retourne tous les Arguments sous forme d'une structure de données.
    def getArgument(self):
        return self.argument["bloc"]

    ##
    #@fn setOperateur(node)
    #@brief Défini le noeud en tant qu'Operateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setOperateur(self, node):
        self.operateur = {} 
        leBloc = BlocSimple(node, self.prog)
        if not leBloc == None:
            self.operateur["bloc"]=leBloc
        else:
            print("!!!!!!! Bloc inexistant pour operateur" + str(node))
        self.operateur["node"] = node
    
    ##
    #@fn getOperateur()
    #@brief Retourne tous les Operateurs sous forme d'une structure de données.
    def getOperateur(self):
        return self.operateur["bloc"]

##@class ExpressionBinaire(Expression)
#@brief Classe héritant de Expression, elle contient tous les objets ExpressionBinaire d'un code, par exemple : while("compteur < 20").
class ExpressionBinaire(Expression):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ExpressionBinaire.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        
        self.prog=progObjetPatrick

        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesExpressionsBinaires.append(self)

    ##
    #@fn setGauche(node)
    #@brief Défini le noeud en tant qu'élement de Gauche.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setGauche(self, node):
        self.gauche = {} 
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.gauche["bloc"] = leBloc
        else:
            print("!!!!!!! Bloc inexistant pour Gauche")
        self.gauche["node"] = node

    ##
    #@fn getGauche()
    #@brief Retourne tous les éléments de Gauche sous forme d'une structure de données.
    def getGauche(self):
        return self.gauche["bloc"]

    ##
    #@fn setOperateur(node)
    #@brief Défini le noeud en tant qu'Operateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setOperateur(self, node):
        self.operateur = {}
        leBloc = BlocSimple(node, self.prog) 
        if not leBloc == None:
            self.operateur["bloc"] = leBloc
        else:
            print("!!!!!!! Bloc inexistant pour Operateur" + str(node))
        self.operateur["node"] = node

    ##
    #@fn getOperateur()
    #@brief Retourne tous les Operateurs sous forme d'une structure de données.
    def getOperateur(self):
        return self.operateur["bloc"]

    ##
    #@fn setDroite(node)
    #@brief Défini le noeud en tant qu'élement de Droite.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setDroite(self, node):
        self.droite = {} 
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.droite["bloc"] = leBloc
        else:
            print("!!!!!!! Bloc inexistant pour Droite")
        self.droite["node"] = node

    ##
    #@fn getDroite()
    #@brief Retourne tous les éléments de Droite sous forme d'une structure de données.
    def getDroite(self):
        return self.droite["bloc"]
'''
class ExpressionBinaireSimple(ExpressionBinaire):
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)

        progObjetPatrick.lesExpressionsBinairesSimples.add(self)

    def setGauche(self, node):
        self.gauche = {} 
        lebloc = Bloc.cherche(node)
        if not lebloc == None:
            self.gauche["bloc"] = lebloc
        else:
            print("!!!!!!! Bloc inexistant pour Gauche")
        self.gauche["node"] = node

    def getGauche(self):
        return self.gauche["bloc"]

    def setDroite(self, node):
        self.droite = {} 
        lebloc = Bloc.cherche(node)
        if not lebloc == None:
            self.droite["bloc"] = lebloc
        else:
            print("!!!!!!! Bloc inexistant pour Droite")
        self.droite["node"] = node

    def getDroite(self):
        return self.droite["bloc"]

class ExpressionBinaireComposee(ExpressionBinaire):
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog = progObjetPatrick
        #self.text = recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)

        progObjetPatrick.lesExpressionsBinairesComposees.add(self)

    
    def setGauche(self, node):
        self.gauche = {} 
        lebloc = Bloc.cherche(node)
        if not lebloc == None:
            self.gauche["bloc"] = lebloc
        else:
            print("!!!!!!! Bloc inexistant pour Gauche")
        self.gauche["node"] = node

    def getGauche(self):
        return self.gauche["bloc"]

    def setDroite(self, node):
        self.droite = {} 
        lebloc = Bloc.cherche(node)
        if not lebloc == None:
            self.droite["bloc"] = lebloc
        else:
            print("!!!!!!! Bloc inexistant pour Droite")
        self.droite["node"] = node

    def getDroite(self):
        return self.droite["bloc"]

'''



##@class StructureConditionnelle(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient toutes les Strucutures Conditionnelles d'un code, par exemple ( if() { } ).         
class StructureConditionnelle(BlocSimple):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe StructureConditionnelle.
    #Exemple de récupération d'une Structure Conditionnelle : p.lesStructuresConditionelles[0] \n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Structure Conditionnelle du programme
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresConditionelles.append(self)




##@class ConditionIf(StructureConditionnelle)
#@brief Classe héritant de StructureConditionnelle, elle contient toutes les Strucutures sous forme de If d'un code.         
class ConditionIf(StructureConditionnelle):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ConditionIf.
    #Exemple de récupération d'une Condition If : p.lesConditionsIf[0] \n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition If du programme
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesConditionsIf.append(self)

    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'un If.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.condition["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur ConditionIf: Noeud inexistant sur condition")
        self.condition["node"] = node
    
    ##
    #@fn getCondition()
    #@brief Retourne tous les Conditions de If sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesConditionsIf[0].getCondition().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition If du programme
    #\n\n Résultat potentiel : i < 20
    def getCondition(self):
        return self.condition["bloc"]
    

    ##
    #@fn setBlocTrt(node)
    #@brief Défini le noeud en tant que Bloc de Traitements.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocAlors(self, node):
        self.blocalors={} 
        
        lebloc=self.prog.cherche(node)
        if not lebloc==None:
            self.blocalors["bloc"]=lebloc
        else:
            pass
            print("!!!!!!! Pb sur If: Bloc inexistant pour blocalors dans if")
        self.blocalors["node"]=node
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesConditionsIf[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition If du programme
    #\n\n Résultat potentiel : { int toto = 4; }
    def getBlocAlors(self):
        return self.blocalors["bloc"]


    ##
    #@fn setBlocSinon(node)
    #@brief Défini le noeud en tant que Bloc de Traitements Else.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocSinon(self, node):
        self.blocsinon={} 
        if node==None:
            self.blocsinon["bloc"]=None
        else:
            lebloc=self.prog.cherche(node)
            if not lebloc==None:
                self.blocsinon["bloc"]=lebloc
            else:
                pass
                print("!!!!!!! Pb sur If: Bloc inexistant pour bloc sinon dans if")
        self.blocsinon["node"]=node



    ##
    #@fn getBlocSinon()
    #@brief Retourne tous les Blocs de Traitements Else sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesConditionsIf[0].getBlocSinon().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition If du programme
    #\n\n Résultat potentiel : { int toto = 4; }
    def getBlocSinon(self):
        return self.blocsinon["bloc"]



##@class Switch(StructureConditionnelle)
#@brief Classe héritant de StructureConditionnelle, elle contient toutes les Strucutures sous forme de Switch d'un code.         
class Switch(StructureConditionnelle):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Switch.
    #Exemple de récupération d'une Switch : p.lesSwitchs)[0] \n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Premier Switch du programme
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSwitchs.append(self)

    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'un Switch.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.condition["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur ConditionIf: Noeud inexistant sur condition")
        self.condition["node"] = node
        #self.condition["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getCondition()
    #@brief Retourne tous les Conditions des Switchs sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesSwitchs[0].getCondition().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition d'un Switch du programme
    #\n\n Résultat potentiel : i < 20
    def getCondition(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.condition["node"])
        return self.condition["bloc"]
    

    ##
    #@fn setBlocTrt(node)
    #@brief Défini le noeud en tant que Bloc de Traitements.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocTrt(self, node):
        self.bloctrt = {}
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.bloctrt["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur ConditionIf: Noeud inexistant sur bloctrt")        
        self.bloctrt["node"] = node
        #self.bloctrt["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesSwitchs[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition d'un Switch du programme
    #\n\n Résultat potentiel : { int toto = 4; }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]


    ##
    #@fn setCase(node)
    #@brief Défini le noeud en tant que Cas de Switch.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setCase(self, node):
        self.case = {}
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.case["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur Switch: Noeud inexistant sur case")        
        self.case["node"] = node
        #self.case["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getCase()
    #@brief Retourne tous les Cas sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesSwitchs[0].getCase().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Condition d'un Switch du programme
    #\n\n Résultat potentiel : { int toto = 4; }
    def getCase(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.case["node"])
        return self.case["bloc"]




##@class Sous_Programme(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Sous_Programme d'un code.         
class Sous_Programme(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Sous_Programme.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSousProgrammes.append(self)


##@class Function(Sous_Programme)
#@brief Classe héritant de Sous_Programme, elle contient tous les objets Function d'un code, par exemple : "int function()".
class Function(Sous_Programme):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Function.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesFonctions.append(self)



##@class Boucle(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Boucle d'un code.
class Boucle(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Boucle.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBoucles.append(self)

    ##
    #@fn natureBoucle(indexBoucle, programme)
    #@brief Méthode permettant de savoir si la boucle a un nombre de répétitions connues ou non.
    #\n Exemple d'utilisation : \n
    #- toto = p.lesBoucles[0].natureBoucle()
    #\n \n Résultat potentiel : "Cette boucle est une boucle à nombre de répétitions connues." \n \n
    #@warning Les boucles ne sont pas rangées dans l'ordre du code.
    def natureBoucle(self): 
        verdict = self.noeud.node.type
        if verdict == "for_statement":
            return "Cette boucle est une boucle à nombre de répétitions connues."
        if verdict == "while_statement" or "do_statement":
            return"Cette boucle est une boucle à nombre de répétitions inconnues."





##@class BoucleNbRepConnu(Boucle)
#@brief Classe héritant de Boucle, elle contient tous les objets BoucleNbRepConnu d'un code.
class BoucleNbRepConnu(Boucle):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe BoucleNbRepConnu.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBouclesNbRepConnu.append(self)



##@class BoucleNbRepNonConnu(Boucle)
#@brief Classe héritant de Boucle, elle contient tous les objets BoucleNbRepNonConnu d'un code.
class BoucleNbRepNonConnu(Boucle):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe BoucleNbRepNonConnu.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBouclesNbRepNonConnu.append(self)




##@class BoucleWhile(Boucle)
#@brief Classe héritant de Boucle, elle contient tous les objets BoucleWhile d'un code.
class BoucleWhile(BoucleNbRepNonConnu):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe BoucleWhile.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBouclesWhile.append(self)

    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'une Boucle While.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.condition["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur BoucleWhile: Noeud inexistant sur condition")
        self.condition["node"] = node
        #self.condition["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getCondition()
    #@brief Retourne tous les Conditions de Boucle While sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesBouclesWhile[0].getCondition().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle While du programme
    #\n\n Résultat potentiel : compteur < 20
    def getCondition(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.condition["node"])
        return self.condition["bloc"]
    
    ##
    #@fn setBlocTrt(node)
    #@brief Défini le noeud en tant que Bloc de Traitements.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocTrt(self, node):
        self.bloctrt = {}
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.bloctrt["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur BoucleWhile: Noeud inexistant sur bloctrt")        
        self.bloctrt["node"] = node
        #self.bloctrt["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.*
    #Exemple d'utilisation : p.lesBouclesWhile[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle While du programme
    #\n\n Résultat potentiel : { int toto = 3 }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]


##@class BoucleDoWhile(Boucle)
#@brief Classe héritant de Boucle, elle contient tous les objets BoucleDoWhile d'un code.
class BoucleDoWhile(BoucleNbRepNonConnu):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe BoucleDoWhile.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBouclesDoWhile.append(self)


    ##
    #@fn setBlocTrt(node)
    #@brief Défini le noeud en tant que Bloc de Traitements.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocTrt(self, node):
        self.bloctrt = {}
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.bloctrt["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur BoucleWhile: Noeud inexistant sur bloctrt")        
        self.bloctrt["node"] = node
        #self.bloctrt["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesBouclesDoWhile[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle DoWhile du programme
    #\n\n Résultat potentiel : { int toto = 3 }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]


    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'une Boucle DoWhile.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.condition["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur BoucleWhile: Noeud inexistant sur condition")
        self.condition["node"] = node
        #self.condition["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getCondition()
    #@brief Retourne tous les Conditions de Boucle DoWhile sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesBouclesDoWhile[0].getCondition().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle DoWhile du programme
    #\n\n Résultat potentiel : compteur < 20
    def getCondition(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.condition["node"])
        return self.condition["bloc"]
    
    

##@class BoucleFor(Boucle)
#@brief Classe héritant de Boucle, elle contient tous les objets BoucleFor d'un code, par exemple : "for( ; ; )".      
class BoucleFor(BoucleNbRepConnu):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Boucle.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesBouclesFor.append(self)
    
    ##
    #@fn setInit(node)
    #@brief Défini le noeud en tant qu'Initialisateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setInit(self, node):
        self.init = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.init["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur BoucleFor: Bloc inexistant pour init")
        self.init["node"] = node
        #self.init["text"] = recupereTexteDansSource(self.prog.codeSource, node)   

    ##
    #@fn getInit()
    #@brief Retourne tous les Initialisateurs sous forme d'une structure de données.\n
    #Exemple d'utilisation : p.lesBouclesFor[0].getInit().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle For du programme
    #\n\n Résultat potentiel : int i = 0
    def getInit(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.init["node"])
        return self.init["bloc"]


    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition de continuation.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.condition["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur condition")
        self.condition["node"] = node
        #self.condition["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getCondition()
    #@brief Retourne tous les Conditions de continuation sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesBouclesFor[0].getCondition().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle For du programme
    #\n\n Résultat potentiel : i < 5 , i >= 3
    def getCondition(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.condition["node"])
        return self.condition["bloc"]

    ##
    #@fn setPas(node)
    #@brief Défini le noeud en tant que Pas.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setPas(self, node):
        self.pas = {} 
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.pas["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur pas")
        self.pas["node"] = node
        #self.pas["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getPas()
    #@brief Retourne tous les Pas sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesBouclesFor[0].getPas().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle For du programme
    #\n\n Résultat potentiel : i++, i--, i += 1, i = i + 1;
    def getPas(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.pas["node"])
        return self.pas["bloc"]

    ##
    #@fn setBlocTrt(node)
    #@brief Défini le noeud en tant que Bloc de Traitements.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocTrt(self, node):
        self.bloctrt = {}
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.bloctrt["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur bloctrt")        
        self.bloctrt["node"] = node
        #self.bloctrt["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.
    #Exemple d'utilisation : p.lesBouclesFor[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle For du programme
    #\n\n Résultat potentiel : { int i = 0; }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]

    ##
    #@fn estCroissante()
    #@brief Retourne "true" si la boucle a une incrémentation croissante et "false" sinon.
    #Exemple d'utilisation : p.lesBouclesFor[0].estCroissante()
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle For du programme
    #\n\n Résultat potentiel : True
    def estCroissante(self):
        operateur = ""

        if self.getPas().getType() == Affectation:
            operateur = self.getPas().getOperateur().getValeur()
            #Dans le cas de "i = i + 1" l'opérateur sera "=" on doit donc dissocier
            if operateur == "=":
                #Si c'est "=" alors on a affaire à une BinaryExpression, on a alors accès à getExpression()
                operateur = self.getPas().getExpression().getOperateur().getValeur()
        
        if self.getPas().getType() == ExpressionUpdate:
            operateur = self.getPas().getOperateur().getValeur()

        if operateur == "++" or operateur == "+=" or operateur == "+":
            return True
        else:
            return True


        
        




##@class Entree(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Entree d'un code, par exemple : i = "i + 1".      
class Entree(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Entree.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        
        progObjetPatrick.lesEntrees.append(self)

##@class Sortie(BlocSimple)
#@brief Classe héritant de BlocSimple, elle contient tous les objets Sortie d'un code, par exemple : "i" = i + 1.      
class Sortie(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Sortie.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick): 
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSorties.append(self)


##@class Programme
#@brief Base de tout, la classe Programme contient tous les Blocs.
class Programme:

    ##
    #@fn __init__(liste_lignescode, arbre_TreeSitter, langage)
    #@brief Constructeur de la classe Programme.
    #@param liste_lignescode : Correspond au tableau contenant à chaque index toutes lignes du code que vous analysez
    #@param arbre_TreeSitter : Noeud principal du code que vous analysez
    #@param langage : Langage du code que vous analysez
    def __init__(self, liste_lignescode, arbre_TreeSitter, langage):
        self.codeSource = liste_lignescode
        self.TreeNode = arbre_TreeSitter
        self.language = langage
        
        #ici References pour récuperer des infos sur les noeuds
        ##Conteneur de tous les Noeuds
        ## structures de données utilitaires à ne pas utiliser dans les programmes (à rendre privées)
        self.lesNoeuds =  {}
        self.mondictCles= {}
        ##Conteneur de toutes les Clés
        self.lesCles = set()


        #on utilise des set pour éviter les problemes de doublons
        ##Conteneur de tous les Blocs
        self.lesBlocs = listeOrdonnee(getCle)
        ##Conteneur de tous les Blocs Simples
        self.lesBlocsSimples = listeOrdonnee(getCle)
        ##Conteneur de tous les Blocs Composés
        self.lesBlocsComposes = listeOrdonnee(getCle)
        ##Conteneur de tous les Commentaires (EX : /* */)
        self.lesCommentaires = listeOrdonnee(getCle)
        ##Conteneur de tous les TypesQualificateurs (EX : const)
        self.lesTypesQualificateurs = listeOrdonnee(getCle)
        ##Conteneur de tous les SizedTypeSpecificateurs (EX : unsigned int)
        self.lesSizedTypeSpecificateurs=listeOrdonnee(getCle)
        ##Conteneur de tous les Types (EX : int)
        self.lesTypes = listeOrdonnee(getCle)
        ##Conteneur de tous les Identificateurs (EX : Nom d'une variable)
        self.lesIdentificateurs = listeOrdonnee(getCle)
        ##Conteneur de toutes les Déclarations (EX : int toto)
        self.lesDeclarations = listeOrdonnee(getCle)
        ##Conteneur de toutes les Affectations (EX : toto = toto + 1)
        self.lesAffectations = listeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions (EX : cout << endl)
        self.lesExpressions = listeOrdonnee(getCle)
        ##Conteneur de toutes les Instructions Break (EX : break;)
        self.lesInstructionsBreak=listeOrdonnee(getCle)
        ##Conteneur de toutes les Instructions Return (EX : return ();)
        self.lesInstructionsReturn=listeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Parenthesées (EX : i <= "(nbCases - 2)")
        self.lesExpressionsParenthesees = listeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Unaires (EX : (!estTriee))
        self.lesExpressionsUnaires = listeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Binaires (EX : (compteur < 20))
        self.lesExpressionsBinaires = listeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Binaires Simples
        self.lesExpressionsBinairesSimples = listeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Binaires Composées
        self.lesExpressionsBinairesComposees = listeOrdonnee(getCle)
        ##Conteneur de tous les Litéraux (EX : 3)
        self.lesLiteral = listeOrdonnee(getCle)
        ##Conteneur de toutes les Expressions Update (EX : i++)
        self.lesExpressionsUpdate = listeOrdonnee(getCle)
        ##Conteneur de toutes les Entrées (EX : toto = "titi + 1")
        self.lesEntrees = listeOrdonnee(getCle)
        ##Conteneur de toutes les Sorties (EX : "toto" = titi + 1)
        self.lesSorties = listeOrdonnee(getCle)
        ##Conteneur de toutes les Boucles While (EX : while())
        self.lesBouclesWhile = listeOrdonnee(getCle)
        ##Conteneur de toutes les Boucles DoWhile (EX : do{} while())
        self.lesBouclesDoWhile = listeOrdonnee(getCle)
        ##Conteneur de toutes les Boucles For (EX : for( ; ; ))
        self.lesBouclesFor = listeOrdonnee(getCle)
        ##Conteneur de toutes les Boucles avec un nombre de répétition connu (EX : for( ; ; ))
        self.lesBouclesNbRepConnu = listeOrdonnee(getCle)
        ##Conteneur de toutes les Boucles avec un nombre de répétition inconnu (EX : while(), dowhile())
        self.lesBouclesNbRepNonConnu = listeOrdonnee(getCle)
        ##Conteneur de toutes les Boucles (EX : for( ; ; ), while())
        self.lesBoucles = listeOrdonnee(getCle)
        ##Conteneur de toutes les Conditions If (EX : if())
        self.lesConditionsIf = listeOrdonnee(getCle)
        ##Conteneur de tous les Switchs (EX : switch())
        self.lesSwitchs = listeOrdonnee(getCle)
        ##Conteneur de toutes les Conditions (EX : (!estTriee))
        self.lesFonctions = listeOrdonnee(getCle)
        ##Conteneur de tous les Sous-Programmes (EX : function())
        self.lesSousProgrammes = listeOrdonnee(getCle)
        ##Conteneur de toutes les Structures Conditionelles If (EX : if() { })
        self.lesStructuresConditionelles = listeOrdonnee(getCle)
        
        
    
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
    #@fn getBloc()
    #@brief Retourne tous les Blocs
    def getBloc(self):
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
    #@fn getBlocSimple()
    #@brief Retourne tous les Blocs Simples
    def getBlocSimple(self):
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
    #@fn getBlocCompose()
    #@brief Retourne tous les Blocs Composés
    def getBlocCompose(self):
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
    #@fn getCommentaire()
    #@brief Retourne tous les Commentaires
    def getCommentaire(self):
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
    #@fn getTypeQualificateur()
    #@brief Retourne tous les Type Qualificateur comme "const"
    def getTypeQualificateur(self):
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
    #@fn getLeType()
    #@brief Retourne tous les Types de variables initialisés (int, string, ...)
    def getLeType(self):
        return self.lesTypes
    ##
    #@fn getLeTypeAt(pos)
    #@brief Retourne le Type correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getLeTypeAt(self, pos):
        try:
            return self.lesTypes[pos]
        except:
            return False





    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Identificateurs comme les noms de variables par exemple
    def getIdentificateur(self):
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
    #@fn getDeclaration()
    #@brief Retourne toutes les Déclarations (int i = 0)
    def getDeclaration(self):
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
    #@fn getgetAffectationBloc()
    #@brief Retourne toutes les Affectations (i = i + 1)
    def getAffectation(self):
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
    #@fn getExpression()
    #@brief Retourne toutes les Expressions (2 * 3)
    def getExpression(self):
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
    #@fn getBreak()
    #@brief Retourne tous les Breaks (break;)
    def getBreak(self):
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
    #@fn getReturn()
    #@brief Retourne tous les Return (return 0;)
    def getReturn(self):
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
    #@fn getExpressionParenthesee()
    #@brief Retourne toutes les Expressions Parenthesées ( (i < 4) )
    def getExpressionParenthesee(self):
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
    #@fn getExpressionUnaire()
    #@brief Retourne toutes les Expressions Unaires (!estTriee)
    def getExpressionUnaire(self):
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
    #@fn getExpressionBinaire()
    #@brief Retourne toutes les Expressions Binaires ( compteur < 20 )
    def getExpressionBinaire(self):
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
    #@fn getExpressionBinaireSimple()
    #@brief Retourne toutes les Expressions Binaires Simples
    def getExpressionBinaireSimple(self):
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
    #@fn getExpressionBinaireComposee()
    #@brief Retourne toutes les Expressions Binaires Composées 
    def getExpressionBinaireComposee(self):
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
    #@fn getLiteral()
    #@brief Retourne tous les Litéraux ( 4 )
    def getLiteral(self):
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
    #@fn getExpressionUpdate()
    #@brief Retourne toutes les Expressions Updates (i++)
    def getExpressionUpdateAt(self):
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
    #@fn getEntree()
    #@brief Retourne toutes les Entrées
    def getEntree(self):
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
    #@fn getSortie()
    #@brief Retourne toutes les Sorties
    def getSortie(self):
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
    #@fn getBoucleWhile()
    #@brief Retourne toutes les Boucles While ( while() { } )
    def getBoucleWhile(self):
        return self.lesBouclesWhile
    ##
    #@fn getBoucleWhileAt(pos)
    #@brief Retourne la Boucle While correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBoucleWhileAt(self, pos):
        try:
            return self.lesBouclesWhile[pos]
        except:
            return False





    ##
    #@fn getBoucleDoWhile()
    #@brief Retourne toutes les Boucles Do While ( do { } while() )
    def getBoucleDoWhile(self):
        return self.lesBouclesDoWhile
    ##
    #@fn getBoucleDoWhileAt(pos)
    #@brief Retourne la Boucle Do While correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBoucleDoWhileAt(self, pos):
        try:
            return self.lesBouclesDoWhile[pos]
        except:
            return False





    ##
    #@fn getBoucleFor()
    #@brief Retourne toutes les Boucles For ( for( ; ; ) { } )
    def getBoucleFor(self):
        return self.lesBouclesFor
    ##
    #@fn getBoucleForAt(pos)
    #@brief Retourne la Boucle For correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBoucleForAt(self, pos):
        try:
            return self.lesBouclesFor[pos]
        except:
            return False





    ##
    #@fn getBloc()
    #@brief Retourne toutes les Boucles à nombres de répétitions connues
    def getBoucleNbRepConnu(self):
        return self.lesBouclesNbRepConnu
    ##
    #@fn getBoucleNbRepConnuAt(pos)
    #@brief Retourne la Boucle à nombre de répétitions connues correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBoucleNbRepConnuAt(self, pos):
        try:
            return self.lesBouclesNbRepConnu[pos]
        except:
            return False





    ##
    #@fn getBloc()
    #@brief Retourne toutes les Boucles à nombres de répétitions inconnues
    def getBoucleNbRepNonConnu(self):
        return self.lesBouclesNbRepNonConnu
    ##
    #@fn getBoucleNbRepNonConnuAt(pos)
    #@brief Retourne la Boucle à nombre de répétitions inconnues correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBoucleNbRepNonConnuAt(self, pos):
        try:
            return self.lesBouclesNbRepNonConnu[pos]
        except:
            return False





    ##
    #@fn getBoucle()
    #@brief Retourne toutes les Boucles
    def getBoucle(self):
        return self.lesBoucles
    ##
    #@fn getBoucleAt(pos)
    #@brief Retourne la Boucle correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getBoucleAt(self, pos):
        try:
            return self.lesBoucles[pos]
        except:
            return False






    ##
    #@fn getConditionIf()
    #@brief Retourne toutes les Condition If ( if() { } )
    def getConditionIf(self):
        return self.lesConditionsIf
    ##
    #@fn getConditionIfAt(pos)
    #@brief Retourne la Condition If correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getConditionIfAt(self, pos):
        try:
            return self.lesConditionsIf[pos]
        except:
            return False





    ##
    #@fn getSwitch()
    #@brief Retourne tous les Switchs ( switch() { } )
    def getSwitch(self):
        return self.lesSwitchs
    ##
    #@fn getSwitchAt(pos)
    #@brief Retourne le Swtich correspondant à la position donnée en paramètre, si la position est trop grande, renvoie False.
    #@param pos : Position de l'objet souhaité
    def getSwitchAt(self, pos):
        try:
            return self.lesSwitchs[pos]
        except:
            return False





    ##
    #@fn getFonction()
    #@brief Retourne toutes les Fonctions ( bool estCroissante() { } )
    def getFonction(self):
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
    #@fn getSousProgramme()
    #@brief Retourne tous les Sous-Programmes
    def getSousProgramme(self):
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
    #@fn getStructureConditionelle()
    #@brief Retourne toutes les Structures Conditionnelles
    def getStructureConditionelle(self):
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

