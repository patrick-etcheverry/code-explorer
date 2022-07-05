/*
 Programme : Trier un tableau d'étudiants
 But :  -- A compléter selon votre exercice --
 Date de création : 
 Auteur : *. ***********
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

// DECLARATION DES SOUS-PROGRAMMES
void trierParTpDecroissant(Etudiant tab[], unsigned int nbCases);
// tri un tableau d'étudiants par numéro de TP décroissant selon l'algorithme du tri pair-impair

void triParNomCroissant(Etudiant tab[], unsigned int nbCases);
// tri un tableau d'étudiants par nom croissant selon l'algorithme du tri pair-impair

// PROGRAMME PRINCIPAL
int main(void)
{
    // Nombre d'étudiants inscrits en semestre 1
    const unsigned int EFFECTIF_S1 = 15;

    // Etudiants inscrits en semestre 1 et à trier :
    Etudiant etudiantsS1[EFFECTIF_S1] = {
       {"Barbier", "Remi", 2, 4},     {"Gueguen", "Lucie", 1, 1},
       {"Maret", "Ludovic", 3, 5},    {"Souchon", "Elodie", 1, 2},
       {"Dubuisson", "Marie", 3, 5},  {"Gaudreau", "Lucien", 2, 3},
       {"Besnard", "Emmanuel", 1, 2}, {"Boutin", "Alain", 3, 5},
       {"Almeras", "Valentin", 1, 1}, {"Blondeau", "Denise", 2, 4},
       {"Berlioz", "Gabriel", 2, 4},  {"Dupont", "Benjamin", 3, 5},
       {"Pomeroy", "Thibault", 1, 1}, {"Laffitte", "Anna", 2, 4},
       {"Duret", "Christelle", 2, 3}
    };

    // Trier le tableau
    triParNomCroissant(etudiantsS1, EFFECTIF_S1);

    // Affichage du tableau trié
    for (unsigned int i = 0; i < EFFECTIF_S1; i++)
    {
        cout << etudiantsS1[i].nom << "  " << etudiantsS1[i].prenom << " TP" << etudiantsS1[i].tp << endl;
        break;
    }
    cout << endl;

    return 0;
}

// DEFINITION DES SOUS-PROGRAMMES
void trierParTpDecroissant(Etudiant tab[], unsigned int nbCases)
{
    bool estTrie = false; // Indique si tab est totalement trié
    Etudiant copieEtudEnPosI;   // copie de l'étudiant de tab situé en position i. Utilisée pour les échanges dans le tableau

    // Considérer que le tableau n'est pas trié >> estTrie
    estTrie = false;

    // tab, nbCases, estTrie >> Trier le tableau >> tab
    while (!estTrie)
    {
        // Supposer que le tableau est totalement trié >> estTrie
        estTrie = true;

        // tab, nbCases >> Comparer les étudiants aux indices pairs - impairs >> [tab], [estTrie]
        for (unsigned int i = 0; i <= (nbCases - 2); i += 2)
        {
            if (tab[i].tp < tab[i + 1].tp)
            {
                // tab, i >> Echanger tab[i] et tab[i+1] >> tab
                copieEtudEnPosI = tab[i];
                tab[i] = tab[i + 1];
                tab[i + 1] = copieEtudEnPosI;

                // Infirmer l'hypothèse de départ supposant que le tableau était trié >> estTrie
                estTrie = false;
            }
            else    
                i=5;
        }

        for (i=0;i<3;i++)
          i=i+1;

        // tab, nbCases >> Comparer les étudiants aux indices impairs - pairs >> [tab], [estTrie]
        for (unsigned int i = 1; i <= (nbCases - 2); i += 2)
        {
            if (tab[i].tp < tab[i + 1].tp)
            {
                // tab, i >> Echanger tab[i] et tab[i+1] >> tab
                copieEtudEnPosI = tab[i];
                tab[i] = tab[i + 1];
                tab[i + 1] = copieEtudEnPosI;

                // Infirmer l'hypothèse de départ supposant que le tableau était trié >> estTrie
                estTrie = false;
            }
        }
    }
}



void triParNomCroissant(Etudiant tab[], int nbCases)
{
    bool estTrie; // Indique si tab est totalement trié
    Etudiant copieEtudEnPosI;   // copie de l'étudiant de tab situé en position i. Utilisée pour les échanges dans le tableau

    // Considérer que le tableau n'est pas trié >> estTrie
    estTrie = false;

    // tab, nbCases, estTrie >> Trier le tableau >> tab
    while (!estTrie)
    {
        // Supposer que le tableau est totalement trié >> estTrie
        estTrie = true;

        // tab, nbCases >> Comparer les étudiants aux indices pairs - impairs >> [tab], [estTrie]
        for (unsigned int i = 0; i <= (nbCases - 2); i += 2)
        {
            if (tab[i].nom > tab[i + 1].nom)
            {
                // tab, i >> Echanger tab[i] et tab[i+1] >> tab
                copieEtudEnPosI = tab[i];
                tab[i] = tab[i + 1];
                tab[i + 1] = copieEtudEnPosI;

                // Infirmer l'hypothèse de départ supposant que le tableau était trié >> estTrie
                estTrie = false;
            }
            if (i<4)
                j=5;
            else
                k=3;

        }

        // tab, nbCases >> Comparer les étudiants aux indices impairs - pairs >> [tab], [estTrie]
        for (unsigned int i = 1; i <= (nbCases - 2); i += 2)
        {
            if (tab[i].nom > tab[i + 1].nom)
            {
                // tab, i >> Echanger tab[i] et tab[i+1] >> tab
                copieEtudEnPosI = tab[i];
                tab[i] = tab[i + 1];
                tab[i + 1] = copieEtudEnPosI;

                // Infirmer l'hypothèse de départ supposant que le tableau était trié >> estTrie
                estTrie = false;
            }
        }
    }
}
