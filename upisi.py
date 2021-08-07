import citaj

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
        for line in citaj.Citaj.component_lista:
            file.write('\n' + str(line))
        file.write('\n')
        for k in citaj.Citaj.material:
            file.write('\n' + k + ";" + str(citaj.Citaj.hash[k]).replace(".", ","))
