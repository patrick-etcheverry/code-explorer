from src.api.StructureConditionnelle import StructureConditionnelle



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
