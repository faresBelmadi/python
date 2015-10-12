class Bateau:

    def __init__(self, positions):
        self.estCoule=False
        self.positions=positions

    def estTouche(self, case):
        for position in self.positions:
            if case == position:
                return True
        return False
