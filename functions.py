def quit_program():
    x = input()
    if x == 'q':
        exit()
    return x


def enter_number_int():
    while True:
        try:
            x = int(
                quit_program())
            while x <= 0:
                print('Введены не коректные данные, повторите ввод: ')
                x = int(quit_program())
            break
        except:
            print('Введены не коректные данные, повторите ввод: ')
    return x


def enter_number_float():
    while True:
        try:
            x1 = float(
                quit_program())
            while x1 <= 0:
                print('Введены не коректные данные, повторите ввод: ')
                x1 = float(quit_program())
            break
        except:
            print('Введены не коректные данные, повторите ввод: ')
    return x1


def answer_yes_no():
    while True:
        try:
            x = quit_program()
            while x not in ('yes', 'no', 'y', 'n'):
                print('Введены не коректные данные, повторите ввод: ')
                x = quit_program()
                x.lower()
            break
        except:
            print('Введены не коректные данные, повторите ввод: ')
    return x