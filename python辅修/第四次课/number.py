def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' +secs)
   
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

'''
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest time are:'" +
      str(sorted(set([sanitize(t) for t in sarah]))[0: 3]))

'''
sarah = get_coach_data('sarah2.txt')
sarah_data = {}
sarah_data['sarah_name'] = sarah.pop(0)
sarah_data['sarah_dob'] = sarah.pop(0)
sarah_data['times'] = sarah
print(sarah_data['sarah_name'] + "'s fastest time are:'" + str(sorted(set([sanitize(t) for t in sarah_data['times']]))[0: 3]))
