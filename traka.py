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
        self.duznih_metara += elem.duzni_metar_trake()
        self.povrsina += (self.duznih_metara * self.sirina / 1000) * elem.broj_elemenata

    def __str__(self):
        return self.oznaka + ";" + \
               str(self.debljina) + ";" + \
               str(self.duznih_metara).replace(".", ",") + ";" + \
               str(self.sirina) + ";" + \
               str(self.povrsina).replace(".", ",")

    @staticmethod
    def novi_element(elem):
        if elem.broj_kantovanih_duzina + elem.broj_kantovanih_sirina == 0:
            return
        oznaka = "Traka: " + elem.materijal + " " + str(elem.debljina) + " mm"
        if oznaka not in Traka.set_Traka:
            Traka.set_Traka.add(oznaka)
            Traka.vrste_Traka[oznaka] = Traka(elem.debljina, 1, oznaka)  # neka bude uvek debljine 1 mm traka za sad

        Traka.vrste_Traka[oznaka].__sracunaj_traku(elem)

    @staticmethod
    def postavi_kant(broj_kantova):
        if broj_kantova == 0:
            return ""
        elif broj_kantova == 1:
            return "(x,0)"
        else:
            return "(x,x)"

    @staticmethod
    def csv_array():
        data = ["Oznaka;Debljina;Duznih metara;Sirina;Povrsina"]
        for oznaka in Traka.set_Traka:
            tr = Traka.vrste_Traka[oznaka]
            data.append(str(tr))

        return data
