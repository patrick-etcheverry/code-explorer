/*
Programme: moyenne d'un module v2 (TD4-M1102)
But: Calculer la moyenne d'une série de notes entrées au clavier

Propriétés retenues :
- Le nombre de notes à saisir n'est pas connu d'avance
- Les valeurs saisies erronées (non comprise entre 0 et 20) sont traitées
  via un message d'erreur et ne sont pas comptabilisées dans le calcul de la moyenne.
- La saisie des valeurs prend fin lorsque l'utilisateur entre une valeur particulière (999 ici)
  afin d'indiquer qu'il a terminé de saisir ses notes.
- Le cas où l'utilisateur n'entre aucune note (saisie de la valeur 999 dès le début) est
  pris en compte : la calcul de la moyenne est protégé et l'affichage final adapté.

Auteur : Patrick Etcheverry
Date de dernière modification: 29 septembre 2013
Remarques : Code conforme aux spécifications élaborées au TD4
*/

#include <iostream>
using namespace std;

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
    for ( ; ; )
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

