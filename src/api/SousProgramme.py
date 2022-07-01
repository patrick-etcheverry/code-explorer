from src.api.BlocSimple import BlocSimple

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 


##@brief Classe héritant de BlocSimple, elle contient tous les objets SousProgramme d'un code.         
class SousProgramme(BlocSimple):

    ##
    #@fn __init__(lenodeTreeSitter,  progObjetPatrick)
    #@brief Constructeur de la classe Sous_Programme.
    #@param lenodeTreeSitter : Correspond à un Node de Tree-Sitter
    #@param progObjetPatrick : Objet instancié de la classe "Programme"
    def __init__(self, lenodeTreeSitter, progObjetPatrick):
        super().__init__(lenodeTreeSitter, progObjetPatrick)
        progObjetPatrick.lesSousProgrammes.append(self)


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
    #@brief Retourne tous les Noms de Sous-Programmes sous forme d'une structure de données.
    def getIdentificateur(self):
        return self.nom["bloc"]



    ##
    #@fn setParametres(node)
    #@brief Défini le noeud en tant que liste de parametres.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setParametres(self, listNode):
        self.parametres = []
        if listNode==None:
                    self.parametres = False
        else:
            for node in listNode:
                leBloc = self.prog.cherche(node)
                if not leBloc == None:
                    self.parametres.append(leBloc)
                else:
                    pass
                    logger.debug("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur parametres")
            
    
    ##
    #@fn getParametres()
    #@brief Retourne tous les listes de parametres sous forme d'une structure de données.
    #Exemple d'utilisation : p.getSousProgrammes[0].getListParametres()[0].getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Premier Sous-Programme du code
    #\n\n Résultat potentiel : int compteur \n
    #@warning La récupération des paramètres n'est pas encore fonctionnelle.
    def getParametres(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.parametres["node"])
        return self.parametres


    
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
    #Exemple d'utilisation : p.getSousProgrammes[0].getBlocTrt().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Premier Sous-Programme du code
    #\n\n Résultat potentiel : { int i = 0; }
    def getBlocTrt(self):
        #return recupereTexteDansSource(self.prog.codeSource, self.bloctrt["node"])
        return self.bloctrt["bloc"]




    ##
    #@fn setDeclaration(node)
    #@brief Défini le noeud en tant que Déclaration de la fonction.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setDeclaration(self, node):
        self.declaration = {}

        if node==None:
            self.declaration["bloc"]=False
        else:
            lebloc=self.prog.cherche(node)
            if not lebloc==None:
                self.declaration["bloc"]=lebloc
            else:
                pass
                logger.debug("!!!!!!! Pb sur If: Bloc inexistant pour declaration dans Fonction")
        self.declaration["node"]=node



    
    ##
    #@fn getDeclaration()
    #@brief Retourne toutes les déclarations sous forme d'une structure de données.
    #Exemple d'utilisation : p.getSousProgrammes[0].getDeclaration().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Premier Sous-Programme du code
    #\n\n Résultat potentiel : int tri(Etudiant tab[], int nbCases);
    def getDeclaration(self):
        return self.declaration["bloc"]



    ##
    #@fn setAppel(node)
    #@brief Défini le noeud en tant qu'Appel de la fonction.
    #@param lenodeTreeSitter : Correspond à objet un Noeud
    def setAppel(self, listNode):
        self.appel = []
        if listNode==None:
                    self.appel = False
        else:
            for node in listNode:
                leBloc = self.prog.cherche(node)
                if not leBloc == None:
                    self.appel.append(leBloc)
                else:
                    pass
                    logger.debug("!!!!!!! Pb sur BoucleFor: Noeud inexistant sur appel")    
    
    ##
    #@fn getAppel()
    #@brief Retourne tous les Appels sous forme d'une structure de données.
    #Exemple d'utilisation : p.getSousProgrammes[0].getAppel().getValeur()\n
    #\n Avec :\n
    #- p = Objet Programme
    #- [0] = Premier Sous-Programme du code
    #\n\n Résultat potentiel : tri(etudiantsS1, EFFECTIF_S1);
    def getAppel(self):
        return self.appel