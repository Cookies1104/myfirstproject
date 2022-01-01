import json as js
import functions as fun
from calculate import Calculate


"""This program performs a data request from the user and write it to a file "Saves.json"."""
answer = 'yes'
while answer in ('Yes', 'yes', 'y', 'Y'):
    with open('Saves.json') as file_saves:
        saves = js.load(file_saves)
    storage = {}

    print('Описание программы:' +
          '\n  Данная программа предназначена для расчёта ленточных конвейеров с углом роликоопор 30 градусов.' +
          '\nСпециальные команды:' +
          '\n - для выхода из программы введите - "q".'
          )
    storage_keys = []
    for key in saves.keys():
        storage_keys.append(key)
    print('Существующие имена: ' + str(storage_keys))
    print('Введите имя конвейера (Например: NMK2_BC1):')
    name_conveyor = fun.quit_program()
    name_conveyor.lower()
    while name_conveyor.lower() in storage_keys:
        print('Такое имя уже существует. Введите другое.')
        name_conveyor = fun.quit_program()
        name_conveyor.lower()

    print('Введите потребную производительность конвейера в т/ч Q: ')
    capacity = fun.enter_number_float()
    storage['capacity'] = capacity

    print('Введите количество конвейеров в линии: ')
    number_of_conveyor = fun.enter_number_int()
    storage['number of conveyor'] = number_of_conveyor

    calculate_conveyor = Calculate(name_conveyor, capacity, number_of_conveyor)
    calculate_conveyor.calculate()
    calculate_conveyor.results()

    print('Сохранить расчёт? yes/no')
    save_answer = fun.answer_yes_no()
    if save_answer in ('yes', 'y'):
        saves[name_conveyor.lower()] = storage
        with open('Saves.json', 'w') as file_saves:
            js.dump(saves, file_saves)

    print('Перезапустить программу? yes')
    answer = fun.answer_yes_no()
    if answer in ('no', 'n'):
        while True:
            fun.quit_program()



