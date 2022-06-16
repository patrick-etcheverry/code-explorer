from src.api.BlocSimple import BlocSimple

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

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
            logger.debug("!!!!!!! Bloc inexistant pour type")
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
            logger.debug("!!!!!!! Bloc inexistant pour identificateur")
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
                logger.debug("!!!!!!! Bloc inexistant pour setvaleurexpression")
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
            logger.debug("!!!!!!! Bloc inexistant pour setDeclaration")
        self.declaration["node"] = node


    ##
    #@fn getDeclaration()
    #@brief Retourne toutes les Declarations sous forme d'une structure de données.
    def getDeclaration(self):
        return self.declaration["bloc"]
  