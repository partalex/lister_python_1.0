import citaj
import csv

import materijal
import traka


def upisi():
    with open('Izlaz.csv', "w", encoding="utf-8") as file:
        data_Materijal = materijal.Materijal.csv_export()
        for line in data_Materijal:
            file.write(line + "\n")

        data_Traka = traka.Traka.csv_export()
        for line in data_Traka:
            file.write(line + "\n")

