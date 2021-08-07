import materijal
import element
class Lista:
    ulaz_csv = {}
    material = set()
    hash = {}
    redni_broj = 0

    def __init__(self, material: materijal.Materijal):
        self.material = material
        self.povrsina = 0
        self.elementi = []

    def ubaci_element(self, element: element.Element):
        self.elementi.append(element)


    @staticmethod
    def kvadratura_materijala(material, kolicina):
        try:
            Lista.hash[material]
        except:
            Lista.material.add(material)
            Lista.hash[material] = 0
        Lista.hash[material] += kolicina

