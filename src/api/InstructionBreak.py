from src.api.BlocSimple import BlocSimple



##@brief Classe héritant de BlocSimple, elle contient toutes InstructionBreak d'un code.
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
  


