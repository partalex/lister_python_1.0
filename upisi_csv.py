import materijal
import traka
import element

import os
script_dir = os.path.dirname(__file__)
rel_path = "liste"
abs_file_path = os.path.join(script_dir, rel_path)
print(abs_file_path)

def element_lista():
    with open(os.path.join(abs_file_path, "Elementi.csv"), "w", encoding="utf-8") as file:
        for line in element.Element.csv_array():
            file.write(line)


def materijal_statistika():
    with open(os.path.join(abs_file_path, "Statistika Materijal.csv"), "w", encoding="utf-8") as file:
        data = materijal.Materijal.csv_array()
        for line in data:
            file.write(str(line) + "\n")


def materijal_liste():
    for oznaka in materijal.Materijal.set_Materijali:
        with open(os.path.join(abs_file_path, oznaka + ".csv"), "w", encoding="utf-8") as file:
            data = materijal.Materijal.vrste_Materijala[oznaka].csv_export()
            for line in data:
                file.write(line + "\n")


def traka_statistika():
    with open(os.path.join(abs_file_path, "Statistika Traka.csv"), "w", encoding="utf-8") as file:
        data = traka.Traka.csv_array()
        for line in data:
            file.write(line + "\n")


def upisi():
    materijal_statistika()
    materijal_liste()
    traka_statistika()
