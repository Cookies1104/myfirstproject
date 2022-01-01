import math


def fun_quit_program():
    x = input()
    if x == 'q':
        exit()
    return x


def fun_rate_calculate_2(variable, matrix, row_result):
    while True:
        x = 0
        while variable > matrix[0][x]:
            x += 1
        x = matrix[row_result][x]
        break
    return x


def func_enter_number_int():
    while True:
        try:
            x = int(
                fun_quit_program())
            while x <= 0:
                print('Введены не коректные данные, повторите ввод: ')
                x = int(fun_quit_program())
            break
        except:
            print('Введены не коректные данные, повторите ввод: ')
    return x


def func_enter_number_float():
    while True:
        try:
            x1 = float(
                fun_quit_program())
            while x1 <= 0:
                print('Введены не коректные данные, повторите ввод: ')
                x1 = float(fun_quit_program())
            break
        except:
            print('Введены не коректные данные, повторите ввод: ')
    return x1


def fun_answer_yes_no():
    while True:
        try:
            x = fun_quit_program()
            while x not in ('yes', 'no', 'Yes', 'No', 'Y', 'y', 'n', 'N'):
                print('Введены не коректные данные, повторите ввод: ')
                x = fun_quit_program()
            break
        except:
            print('Введены не коректные данные, повторите ввод: ')
    return x


def fun_check_list(list):
    while True:
        try:
            x = func_enter_number_float()
            while x not in list:
                print('Введены не коректные данные, повторите ввод: ')
                x = func_enter_number_float()
            break
        except:
            print('Введены не коректные данные, повторите ввод: ')
    return x


def fun_closest_value(value, iterable):
    random_list = []
    for i in iterable:
        random_list.append((abs(value - i), i))
    result = min(random_list)
    return result[1]


V_list = (0.25, 0.315, 0.4, 0.5, 0.63, 0.8, 1, 1.25, 1.6, 2, 2.5, 3.15, 4, 5, 6.3)  # standard speeds
B_list = (-1, 400, 650, 800, 1000, 1200, 1400, 1600, 2000)  # standard width belt
material_size_list = (-1, 80, 160, 350, 1000000)  # material size
friction_list = (0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5)
drum_girth_angle_list = (180, 190, 200, 210, 240, 360)
drum_diameter_list = (155, 190, 216, 240, 270, 320, 373, 420, 525, 625)
rate_V_max = [[1.6, 2, 2.5, 3.15, 4, 4, 5, 6.3],  # material size < 80 mm
              [1.6, 1.6, 2, 2.5, 2.5, 3.15, 4, 5],  # material size < 160 mm
              [False, False, 1.6, 1.6, 2, 2.5, 3.15, 4],  # material size < 350 mm
              [False, False, False, False, 2, 2, 2.5, 3.15]]  # material size > 350 mm
rate_C = [[30, 30, 30, 30, 35, 35, 35, 35, 40, 40, 40, 40, 45, 45, 45, 45],  # angle_phi
          [10, 15, 18, 22, 10, 15, 18, 22, 10, 15, 18, 22, 10, 15, 18, 22],  # angle_beta
          [296, 282, 267, 259, 319, 302, 288, 276, 338, 320, 304, 288, 358, 340, 322, 305]]  # rate_C
rate_q_l = {400: 3.6, 500: 4.6, 650: 5.9, 800: 8, 1000: 14, 1200: 16.8, 1400: 19.6, 1600: 26.7, 2000: 33.4}  # belt width
rate_q_p = {400: 7.8, 500: 8.2, 650: 9.6, 800: 19.2, 1000: 22.2, 1200: 26.6, 1400: 33.5, 2000: 62.5}  # belt width
rate_q_p1 = {400: 2.2, 500: 2.7, 650: 4, 800: 7, 1000: 8.5, 1200: 12.2, 1400: 17, 1600: 18, 2000: 28.5}
rate_abrasiveness = [0, 5, 15, 25]
rate_density = [[1, 1.7, 2.3, 2.7, 1000000],  # material density
                [0, 0.2, 0.4, 0.5, 0.7]]  # rate
