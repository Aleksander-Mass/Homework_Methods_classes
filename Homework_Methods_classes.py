#Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

# Необходимо дополнить класс House следующими специальными методами:
'''
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
'''


class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли такой этаж
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод всех этажей от 1 до нового этажа
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращаем строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# Пример использования:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

###     Вывод на консоль:
# => Название: ЖК Эльбрус, кол-во этажей: 10
# => Название: ЖК Акация, кол-во этажей: 20
# => 10
# => 20