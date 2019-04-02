'''
import os
print(os.getcwd())
'''
try:
    with open('sketch2.txt') as the_file:
        '''
        print(the_file.readline(), end='')
        print(the_file.readline())
        the_file.seek(0)
        '''
        for one_line in the_file:
            # if not one_line.find(":") == -1:
            try:
                (role, speak) = one_line.split(":", maxsplit=1)
                print(role, end=" ")
                print("said : ", end="")
                print(speak, end="")
            except ValueError:
                pass
except IOError:
    print("don't have this file")