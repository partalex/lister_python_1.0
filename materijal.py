

class Materijal:
    hash_Materijal = {}
    materijali = set()

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
        try:
            Materijal.materijali[elem.materijal]
        except:
            Materijal.materijali.add(elem.materijal)
            Materijal.hash_Materijal[elem.materijal] = Materijal(elem.materijal, elem.debljina, elem.tekstura)

        Materijal.hash_Materijal[elem.materijal].sracunaj_materijal(elem)
