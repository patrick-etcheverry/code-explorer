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

//Declaration du sous programme
void triPairImpair(NB_CASES, tab);

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
    triPairImpair(EFFECTIF_S1,&etudiantsS1)


    // Définition du sous-programme

    void triPairImpair(NB_CASES,tab)
    {
        unsigned int NB_CASES; //Lee nombre de cases du tableau tab
        int tab[NB_CASES]; //Le tableau contenant les étudiants a trier par numéro de TP décroissant
        bool estTriee = false; // indiquesi tab est totalement trié
        unsigned int i; //indice de parcours du tableau tab
          

        while (!estTrie)
        {
            estTrie = true;
            
            for (i = 0; i <= (NB_CASES); i+=2)
            {
                if (tab[i].tp < tab[i+1].tp)
                {
                    
                    tab[i] = tab[i+1] ////////////////
                    estTrie = false;
                }

                for (i = 1; i <= (NB_CASES-2); i += 2)
                {
                    if(tab[i].tp < tab[i+1])
                    {
                        tab[i] = tab[i+1]; ///////////////////////////
                        estTrie = false;
                    }
                }
            }
        }

    for (unsigned int i = 0; i < EFFECTIF_S1; i++)
    {
        cout << etudiantsS1[i].nom << "  " << etudiantsS1[i].prenom << " TP" << etudiantsS1[i].tp << endl;
    }
    cout << endl;

    return 0;
        
    }

    
}