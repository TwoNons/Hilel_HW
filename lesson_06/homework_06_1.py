string = input('Натиснiть випадковi клавiшi:\n')
if len(set(string)) > 10:
    print(True)
else:
    print(False)