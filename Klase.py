import re
import locale
from builtins import print

class List:
    component_lista = []
    material = set()
    hash = {}
    @staticmethod
    def kvadratura_materijala(material, kolicina):
        try:
            List.hash[material]
        except:
            List.material.add(material)
            List.hash[material] = 0
        List.hash[material] += kolicina


class Component:
    opis = ""
    kolicina = 0
    duzina = 0
    broj_kantovanih_duzina = 0
    sirina = 0
    broj_kantovanih_sirina = 0
    debljina = 0
    materijal = ""
    kvadratura_materijala = 0
    duzni_metar_materijala = 0
    duzni_metar_trake = 0

    def __init__(self, string):
        lista = string.split(',')

        self.materijal = lista[0][1:-1]
        self.opis = lista[1][1:-1]
        generic = re.search("^generic_", self.opis)
        if generic != None:
            raise Exception('Genericka komponenta je u pitanju, ne upisuj je u listu')
        self.kolicina = int(lista[5][1:-2])

        self.duzina = locale.atof((re.search("^\d+", lista[2][1:-1])).group())
        self.sirina = locale.atof((re.search("^\d+", lista[3][1:-1])).group())
        self.debljina = locale.atof((re.search("^\d+", lista[4][1:-1])).group())

        kant = re.search("_kant_.+$", lista[1][1:-1])
        if kant != None:
            kant = kant.group()
            obe_kant = re.search("_obe_\d", kant)
            if obe_kant != None:
                obe_kant = obe_kant.group()
                self.broj_kantovanih_duzina = int(obe_kant[-1])
                self.broj_kantovanih_sirina = int(obe_kant[-1])
            else:
                duzina_kant = re.search("_duzina_\d", kant)
                if duzina_kant != None:
                    duzina_kant = duzina_kant.group()
                    self.broj_kantovanih_duzina = int(duzina_kant[-1])
                sirina_kant = re.search("_sirina_\d", kant)
                if sirina_kant != None:
                    sirina_kant = sirina_kant.group()
                    self.broj_kantovanih_sirina = int(sirina_kant[-1])

        self.duzni_metar_materijala = self.duzina * self.kolicina / 1000
        self.kvadratura_materijala = self.duzina * self.sirina * self.kolicina
        self.kvadratura_materijala /= 1000000
        self.duzni_metar_trake = self.duzina * self.broj_kantovanih_duzina + self.sirina * self.broj_kantovanih_sirina
        self.duzni_metar_trake *= self.kolicina
        self.duzni_metar_trake /= 1000
        List.component_lista.append(self)

        List.kvadratura_materijala(self.materijal, self.kvadratura_materijala)

    def __str__(self):

        return str(self.materijal) + ";" + \
               str(self.kolicina) + ";" + \
               str(self.duzina).replace(".0","") + ";" + \
               str(self.broj_kantovanih_duzina) + ";" + \
               str(self.sirina).replace(".0","")  + ";" + \
               str(self.broj_kantovanih_sirina) + ";" + \
               str(self.debljina).replace(".0","")  + ";" + \
               str(self.opis) + ";" + \
               str(self.kvadratura_materijala).replace(".", ",") + ";" + \
               str(self.duzni_metar_materijala).replace(".", ",")+ ";" + \
               str(self.duzni_metar_trake).replace(".", ",")
