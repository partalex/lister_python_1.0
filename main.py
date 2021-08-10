import citaj_csv
import upisi_csv
import materijal
import traka
import element

if __name__ == "__main__":
    import sys

    path = sys.argv[1]

citaj_csv.Citaj.read(path)

# for line in materijal.Materijal.csv_array():
#     print(line)
# for line in element.Element.csv_array():
#     print(line)
# for line in traka.Traka.csv_array():
#     print(line)

upisi_csv.upisi()