rate_drop_height = [[300, 800, 1500, 1000000],
                    [0.2, 0.5, 0.7, 1]]
rate_w = [[20, 50, 75, 100],  # point_w
          [0.02, 0.025, 0.045, 0.055],  # when length conveyor <= 100 m
          [0.018, 0.022, 0.042, 0.05]]  # when length conveyor > 100 m
rate_friction = [[20, 50, 75, 100],  # point_w
                 [0.5, 0.4, 0.25, 0.15],  # when lining - yes
                 [0.35, 0.3, 0.2, 0.15]]  # when lining - no
matrix_rate_J = [[0, 2.66, 2.55, 2.48, 2.37, 2.14],  # when friction = 0.15
                 [0, 2.14, 2.06, 1.99, 1.92, 1.76],  # when friction = 0.2
                 [0, 1.84, 1.77, 1.72, 1.67, 1.54],  # when friction = 0.25
                 [0, 0.64, 0.59, 0.54, 0.5, 0.4],  # when friction = 0.3
                 [0, 1.5, 1.46, 0.42, 1.38, 1.31],  # when friction = 0.35
                 [0, 1.4, 1.36, 1.33, 1.3, 1.23]]  # when friction = 0.4 and >
matrix_rate_ph = ((0, 1.6, 1.65, 1.69, 1.73, 1.88),  # when friction = 0.15
                  (0, 1.88, 1.94, 2.01, 2.08, 2.31),  # when friction = 0.2
                  (0, 2.2, 2.29, 2.4, 2.5, 2.85),  # when friction = 0.25
                  (0, 2.57, 2.71, 2.85, 3.01, 3.52),  # when friction = 0.3
                  (0, 3.01, 3.2, 3.4, 3.61, 4.34),  # when friction = 0.35
                  (0, 3.52, 3.78, 4.05, 4.34, 5.35))  # when friction = 0.4 and >
# idlers_dictionary = {400: 108, 500: 108, 650: 127, 800: 127, 1000: 127, 1200: 159, 1400: 159, 1600: 194, 2000: 194}
l_p_dictionary = {400: (1.6, 1.5, 1.5, 1.5, 1.2, 1.2),
                  500: (1.6, 1.5, 1.4, 1.2, 1.2, 1),
                  650: (1.5, 1.4, 1.4, 1.2, 1, 1),
                  800: (1.5, 1.4, 1.4, 1.4, 1.2, 1),
                  1000: (1.4, 1.4, 1.2, 1, 1, 0.9),
                  1200: (1.4, 1.2, 1.2, 1, 1, 0.9),
                  1400: (1.3, 1.2, 1.2, 1, 1, 0.9),
                  1600: (1.3, 1.2, 1.2, 1, 1, 0.9),
                  2000: (1.3, 1.2, 1.2, 1, 1, 0.9)}
density_list = (0.5, 0.8, 1.2, 1.6, 2, 1000)
rate_k_drum = ((25, 50, 75, 100),
               (0.63, 0.63, 0.8, 1),
               (0.5, 0.63, 0.8, 1),
               (0.4, 0.5, 0.63, 0.63),
               (0.32, 0.4, 0.4, 0.4))
length_drum_dictionary = {400: 500, 500: 600, 650: 750, 800: 950, 1000: 1150, 1200: 1400, 1400: 1600, 1600: 1800,
                          2000: 2200}
width_conveyor = {400: 700,
                  500: 800,
                  650: 950,
                  800: 1150,
                  1000: 1350,
                  1200: 1600,
                  1400: 1800,
                  1600: 2050,
                  2000: 2600}
