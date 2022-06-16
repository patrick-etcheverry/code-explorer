from src.api.BoucleNbRepConnu import BoucleNbRepConnu
from src.api.ExpressionUpdate import ExpressionUpdate
from src.api.Affectation import Affectation

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

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
            logger.debug("!!!!!!! Pb sur BoucleFor: Bloc inexistant pour init")
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
            logger.debug("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur condition")
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
            logger.debug("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur pas")
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
            logger.debug("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur bloctrt")        
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

