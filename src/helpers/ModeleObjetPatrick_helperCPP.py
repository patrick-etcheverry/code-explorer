from tree_sitter import Language, Parser
from src.api.Commentaire import Commentaire
from src.api.Type import Type
from src.api.Literal import Literal
from src.api.TypeQualificateur import TypeQualificateur
from src.api.BoucleFor import BoucleFor
from src.api.Affectation import Affectation
from src.api.BoucleWhile import BoucleWhile
from src.api.BoucleDoWhile import BoucleDoWhile
from src.api.ConditionIf import ConditionIf
from src.api.Declaration import Declaration
from src.api.Expression import Expression
from src.api.ExpressionBinaire import ExpressionBinaire
from src.api.ExpressionParenthesee import ExpressionParenthesee
from src.api.ExpressionUnaire import ExpressionUnaire
from src.api.ExpressionUpdate import ExpressionUpdate
from src.api.Function import Function
from src.api.InstructionBreak import InstructionBreak
from src.api.InstructionReturn import InstructionReturn
from src.api.SizeTypedSpecificateur import SizedTypeSpecificateur
from src.api.Identificateur import Identificateur
from src.api.BlocCompose import BlocCompose
from src.api.Switch import Switch
<<<<<<< Updated upstream

#from src.api.Programme import Programme


import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 












=======
>>>>>>> Stashed changes
from src.api.tree_sitter_utilities import traverse, extraireByType, extraireByName, cherche, cherchev2, creeObjetsBlocs, recupereNoeud, recupereTexteDansSource
#un objet Noeud encapsule un Node de Tree-sitter 

    #Comme ce sont de simples objets, on se sert de l'arbre TreeSitter et pas des requetes

