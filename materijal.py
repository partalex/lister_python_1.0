

class Materijal:
    def __init__(self, oznaka, debljina: int, teskstura):
        self.oznaka = oznaka
        self.debljina = debljina
        self.teskstura = teskstura
        self.kvadratura = 0
        self.duzni_metar_materijala = 0
        self.broj_elemenata = 0

    def sracunaj_materijal(self, elem):
        self.kvadratura += elem.kvadratura_materijala
        self.duzni_metar_materijala += elem.duzni_metar_materijala
        self.broj_elemenata += elem.broj_elemenata

    @staticmethod
    def novi_element(elem):
        print(elem)
