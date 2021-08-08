import citaj_csv
import upisi_csv
import materijal
import traka
import element

if __name__ == "__main__":
    import sys

    path = sys.argv[1]

citaj_csv.Citaj.read(path)

materijal.Materijal.ispisi_sve()
element.Element.ispisi_sve()
traka.Traka.ispisi_sve()

upisi_csv.upisi()
