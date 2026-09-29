def error(string):
    for i in string:
        try:
            string2 = i.split(',')
            string3 = map(int, string2)
            print(sum(string3))
        except ValueError:
            print('Не можу це зробити!')

string = ['1,2,3,4', '1,2,3,4,50','qwerty1,2,3']
error(string)