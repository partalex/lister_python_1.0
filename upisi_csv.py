import materijal
import traka


def upisi():
    with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\Statistika Materijal.csv", "w", encoding="utf-8") as file:
        data = materijal.Materijal.csv_statistika()

        for line in data:
            file.write(line + "\n")

    for oznaka in materijal.Materijal.set_Materijali:
        with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\" + oznaka + ".csv", "w", encoding="utf-8") as file:
            # data_Materijal = materijal.Materijal.csv_export()
            # for line in data_Materijal:
            #     file.write(line + "\n")
            data = materijal.Materijal.vrste_Materijala[oznaka].csv_export()
            for line in data:
                file.write(line + "\n")

    with open("C:\\Users\\SKT BABA ZOKA\\Desktop\\liste\\trake.csv", "w", encoding="utf-8") as file:
        data_Traka = traka.Traka.csv_export()
        for line in data_Traka:
            file.write(line + "\n")
