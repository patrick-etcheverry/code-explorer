#include <iostream>
using namespace std;


int main(void)
{
    float valeurSaisie ; // Prend successivement les différentes valeurs entrées par l'utilisateur
    int sommeNotes = 0;
    int nombreDeNotes = 0;


    for (int i=5 ;i<20 ;i=i+1 )
    {
        cout  << "Entrez une note comprise dans l'intervalle [0..20] : ";
        cin >> valeurSaisie;
    }    

    for (int i=0 ;i<10 ; i=i+1 )
    {
        // (clavier) >> Saisir une valeur >> valeurSaisie
        cout  << "Entrez une note comprise dans l'intervalle [0..20] : ";
        cin >> valeurSaisie;

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

    int i = 0;
    do {
        cout << i << "\n";
        i++;
    }
    while (i < 5);


    while(true)
        i++;

    while(i < 20)
        i++;

}

void titi(int valeur, int toto, bool x) 
{
    int i=0;
    int k = i;
    i=2;
    int k = i;
    if (i<0) {
        i=4;
    }
}

