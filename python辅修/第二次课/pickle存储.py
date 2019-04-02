import pickle

man = []
other = []
try:
    with open("sketch.txt") as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", maxsplit=1)
                line_spoken = line_spoken.strip()
                if role == "Man":
                    man.append(line_spoken)
                if role == "Other Man":
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError:
    print("The datafile is missing")

with open("man.pk", "wb") as a:
    pickle.dump(man, a)
with open("other.pk", "wb") as b:
    pickle.dump(other, b)

with open("man.pk", "rb") as man:
    a = pickle.load(man)
    print(a)
with open("other.pk", "rb") as other:
    b = pickle.load(other)
    print(b)