import pickle
try:
    with open("car.csv") as the_file:
        file_company = []
        for one_line in the_file:
            if one_line.find("#") == -1:
                file_company.append(one_line.split(",")[2])
        print(file_company)

except IOError as error:
    print("Error:" + error)


with open("first.pk", "wb") as file:
    pickle.dump(file_company, file=file)
with open("first.pk", "rb") as file:
    a = pickle.load(file)
    print(a)