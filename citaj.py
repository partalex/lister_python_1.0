import csv
import re
from lista import *
from element import *

def read(ulaz):
    with open(ulaz, 'r') as file:
        input_list = csv.reader(file)

        next(input_list)
        for line in input_list:
            generic = re.search("^generic_", line[1])
            try:
                if generic != None:
                    raise Exception('Genericka komponenta je u pitanju, ne upisuj je u listu')
            except:
                continue

            comp = Element(line, 1)

            Lista.ulaz_csv[line[0]]["komponente"].append(comp)





