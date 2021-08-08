import re

import materijal
import traka


class Element:
    svi_elementi = []

    oznaka = ""
    tekstura = "-"
    broj_elemenata = 0
    duzina = 0
    broj_kantovanih_duzina = 0
    sirina = 0
    broj_kantovanih_sirina = 0
    debljina = 0
    materijal = ""

    @staticmethod
    def ispisi_sve():
        print("\tClass Element")
        for elem in Element.svi_elementi:
            print(elem)

    def __procitaj_oznaka_duzina_sirina_debljina_broj_elemenata(self, line):
        self.materijal = line[0]
        self.oznaka = line[1]
        self.duzina = int(line[2][0: -3])
        self.sirina = int(line[3][0: -3])
        self.debljina = int(line[4][0: -3])
        self.broj_elemenata = int(line[5])

    def __odredi_kantove(self):
        kant = re.search("_kant_.+$", self.oznaka)
        if kant is not None:
            kant = kant.group()
            obe_kant = re.search("_obe_\d", kant)
            if obe_kant is not None:
                obe_kant = obe_kant.group()
                self.broj_kantovanih_duzina = int(obe_kant[-1])
                self.broj_kantovanih_sirina = int(obe_kant[-1])
            else:
                duzina_kant = re.search("_duzina_\d", kant)
                if duzina_kant is not None:
                    duzina_kant = duzina_kant.group()
                    self.broj_kantovanih_duzina = int(duzina_kant[-1])
                sirina_kant = re.search("_sirina_\d", kant)
                if sirina_kant is not None:
                    sirina_kant = sirina_kant.group()
                    self.broj_kantovanih_sirina = int(sirina_kant[-1])

    def duzni_metar_materijala(self):
        return self.duzina * self.broj_elemenata / 1000

    def kvadratura_materijala(self):
        return self.duzina * self.sirina * self.broj_elemenata / 1000000

    def duzni_metar_trake(self):
        ret = self.duzina * self.broj_kantovanih_duzina + self.sirina * self.broj_kantovanih_sirina
        ret *= self.broj_elemenata
        return ret / 1000

    def __povezi(self):
        materijal.Materijal.novi_element(self)
        traka.Traka.novi_element(self)
        Element.svi_elementi.append(self)

    def __init__(self, line):

        self.__procitaj_oznaka_duzina_sirina_debljina_broj_elemenata(line)
        self.__odredi_kantove()  # cita katnove iz oznake pa mu treba line kao argument

        self.__povezi()

    def __str__(self):
        return str(self.duzina) + ";" + \
               traka.Traka.postavi_kant(self.broj_kantovanih_duzina) + ";" + \
               str(self.sirina) + ";" + \
               traka.Traka.postavi_kant(self.broj_kantovanih_sirina) + ";" + \
               self.oznaka + ";" + \
               str(self.broj_elemenata) + ";" + \
               self.materijal + ";" + \
               str(self.kvadratura_materijala()).replace(".", ",") + ";" + \
               str(self.duzni_metar_materijala()).replace(".", ",") + ";" + \
               str(self.duzni_metar_trake()).replace(".", ",")
