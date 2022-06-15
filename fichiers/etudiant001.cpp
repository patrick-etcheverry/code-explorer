/*
 Exercice : B
 Auteur : etudiant001
 Programme : Trier un tableau d'étudiants
 But : Trier un tableau d'étudiants par nom dans l'ordre croissant.
 Date de création : 9/11/2021 
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


// Déclaration du sous-programme
void trierTabCroissant(unsigned const int nbCases, Etudiant tab[]);
/* BUT : Trier un tableau tab d'éléments de la structutre Etudiant 
en fonction de leur nom de manière croissante */



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

    // Trier le tableau : A COMPLETER AVEC L'APPEL DE VOTRE SOUS-PROGRAMME
    trierTabCroissant(EFFECTIF_S1, etudiantsS1);

    // Affichage du tableau trié
    for (unsigned int i = 0; i < EFFECTIF_S1; i++)
    {
        cout << etudiantsS1[i].nom << "  " << etudiantsS1[i].prenom << " TP" << etudiantsS1[i].tp << endl;
    }
    cout << endl;

    return 0;
}

// Définition du sous-programme
void trierTabCroissant(unsigned const int nbCases, Etudiant tab[]) {

    // Considérer que le tableau n'est pas trié
    bool estTrie = false;

    // Boucle while true
    while (true) {

        // Si le tableau estTrie, alors estTrie vaudra true, la condition sera validée et la boucle se terminera
        if (estTrie) { 
            break;
        }

        // Supposer que le tableau est totalement trié
        estTrie = true;

        // Comparer les étudiants aux indices pairs-impairs
        for (unsigned int i = 0; i <= nbCases-2; i=i+2) {
            if (tab[i].nom > tab[i+1].nom) {
                Etudiant temp = tab[i+1]; // Echange de deux valeurs du tableau en indice i et i+1
                tab[i+1] = tab[i];
                tab[i] = temp;
                estTrie = false; // Infirme le fait que tableau est trié, permet la continuation de la boucle
            }
        }

        // Comparer les étudiants aux indices impairs-pairs
        for (unsigned int i = 1; i <= nbCases-2; i+=2) {
            if (tab[i].nom > tab[i+1].nom) {
                Etudiant temp = tab[i+1]; // Echange de deux valeurs du tableau en indice i et i+1
                tab[i+1] = tab[i];
                tab[i] = temp;
                estTrie = false; // Infirme le fait que tableau est trié, permet la continuation de la boucle
            }
        }
    }
}
