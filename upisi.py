import lista

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

def upisi():
    with open('Izlaz.csv', "w", encoding="utf-8") as file:
        file.writelines(kolone)
        for line in lista.Lista.component_lista:
            file.write('\n' + str(line))
        file.write('\n')
        for k in lista.Lista.material:
            file.write('\n' + k + ";" + str(lista.Lista.hash[k]).replace(".", ","))
