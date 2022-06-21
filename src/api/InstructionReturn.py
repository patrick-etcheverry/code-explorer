from src.api.BlocSimple import BlocSimple

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
        


    ##
    #@fn getType()
    #@brief Retourne le type du Bloc en se basant sur le nom des classes. \n
    #Exemple d'utilisation : p.getInstructionsReturn()[2].getType() \n \n
    #Résultat possible : \n \n
    #'InstructionReturn'
    def getType(self):
        return self.getTypeBloc()