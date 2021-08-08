import materijal
import traka


def materijal_statistika():
    with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\Statistika Materijal.csv", "w", encoding="utf-8") as file:
        data = materijal.Materijal.csv_statistika()
        for line in data:
            file.write(line + "\n")


def materijal_liste():
    for oznaka in materijal.Materijal.set_Materijali:
        with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\" + oznaka + ".csv", "w", encoding="utf-8") as file:
            data = materijal.Materijal.vrste_Materijala[oznaka].csv_export()
            for line in data:
                file.write(line + "\n")


def traka_statistika():
    with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\Statistika Traka.csv", "w", encoding="utf-8") as file:
        data = traka.Traka.csv_statistika()
        for line in data:
            file.write(line + "\n")


def upisi():
    materijal_statistika()
    materijal_liste()
    traka_statistika()

