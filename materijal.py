import traka


class Materijal:
    vrste_Materijala = {}
    set_Materijali = set()

    @staticmethod
    def ispisi_sve():
        print("\tClass Materijal")
        for key in Materijal.set_Materijali:
            print(Materijal.vrste_Materijala[key])

    def __init__(self, oznaka, debljina: int, teskstura):
        self.oznaka = oznaka
        self.debljina = debljina
        self.teskstura = teskstura
        self.kvadratura = 0
        self.duzni_metar_materijala = 0
        self.broj_elemenata = 0
        self.lista = []

    @staticmethod
    def csv_statistika():
        data = ["Oznaka;Debljina;Kvadratura;Duznih metara materijala;Broj elemenata"]
        for oznaka in Materijal.set_Materijali:
            mat = Materijal.vrste_Materijala[oznaka]
            data.append(mat.oznaka + ";" + \
                        str(mat.debljina) + ";" + \
                        str(mat.kvadratura).replace('.', ',') + ";" + \
                        str(mat.duzni_metar_materijala).replace('.', ',') + ";" + \
                        str(mat.broj_elemenata))
        return data

    def sracunaj_materijal(self, elem):
        self.kvadratura += elem.kvadratura_materijala()
        self.duzni_metar_materijala += elem.duzni_metar_materijala()
        self.broj_elemenata += elem.broj_elemenata

    @staticmethod
    def novi_element(elem):
        if elem.materijal not in Materijal.set_Materijali:
            Materijal.set_Materijali.add(elem.materijal)
            Materijal.vrste_Materijala[elem.materijal] = Materijal(elem.materijal, elem.debljina, elem.tekstura)

        Materijal.vrste_Materijala[elem.materijal].sracunaj_materijal(elem)
        Materijal.vrste_Materijala[elem.materijal].lista.append(elem)

    def csv_export(self):
        data = ["RB;DUZINA;KT;SIRINA;KT1;OZNAKA;T;KOM"]
        rb = 1
        for elem in self.lista:
            line = "0" + str(rb) + ";" + \
                   str(elem.duzina).replace(".0", "") + ";" + \
                   traka.Traka.postavi_kant(elem.broj_kantovanih_duzina) + ";" + \
                   str(elem.sirina).replace(".0", "") + ";" + \
                   traka.Traka.postavi_kant(elem.broj_kantovanih_sirina) + ";" + \
                   elem.oznaka + ";" + \
                   self.teskstura + ";" + \
                   str(elem.broj_elemenata) + ";"
            data.append(line)
            rb += 1

        return data
