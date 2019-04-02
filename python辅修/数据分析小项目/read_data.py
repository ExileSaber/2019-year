def clean(i):
    if "\n" in i:
        return int(i[:len(i)])
    else:
        return int(i)

def get_sales():
    try:
        with open("car.csv") as the_file:
            all_sale_1 = []
            for one_line in the_file:
                if one_line.find("#") == -1:
                    sale = one_line.strip().split(",")
                    all_sale_1.append(sale)
            return all_sale_1

    except IOError as error:
        print("Error:" + error)


