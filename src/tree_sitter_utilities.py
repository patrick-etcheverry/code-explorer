##
#@file tree_sitter_utilities.py
#Fichier contenant toutes les fonctions servant à la création du programme
#@author NODENOT Thierry
#@date 06/2022
#@version 0.0.1 Alpha
#

import copy
from xmlrpc.client import Boolean
from tree_sitter import TreeCursor




    
def RecupereObjetsExpressionBinaire(lenode):
    danslaliste=[]
    traverse(lenode, extraireTxt,["binary_expression", danslaliste])
    return danslaliste

def RecupereObjetsExpressionParenthesee(lenode):
    danslaliste=[]
    traverse(lenode, extraireTxt,["parenthesized_expression", danslaliste])
    return danslaliste

def RecupereObjetsExpressionUnaire(lenode):
    danslaliste=[]
    traverse(lenode, extraireTxt,["unary_expression", danslaliste])
    return danslaliste

def RecupereObjetsIdentificateur(lenode):
    danslaliste=[]
    traverse(lenode, extraireTxt,["identifier", danslaliste])
    return danslaliste


def RecupereObjetsBlocCompose(lenode):
    danslaliste=[]
    traverse(lenode, extraireTxt,["compound_statement", danslaliste])
    return danslaliste

'''
def RecupereObjetsAffectation(lenode):
    danslaliste=[]
    traverse(lenode, extraireTxt,["assignment_expression", danslaliste])
    return danslaliste

def RecupereObjetsDeclaration(lenode):
    danslaliste=[]
    traverse(lenode, extraireTxt,["declarator", danslaliste])
    return danslaliste          
'''




def _traversev0_recursif(cursor:TreeCursor, fonction,  args):
   
    fonction(cursor.node, *args)
    for ch in cursor.node.children:
        _traversev0_recursif(ch.walk(), fonction, args)
    

def traverse(noeud, fonction,  args): # args = arguments list : liste contenant le nom de l'élement et une liste qui contiendra les résultats
    _traversev0_recursif(noeud.walk(), fonction, args)




def _traverse_recursif(cursor:TreeCursor, preordre : Boolean, fonction,  args):
    if preordre is True:
        fonction(cursor.node, *args)
    for ch in cursor.node.children:
        _traverse_recursif(ch.walk(), preordre, fonction, args)
    if preordre is False:
        fonction(cursor.node, *args)

#selon que preordre vaut True ou False, le noeud pere est prélevé avant ou après ses fils
#chaque fois qu'un noeud est prélevé on lui applique la fonction et ses arguments 
def traverse(noeud, preordre : Boolean, fonction,  args):
    _traverse_recursif(noeud.walk(), preordre, fonction, args)

def extraireByType(node, eltaextraire, exact: Boolean, danslaliste):
    if exact is True:
        if node.type == eltaextraire:
            danslaliste.append(node)
    else:
        if eltaextraire in node.type:
            print(eltaextraire + " " + str(node.type))
            danslaliste.append(node)


def extraireByName(node, eltaextraire, exact: Boolean, danslaliste):
    if exact is True:
        if node.parent.child_by_field_name("eltaextraire") == node:
            danslaliste.append(node)
    else:
        if node.parent.child_by_field_name("eltaextraire") == node:
            print(eltaextraire + " " + str(node.type))
            danslaliste.append(node)  





def recupereNoeud(listeNoeuds, elemcherche):
    monresult = [r for r in listeNoeuds if r[1] == elemcherche]
    #attention monresult est une liste même s'il n'y a qu'un element
    return monresult[0][0]   


def extraireTxt(codesource, rowdeb, coldeb, rowfin, colfin):
    chaine = ""
    txtligne = codesource[rowdeb]
    #traitement première ligne 
    if rowdeb == rowfin:
        chaine = chaine+txtligne[coldeb:colfin]
    else:
        chaine = chaine+txtligne[coldeb:]
        for i in range(rowdeb+1,rowfin):
            chaine = chaine+codesource[i]
        #traitement dernière ligne
        txtligne = codesource[rowfin]
        chaine = chaine+txtligne[0:colfin]

    return chaine

def recupereTexteDansSource(codesource, node):
    x1 = node.start_point[0]
    y1 = node.start_point[1]
    x2 = node.end_point[0]
    y2 = node.end_point[1]
    return extraireTxt(codesource, x1, y1, x2, y2)


#Sur la base d'un query et donc d'une liste de noeuds rattachés au noeud pere, recherche l'element de ce type et en extrait le texte
def captureDansSource(codesource, node, kind):
    for child in node.children:
        if child.type == kind:
            #cursor = child.node.walk()
            x1 = child.start_point[0]
            y1 = child.start_point[1]
            x2 = child.end_point[0]
            y2 = child.end_point[1]
            return extraireTxt(codesource, x1, y1, x2, y2)
           
    

def formatCaptures(tree, codesource, resultcaptures):
    resultformate=[]
    for c in resultcaptures:
        t = {}
        node=c[0]
        t["startPositionrow"]=node.start_point[0]
        t["startPositioncolumn"]=node.start_point[1]
        t["endPositionrow"] = node.end_point[0]
        t["endPositioncolumn"]=node.end_point[1]
        t["noeud"]=node
        t["text"]=extraireTxt(codesource, t["startPositionrow"], t["startPositioncolumn"], t["endPositionrow"], t["endPositioncolumn"])
        resultformate.append(t)
    return resultformate
    
