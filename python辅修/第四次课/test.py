import Athlete

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return Athlete.Athlete(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None


james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are:'" + str(james.top3()))

vera = Athlete.Athlete('Li')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['1.34', '1.42', '1.86', '1.43'])
print(vera.top3())
print(vera.average())
