from Klase import Component
from Klase import List
from upisi import List


kolone = ["RB;",
          "DUZINA;",
          "KT;",
          "SIRINA;",
          "KT;",
          "OZNAKA;",
          "T;",
          "KOM;",
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
        for line in  List.component_lista:
            file.write('\n' + str(line))
        file.write('\n')
        for k in List.material:
            file.write('\n' + k + ";" + str(List.hash[k]).replace(".", ","))
