##@brief Classe permettant la conversion des objets en ListeOrdonnee
class ListeOrdonnee(list):

    def __init__(self, cletri):  #on lui passe le critère de tri
        super().__init__()
        self.laCleTri=cletri
        self.iterListe=iter(self)
    
    #def __iter__(self):
    #    return self

    
    def append(self, val):
        super().append(val)
        self.sort(key=self.laCleTri)

    def getNext(self):
        return next(self.iterListe)

    def getLongueur(self):
        return len(self)