rate_shaft = {35: 60,
              40: 60,
              45: 60,
              50: 70,
              55: 70,
              60: 80,
              65: 80,
              70: 90,
              75: 90,
              80: 100,
              90: 110,
              100: 120}


"""This program performs a data request from the user, followed by the calculation and output of the received data"""
answer = 'yes'
while answer in ('Yes', 'yes', 'y', 'Y'):
    print('Описание программы:' +
          '\n  Данная программа предназначена для расчёта ленточных конвейеров с углом роликоопор 30 градусов.' +
          '\nСпециальные команды:' +
          '\n - для выхода из программы введите - "q".')
    # Раздел 2 пособия. Определение основных параметров ленточных конвейеров
    print('Введите потребную производительность конвейера в т/ч Q: ')
    Q_p = func_enter_number_float()  # потребная производительность
    print('Введите количество конвейеров в линии: ')
    n = func_enter_number_int()
    k_n = 1.2  # коэффициент неравномерности загрузки конвейерной линии (для равномерно грузопотока 1-1.2)
    k_v = 0.7  # коэффициент использования конвейерной линии по времени (0.7-0.95)
    k_g = 0.96  # коэффициент готовности конвейерной линии
    Q_calculated = math.ceil(Q_p * k_n / (k_v * k_g ** n))  # необходимая расчётная производительность;

    print('Введите тип материала (Щебень - 1,): ')
    material = func_enter_number_int()
    while material >= 2:
        print('Введены не коректные данные, повторите ввод: ')
        material = func_enter_number_int()
    print("Введите максимальный размер кусков транспортируемого материала а', мм:")
    material_size = func_enter_number_float()
    while material_size > 900:
        print('Введены не коректные данные, повторите ввод: ')
        material_size = func_enter_number_float()

    # Выбор скорости и ширины ленты
    if str(material) in ('1'):
        material = 'Щебень'
        density = 1.250  # плотность материала т/м³;
        angle_phi = 35  # угол естественного откоса в градусаох;
        angle_conveyor_max = 18
        abrasiveness = 3

    print('Конвейер работает на спуск? yes/no:')
    answer_ascent_or_descent = fun_answer_yes_no()
    if answer_ascent_or_descent in ('yes', 'Yes', 'Y', 'y'):
        V_max = 1.6  # maximum speed
        angle_conveyor_max = angle_conveyor_max - 8
        angle_phi = angle_phi - 8
        ascent_or_descent = 1
    else:
        ascent_or_descent = 0

    print('Введите длину горизонтальной проекции конвейера L в мм: ')
    length_conveyor = func_enter_number_float()
    print('Введите высоту подъёма груза конвейером H в мм: ')
    height_conveyor = func_enter_number_float()
    angle_beta = int(180 / math.pi * height_conveyor / length_conveyor)
    while angle_beta > angle_conveyor_max:
        print('Угол конвейера превышает допустимый, измените значения:')
        print('Введите длину горизонтальной проекции конвейера L в мм: ')
        length_conveyor = func_enter_number_float()
        print('Введите высоту подъёма груза конвейером H в мм: ')
        height_conveyor = func_enter_number_float()
        angle_beta = int(180 / math.pi * height_conveyor / length_conveyor)

    k_b = 2  # 2 - для рядового груза и 3.3 ддля сортированного;
    B_calculated = material_size * k_b + 200  # предварительный расчёт ширины ленты;

    V_max = 1.6  # constant
    V_calc = 100  # constant
    index_B = 0  # constant
    while V_calc > V_max:
        while B_calculated > B_list[index_B]:
            index_B += 1
        B = B_list[index_B]

        if ascent_or_descent == 0:
            x = 0
            while B != B_list[x]:
                x += 1
            B1 = x
            x = 0
            while material_size >= material_size_list[x]:
                x += 1
                B2 = x
            V_max = rate_V_max[B2][B1]

        if angle_phi in range(0, 31):
            C1 = 1
        elif angle_phi in range(31, 36):
            C1 = 2
        elif angle_phi in range(36, 41):
            C1 = 3
        else:
            C1 = 4
        if angle_beta in range(0, 11):
            C2 = 1
        elif angle_beta in range(11, 16):
            C2 = 2
        elif angle_beta in range(16, 19):
            C2 = 3
        else:
            C2 = 4
        C = rate_C[2][C1 * C2 - 1]
        V_calc = round(Q_calculated / (B ** 2 * C * density) * 1000 * 1000, 2)
        index_B += 1

    x = 0
    while V_calc > V_list[x]:
        x += 1
    V = V_list[x]

    Q = round((B / 1000) ** 2 * C * V * density, 2)

    # Раздел 3 пособия. Тяговый расчёт. Приближенный метод.
    if material_size <= 80:
        point_material_size = 0
    elif material_size <= 150:
        point_material_size = 8
    elif material_size <= 350:
        point_material_size = 18
    else:
        point_material_size = 25

    point_abrasiveness = rate_abrasiveness[abrasiveness - 1]

    point_density = point_material_size * fun_rate_calculate_2(density, rate_density, 1)

    print('Введите высоту падения груза на ленту в мм: ')
    drop_height = func_enter_number_float()
    point_drop_height = fun_rate_calculate_2(drop_height, rate_drop_height, 1)
    print('Скорость и направление движения груза и ленты в месте загрузки близки? yes/no: ')
    answer_point_speed = fun_answer_yes_no()
    if answer_point_speed in ('yes', 'Yes', 'y', 'Y'):
        point_speed = 0
    else:
        point_speed = 0.4
    point_speed = point_speed * point_abrasiveness
    print('Воздействие атмосферных осадков или грузов с высокой влажностью. yes/no: ')
    answer_point_precipitation = fun_answer_yes_no()
    if answer_point_precipitation in ('yes', 'Yes', 'y', 'Y'):
        point_precipitation = 10
    else:
        point_precipitation = 0
    print('Условия технического обслуживания затруднительные? yes/no: ')
    answer_point_conditions = fun_answer_yes_no()
    if answer_point_conditions in ('yes', 'Yes', 'y', 'Y'):
        point_conditions = 20
    else:
        point_conditions = 0
    point_w = point_material_size + point_abrasiveness + point_density + point_drop_height + point_speed + 10 + \
              point_precipitation + point_conditions

    while point_w > 100:
        print('В данных условиях ленточный конвейер использовать не допускается. Улучшите условия '
              'эксплуатации конвейера.')
        print('Введите высоту падения груза на ленту в мм: ')
        point_drop_height = fun_rate_calculate_2(func_enter_number_float(), rate_drop_height, 1)
        print('Скорость и направление движения груза и ленты в месте загрузки близки? yes/no: ')
        if fun_answer_yes_no() in ('yes', 'Yes', 'y', 'Y'):
            point_speed = 0
        else:
            point_speed = 0.4
        point_speed = point_speed * point_abrasiveness
        print('Воздействие атмосферных осадков или грузов с высокой влажностью. yes/no: ')
        if fun_answer_yes_no() in ('yes', 'Yes', 'y', 'Y'):
            point_precipitation = 10
        else:
            point_precipitation = 0
        print('Условия технического обслуживания затруднительные? yes/no: ')
        if fun_answer_yes_no() in ('yes', 'Yes', 'y', 'Y'):
            point_conditions = 20
        else:
            point_conditions = 0
        point_w = point_material_size + point_abrasiveness + point_density + point_drop_height + point_speed + 10 + \
                  point_precipitation + point_conditions

    if (length_conveyor ** 2 + height_conveyor ** 2) ** (1 / 2) <= 100000:
        w = fun_rate_calculate_2(point_w, rate_w, 1)
    else:
        w = fun_rate_calculate_2(point_w, rate_w, 2)

    g = 9.81  # ускорение свободного падения
    k_d = 10.396 * (((length_conveyor ** 2 + height_conveyor ** 2) ** (1 / 2) / 1000) ** (-0.383))
    q_r = Q * g / (36 * V)  # масса груза на ленте
    q_l = rate_q_l[B]  # масса ленты
    q_p = rate_q_p[B]  # масса роликоопор верхней ветви
    q_p1 = rate_q_p1[B]  # масса роликоопор нижней ветви

    if ascent_or_descent == 0:
        P = (k_d * length_conveyor * w * (q_r + q_p + q_p1 + 2 * q_l) + q_r * height_conveyor) / 1000
    else:
        P = math.fabs((k_d * length_conveyor * w * (q_r + q_p + q_p1 + 2 * q_l) - q_r * height_conveyor)) / 1000

    print('Наличие футеровки на приводном барабане? yes/no: ')
    lining = fun_answer_yes_no()
    if lining in ('Yes', 'yes', 'y', 'Y'):
        friction = fun_rate_calculate_2(point_w, rate_friction, 1)
    else:
        friction = fun_rate_calculate_2(point_w, rate_friction, 2)

    x = 0
    while friction != friction_list[x]:
        x += 1
    rate_J1 = x
    if rate_J1 == 6:
        rate_J1 = 5

    print('Введите угол обхвата барабана(180-240°):')
    drum_girth_angle = func_enter_number_float()
    while drum_girth_angle < 180 or drum_girth_angle > 240:
        print('Введено не корректное значение. Повторите ввод: ')
        drum_girth_angle = func_enter_number_float()
    x = 0
    while drum_girth_angle >= drum_girth_angle_list[x]:
        x += 1
    rate_J2 = x
    rate_J = matrix_rate_J[rate_J1][rate_J2]

    S_nb = P * rate_J
    S_sb = S_nb - P
    print(S_sb)

    # Определение мощности привода.
    motor_power = P * V / 100

    if motor_power > 50:
        k = 1.2
    else:
        k = 1.1

    KPD = 0.92
    motor_power_calc = motor_power * k / KPD
    print('При КПД двигателя - ', str(KPD), '%. Расчётная мощность привода - ', str(math.ceil(motor_power_calc)),
          ' кВт.')
    print('Изменить КПД двигателя? yes/no')
    x = fun_answer_yes_no()
    while x in ('yes', 'Yes', 'y', 'Y'):
        print('Введите КПД двигателя в диапазоне 0,86-0,92: ')
        KPD = func_enter_number_float()
        while KPD < 0.86 or KPD > 0.92:
            print('Введены не корректные данные, повторите ввод:')
            KPD = func_enter_number_float()
        motor_power_calc = motor_power * k / KPD
        print('При КПД двигателя - ', str(KPD), '%. Расчётная мощность привода - ', str(math.ceil(motor_power_calc)),
              ' кВт.')
        print('Изменить КПД двигателя? yes/no')
        x = fun_answer_yes_no()

    # Раздел 4 пособия. Выбор основного оборудования.
    z_p = 7
    while z_p > 6:
        k_p = 200  # daN/sm nominal strength, даН/см номинальная прочность прокладки
        factor_safety = 9
        z_p = math.ceil(S_nb * factor_safety / (B * k_p * 0.1))
        if z_p > 5 and angle_beta >= 10:
            new_factor_safety = 10
            z_p = math.ceil(z_p * new_factor_safety / factor_safety)
        elif z_p > 5 and angle_beta < 10:
            new_factor_safety = 9
            z_p = math.ceil(z_p * new_factor_safety / factor_safety)
        elif z_p < 5 and angle_beta >= 10:
            new_factor_safety = 9
            z_p = math.ceil(z_p * new_factor_safety / factor_safety)
        elif z_p < 5 and angle_beta < 10:
            new_factor_safety = 8
            z_p = math.ceil(z_p * new_factor_safety / factor_safety)
        if z_p < 3:
            z_p = 3
        if z_p > 6:
            k_p += 100

    x = 0 # constant
    while density >= density_list[x]:
        x += 1
    l_p = l_p_dictionary[B][x]  # distance top rollers

    if material_size >= 350:
        l_p = round(l_p * 0.9, 1)


    x = 2.5  # constant
    l_p2 = x * l_p  # distance down rollers
    while l_p2 > 3.5:
        x -= 0.05
        l_p2 = x * l_p
    while S_sb < (8 * q_l * l_p2 * math.cos(math.radians(angle_beta))):
        x -= 0.05
        l_p2 = x * l_p

    if B in (400, 500, 600):
        if density < 1.6 and V < 2:
            d_rollers = 89
        elif density < 2 and V < 2.5:
            d_rollers = 108
    if B == 800 and density < 1.6 and V < 1.6:
        d_rollers = 89
    if B in (800, 1000, 1200):
        if density < 1.6 and V < 2.5:
            d_rollers = 108
        elif density < 2 and V < 2.5:
            d_rollers = 127
        elif density < 3.15 and V < 4:
            d_rollers = 159
    if B in (1400, 1600, 2000) and density < 3.15 and V < 3.1:
        d_rollers = 194
    if B == 1400 and density < 3.15 and V < 4:
        d_rollers = 194
    if B in (1600, 2000) and density < 3.15 and V < 6.3:
        d_rollers = 194

    # Определение диаметра барабанов и валов.
    if angle_beta <= 10:
        S_g = k_p * B * 0.1 * z_p / new_factor_safety
    else:
        S_g = k_p * B * 0.1 * z_p / new_factor_safety

    k_s = round(S_nb / S_g)
    x = 0
    while k_s * 100 > rate_k_drum[0][x]:
        x += 1
    k_drum_drive = rate_k_drum[1][x]  # table 24
    k_drum_driven = rate_k_drum[2][x]  # table 24
    k_drum_revolving = rate_k_drum[3][x]  # table 24
    k_drum_deflecting = rate_k_drum[4][x]  # table 24

    k_z = 175  # table 23

    drive_drum_diameter = fun_closest_value(k_z * k_drum_drive * z_p, drum_diameter_list)
    driven_drum = fun_closest_value(k_z * k_drum_driven * z_p, drum_diameter_list)
    revolving_drum = fun_closest_value(k_z * k_drum_revolving * z_p, drum_diameter_list)
    deflecting_drum = fun_closest_value(k_z * k_drum_deflecting * z_p, drum_diameter_list)

    rate_ph = matrix_rate_ph[rate_J1][rate_J2]
    pressure_drum = 0.3  # constant
    permissible_pressure = 0.2  # constant
    while pressure_drum > permissible_pressure:
        pressure_drum = (3600 * S_nb * (rate_ph + 1)) / (drum_girth_angle * math.pi * B * drive_drum_diameter * rate_ph)
        if pressure_drum > permissible_pressure:
            x = drum_diameter_list.index(drive_drum_diameter)
            drive_drum_diameter = drum_diameter_list[x + 1]

    torque = round(0.5 * P * drive_drum_diameter, 2)

    length_drive_drum = length_drum_dictionary[B]
    distance_between_bearings = width_conveyor[B]
    shaft_drive_drum = ((((S_nb + S_sb) * 10) / 2) * ((distance_between_bearings - length_drive_drum) * 0.001) / (
            65 * 1000000)) ** (1 / 3) * 1000
    shafts = []
    for i in rate_shaft:
        shafts.append(i)
    random_list = []
    for i in rate_shaft.keys():
        random_list.append((abs(shaft_drive_drum - i), i))
    result = min(random_list)
    if result[1] < shaft_drive_drum:
        index_result = shafts.index(result[1])
        index_result += 1
        shaft_drive_drum = shafts[index_result]
    else:
        shaft_drive_drum = result[1]

    rotation_speed_drive_drum = round(60 / (math.pi * drive_drum_diameter / 1000 / V))

    # Определение тормозного момент и необходимости установки тормоза
    k_i = 0.55  # constant
    braking_torque = 0.5 * (q_r * height_conveyor) - k_i * (P - q_r * height_conveyor) * drive_drum_diameter * KPD
    if q_r * height_conveyor <= P:
        brake = 'Yes'
    else:
        brake = 'No'

    #  Определение параметров натяжного устройства
    k_c = 0.3
    tension_length_inst = k_c * B
    if angle_beta <= 10:
        k_y = 0.85
    else:
        k_y = 0.65
    e_o = 0.015
    tension_length_work = k_y * k_s * e_o * length_conveyor

    tension_length = round(tension_length_inst + tension_length_work)

    # Вывод данных
    print()
    print('Введённые данные:' +
          '\nПотребная производительность в т/ч - ' + str(Q_p) +
          '\nКоличество конвейеров в линии в шт - ' + str(n) +
          '\nТип материала - ' + material +
          '\nРазмер кусков материала в мм - ' + str(material_size) +
          '\nКонвейер работает на спуск - ' + answer_ascent_or_descent +
          '\nДлина горизонтальной проекции конвейера в мм - ' + str(length_conveyor) +
          '\nВысота подъёма материала конвейером в мм - ' + str(height_conveyor) +
          '\nВысота падения груза на ленту в мм - ' + str(drop_height) +
          '\nСкорость и направление движения груза и ленты в месте загрузки близки - ' + answer_point_speed +
          '\nВоздействие атмосферных осадков или грузов с высокой влажностью - ' + answer_point_precipitation +
          '\nУсловия технического обслуживания - ' + answer_point_conditions +
          '\nФутеровка на приводном барабане - ' + lining +
          '\nУгол обхвата барабана - ' + str(drum_girth_angle) +
          '\nКПД двигателя - ' + str(KPD)
          )
    print()
    print('Полученные данные конвейера:' +
          '\nУгол конвейера - ' + str(angle_beta) +
          '\nМаксимальная скорость конвейера в м/с - ' + str(V_max) +
          '\nУгол естественного откоса материала - ' + str(angle_phi) +
          '\nМаксимальный угол конвейера для данного типа материала  - ' + str(angle_conveyor_max) +
          '\nШирина ленты в мм - ' + str(B) +
          '\nСкорость конвейера для данной производительности в т/ч - ' + str(V) +
          '\nОкружное усилие на приводном барабане в даН - ' + str(round(P)) +
          '\nМощность привода в кВт - ' + str(math.ceil(motor_power_calc)) +
          '\nКоличество тяговых прокладок - ' + str(z_p) +
          '\nПрочность тяговых прокладок - ' + str(k_p) +
          '\nРасстояние между верхними роликоопорами в м - ' + str(l_p) +
          '\nРасстояние между нижними роликоопорами в м - ' + str(round(l_p2, 2)) +
          '\nДиаметр роликов в мм - ' + str(d_rollers) +
          '\nДиаметр приводного барабана в мм - ' + str(drive_drum_diameter) +
          '\nДиаметр ведомого барабана в мм - ' + str(driven_drum) +
          '\nДиаметр оборотного барабана в мм - ' + str(revolving_drum) +
          '\nДиаметр оклоняющий барабана в мм - ' + str(deflecting_drum) +
          '\nКрутящий момент на валу ведущего барабана в Нм - ' + str(torque) +
          '\nДиаметр вала приводного барабана в мм - ' + str(shaft_drive_drum) +
          '\nНеобходимость установки тормоза - ' + brake +
          '\nХод натяжного устройства в мм - ' + str(tension_length) +
          '\nЧастота вращения приводного барабана об/мин - ' + str(rotation_speed_drive_drum))
    print()
    print('Перезапустить программу? yes/no')
    answer = fun_answer_yes_no()
