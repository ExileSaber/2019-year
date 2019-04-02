def clean(x):
    if "-" in x:
        splitter = "-"

    elif ":" in x:
        splitter = ":"
    else:
        return x
    (mins, secs) = x.split(splitter)
    return (mins + "." + secs)

with open("james.txt") as fil:
    data = fil.readline()
list_1 = data.strip().split(",")
clean_list_1 = [clean(x) for x in list_1]

with open("julie.txt") as fil:
    data = fil.readline()
list_2 = data.strip().split(",")
clean_list_2 = [clean(x) for x in list_2]

with open("mikey.txt") as fil:
    data = fil.readline()
list_3 = data.strip().split(",")
clean_list_3 = [clean(x) for x in list_3]

with open("sarah.txt") as fil:
    data = fil.readline()
list_4 = data.strip().split(",")
clean_list_4 = [clean(x) for x in list_4]

print(sorted(set(clean_list_1))[0: 3])
print(sorted(set(clean_list_2))[0: 3])
print(sorted(set(clean_list_3))[0: 3])
print(sorted(set(clean_list_4))[0: 3])
