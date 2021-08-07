from element import Element
from lista import Lista
from upisi import Lista


kolone = ["RB;",
          "DUZINA;",
          "KT;",
          "SIRINA;",
          "KT;",
          "OZNAKA;",
          "T;",
          "KOM;",
          "Materijal;",
          "Kvadratura materijala;"
          "Duzni metar materijala;",
          "Duzni metar trake"
          ]
def preuredi():
    with open('ulaz.csv', "a", encoding="utf-8") as file:
        file.write("\n")

def upisi():
    with open('Izlaz.csv', "w", encoding="utf-8") as file:
        file.writelines(kolone)
        for line in  Lista.component_lista:
            file.write('\n' + str(line))
        file.write('\n')
        for k in Lista.material:
            file.write('\n' + k + ";" + str(Lista.hash[k]).replace(".", ","))