def filtrerTypeResult(unresultat, nom):
    if unresultat[1]==nom:
        return True
    else:
        return False


#Cette fonction permet de fabriquer correctement les différentes balises @....
def remplaceArrobasListe(chaine, liste):        
    #on cherche la position des @
    substr = "@"
    positions = [i for i in range(len(chaine)) if chaine.startswith(substr, i)]
    #on tronconne la chaine en caracteres
    laliste = list(chaine)
    #on modifie le texte aux positions de présence du @
    for i, pos in enumerate(positions):
        laliste[pos] = '@' + liste[i]
    return ''.join(laliste)
    
def creeObjetsBlocs(node, liste):
    leTypeNode = node[1]
    if leTypeNode == liste[len(liste) - 1]:
        #il faut recommencer avec les fils puisque l'objet trouvé est du même type que l'objet père
        pass
        creeObjetsBlocs(node.children[0], liste)
    else:
        pass

        


#cette méthode fabrique des listes de listes avec les critères de recherche donnés en entrée
def cherchev2(language, TreeNode, codeSource, txtquery, listecherchee):
    txtquerybalises = remplaceArrobasListe(txtquery, listecherchee)  
    query = language.query(txtquerybalises)
    uniqueresult = capturesUnique(TreeNode, query)
    return uniqueresult
    #monresult = [r for r in uniqueresult if r[1] == nom]


#Cette fonction elimine les doublons dans le cas où les résultats d'un query pointent de mêmes Node Treesitter    
def capturesUnique(tree, query):
    result=query.captures(tree)
    uniqueresults=[]
    for x in result:
        if x not in uniqueresults:
            uniqueresults.append(x)
    return uniqueresults


#cette méthode fabrique des listes de listes avec les critères de recherche donnés en entrée
def cherche(language, TreeNode, codeSource, txtquery, listecherchee):
    
    
    #Cette fonction fabrique les sous-listes de résultats
    def capturesBySousListes(tree, codesource, query, ensBalises): # C'est quoi ensBalises ?
        result = capturesUnique(tree, query)
        nb = len(ensBalises)
        matrice = []
        while result != []:
            matrice.append(result[:nb])
            result = result[nb:]
        return matrice

    txtquerybalises = remplaceArrobasListe(txtquery, listecherchee)  
    query = language.query(txtquerybalises)


    result_declarations=capturesBySousListes(TreeNode, codeSource, query, listecherchee)
    return result_declarations    
        



#Cette méthode permet de requetes puis de filtrer les résultats d'une capture sur un critère donné
def capturesByName(tree, codesource, query, nom):
    #result=query.captures(tree.root_node)
    uniqueresult = capturesUnique(tree, query)
    monresult = [r for r in uniqueresult if r[1] == nom]
    return formatCaptures(tree, codesource, monresult)
    
#methode testée mais pas forcément utilisée    
def lint(tree, codesource, msg, query, nom, fonction_appliquee = None):
    if fonction_appliquee == None:
        print("on retourne " + msg)
        return capturesByName(tree, codesource, query, nom)
    else:
        print("on applique " + str(fonction_appliquee) + " " + msg)
        fonction_appliquee(capturesByName(tree, codesource, query, nom))


#Cette fonction recupère les expressions binaires filles à partir du noeud considéré 

def recupereExpressionsFilles(nodeTreeSitter):
    def estExpressionBinaire(nodeexpr):
        return True
    noeudGauche = nodeTreeSitter
    if estExpressionBinaire(noeudGauche):
        pass
    else:
        #on cree 
        pass

def splited(word):
    liste = [char for char in word]

    for x in liste:
        if x == " ":
            liste.remove(x)
    return liste  


'''
def TraverseIteratif(cursor, ordre, liste):
    while(True):
        if ordre == "pre":
           liste.append(cursor.node)
        if cursor.goto_first_child():
            pass
        node = cursor.node
        if cursor.goto_next_sibling():
            if ordre == "post":
                liste.append(cursor.node)
            pass
        while (True):
            if ordre == "post":
                liste.append(cursor.node)
            if cursor.goto_parent() is None:
                break
'''










'''
def TraverseRecur(cursor, ordre, liste):
   
    #cursor = rootnode.walk()
    
    if ordre == "pre":
        liste.append(cursor.node)
    if cursor.goto_first_child():
        moncurseur = copy.copy(cursor)
        while (True):
            TraverseRecur(cursor, ordre, liste)
            if cursor.goto_next_sibling() is None:
                break
        #cursor.goto_parent()
        cursor = moncurseur
    if ordre == "post":
        liste.append(cursor.node)
    


            



    

def AllNodesFromType(rootnode, letype):
    cursor = rootnode.walk()
    while cursor.goto_first_child():
        node = cursor.node
        while (True):
            if cursor.node.type == letype:
                print(cursor.node)
            if cursor.goto_next_sibling() is None:
                break
        cursor = node
        

    
'''