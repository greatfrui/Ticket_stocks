import csv
#основныке переменные
#забираем названия нужных тикетов
with open('stocks.txt')as file:
    src=file.read()
source_name=src.split('\n')
slovar={}#словарь в котором буду храниться данные по нужным дням
#время и дата по, которым будет проходить отбор
with open('dates_and_time.txt')as file:
    src=file.read()
list_by_data=src.split('\n')
#узнаем нужное значение
with open('value.txt')as file:
    src=file.read()
value=src
#заполнение словоря
for i in range(len(list_by_data)):
    keys=list_by_data[i]
    slovar[keys]=[]
    data_split = list_by_data[i].split(',')
    slovar[keys].append(data_split[0])
    slovar[keys].append(data_split[1])
#цикл, с помощью которого находится нужное значение
for name in source_name:
    #считываем файл по тикету
    with open(f'quotes/{name.lower()}.us.txt') as file:
        src = file.read()
    data_ticket = src.split('\n')#делим данные при помощи абзаца
    #смотрим есть ли в какой-то строке нужная дата и время
    for i in range(len(list_by_data)):
        #поднимаем флаг
        flag=True
        for j in range(len(data_ticket)):
            if list_by_data[i] in data_ticket[j]:
                #если элемент нашёлся флаг опускаем
                flag=False
                data_date = data_ticket[j]
                value_data = ''
                part_nedeed_data = data_date.split(',')
                #находим какое значение нужно отыскать
                if value == 'OPEN':
                    value_data = part_nedeed_data[4].strip('')
                elif value == 'HIGH':
                    value_data = part_nedeed_data[5].strip('')
                elif value == 'LOW':
                    value_data = part_nedeed_data[6].strip('')
                elif value == 'CLOSE':
                    value_data = part_nedeed_data[7].strip('')
                elif value == 'VOL':
                    value_data = part_nedeed_data[8].strip('')
                else:
                    print('некоректно введено значение из файла value.txt')
                    print(value)
                    '''''''''
                    #######################################################3
                    # можно убрать,при записи в таблицу не дает перефразировать число в дату
                if '.' in value_data:
                    if len(value_data.split('.')[1]) == 2:
                        value_data += '0'
                    elif len(value_data.split('.')[1]) == 1:
                        value_data += '00'
                    if len(value_data)==6 :
                        value_data += '0'
                    ######################################################
                    '''''''''
                slovar[list_by_data[i]].append(value_data)
                break#в случае нахождения остальные элементы просматривать смысла нет выходим из цикла
        if list_by_data[i] in slovar.keys() and flag==True:
            slovar[list_by_data[i]].append('')#проверяем был ли найден элемент по итогу цикла,при помощи флага,если нет вносим пустую строку
    print(f'Данные по {name} собраны')
#создаем файл и вносим в него все необходимые данные
name_rows=['','']
for i in range(len(source_name)):
    name_rows.append(source_name[i])#создаю заголовки столбцов
with open('table.csv', 'w', encoding='utf-8',newline='') as file:
    writer = csv.writer(file, delimiter = ";" )
    writer.writerows(
        (
            name_rows,
        )
    )
with open('table.csv','a',newline='')as file:
    writer=csv.writer(file,delimiter = ';' )
    for keys in list_by_data:
        writer.writerow(slovar[keys])
print('Все данные занесены в таблицу')