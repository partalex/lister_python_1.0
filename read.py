import csv
import re
from List import *
from Component import *


with open("ulaz.csv", 'r') as file:
    input_list = csv.reader(file)

    next(input_list)
    for line in input_list:
        generic = re.search("^generic_", line[1])
        if generic != None:
            # raise Exception('Genericka komponenta je u pitanju, ne upisuj je u listu')
            continue

        comp = Component(line, 1)

        List.svi_materijali[line[0]]["komponente"].append(comp)

for key in List.svi_materijali:
    print(key, ' : ',  List.svi_materijali[key])





