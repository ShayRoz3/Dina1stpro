import csv
# print(file.read())
def flower_dict():
        file = open("iris.data.csv", "r")
        flower_dictionary = {}
        cvs_f = list(csv.reader(file))
        print(cvs_f)
        # ran_ge = (cvs_f)
        # for row in cvs_f:
                # print(row)
                # for col in row:
                #         print(col[0:3])
                        # flower_dictionary.update(keys = cvs_f[:-1][-1] )
                        # print(flower_dictionary)
                        # print(col)

flower_dict()