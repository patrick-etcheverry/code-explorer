from src.api.BlocSimple import BlocSimple


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
  


    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getInstructionsBreak()[2].getType() \n \n
    #Résultat possible : \n \n
    #'InstructionBreak'
    def getType(self):
        return self.getTypeBloc()