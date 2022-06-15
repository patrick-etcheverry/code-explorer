from src.api.BlocSimple import BlocSimple


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

