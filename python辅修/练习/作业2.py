def clean(i):
    if "\n" in i:
        return int(i[:len(i)])
    else:
        return int(i)


try:
    with open("car.csv") as the_file:
        all_sale = []
        for one_line in the_file:
            if one_line.find("#") == -1:
                sale = one_line.split(",")[3:]
                all_sale.append(sale)

        all_sale_2 = []
        for sale in all_sale:
            sale_2 = [clean(i) for i in sale]
            all_sale_2.append(sale_2)

        for i in all_sale_2:
            print(sorted(i)[0])

except IOError as error:
    print("Error:" + error)