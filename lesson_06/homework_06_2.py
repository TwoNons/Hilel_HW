string = input('Введiть слово у якому є літера "h"\n')
count = False
while True:
    if 'h' in string or 'H' in string:
        print('є потрiбна лiтера у текстi')
        break
    else:
        string = input('Нема потрiбноi букви. Введiть слово у якому є літера "h"\n')
