from datetime import datetime

condition = "health"
# weekday = {"1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saturday", "7": "Sunday"}
# today = weekday[str(datetime.today().isoweekday())]
today = "Sunday"

if today == "Saturday":
    print("Party!")
elif today == "Sunday":
    if condition == "Headache":
        print("Recover, then test")
    else:
        print("test")
else:
    print("work,work,work")