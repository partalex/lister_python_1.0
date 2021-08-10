import csv
import re
import element


class Citaj:
    redni_broj = 0

    @staticmethod
    def read(ulaz):
        with open(ulaz, 'r') as file:
            input_list = csv.reader(file)

            next(input_list)
            for line in input_list:
                generic = re.search("^generic_", line[1])
                if generic is not None:
                    continue
                element.Element(line)