def creeObjets(prog):
    def _creeObjet_Commentaire(lenode, prog):
        d=Commentaire(lenode, prog)

    def _creeObjet_Literal(lenode, prog):
        d=Literal(lenode, prog)

    def _creeObjet_TypeQualificateur(lenode, prog):
        o=TypeQualificateur(lenode, prog)

    def _creeObjet_SizedTypeSpecificateur(lenode, prog):
        o=SizedTypeSpecificateur(lenode, prog)

    def _creeObjet_Type(lenode, prog):
        if lenode.parent is not None:
            #if node.parent.child_by_field_name(eltaextraire)==node:
                #on traite l'element
            o=Type(lenode, prog)
    
    def _creeObjet_Identificateur(lenode, prog):
        obj=Identificateur(lenode, prog)

    def _creeObjet_Expression(lenode, prog):
        obj=Expression(lenode, prog)
        lenode_expression=lenode.children[0]
        obj.setExpression(lenode_expression)

    def _creeObjet_InstructionBreak(lenode, prog):
        obj=InstructionBreak(lenode, prog)
        
    def _creeObjet_InstructionReturn(lenode, prog):
        obj=InstructionReturn(lenode, prog)
    
    
    def _creeObjet_ExpressionUnaire(lenode, prog):
        obj=ExpressionUnaire(lenode, prog)  #creation de l'objet
        lenode_operateur=lenode.children[0]
        obj.setOperateur(lenode_operateur)  #creation de l'operateur
        lenode_argument=lenode.children[1]
        obj.setArgument(lenode_argument)  #creation de l'argument (=une expression)


    def _creeObjet_ExpressionBinaire(lenode, prog):
        obj=ExpressionBinaire(lenode, prog)
        lenode_gauche=lenode.children[0]
        obj.setGauche(lenode_gauche)
        obj.setOperateur(lenode.children[1])
        lenode_droit=lenode.children[2]
        obj.setDroite(lenode_droit)
    
    def _creeObjet_ExpressionParenthesee(lenode, prog):
        obj=ExpressionParenthesee(lenode, prog)
        lenode_parenthesee=lenode.children[1]
        obj.setExpression(lenode_parenthesee)
       
    
    def _creeObjet_UpdateExpression(lenode, prog):
        obj=ExpressionUpdate(lenode, prog)
        lenode_identifier=lenode.children[0]
        obj.setIdentificateur(lenode_identifier)
        lenode_operateur=lenode.children[1]
        obj.setOperateur(lenode_operateur)
        #A faire
        #noeud=None  #A modifier
        #d.setOperateur(noeud)


    def _creeObjet_Function(lenode, prog):
        obj=Function(lenode, prog)
        lenode_operateur=lenode.children[0]
        obj.setType(lenode_operateur)
        lenode_identifier=lenode.children[1].children[0]
        obj.setIdentificateur(lenode_identifier)
        if not lenode.children[1].children[1].children[1] == None:
            lenode_operateur=lenode.children[1].children[1].children[1]
            obj.setListParametres(lenode_operateur)
        lenode_operateur=lenode.children[2]
        obj.setBlocTrt(lenode_operateur)
        
         

    def _creeObjet_Affectation(lenode, prog):
        obj=Affectation(lenode, prog)
        node_identificateur=lenode.children[0]
        obj.setIdentificateur(node_identificateur)

        node_expression=lenode.children[2]
        obj.setExpression(node_expression)

        lenode_operateur=lenode.children[1]
        obj.setOperateur(lenode_operateur)
    

        #noeud=recupereNoeud(elem, listebalises[0])
        #obj.setType(noeud)

        #noeud=recupereNoeud(elem, listebalises[1])
        #d.setIdentificateur(noeud)

    def _creeObjet_Declaration(lenode, prog):
        d=Declaration(lenode, prog)
        #attention il y a le cas ou on a une initialisation ou pas ///
        #           #L'objet etant créée, on peut maintenant créer les 
        
        if lenode.children[0].type=="type_qualifier":
            rang=1
        else:
            rang=0

        lenode_type=lenode.children[rang]
        d.setType(lenode_type)

        if lenode.children[rang+1].type=="init_declarator":
            #on recupere l'identificateur dans le declarateur
            lenode_identificateur=lenode.children[rang+1].children[0]
            d.setIdentificateur(lenode_identificateur)
            #on recupere la valeur de l'expression
            lenode_valeurExpression=lenode.children[rang+1].children[2]
            d.setValeurExpression(lenode_valeurExpression) 
        else:
            #on recupere l'identificateur dans le declarateur
            lenode_identificateur=lenode.children[rang+1]
            d.setIdentificateur(lenode_identificateur)
            #il n'y a pas de valeur d'expression
            d.setValeurExpression(None)

            
        #lenode_declaration=lenode.children[3]
        #d.setDeclaration(lenode_declaration)

        
    def _creeObjet_BlocCompose(lenode, prog):
        obj=BlocCompose(lenode, prog)


    def _creeObjet_BoucleFor(lenode, prog):
        obj=BoucleFor(lenode, prog)
        
        lenoeud_init=lenode.children[2]
        obj.setInit(lenoeud_init)
        if lenode.children[2].type=="assignment_expression":
            #il n'y a pas de déclaration de type
            lenoeud_condition=lenode.children[4]
            obj.setCondition(lenoeud_condition)

            lenoeud_pas=lenode.children[6]
            obj.setPas(lenoeud_pas)

            lenoeud_bloctrt=lenode.children[8]
            obj.setBlocTrt(lenoeud_bloctrt)

        else:
            #il y a une déclaration de type 
            lenoeud_condition=lenode.children[3]
            obj.setCondition(lenoeud_condition)
        
            lenoeud_pas=lenode.children[5]
            obj.setPas(lenoeud_pas)

            lenoeud_bloctrt=lenode.children[7]
            obj.setBlocTrt(lenoeud_bloctrt)


    def _creeObjet_InstructionIf(lenode, prog):
        obj=ConditionIf(lenode, prog)
        
        lenoeud_condition=lenode.children[1].children[1]
        obj.setCondition(lenoeud_condition)

        lenoeud_then=lenode.children[2]
        obj.setBlocAlors(lenoeud_then)
        
        if len(lenode.children)==5:
            lenoeud_else=lenode.children[4]
            obj.setBlocSinon(lenoeud_else)
        else:
            obj.setBlocSinon(None)

    
    def _creeObjet_Switch(lenode, prog):
        obj=Switch(lenode, prog)
        
        lenoeud_condition=lenode.children[1].children[1]
        obj.setCondition(lenoeud_condition)

        lenoeud_corps=lenode.children[2]
        obj.setBlocTrt(lenoeud_corps)
        
        lenoeud_case=lenode.children[2].children[1]
        obj.setCase(lenoeud_case)


    def _creeObjet_BoucleWhile(lenode, prog):
        obj=BoucleWhile(lenode, prog)
        
        lenoeud_condition=lenode.children[1].children[1]
        obj.setCondition(lenoeud_condition)

        lenoeud_then=lenode.children[2]
        obj.setBlocTrt(lenoeud_then)

    def _creeObjet_BoucleDoWhile(lenode, prog):
        obj=BoucleDoWhile(lenode, prog)
        
        lenoeud_then=lenode.children[1]
        obj.setBlocTrt(lenoeud_then)

        lenoeud_condition=lenode.children[3].children[1]
        obj.setCondition(lenoeud_condition)


    def _creeContenus_bloc_compose(prog):
        for bloc_compose in prog.lesBlocsComposes:
            lenoeud=bloc_compose.noeud
            for node in lenoeud.node.children:
                    lebloc= prog.cherche(node) 
                    if not lebloc==None:
                        bloc_compose.lesBlocs.append(lebloc)
                    else:
                        pass
                        logger.debug("!!!!!!! Bloc inexistant dans BlocCompose"+str(node))    



    def _creeElement(node):
        if node.type=="comment":
            _creeObjet_Commentaire(node, prog) 
        elif node.type in {"true, false", "string_literal", "number_literal"}:
            _creeObjet_Literal(node, prog)
        elif node.type =="type_qualifier":
            _creeObjet_TypeQualificateur(node, prog)
        elif node.type =="primitive_type":
            _creeObjet_Type(node, prog)
        elif node.type =="sized_type_specifier":
            _creeObjet_SizedTypeSpecificateur(node, prog)
        elif node.type=="identifier":
            _creeObjet_Identificateur(node, prog)
        elif node.type=="expression_statement":
            _creeObjet_Expression(node, prog)
        elif node.type=="unary_expression":
            _creeObjet_ExpressionUnaire(node, prog)
        elif node.type=="break_statement":
            _creeObjet_InstructionBreak(node, prog)
        elif node.type=="binary_expression":
            _creeObjet_ExpressionBinaire(node, prog)
        elif node.type=="parenthesized_expression":
            _creeObjet_ExpressionParenthesee(node, prog)
        elif node.type=="update_expression":
            _creeObjet_UpdateExpression(node, prog)  
        elif node.type=="function_definition":
            _creeObjet_Function(node, prog)  
        elif node.type=="assignment_expression":
            _creeObjet_Affectation(node, prog)
        elif node.type=="declaration":
            _creeObjet_Declaration(node, prog)
        elif node.type=="compound_statement":
            _creeObjet_BlocCompose(node, prog)
        elif node.type=="for_statement":
            _creeObjet_BoucleFor(node, prog)
        elif node.type=="if_statement":
            _creeObjet_InstructionIf(node, prog)
        elif node.type=="switch_statement":
            _creeObjet_Switch(node, prog)
        elif node.type=="while_statement":
            _creeObjet_BoucleWhile(node, prog)
        elif node.type=="do_statement":
            _creeObjet_BoucleDoWhile(node, prog)
        else:
            pass
            logger.debug("element non categorisé : "+ str(node))

      
    traverse(prog.TreeNode, False, _creeElement,[])
    _creeContenus_bloc_compose(prog)







