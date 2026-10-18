import csv

data = []
with open('r-m-c.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows1 = list(reader)
    print('Записей в 1м файле:', len(rows1))
    for row in rows1:
        if row not in data:
            data.append(row)

with open('rmc.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows2 = list(reader)
    print('Записей во 2м файле:', len(rows2))
    for row in rows2:
        if row not in data:
            data.append(row)

print('Уникальных записей:', len(data))
with open('result.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)