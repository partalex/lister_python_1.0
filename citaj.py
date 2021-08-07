import csv
import re
import element
import lista


def read(ulaz):
    with open(ulaz, 'r') as file:
        input_list = csv.reader(file)

        next(input_list)
        for line in input_list:
            generic = re.search("^generic_", line[1])
            if generic is not None:
                continue
            comp = element.Element(line)
            lista.Lista.ulaz_csv[line[0]]["komponente"].append(comp)
