from datetime import datetime

odds = [1, 3, 5, 7, 9]
time = datetime.today().minute
if time in odds:
    print("True")
else:
    print("False")