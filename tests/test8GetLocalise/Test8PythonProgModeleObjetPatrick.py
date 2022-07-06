import os
import sys
sys.path.append(os.getcwd())
from src.api.Programme import Programme

# TEST SUR LES PARAMETRES


p = Programme("tests/test8GetLocalise/essai.cpp")




print("---------------------------------")
print(p.getSousProgrammeAt(1).getStructuresIteratives())
print("---------------------------------")


print(p.getSousProgrammeAt(1).getStructureIterativeAt(1).getStructureIfAt(0).getCondition())


print("---------------------------------")
print(p.getSousProgrammeAt(1).getStructureIterativeAt(10))








