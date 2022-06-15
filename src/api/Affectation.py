from src.api.BlocSimple import BlocSimple


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

