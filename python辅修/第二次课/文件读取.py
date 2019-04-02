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

try:
    man_file = open("man_file", "w")
    other_file = open("other_file", "w")
    for i in man:
        print(i, file=man_file)
    for j in other:
        print(j, file=other_file)
except IOError:
    print("error")
finally:
    man_file.close()
    other_file.close()