import csv
import re
import element
import materijal


class Lista:
    ulaz_csv = {}
    material = set()
    hash = {}
    redni_broj = 0

    def __init__(self, material: materijal.Materijal):
        self.material = material
        self.povrsina = 0
        self.elementi = []

    def ubaci_element(self, elem):
        self.elementi.append(elem)

    @staticmethod
    def kvadratura_materijala(material, kolicina):
        try:
            Lista.hash[material]
        except:
            Lista.material.add(material)
            Lista.hash[material] = 0
        Lista.hash[material] += kolicina


def read(ulaz):
    with open(ulaz, 'r') as file:
        input_list = csv.reader(file)

        next(input_list)
        for line in input_list:
            generic = re.search("^generic_", line[1])
            if generic is not None:
                continue
            comp = element.Element(line)
            Lista.ulaz_csv[line[0]]["komponente"].append(comp)