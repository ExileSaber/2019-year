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
except IOError as error:
    print("Error：" + error)

try:
    with open("man_file", "w") as man_file:
        for i in man:
            print(i, file=man_file)
    with open("other_file", "w") as other_file:
        for j in other:
            print(j, file=other_file)
except IOError as error:
    print("Error: " + error)
