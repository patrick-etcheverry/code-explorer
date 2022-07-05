from cmath import e
from platform import node
from tree_sitter import Language, Parser
from src.api.ConditionArret import ConditionArret
from src.api.Parametre import Parametre
from src.api.Procedure import Procedure
from src.api.SousProgramme import SousProgramme
from src.api.Noeud import Noeud
from src.api.Commentaire import Commentaire
from src.api.Type import Type
from src.api.Literal import Literal
from src.api.TypeQualificateur import TypeQualificateur
from src.api.StructureFor import StructureFor
from src.api.Affectation import Affectation
from src.api.StructureWhile import StructureWhile
from src.api.StructureDoWhile import StructureDoWhile
from src.api.StructureIf import StructureIf
from src.api.Declaration import Declaration
from src.api.Expression import Expression
from src.api.ExpressionBinaire import ExpressionBinaire
from src.api.ExpressionParenthesee import ExpressionParenthesee
from src.api.ExpressionUnaire import ExpressionUnaire
from src.api.ExpressionUpdate import ExpressionUpdate
from src.api.Function import Function
from src.api.InstructionBreak import InstructionBreak
from src.api.InstructionReturn import InstructionReturn
from src.api.SizedTypeSpecificateur import SizedTypeSpecificateur
from src.api.Identificateur import Identificateur
from src.api.BlocCompose import BlocCompose
from src.api.StructureSwitch import StructureSwitch
from src.api.Condition import Condition
from src.api.ConditionContinuation import ConditionContinuation
from src.api.ConditionIf import ConditionIf
from src.api.ConditionSwitch import ConditionSwitch
from src.api.Programme import Programme



#from src.api.Programme import Programme
import logging

