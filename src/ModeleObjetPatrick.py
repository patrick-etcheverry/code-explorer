##
#@file ModeleObjetPatrick.py
#Fichier contenant les classes du programme
#@author NODENOT Thierry
#@date 06/2022
#@version 0.0.1 Alpha
#

from tree_sitter_utilities import splited, traverse, extraireByType, extraireByName, cherche, recupereNoeud, recupereTexteDansSource


##
#@class Noeud
#@brief Base de toutes choses dans le programme, elle encapsule un "node" de Tree-Sitter.
class Noeud:

    ##Structure de données de la classe "Noeud" constituée d'un ensemble de clés.
    lesCles = set()
    ##Structure de données qui permet de récupérer le "Noeud" associé à une clé.
    mondictCles = {}

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
    #@fn cherche(node)
    #@brief Renvoie une instance de Noeud correspondant au node Tree-Sitter si elle existe, sinon elle renvoie "None"
    #@param node : Correspond au Noeud dont on veut savoir si sa clé existe déjà ou non.
    def cherche(node):
        laCleCherchee = Noeud.get_laCle(node)
        if laCleCherchee in Noeud.getToutesLesCles():
            return Noeud.getdictNoeuds()[laCleCherchee] # Si la clé existe, on récupère son noeud
        else:
            return None
    
    ##
    #@fn __init__(nodeTreesitter, leBloc)
    #@brief Constructeur de la classe Noeud.
    #@param nodeTreesitter : Correspond à un Node de Tree-Sitter à qui on va associer une clé
    #@param leBloc : Bloc qui va être associé à cet objet Noeud.
    def __init__(self, nodeTreesitter, leBloc):
        self.node = nodeTreesitter
        self.bloc = leBloc
        #on cree l'element du dictionnaire qui va permettre d'associer un Node au sens tree-sitter à une clé
        maCle = Noeud.get_laCle(nodeTreesitter)
        Noeud.lesCles.add(maCle)
        Noeud.mondictCles[maCle] = self 
    

    ##
    #@fn getdictNoeuds()
    #@brief Retourne la structure de données contenant tous les "Noeuds" associés à une clé. 
    def getdictNoeuds():
        return Noeud.mondictCles
    

    ##
    #@fn getToutesLesCles()
    #@brief Retourne la structure de données contenant l'ensemble de toutes les clés.
    def getToutesLesCles():
        return Noeud.lesCles
    
    

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
        if cleNoeud in Noeud.lesCles:
            self.noeud = Noeud.mondictCles[cleNoeud]   #On récupère le noeud
        else:
            self.noeud = Noeud(lenodeTreeSitter, self)  #On cree l'objet Noeud
        
        self.prog = progObjetPatrick
        progObjetPatrick.lesBlocs.add(self) #Ajoute à progObjetPatrick le Bloc que l'on vient de créer
    

    ##
    #@fn __str__()
    #@brief Renvoie le texte correspondant à un objet Noeud. Diffère de la fonction str() de base de Python.
    def __str__(self):
        val = recupereTexteDansSource(self.prog.codeSource, self.noeud.node)
        return val       


    ##
    #@fn cherche(leNodeTreeSitter)
    #@brief Vérifie si un noeud existe déjà. A pour but d'éviter les doublons.
    #@param leNodeTreeSitter : Correspond à un Node de Tree-Sitter dont on veut vérifier s'il existe déjà dans le "Programme"
    def cherche(leNodeTreeSitter):
        leNoeud = Noeud.cherche(leNodeTreeSitter)
        if not leNoeud is None:
            return leNoeud.bloc
        else: 
            return None


    ##
    #@fn getValeur()
    #@brief Récupère la valeur d'un Bloc.
    def getValeur(self):
        return self.__str__()    

    ##
    #@fn getPosition()
    #@brief Récupère la position d'un Bloc.
    def getPosition(self):
        x1=self.noeud.node.start_point[0]
        y1=self.noeud.node.start_point[1]
        x2=self.noeud.node.end_point[0]
        y2=self.noeud.node.end_point[1]
        return "("+str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+")"


    
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
        progObjetPatrick.lesBlocsSimples.add(self) # Surcharge de progObjetPatrick en le définissant en BlocSimple

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
        progObjetPatrick.lesBlocsComposes.add(self)# Surcharge de progObjetPatrick en le définissant en BlocComposee
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
        progObjetPatrick.lesCommentaires.add(self)


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
        progObjetPatrick.lesLiteral.add(self)
    


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
        progObjetPatrick.lesInstructionsBreak.add(self)



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
        progObjetPatrick.lesInstructionsReturn.add(self)




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
        progObjetPatrick.lesTypesQualificateurs.add(self)


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
        progObjetPatrick.lesSizedTypeSpecificateurs.add(self)



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
        progObjetPatrick.lesTypes.add(self)

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
        progObjetPatrick.lesIdentificateurs.add(self)

    ##
    #@fn setIdentificateur(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):
        self.identificateur = {}
        
        leBloc = Bloc.cherche(node)
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
        progObjetPatrick.lesDeclarations.add(self)
    

    ##
    #@fn setType(node)
    #@brief Défini le noeud en tant que Type.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setType(self, node):
        self.type = {}
        
        leBloc = Bloc.cherche(node)
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

        leBloc = Bloc.cherche(node)
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
            lebloc=Bloc.cherche(node)
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
        progObjetPatrick.lesExpressionsUpdate.add(self)

    ##
    #@fn setIdentificateur(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):
        self.identificateur={}
        leBloc = Bloc.cherche(node)
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
        progObjetPatrick.lesAffectations.add(self)
    
    ##
    #@fn setIdentificateur(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):
        self.identifier = {}
        
        leBloc = Bloc.cherche(node)
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
        leBloc = Bloc.cherche(node)
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

        progObjetPatrick.lesExpressions.add(self)

    def setExpression(self, node):
        self.expression={} 
        lebloc=Bloc.cherche(node)
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
        progObjetPatrick.lesExpressionsParenthesees.add(self)

    ##
    #@fn setExpression(node)
    #@brief Défini le noeud en tant qu'Expression.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setExpression(self, node):
        self.expression = {} 
        leBloc = Bloc.cherche(node)
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
        progObjetPatrick.lesExpressionsUnaires.add(self)


    ##
    #@fn setArgument(node)
    #@brief Défini le noeud en tant qu'Argument.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setArgument(self, node):
        self.argument = {} 
        leBloc = Bloc.cherche(node)
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
        #self.prog=progObjetPatrick
        #self.text=recupereTexteDansSource(self.prog.codeSource, lenodeTreeSitter)
        progObjetPatrick.lesExpressionsBinaires.add(self)

    ##
    #@fn setGauche(node)
    #@brief Défini le noeud en tant qu'élement de Gauche.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setGauche(self, node):
        self.gauche = {} 
        leBloc = Bloc.cherche(node)
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
        leBloc = Bloc.cherche(node)
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



