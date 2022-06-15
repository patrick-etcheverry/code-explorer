
class ListeOrdonnee(list):

    def __init__(self, cletri):  #on lui passe le critère de tri
        super().__init__()
        self.laCleTri=cletri
        self.iterListe=iter(self)
    
    def append(self, val):
        super().append(val)
        self.sort(key=self.laCleTri)

    def next(self):
        return next(self.iterListe)
