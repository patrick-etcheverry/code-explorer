/*
 Programme : Trier un tableau d'étudiants
 But :  Trier une liste d'étudiant par nom croissant 
 Date de création : 09/11/2021
 Auteur : etudiant002
 Remarques éventuelles pour le correcteur:
 */

#include <iostream>
using namespace std;

// Définition du type Etudiant
struct Etudiant
{
    string nom;            // nom de l'étudiant
    string prenom;         // prénom de l'étudiant
    unsigned short int td; // numéro de TD de l'étudiant
    unsigned short int tp; // numéro de TP de l'étudiant
};

Etudiant trierEtudiantParNomCroissant(Etudiant tab[], const unsigned int NB_CASES);
//But : Trier une liste d'étudiant rentré dans un tableau (tab[]) d'un nombre de case définie (NB_CASES) et retourné ce tableau

// PROGRAMME PRINCIPAL
int main(void)
{
    // Nombre d'étudiants inscrits en semestre 1
    const unsigned int EFFECTIF_S1 = 15;

    // Etudiants inscrits en semestre 1 et à trier :
    Etudiant etudiantsS1[EFFECTIF_S1] = {
        {"Barbier", "Remi", 2, 4}, {"Gueguen", "Lucie", 1, 1}, {"Maret", "Ludovic", 3, 5}, {"Souchon", "Elodie", 1, 2}, {"Dubuisson", "Marie", 3, 5}, {"Gaudreau", "Lucien", 2, 3}, {"Besnard", "Emmanuel", 1, 2}, {"Boutin", "Alain", 3, 5}, {"Almeras", "Valentin", 1, 1}, {"Blondeau", "Denise", 2, 4}, {"Berlioz", "Gabriel", 2, 4}, {"Dupont", "Benjamin", 3, 5}, {"Pomeroy", "Thibault", 1, 1}, {"Laffitte", "Anna", 2, 4}, {"Duret", "Christelle", 2, 3}};

    // Trier le tableau : A COMPLETER AVEC L'APPEL DE VOTRE SOUS-PROGRAMME

    //Trie du tableau :
    etudiantsS1[EFFECTIF_S1] = trierEtudiantParNomCroissant(etudiantsS1[EFFECTIF_S1], EFFECTIF_S1);

    // Affichage du tableau trié
    for (unsigned int i = 0; i < EFFECTIF_S1; i++)
    {
        cout << etudiantsS1[i].nom << "  " << etudiantsS1[i].prenom << " TP" << etudiantsS1[i].tp << endl;
    }
    cout << endl;

    return 0;
}

//Sous Programme :

Etudiant trierEtudiantParNomCroissant(Etudiant tab[], const unsigned int NB_CASES)
{

    Etudiant temp;
    bool estTrie = false;
    while (true)
    {
        if (estTrie == true)
        {
            break;
        }
        estTrie = true;

        for (unsigned int i = 0; i <= NB_CASES - 2; i += 2)
        {
            if (tab[i].nom > tab[i+1].nom)
            {
                temp = tab[i];
                tab[i] = tab[i+1];
                tab[i+1] = temp;
                estTrie = false;
            }
        }
        for (unsigned int i = 1; i <= NB_CASES - 2; i += 2)
        {
            if (tab[i].nom > tab[i+1].nom)
            {
                temp = tab[i];
                tab[i] = tab[i+1];
                tab[i+1] = temp;
                estTrie = false;
            }
        }
    }
}