# Gets or creates a logger
logger = logging.getLogger(__name__) 












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
        lenode_identifiant=lenode.children[0].children[0]
        obj.setIdentificateur(lenode_identifiant)





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


    def _creeObjet_SousProgramme(lenode, prog):
        obj=SousProgramme(lenode, prog)
        lenode_type=lenode.children[0]
        obj.setType(lenode_type)

        lenode_identifier=lenode.children[1].children[0]
        obj.setIdentificateur(lenode_identifier)

        obj.setParametres(None)

        lenode_trt=lenode.children[2]
        obj.setBlocTrt(lenode_trt)
        

         

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
        obj=Declaration(lenode, prog)
        #Attention il y a le cas ou on a une initialisation ou pas ///
        #L'objet etant créée, on peut maintenant créer les 
        if lenode.children[0].type=="type_qualifier":
            rang=1
        else:
            rang=0

        lenode_type=lenode.children[rang]
        obj.setType(lenode_type)

        if lenode.children[rang+1].type=="init_declarator":
            #on recupere l'identificateur dans le declarateur
            lenode_identificateur=lenode.children[rang+1].children[0]
            obj.setIdentificateur(lenode_identificateur)
            #on recupere la valeur de l'expression
            lenode_valeurExpression=lenode.children[rang+1].children[2]
            obj.setValeurExpression(lenode_valeurExpression) 
        elif lenode.children[1].type=="function_declarator":
            lenode_identificateur=lenode.children[1].children[0]
            obj.setIdentificateur(lenode_identificateur)

        else:
            #on recupere l'identificateur dans le declarateur
            lenode_identificateur=lenode.children[rang+1]
            obj.setIdentificateur(lenode_identificateur)
            #il n'y a pas de valeur d'expression
            obj.setValeurExpression(None)

            
        #lenode_declaration=lenode.children[3]
        #d.setDeclaration(lenode_declaration)

        
    def _creeObjet_BlocCompose(lenode, prog):
        obj=BlocCompose(lenode, prog)





    def _creeObjet_StructureFor(lenode, prog):
        obj=StructureFor(lenode, prog)
        
        if len(lenode.children) > 6:

            lenoeud_init=lenode.children[2]
            obj.setInit(lenoeud_init)
            if lenode.children[2].type=="assignment_expression":
                #il n'y a pas de déclaration de type

                lenoeud_bloctrt=lenode.children[8]
                obj.setBlocTrt(lenoeud_bloctrt)

                lenoeud_condition=lenode.children[4]
                ConditionContinuation(lenoeud_condition, prog)
                obj.setConditionContinuation(lenoeud_condition)

                obj.setConditionsArret(None)

                lenoeud_pas=lenode.children[6]
                obj.setPas(lenoeud_pas)



            else:
                #il y a une déclaration de type 
                lenoeud_bloctrt=lenode.children[7]
                obj.setBlocTrt(lenoeud_bloctrt)

                lenoeud_condition=lenode.children[3]
                ConditionContinuation(lenoeud_condition, prog)
                obj.setConditionContinuation(lenoeud_condition)

                obj.setConditionsArret(None)

                lenoeud_pas=lenode.children[5]
                obj.setPas(lenoeud_pas)




        else:
            obj.setInit(None)
            obj.setConditionContinuation(None)
            obj.setBlocTrt(lenode.children[5])
            obj.setPas(None)
            obj.setConditionsArret(None)


    



    def _creeObjet_StructureIf(lenode, prog):
        obj=StructureIf(lenode, prog)
        
        lenoeud_condition=lenode.children[1].children[1]
        ConditionIf(lenoeud_condition, prog)
        obj.setCondition(lenoeud_condition)

        lenoeud_then=lenode.children[2]
        obj.setBlocAlors(lenoeud_then)
        
        if len(lenode.children)==5:
            lenoeud_else=lenode.children[4]
            obj.setBlocSinon(lenoeud_else)
        else:
            obj.setBlocSinon(None)

    
    def _creeObjet_StructureSwitch(lenode, prog):
        obj=StructureSwitch(lenode, prog)
        
        lenoeud_condition=lenode.children[1].children[1]
        ConditionSwitch(lenoeud_condition, prog)
        obj.setCondition(lenoeud_condition)

        lenoeud_corps=lenode.children[2]
        obj.setBlocTrt(lenoeud_corps)
        
        lenoeud_case=lenode.children[2].children[1]
        obj.setCase(lenoeud_case)




    def _creeObjet_StructureWhile(lenode, prog):
        obj=StructureWhile(lenode, prog)

        lenoeud_bloctrt=lenode.children[2]
        obj.setBlocTrt(lenoeud_bloctrt)

        lenoeud_condition=lenode.children[1].children[1]
        ConditionContinuation(lenoeud_condition, prog)
        obj.setConditionContinuation(lenoeud_condition)

        obj.setConditionsArret(None)




    def _creeObjet_StructureDoWhile(lenode, prog):
        obj=StructureDoWhile(lenode, prog)
        
        lenoeud_bloctrt=lenode.children[1]
        obj.setBlocTrt(lenoeud_bloctrt)

        lenoeud_condition=lenode.children[3].children[1]
        ConditionContinuation(lenoeud_condition, prog) 
        obj.setConditionContinuation(lenoeud_condition)

        obj.setConditionsArret(None)


        
    def _creeObjet_Parametre(lenode, prog):
        obj=Parametre(lenode, prog)
        if lenode.child_count == 1:
            lenoeud_type=lenode.children[0]
            obj.setType(lenoeud_type)
            obj.setIdentificateur(None)
        else:
            lenoeud_type=lenode.children[0]
            obj.setType(lenoeud_type)
            lenoeud_identifiant=lenode.children[1]
            obj.setIdentificateur(lenoeud_identifiant)

        




    def _creeContenus_bloc_compose(prog):
        for bloc_compose in prog.lesBlocsComposes:
            lenoeud=bloc_compose.noeud
            for node in lenoeud.node.children:
                    lebloc= prog.cherche(node) 
                    if not lebloc==None:
                        bloc_compose.lesBlocs.append(lebloc)
                        #lebloc.dansbloc=bloc_compose
                    else:
                        pass
                        logger.debug("!!!!!!! Bloc inexistant dans BlocCompose"+str(node))    




    def _creeElement(node):
        if node.type=="comment":
            _creeObjet_Commentaire(node, prog) 
        elif node.type=="compound_statement":
            _creeObjet_BlocCompose(node, prog)
        elif node.type in {"true", "false", "string_literal", "number_literal"}:
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
        elif node.type=="return_statement":
            _creeObjet_InstructionReturn(node, prog)
        elif node.type=="binary_expression":
            _creeObjet_ExpressionBinaire(node, prog)
        elif node.type=="parenthesized_expression":
            _creeObjet_ExpressionParenthesee(node, prog)
        elif node.type=="update_expression":
            _creeObjet_UpdateExpression(node, prog)  
        elif node.type=="function_definition":
            _creeObjet_SousProgramme(node, prog)  
        elif node.type=="assignment_expression":
            _creeObjet_Affectation(node, prog)
        elif node.type in {"declaration", "array_declarator"}:
            _creeObjet_Declaration(node, prog)
        elif node.type=="for_statement":
            _creeObjet_StructureFor(node, prog)
        elif node.type=="if_statement":
            _creeObjet_StructureIf(node, prog)
        elif node.type=="switch_statement":
            _creeObjet_StructureSwitch(node, prog)
        elif node.type=="while_statement":
            _creeObjet_StructureWhile(node, prog)
        elif node.type=="do_statement":
            _creeObjet_StructureDoWhile(node, prog)
        elif node.type=="parameter_declaration":
            _creeObjet_Parametre(node, prog)
        else:
            pass
            logger.debug("element non categorisé : "+ str(node))

        
      
    traverse(prog.TreeNode, False, _creeElement,[])
    _creeContenus_bloc_compose(prog)
    _creeParents_allblocs(prog)
    _creeAllConditionsArretBoucles(prog)
    _creeObjet_Fonction(prog)
    _detection_Declaration(prog)
    _detection_Appel(prog)
    _detection_parametres(prog)

    








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



