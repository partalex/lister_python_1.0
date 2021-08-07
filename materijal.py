
class Materijal:
    vrste_Materijala = {}
    set_Materijali = set()

    @staticmethod
    def ispisi_sve():
        print("\tClass Materijal")
        for key in Materijal.set_Materijali:
            print(key)
            for line in Materijal.vrste_Materijala[key].lista:
                print(line)


    def __init__(self, oznaka, debljina: int, teskstura):
        self.oznaka = oznaka
        self.debljina = debljina
        self.teskstura = teskstura
        self.kvadratura = 0
        self.duzni_metar_materijala = 0
        self.broj_elemenata = 0
        self.lista = []

    def sracunaj_materijal(self, elem):
        self.kvadratura += elem.kvadratura_materijala
        self.duzni_metar_materijala += elem.duzni_metar_materijala
        self.broj_elemenata += elem.broj_elemenata

    @staticmethod
    def novi_element(elem):
        if elem.materijal not in Materijal.set_Materijali:
            Materijal.set_Materijali.add(elem.materijal)
            Materijal.vrste_Materijala[elem.materijal] = Materijal(elem.materijal, elem.debljina, elem.tekstura)

        Materijal.vrste_Materijala[elem.materijal].sracunaj_materijal(elem)
        Materijal.vrste_Materijala[elem.materijal].lista.append(elem)
