from colorama import init, Fore, Back, Style

# Инициализируйте библиотеку
init(autoreset=True)

print()
print(Back.GREEN + "18 вариант класс")

print()
# Python
# Задание: создать класс с полями, указанными в индивидуальном зада-
# Реализовать в классе методы:
# - конструктор по умолчанию;
# - конструктор перезагрузки с параметрами;
# - деструктор для освобождения памяти (с сообщением об уничтожении объекта);
# - функции обработки данных (1 и 2), указанные в индивидуальном задании (табл. 11.2, столбцы 3 и 4);
# - функцию формирования строки информации об объекте.
# Создать проект для демонстрации работы: сформировать объекты со значениями константами и с введенными значениями полей объекта из компонентов Edit.
# Класс родитель и его поля:
# Вектор на плоскости: координаты вектора на плоско-
# сти (x1, yl, x2, y2)
#
# Функция метод 1 обработки данных
# вычислить координаты середины вектора
#
# Функция метод 2 обработки данных
# Равен ли угол наклона вектора 45 градусов?
import math

class VectorOnPlane:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_midpoint(self):
        mid_x = (self.x1 + self.x2) / 2
        mid_y = (self.y1 + self.y2) / 2
        return mid_x, mid_y

    def is_angle_45_degrees(self):
        # Вычисляем угол между вектором и осью X
        angle = math.atan2(self.y2 - self.y1, self.x2 - self.x1)
        angle_degrees = math.degrees(angle)
        return abs(angle_degrees - 45) < 1e-6

    def get_info_string(self):
        return f"Вектор: ({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"

# Пример использования класса
if __name__ == "__main__":
    vector1 = VectorOnPlane(1, 2, 3, 4)
    vector2 = VectorOnPlane(0, 0, 1, 1)

    print(vector1.get_info_string())
    print(f"Середина вектора: {vector1.calculate_midpoint()}")
    print(f"Угол наклона 45 градусов? {vector1.is_angle_45_degrees()}")

    print(vector2.get_info_string())
    print(f"Середина вектора: {vector2.calculate_midpoint()}")
    print(f"Угол наклона 45 градусов? {vector2.is_angle_45_degrees()}")




print()
print()
print()
print()
print()
print()
print(Back.GREEN +"18 вариант наследование классов")
print()

# Для класса, созданного в предыдущем задании (по вариантам табл. 11.2) создать класс-потомок с полями, указанными в индивидуальном задании (табл. 11.5, столб 2).
# Реализовать в классе-потомке методы:
# - конструктор;
# - функцию обработки данных, указанную в индивидуальном задании (табл. 11.5, столб 3);
# - функцию формирования строки информации об объекте.
# Создать проект для демонстрации работы: ввод и вывод информации об объектах: классе-родителе и классе-потомке.
# Класс родитель и его поля:
# Вектор на плоскости: координаты вектора на плоскости (x1, уl, x2, у2)
#
#  Класс потомок и его поля
# Два вектора с общим началом ( xl, yl) на плоскости: координаты первого вектора xl, yl, x2, y2; координаты второго вектора -x1, vl, x3, v3
#
# Функция метод обработки данных класса потомка
# Определить координаты вектора суммы двух векторов.
class Vector2D:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_vector_sum(self):
        sum_x = self.x1 + self.x2
        sum_y = self.y1 + self.y2
        return sum_x, sum_y

    def info_string(self):
        return f"Vector: ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})"


class TwoVectorsWithCommonStart(Vector2D):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1, x2, y2)
        self.x3 = x3
        self.y3 = y3

    def get_vector_sum(self):
        sum_x1, sum_y1 = super().get_vector_sum()
        sum_x2 = self.x3 - self.x1 + sum_x1
        sum_y2 = self.y3 - self.y1 + sum_y1
        return sum_x2, sum_y2

    def info_string(self):
        return f"Vector 1: ({self.x1}, {self.y1}) to ({self.x2}, {self.y2}), " \
               f"Vector 2: ({self.x1}, {self.y1}) to ({self.x3}, {self.y3})"


# Пример использования
if __name__ == "__main__":
    vector_parent = Vector2D(1, 2, 3, 4)
    print(vector_parent.info_string())
    print(f"Sum of Vectors: {vector_parent.get_vector_sum()}")

    two_vectors_child = TwoVectorsWithCommonStart(1, 2, 3, 4, 5, 6)
    print(two_vectors_child.info_string())
    print(f"Sum of Vectors: {two_vectors_child.get_vector_sum()}")




print()
print()
print()
print(Back.GREEN +" 18 вариант полиморфизм")
print()
# Задание: построить класс 1-го уровня с указанными в индивидуальном задании (табл. 11.7) полями и методами:
# -конструктор;
# - функция, которая определяет «качество» объекта - Q по заданной формуле (табл11. 7, столб 2);
# - вывод информации об объекте.
# Построить класс 2-го уровня (класс-потомок), который содержит:
# - дополнительное поле Р;
# - функция, которая определяет «качество» объекта класса 2-го уровня - Qp, которая перекрывает функцию качества класса 1-го уровня (Q ), выполняя вычисление по новой формуле (табл. 11.7, столб 3).
# Создать проект для демонстрации работы: ввод и вывод информации об объектах классов 1-го и 2-го уровней.
# Поля и функция «качества» (О
# класса 1-го уровня
# Солдат:
# - фамилия;
# - рост (м);
# - вес (кг).
# q=рост*вес
#
# Поле и функция «качества»
# Ор класса 2-го уровня
#
# Р: образование (начальное, среднее, высшее) qр: если образование высшее, то qр=2*q; а если начальное, то qр=0,5-q; иначе qр=q
class FirstLevelClass:
    def __init__(self, last_name, height, weight):
        self.last_name = last_name
        self.height = height
        self.weight = weight

    def calculate_quality(self):
        return self.height * self.weight

    def display_info(self):
        print(f"Фамилия: {self.last_name}")
        print(f"Рост: {self.height} м")
        print(f"Вес: {self.weight} кг")
        print(f"Качество: {self.calculate_quality()}")


class SecondLevelClass(FirstLevelClass):
    def __init__(self, last_name, height, weight, education):
        super().__init__(last_name, height, weight)
        self.education = education

    def calculate_quality(self):
        if self.education == "высшее":
            return 2 * super().calculate_quality()
        elif self.education == "начальное":
            return 0.5 - super().calculate_quality()
        else:
            return super().calculate_quality()

    def display_info(self):
        super().display_info()
        print(f"Образование: {self.education}")


# Пример использования классов
if __name__ == "__main__":
    soldier1 = FirstLevelClass("Иванов", 1.75, 75)
    soldier2 = SecondLevelClass("Петров", 1.80, 80, "высшее")
    soldier3 = SecondLevelClass("Сидоров", 1.70, 70, "начальное")

    print("Солдат 1:")
    soldier1.display_info()

    print("\nСолдат 2:")
    soldier2.display_info()

    print("\nСолдат 3:")
    soldier3.display_info()
