import re
import locale
from List import List

primer = {
    "komponente": [],
    "povrsina": [],
    "debljina": [],
}

class Component:
    redni_broj = 0
    oznaka = ""
    tekstura = "-"
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

    @staticmethod
    def postavi_kant(broj_kantova):
        if broj_kantova == 0:
            return ""
        elif broj_kantova == 1:
            return "(x,0)"
        else:
            return "(x,x)"

    def __init__(self, line, broj):
        if line[0] not in List.svi_materijali.keys():
            List.svi_materijali[line[0]] = primer

        self.oznaka = line[1]
        self.duzina = int(line[2][0: -3])
        self.sirina = int(line[3][0: -3])
        # self.debljina = int(line[4][0: -3])

        self.kolicina = int(line[5])

        kant = re.search("_kant_.+$", self.oznaka)
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

    # def __init__(self, string):
    #     lista = string.split(',')
    #
    #     self.materijal = lista[0][1:-1]
    #     self.oznaka = lista[1][1:-1]
    #     generic = re.search("^generic_", self.oznaka)
    #     if generic != None:
    #         raise Exception('Genericka komponenta je u pitanju, ne upisuj je u listu')
    #     self.kolicina = int(lista[5][1:-2])
    #
    #     self.duzina = locale.atof((re.search("^\d+", lista[2][1:-1])).group())
    #     self.sirina = locale.atof((re.search("^\d+", lista[3][1:-1])).group())
    #     self.debljina = locale.atof((re.search("^\d+", lista[4][1:-1])).group())
    #
    #     kant = re.search("_kant_.+$", lista[1][1:-1])
    #     if kant != None:
    #         kant = kant.group()
    #         obe_kant = re.search("_obe_\d", kant)
    #         if obe_kant != None:
    #             obe_kant = obe_kant.group()
    #             self.broj_kantovanih_duzina = int(obe_kant[-1])
    #             self.broj_kantovanih_sirina = int(obe_kant[-1])
    #         else:
    #             duzina_kant = re.search("_duzina_\d", kant)
    #             if duzina_kant != None:
    #                 duzina_kant = duzina_kant.group()
    #                 self.broj_kantovanih_duzina = int(duzina_kant[-1])
    #             sirina_kant = re.search("_sirina_\d", kant)
    #             if sirina_kant != None:
    #                 sirina_kant = sirina_kant.group()
    #                 self.broj_kantovanih_sirina = int(sirina_kant[-1])
    #
    #     self.duzni_metar_materijala = self.duzina * self.kolicina / 1000
    #     self.kvadratura_materijala = self.duzina * self.sirina * self.kolicina
    #     self.kvadratura_materijala /= 1000000
    #     self.duzni_metar_trake = self.duzina * self.broj_kantovanih_duzina + self.sirina * self.broj_kantovanih_sirina
    #     self.duzni_metar_trake *= self.kolicina
    #     self.duzni_metar_trake /= 1000
    #
    #     List.redni_broj += 1
    #     self.redni_broj  = List.redni_broj
    #     List.kvadratura_materijala(self.materijal, self.kvadratura_materijala)
    #     List.component_lista.append(self)

    def __str__(self):

        return "0" + str(self.redni_broj) + ";" + \
               str(self.duzina).replace(".0","") + ";" + \
               Component.postavi_kant(self.broj_kantovanih_duzina) + ";" + \
               str(self.sirina).replace(".0","")  + ";" + \
               Component.postavi_kant(self.broj_kantovanih_sirina) + ";" + \
               self.oznaka + ";" + \
               "" + ";" + \
               str(self.kolicina) + ";" + \
               self.materijal + ";" + \
               str(self.kvadratura_materijala).replace(".", ",") + ";" + \
               str(self.duzni_metar_materijala).replace(".", ",")+ ";" + \
               str(self.duzni_metar_trake).replace(".", ",")