def _creeParents_allblocs(prog):
    allBlocs = prog.lesBlocs

    for leBloc in allBlocs:
        nodeParent = leBloc.noeud.node.parent

        
        try:
            #deplace ici pour le cas ou le nodeParent n'existe pas (cf. objet Programme) 
            cleParent = Noeud.get_laCle(nodeParent)
            
            noeudParent = prog.mondictCles[cleParent]  
            blocParent = noeudParent.bloc
            leBloc.blocParent = blocParent
        except:
            leBloc.blocParent = None

def _creeAllConditionsArretBoucles(prog):
    for b in prog.getStructuresIteratives():
        #Result : parent d'un potentiel break
        result=_detection_break(b, prog)
        if result is not None:
            for uneCondition in result:
                ConditionArret(uneCondition, prog)    
            b.setConditionsArret(result)
        




def _detection_break(blocBoucle, prog):
    lenode=blocBoucle.getBlocTrt().noeud.node
    query = prog.LANGUAGE.query("""
    (break_statement) @Break
    """
    )

    nodeParent = []
    captures = query.captures(lenode)
    
    if len(captures) != 0:

        for nodeBreak in captures:
            cle = Noeud.get_laCle(nodeBreak[0])
            noeud = prog.mondictCles[cle]  
            bloc = noeud.bloc

            try:
                blocParent = bloc.blocParent
                

                if blocParent.getType() in {"StructureFor", "StructureWhile", "StructureDoWhile", "StructureIf"}:
                    nodeParent.append(blocParent.noeud.node)
                else:
                    blocParentDuParent = blocParent.blocParent
                    nodeParent.append(blocParentDuParent.noeud.node)

            except:
                nodeParent = None

        return nodeParent
    else:
        return None


def _detection_Declaration(prog):
    
    for leSousProgramme in prog.lesSousProgrammes:
        estSet = False
        for laDeclaration in prog.lesDeclarations:
            try:
                if leSousProgramme.getIdentificateur().getValeur() == laDeclaration.getIdentificateur().getValeur():
                    leSousProgramme.setDeclaration(laDeclaration.noeud.node)
                    estSet = True
            except:
                if estSet == True:
                    break
                else:
                    leSousProgramme.setDeclaration(None)



def _detection_Appel(prog):
    
    for leSousProgramme in prog.lesSousProgrammes:
        estSet = False
        lesAppels = []
        for lAppel in prog.lesExpressions:
            try:
                if leSousProgramme.getIdentificateur().getValeur() == lAppel.getIdentificateur().getValeur():
                    lesAppels.append(lAppel.noeud.node)
                    estSet = True
            except:
                if estSet == True:
                    break
                else:
                    leSousProgramme.setAppel(None)

        leSousProgramme.setAppel(lesAppels)


def _creeObjet_Fonction(prog):
    compteur = 0
    nbSousProgramme = len(prog.lesSousProgrammes)
    for leSousProgramme in prog.lesSousProgrammes:
        if compteur == nbSousProgramme:
            break
        else:
            lenode = leSousProgramme.noeud.node
            if leSousProgramme.getType().getValeur() == "void":
                obj=Procedure(lenode, prog)
                obj.setType(leSousProgramme.type["node"])
                obj.setIdentificateur(leSousProgramme.nom["node"])
                obj.setParametres(None)
                obj.setBlocTrt(leSousProgramme.bloctrt["node"])
                del prog.lesSousProgrammes[compteur]
            else:
                obj=Function(lenode, prog)
                obj.setType(leSousProgramme.type["node"])
                obj.setIdentificateur(leSousProgramme.nom["node"])
                obj.setParametres(None)
                obj.setBlocTrt(leSousProgramme.bloctrt["node"])
                del prog.lesSousProgrammes[compteur]
        compteur = compteur + 1
    


def _detection_parametres(prog):
    for leSousProgramme in prog.lesSousProgrammes:
        laListeParametre = []            
        lenode = leSousProgramme.noeud.node
        lesParametres = lenode.children[1].children[1].children

        for unParametre in lesParametres:
            if unParametre.type == "parameter_declaration":
                laListeParametre.append(unParametre)
        leSousProgramme.setParametres(laListeParametre)
        




#setattr(Programme, "creeObjets", creeObjets) #permet de traiter cette fonction comme une mathode de la classe Programme
