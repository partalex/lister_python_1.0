import csv

import traka


class Materijal:
    vrste_Materijala = {}
    set_Materijali = set()

    @staticmethod
    def ispisi_sve():
        print("\tClass Materijal")
        for key in Materijal.set_Materijali:
            print(Materijal.vrste_Materijala[key])
            # for line in Materijal.vrste_Materijala[key].lista:
            #     print(line)

    def __init__(self, oznaka, debljina: int, teskstura):
        self.oznaka = oznaka
        self.debljina = debljina
        self.teskstura = teskstura
        self.kvadratura = 0
        self.duzni_metar_materijala = 0
        self.broj_elemenata = 0
        self.lista = []

    def materijal_info(self):
        data = ["Oznaka;Debljina;Kvadratura;Duznih metara materijala;Broj elemenata", self.oznaka + ";" + \
                str(self.debljina) + ";" + \
                str(self.kvadratura) + ";" + \
                str(self.duzni_metar_materijala) + ";" + \
                str(self.broj_elemenata)]
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

    @staticmethod
    def csv_export():
        kolone = "RB;DUZINA;KT;SIRINA;KT1;OZNAKA;T;KOM"
        line = ""
        data = []
        for key in Materijal.set_Materijali:
            for line in Materijal.vrste_Materijala[key].materijal_info():
                data.append(line)
            rb = 1
            data.append("\n" + kolone)
            for elem in Materijal.vrste_Materijala[key].lista:
                line = "0" + str(rb) + ";" + \
                       str(elem.duzina).replace(".0", "") + ";" + \
                       traka.Traka.postavi_kant(elem.broj_kantovanih_duzina) + ";" + \
                       str(elem.sirina).replace(".0", "") + ";" + \
                       traka.Traka.postavi_kant(elem.broj_kantovanih_sirina) + ";" + \
                       elem.oznaka + ";" + \
                       Materijal.vrste_Materijala[key].teskstura + ";" + \
                       str(elem.broj_elemenata) + ";"
                data.append(line)
                rb += 1
            data.append("\n")

        return data
