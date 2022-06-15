/*
 Programme : Exercice B : Trier les étudiants par noms croissants
 But :  Trier une liste d'étudiants par noms croissants selon un modèle d'algorithme nommé tri pair-impair par transposition.
 Date de création : 09/11/2021
 Auteur : etudiant003
 Remarques éventuelles pour le correcteur : Avant l'appel du sous-programme, j'ai initialisé trie à false et j à 0 pour éviter une remarque du compilateur
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

// Déclaration du sous-progroamme
void trierParNomCroissant(Etudiant tab[], unsigned int nbCases, bool estTrie, unsigned int i);

// But : Trier les valeurs d'un tableau par noms croissants

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
    bool trie = false;  // indique si la liste est triée ou non
    unsigned int j = 0; // numéro de l'itération dans les boucles
    trierParNomCroissant(etudiantsS1, EFFECTIF_S1, trie, j);

    // Affichage du tableau trié
    for (unsigned int i = 0; i < EFFECTIF_S1; i++)
    {
        cout << etudiantsS1[i].nom << "  " << etudiantsS1[i].prenom << " TP" << etudiantsS1[i].tp << endl;
    }
    cout << endl;

    return 0;
}

void trierParNomCroissant(Etudiant tab[], unsigned int nbCases, bool estTrie, unsigned int i) 
{
    // Considérer que le tableau n'est pas trié
    estTrie = false;

    // Trier le tableau
    while (estTrie == false)
    {
        // Supposer que le tableau est totalement trié
        estTrie = true;

        // Comparer les étudiants aux indices pairs - impairs
        for (i = 0; i <= (nbCases - 2); i += 2)
        {
            if (tab[i].nom > tab[i + 1].nom)
            {
                // Echanger tab[i] et tab[i+1]
                Etudiant temp;
                temp = tab[i];
                tab[i] = tab[i + 1];
                tab[i + 1] = temp;

                // Infirmer l'hypothèse de départ supposant que le tableau est trié
                estTrie = false;
            }
            
        }

        // Comparer les étudiants aux indices impairs - pairs
        for (i = 1; i <= (nbCases - 2); i += 2)
        {
            if (tab[i].nom > tab[i + 1].nom)
            {
                // Echanger tab[i] et tab[i+1]
                Etudiant temp;
                temp = tab[i];
                tab[i] = tab[i + 1];
                tab[i + 1] = temp;

                // Infirmer l'hypothèse de départ supposant que le tableau est trié
                estTrie = false; 
            }
        }
    }  
}
