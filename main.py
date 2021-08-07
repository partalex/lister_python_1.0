import element
import citaj
import materijal

if __name__ == "__main__":
    import sys

    path = sys.argv[1]

citaj.Citaj.read(path)

materijal.Materijal.ispisi_sve()
element.Element.ispisi_sve()