class StructureConditionnelle(BlocSimple):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe StructureConditionnelle.
    #Exemple de récupération d'une Structure Conditionnelle : str(list(p.lesStructuresConditionelles)[0]) \n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesStructuresConditionelles" en liste afin de pouvoir sélectionner la Structure Conditionnelle que l'on souhaite
    #- [0] = Première Structure Conditionnelle du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesStructuresConditionelles.add(self)




class ConditionIf(StructureConditionnelle):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe ConditionIf.
    #Exemple de récupération d'une Condition If : str(list(p.lesConditionsIf)[0]) \n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesConditionsIf" en liste afin de pouvoir sélectionner la Condition If que l'on souhaite
    #- [0] = Première Condition If du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesConditionsIf.add(self)

    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'un If.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = Bloc.cherche(node)
        if not leBloc == None:
            self.condition["bloc"] = leBloc
        else:
            pass
            print("!!!!!!! Pb sur ConditionIf: Noeud inexistant sur condition")
        self.condition["node"] = node
    
    ##
    #@fn getCondition()
    #@brief Retourne tous les Conditions de If sous forme d'une structure de données.
    #Exemple d'utilisation : str(list(p.lesConditionsIf)[0].getCondition())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesConditionsIf" en liste afin de pouvoir sélectionner la Condition If que l'on souhaite
    #- [0] = Première Condition If du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
    #\n\n Résultat potentiel : i < 20
    def getCondition(self):
        return self.condition["bloc"]
    

    ##
    #@fn setBlocTrt(node)
    #@brief Défini le noeud en tant que Bloc de Traitements.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocAlors(self, node):
        self.blocalors={} 
        
        lebloc=Bloc.cherche(node)
        if not lebloc==None:
            self.blocalors["bloc"]=lebloc
        else:
            pass
            print("!!!!!!! Pb sur If: Bloc inexistant pour blocalors dans if")
        self.blocalors["node"]=node
    
    ##
    #@fn getBlocTrt()
    #@brief Retourne tous les Blocs de Traitements sous forme d'une structure de données.
    #Exemple d'utilisation : str(list(p.lesConditionsIf)[0].getBlocTrt())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesConditionsIf" en liste afin de pouvoir sélectionner la Condition If que l'on souhaite
    #- [0] = Première Condition If du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
            lebloc=Bloc.cherche(node)
            if not lebloc==None:
                self.blocsinon["bloc"]=lebloc
            else:
                pass
                print("!!!!!!! Pb sur If: Bloc inexistant pour bloc sinon dans if")
        self.blocsinon["node"]=node



    ##
    #@fn getBlocSinon()
    #@brief Retourne tous les Blocs de Traitements Else sous forme d'une structure de données.
    #Exemple d'utilisation : str(list(p.lesConditionsIf)[0].getBlocSinon())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesConditionsIf" en liste afin de pouvoir sélectionner la Condition If que l'on souhaite
    #- [0] = Première Condition If du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
    #\n\n Résultat potentiel : { int toto = 4; }
    def getBlocSinon(self):
        return self.blocsinon["bloc"]



