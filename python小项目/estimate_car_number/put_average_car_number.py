

def put_average_car_number(The_method, mean_number_1, mean_number_2, standard_deviation_1, standard_deviation_2):
    with open('average number', 'a') as f:
        for i in range(0, 5):
            f.write("mean_number:" + str(mean_number_1[i]) + "     " + "standard_deviation:" + str(standard_deviation_1[i]))
            f.write("              ")
        f.write("\n")

        for i in range(0, 5):
            f.write("mean_number:" + str(mean_number_2[i]) + "     " + "standard_deviation:" + str(standard_deviation_2[i]))
            f.write("              ")

        f.write("\n")