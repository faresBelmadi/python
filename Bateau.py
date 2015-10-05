class Bateau:

    def __init__(self, taille):
        self.taille=taille
        self.estCoule=False
        self.positions=[()]

    def estTouche(self, case):
        for position in self.positions:
            if case == position:
                return True
        return False