class Switch(StructureConditionnelle):
    
    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Switch.
    #Exemple de récupération d'une Switch : str(list(p.lesSwitchs)[0]) \n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesSwitchs" en liste afin de pouvoir sélectionner le Switch que l'on souhaite
    #- [0] = Premier Switch du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
    #\n\n Résultat potentiel : (nombreDeNotes > 0)
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSwitchs.add(self)

    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'un Switch.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesSwitchs)[0].getCondition())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesSwitchs" en liste afin de pouvoir sélectionner la Condition d'un Switch que l'on souhaite
    #- [0] = Première Condition d'un Switch du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesSwitchs)[0].getBlocTrt())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesSwitchs" en liste afin de pouvoir sélectionner la Condition d'un Switch que l'on souhaite
    #- [0] = Première Condition d'un Switch du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesSwitchs)[0].getCase())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesSwitchs" en liste afin de pouvoir sélectionner la Condition d'un Switch que l'on souhaite
    #- [0] = Première Condition d'un Switch du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
    #\n\n Résultat potentiel : { int toto = 4; }
    def getCase(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.case["node"])
        return self.case["bloc"]




##@class Sous_Programme(BlocCompose)
#@brief Classe héritant de BlocCompose, elle contient tous les objets Sous_Programme d'un code.         
class Sous_Programme(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Sous_Programme.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSousProgrammes.add(self)


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
        progObjetPatrick.lesFonctions.add(self)



##@class Boucle(BlocCompose)
#@brief Classe héritant de BlocCompose, elle contient tous les objets Boucle d'un code.
class Boucle(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Boucle.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesBoucles.add(self)

    ##
    #@fn natureBoucle(indexBoucle, programme)
    #@brief Méthode permettant de savoir si la boucle a un nombre de répétitions connues ou non.
    #\n Exemple d'utilisation : \n
    #- toto = list(p.lesBoucles)[0].natureBoucle()
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
        progObjetPatrick.lesBouclesNbRepConnu.add(self)



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
        progObjetPatrick.lesBouclesNbRepNonConnu.add(self)




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
        progObjetPatrick.lesBouclesWhile.add(self)

    ##
    #@fn setCondition(node)
    #@brief Défini le noeud en tant que Condition d'une Boucle While.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setCondition(self, node):
        self.condition = {} 
        
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesBouclesWhile)[0].getCondition())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesBouclesWhile" en liste afin de pouvoir sélectionner la Boucle While que l'on souhaite
    #- [0] = Première Boucle While du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesBouclesWhile)[0].getBlocTrt())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesBouclesWhile" en liste afin de pouvoir sélectionner la Boucle While que l'on souhaite
    #- [0] = Première Boucle While du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
        progObjetPatrick.lesBouclesDoWhile.add(self)


    ##
    #@fn setBlocTrt(node)
    #@brief Défini le noeud en tant que Bloc de Traitements.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setBlocTrt(self, node):
        self.bloctrt = {}
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesBouclesDoWhile)[0].getBlocTrt())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesBouclesDoWhile" en liste afin de pouvoir sélectionner la Boucle DoWhile que l'on souhaite
    #- [0] = Première Boucle DoWhile du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
        
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesBouclesDoWhile)[0].getCondition())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesBouclesDoWhile" en liste afin de pouvoir sélectionner la Boucle DoWhile que l'on souhaite
    #- [0] = Première Boucle DoWhile du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
        progObjetPatrick.lesBouclesFor.add(self)
    
    ##
    #@fn setInit(node)
    #@brief Défini le noeud en tant qu'Initialisateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setInit(self, node):
        self.init = {} 
        
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesBouclesFor)[0].getInit())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesBouclesFor" en liste afin de pouvoir sélectionner la Boucle For que l'on souhaite
    #- [0] = Première Boucle For du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
        
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesBouclesFor)[0].getCondition())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesBouclesFor" en liste afin de pouvoir sélectionner la Boucle For que l'on souhaite
    #- [0] = Première Boucle For du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
        
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesBouclesFor)[0].getPas())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesBouclesFor" en liste afin de pouvoir sélectionner la Boucle For que l'on souhaite
    #- [0] = Première Boucle For du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
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
        leBloc = Bloc.cherche(node)
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
    #Exemple d'utilisation : str(list(p.lesBouclesFor)[0].getBlocTrt())\n
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesBouclesFor" en liste afin de pouvoir sélectionner la Boucle For que l'on souhaite
    #- [0] = Première Boucle For du programme
    #- str() = Fonction permettant d'afficher le contenu d'un objet Tree-Sitter
    #\n\n Résultat potentiel : { int i = 0; }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]

    ##
    #@fn estCroissante(indexBoucle, programme)
    #@brief Retourne la nature du pas d'une Boucle For (Croissant ou Décroissant).
    #Exemple d'utilisation : toto = list(p.lesBouclesFor)[0].estCroissante()
    #\n Avec :\n
    #- p = Objet Programme
    #- list() = Conversion de "lesBouclesFor" en liste afin de pouvoir sélectionner la Boucle For que l'on souhaite
    #- [0] = Première Boucle For du programme
    #\n\n Résultat potentiel : "C'est une boucle croissante : i++"
    def estCroissante(self):
        verdict = str(self.getPas())
        verdictFinal = splited(verdict)

        if verdictFinal == "i++" or "i=i+1" or "i+=1":
            return "C'est une boucle croissante : " + verdict
        else:
            return "C'est une boucle décroissante : " + verdict




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
        
        progObjetPatrick.lesEntrees.add(self)

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
        progObjetPatrick.lesSorties.add(self)


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

        #on utilise des set pour éviter les problemes de doublons
        ##Conteneur de tous les Blocs
        self.lesBlocs = set()
        ##Conteneur de tous les Blocs Simples
        self.lesBlocsSimples = set()
        ##Conteneur de tous les Blocs Composés
        self.lesBlocsComposes = set()
        ##Conteneur de tous les Commentaires (EX : /* */)
        self.lesCommentaires = set()
        ##Conteneur de tous les TypesQualificateurs (EX : const)
        self.lesTypesQualificateurs = set()
        ##Conteneur de tous les SizedTypeSpecificateurs (EX : unsigned int)
        self.lesSizedTypeSpecificateurs=set()
        ##Conteneur de tous les Types (EX : int)
        self.lesTypes = set()
        ##Conteneur de tous les Identificateurs (EX : Nom d'une variable)
        self.lesIdentificateurs = set()
        ##Conteneur de toutes les Déclarations (EX : int toto)
        self.lesDeclarations = set()
        ##Conteneur de toutes les Affectations (EX : toto = toto + 1)
        self.lesAffectations = set()
        ##Conteneur de toutes les Expressions (EX : cout << endl)
        self.lesExpressions = set()
        ##Conteneur de toutes les Instructions Break (EX : break;)
        self.lesInstructionsBreak=set()
        ##Conteneur de toutes les Instructions Return (EX : return ();)
        self.lesInstructionsReturn=set()
        ##Conteneur de toutes les Expressions Parenthesées (EX : i <= "(nbCases - 2)")
        self.lesExpressionsParenthesees = set()
        ##Conteneur de toutes les Expressions Unaires (EX : (!estTriee))
        self.lesExpressionsUnaires = set()
        ##Conteneur de toutes les Expressions Binaires (EX : (compteur < 20))
        self.lesExpressionsBinaires = set()
        ##Conteneur de toutes les Expressions Binaires Simples
        self.lesExpressionsBinairesSimples = set()
        ##Conteneur de toutes les Expressions Binaires Composées
        self.lesExpressionsBinairesComposees = set()
        ##Conteneur de tous les Litéraux (EX : 3)
        self.lesLiteral = set()
        ##Conteneur de toutes les Expressions Update (EX : i++)
        self.lesExpressionsUpdate = set()
        ##Conteneur de toutes les Entrées (EX : toto = "titi + 1")
        self.lesEntrees = set()
        ##Conteneur de toutes les Sorties (EX : "toto" = titi + 1)
        self.lesSorties = set()
        ##Conteneur de toutes les Boucles While (EX : while())
        self.lesBouclesWhile = set()
        ##Conteneur de toutes les Boucles DoWhile (EX : do{} while())
        self.lesBouclesDoWhile = set()
        ##Conteneur de toutes les Boucles For (EX : for( ; ; ))
        self.lesBouclesFor = set()
        ##Conteneur de toutes les Boucles avec un nombre de répétition connu (EX : for( ; ; ))
        self.lesBouclesNbRepConnu = set()
        ##Conteneur de toutes les Boucles avec un nombre de répétition inconnu (EX : while(), dowhile())
        self.lesBouclesNbRepNonConnu = set()
        ##Conteneur de toutes les Boucles (EX : for( ; ; ), while())
        self.lesBoucles = set()
        ##Conteneur de toutes les Conditions If (EX : if())
        self.lesConditionsIf = set()
        ##Conteneur de tous les Switchs (EX : switch())
        self.lesSwitchs = set()
        ##Conteneur de toutes les Conditions (EX : (!estTriee))
        self.lesFonctions = set()
        ##Conteneur de tous les Sous-Programmes (EX : function())
        self.lesSousProgrammes = set()
        ##Conteneur de toutes les Structures Conditionelles If (EX : if() { })
        self.lesStructuresConditionelles = set()
        
        
        #ici References pour récuperer des infos sur les noeuds
        ##Conteneur de tous les Noeuds
        self.lesNoeuds = Noeud.mondictCles
        ##Conteneur de toutes les Clés
        self.lesCles = Noeud.lesCles