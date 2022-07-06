#include <iostream>
using namespace std;

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


int main(void)
{
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
    trierParTpDecroissant(etudiantsS1, 15)
}


// DEFINITION DES SOUS-PROGRAMMES
void trierParTpDecroissant(Etudiant tab[], unsigned int nbCases)
{
    bool estTrie = false; // Indique si tab est totalement trié
    Etudiant copieEtudEnPosI;   // copie de l'étudiant de tab situé en position i. Utilisée pour les échanges dans le tableau
    int tab[][];
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

