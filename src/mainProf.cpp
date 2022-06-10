/*
Programme: moyenne d'un module v2 (TD4-M1102)
But: Calculer la moyenne d'une série de notes entrees au clavier

Proprietes retenues :
- Le nombre de notes à saisir n'est pas connu d'avance
- Les valeurs saisies errones (non comprise entre 0 et 20) sont traitees
  via un message d'erreur et ne sont pas comptabilisées dans le calcul de la moyenne.
- La saisie des valeurs prend fin lorsque l'utilisateur entre une valeur particulière (999 ici)
  afin d'indiquer qu'il a termine de saisir ses notes.
- Le cas où l'utilisateur n'entre aucune note (saisie de la valeur 999 dès le début) est
  pris en compte : la calcul de la moyenne est protégé et l'affichage final adapté.

Auteur : Patrick Etcheverry
Date de dernière modification: 29 septembre 2013
Remarques : Code conforme aux spécifications élaborées au TD4
*/

#include <iostream>
using namespace std;

void toto(int val) {
    int i=0;
    int k = i;
    }



int main(void)
{
    float valeurSaisie ; // Prend successivement les différentes valeurs entrées par l'utilisateur
    const unsigned short int VAL_ARRET_SAISIE = 999; // valeur à saisir pour stopper la saisie
    float sommeNotes; // somme des valeurs saisies comprises dans [0..20]
    unsigned int nombreDeNotes; // nombre de valeurs saisies comprises dans [0..20]
    float moyenne; // moyenne des valeurs saisies et comprises dans [0..20]


    /* () >> SAISIE LES VALEURS PERMETTANT DE CALCULER LA MOYENNE >> sommeNotes, nombreDeNotes
    ------------------------------------------------------------------------------------------ */

    // () >> Initialisation de l'accumulateur et du compteur >> sommeNotes, nombreDeNotes
    sommeNotes = 0;
    nombreDeNotes = 0;

    // () >> Saisie, comptage et cumul des notes >> [sommeNotes], [nombreDeNotes]
    
    for (int i=5 ;i<20 ;i=i+1 )
    {
        // (clavier) >> Saisir une valeur >> valeurSaisie
        cout  << "Entrez une note comprise dans l'intervalle [0..20] : ";
        cin >> valeurSaisie;
 
    }    

    for (int i=5 ;i<20 ;i=i+1 )
    	cout << 2;


    for (int i=0 ;i<10 ; i=i+1 )
    {
        // (clavier) >> Saisir une valeur >> valeurSaisie
        cout  << "Entrez une note comprise dans l'intervalle [0..20] : ";
        cin >> valeurSaisie;

        // Vérifier si l'utilisateur a demandé l'arrêt de la saisie
        if (VAL_ARRET_SAISIE == valeurSaisie)
        {
            break ;
        }

        // valeurSaisie >> Traiter la valeur saisie >> [sommeNotes], [sommeNotes]
        if (valeurSaisie >= 0 && valeurSaisie <= 20)
        {
            // Cumuler et comptabiliser la nouvelle note >> [sommeNotes], [nombreDeNotes]
            sommeNotes += valeurSaisie ;
            nombreDeNotes++;
        }
        else
        {
            cout << "Valeur incorrecte, une note doit etre comprise entre 0 et 20." << endl;
        }
    }


     /* sommeNotes, nombreDeNotes >> CALCULER LA MOYENNE SI POSSIBLE >> [moyenne]
    ------------------------------------------------------------------------------------------ */

    if (nombreDeNotes > 0)
    {
        moyenne = sommeNotes / nombreDeNotes;
    }

    int i = 0;
    do {
        cout << i << "\n";
        i++;
    }
    while (i < 5);


    while(i < 3)
        i++;


      /* nombreDeNotes, [moyenne] >> Afficher le résultat >> (ecran)
    ------------------------------------------------------------------------------------------ */

    if (nombreDeNotes > 0)
    {
        cout << "La moyenne des notes valides saisies est : " << moyenne << endl;
    }
    else
    {
        cout << "Impossible de calculer la moyenne, aucune note valide saisie." << endl;
    }

    return 0;
}


void titi(int valeur, int toto, bool x) {
    int i=0;
    int k = i;
    i=2;
    int k = i;
    if (i<0) {
        i=4;
    }

}

