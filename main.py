import citaj
import lista

if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    
citaj.read(path) # cita listu

for key in lista.Lista.ulaz_csv:
    print('\n' + key)
    for koka in lista.Lista.ulaz_csv[key]["komponente"]:
        print(koka)