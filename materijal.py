from element import Element


class Materijal:
    def __init__(self, oznaka, debljina: int, teskstura):
        self.oznaka = oznaka
        self.debljina = debljina
        self.teskstura = teskstura
        self.kvadratura = 0
        self.duzni_metar_materijala = 0
        self.broj_elemenata = 0

    def sracunaj_materijal(self, element: Element):
        self.kvadratura += element.kvadratura_materijala
        self.duzni_metar_materijala += element.duzni_metar_materijala
        self.broj_elemenata += element.broj_elemenata
