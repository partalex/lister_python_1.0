class Traka:
    sve_trake = {}

    def __init__(self, oznaka, debljina: int):
        self.oznaka = oznaka
        self.debljina = debljina
        self.duznih_metara = 0
        self.povrsina = 0
        self.sirina = 0

    def novi_element(self, elem):
        print(elem)

    @staticmethod
    def postavi_kant(broj_kantova):
        if broj_kantova == 0:
            return ""
        elif broj_kantova == 1:
            return "(x,0)"
        else:
            return "(x,x)"
