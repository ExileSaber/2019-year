import read_data
import Car
import pickle_store

Month = ['AUG', 'SEP', 'OCT', 'NOV', 'DEC']

def get_car_data():
    data = read_data.get_sales()
    car_list = []
    for i in data:
        car_list.append(Car.Car(i[0], i[1], i[2], i[3:]))
    return car_list


car_List = get_car_data()
top_three = []
for car in car_List:
    print("brand:" + car.brand + "     price:" + car.price + "     company:" + car.company)
    print("top sale: {}".format(car.top1()[0]) + "     the month: {}".format(Month[car.top1()[1]]))
    print("average sale: {}".format(car.average()))
    print("the number of sales greater than 10000: {}".format(car.best()[0]))
    print("Months of sales greater than 10000: {}".format([Month[i] for i in car.best()[1]]))
    print("---------------------------------------------------------------------\n")
    top_three.append(car.sort())

pickle_store.save(top_three)
