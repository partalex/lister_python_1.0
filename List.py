class List:
    component_lista = []
    material = set()
    hash = {}
    redni_broj = 0

    svi_materijali = {}

    @staticmethod
    def kvadratura_materijala(material, kolicina):
        try:
            List.hash[material]
        except:
            List.material.add(material)
            List.hash[material] = 0
        List.hash[material] += kolicina

