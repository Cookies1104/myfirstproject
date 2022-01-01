import math


class Calculate:
    """Расчёт конвейера после ввода данных"""

    def __init__(self, name_conveyor, capacity, number_of_conveyor):
        """Инициализация атрибутов"""
        self.name_conveyor = name_conveyor
        self.capacity = capacity
        self.number_of_conveyor = number_of_conveyor
        self.capacity_calc = 0

    def calculate(self):
        """Выполняет расчёт конвейера по полученным данным"""
        coefficients = {'k_n': 1.2,
                        'k_v': 0.7,
                        'k_g': 0.96}
        self.capacity_calc = math.ceil(
                    self.capacity * coefficients['k_n'] / (coefficients['k_v']
                    * (coefficients['k_g'] ** self.number_of_conveyor)))
        return self.capacity_calc

    def results(self):
        """Выводит полученные результаты расчёта"""
        print('Расчётная производительность конвейера ' + self.name_conveyor +
                ' - ' + str(self.capacity_calc) + ' т/ч.')


