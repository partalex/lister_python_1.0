
class Traka:
    vrste_Traka = {}
    set_Traka = set()

    def __init__(self, sirina, debljina: int, oznaka):
        self.debljina = debljina
        self.duznih_metara = 0
        self.povrsina = 0
        self.sirina = sirina
        self.oznaka = oznaka


    def __sracunaj_traku(self, elem):
        self.duznih_metara += elem.duzni_metar_trake
        self.povrsina += elem.duzina * self.sirina


    @staticmethod
    def novi_element(elem):
        oznaka = "Traka: " + elem.materijal + "  " + str(elem.debljina) + " mm"
        try:
            Traka.set_Traka[oznaka]
        except:
            Traka.set_Traka.add(oznaka)
            Traka.vrste_Traka[oznaka] = Traka(elem.debljina, 1, oznaka)  # neka bude ovek debljine 1 mm traka za sad

        Traka.vrste_Traka[oznaka].__sracunaj_traku(elem)


    @staticmethod
    def postavi_kant(broj_kantova):
        if broj_kantova == 0:
            return ""
        elif broj_kantova == 1:
            return "(x,0)"
        else:
            return "(x,x)"
