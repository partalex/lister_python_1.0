from Component import Component
from upisi import upisi
from upisi import preuredi

if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    
preuredi()

with open(path, encoding="utf-8") as file:
    line = file.readline()
    while line:
        line = file.readline()
        if line != '':
            try:
                Component(line)
            except:
                print(line)
                pass

upisi()