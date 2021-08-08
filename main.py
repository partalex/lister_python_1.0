import element
import citaj
import upisi_csv
import materijal
import traka

if __name__ == "__main__":
    import sys

    path = sys.argv[1]

citaj.Citaj.read(path)

# materijal.Materijal.ispisi_sve()
# element.Element.ispisi_sve()
# traka.Traka.ispisi_sve()

upisi_csv.upisi()
