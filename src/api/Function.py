from src.api.SousProgramme import SousProgramme

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 

##@class Function(SousProgramme)
#@brief Classe héritant de SousProgramme, elle contient tous les objets Function d'un code, par exemple : "int function()".
class Function(SousProgramme):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Function.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesFonctions.append(self)


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
    #@fn setIdentificateur(node)
    #@brief Défini le noeud en tant qu'Identificateur.
    #@param lenodeTreeSitter : Correspond à un objet Noeud
    def setIdentificateur(self, node):
        self.nom = {}
        
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.nom["bloc"] = leBloc
        else:
            pass
            logger.debug("!!!!!!! Bloc inexistant pour Identificateur")
        self.nom["node"] = node
        #self.type["text"]=recupereTexteDansSource(self.prog.codeSource, nodeNom)


    ##
    #@fn getIdentificateur()
    #@brief Retourne tous les Noms de Fonction sous forme d'une structure de données.
    def getIdentificateur(self):
        return self.nom["bloc"]



    ##
    #@fn setListParametres(node)
    #@brief Défini le noeud en tant que liste de parametres.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setListParametres(self, node):
        self.parametres = {}
        leBloc = self.prog.cherche(node)
        if not leBloc == None:
            self.parametres["bloc"] = leBloc
        else:
            pass
            logger.debug("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur parametres")        
        self.parametres["node"] = node
        #self.bloctrt["text"] = recupereTexteDansSource(self.prog.codeSource, node)   
    
    ##
    #@fn getListParametres()
    #@brief Retourne tous les liste de parametres sous forme d'une structure de données.
    #Exemple d'utilisation : p.getFunction[0].getListParametres().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle For du programme
    #\n\n Résultat potentiel : { int i = 0; } \n
    #@warning La récupération des paramètres n'est pas encore fonctionnelle.
    def getListParametres(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.parametres["node"])
        return self.parametres["bloc"]


    
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
    #Exemple d'utilisation : p.getFunction[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Première Boucle For du programme
    #\n\n Résultat potentiel : { int i = 0; }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]


    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getFunction()[2].getType() \n \n
    #Résultat possible : \n \n
    #'Function', 'BlocCompose'
    def getType(self):
        return self.getTypeBloc()