def _creeObjets_affectation(self):

        listebalises=["left", "right", "affectation"]
        
        #On cherche grâce au query simplifié qui est complété avec les balises nommées
        txtquery="""
        (
	    assignment_expression
    	    left:(identifier) @
		    right:(_) @
        )@
        """
        elements=cherche(self.language, self.TreeNode, self.codeSource, txtquery, listebalises)

        #on parcourt la liste des elements pour créer les objets du modèle de Patrick
        for elem in elements:
            #on recupère l'element qui nous interesse pour construire l'objet du programme de Patrick
            lenoeud=recupereNoeud(elem, listebalises[2])
            d=Affectation(lenoeud, self)

            #L'objet etant créée, on peut maintenant créer les 
            noeud=recupereNoeud(elem, listebalises[0])
            d.setIdentificateur(noeud)

            noeud=recupereNoeud(elem, listebalises[1])
            d.setExpression(noeud)
    




def _creeObjets_bloc_compose(prog):
    def creerObjetBloc_Compose(node, eltaextraire):
        if node.type==eltaextraire:
            #on traite l'element
            o=BlocCompose(node, prog)
    
    traverse(prog.TreeNode, True, creerObjetBloc_Compose,["compound_statement"])

def _creeListes_bloc_compose(prog):
    for bloc_compose in prog.lesBlocsComposes:
         lenoeud=bloc_compose.noeud
         for node in lenoeud.node.children:
                lebloc= prog.cherche(node) 
                if not lebloc==None:
                    bloc_compose.lesBlocs.append(lebloc)
                else:
                    pass
                    logger.debug("!!!!!!! Bloc inexistant pour BlocCompose"+str(node))



#setattr(Programme, "creeObjets", creeObjets) #permet de traiter cette fonction comme une mathode de la classe Programme
