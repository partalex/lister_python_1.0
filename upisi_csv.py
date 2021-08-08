import materijal
import traka
import element


def element_lista():
    with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\Elementi.csv", "w", encoding="utf-8") as file:
        for line in element.Element.csv_array():
            file.write(line)


def materijal_statistika():
    with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\Statistika Materijal.csv", "w", encoding="utf-8") as file:
        data = materijal.Materijal.csv_array()
        for line in data:
            file.write(str(line) + "\n")


def materijal_liste():
    for oznaka in materijal.Materijal.set_Materijali:
        with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\Lista " + oznaka + ".csv", "w", encoding="utf-8") as file:
            data = materijal.Materijal.vrste_Materijala[oznaka].csv_export()
            for line in data:
                file.write(line + "\n")


def traka_statistika():
    with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\Statistika Traka.csv", "w", encoding="utf-8") as file:
        data = traka.Traka.csv_array()
        for line in data:
            file.write(line + "\n")


def upisi():
    materijal_statistika()
    materijal_liste()
    traka_statistika()
