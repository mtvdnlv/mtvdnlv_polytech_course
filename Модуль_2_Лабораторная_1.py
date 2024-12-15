import doctest


class Table:
    def __init__(self, material: str, legs_count: int):
        """
        Инициализация стола.

        :param material: Материал стола, должно быть непустой строкой.
        :param legs_count: Количество ног стола, должно быть положительным целым числом.

        :raises ValueError: Если material пустая или legs_count <= 0.

        Примеры:
        >>> table = Table("Wood", 4)
        >>> table.material
        'Wood'
        """
        if not material:
            raise ValueError("Матриал стола, должно быть непустой строкой.")
        if legs_count <= 0:
            raise ValueError("Количество ног стола, должно быть положительным целым числом.")

        self.material = material
        self.legs_count = legs_count

    def stay_able(self) -> bool:
        """
        Функция, которая проверяет может ли стол стоять

        :return: Может ли стол стоять

        Примеры:
        >>> table = Table("wood", 1)
        >>> table.stay_able()
        """
        ...

    def resize_plus(self, leg: int) -> None:
        """Увеличивает кол-во ножек стола.

        :param leg: Кол-во прибавляемых ножек

        :raises ValueError: Если кол-во прибавляемых ножек отрицательное.

        Примеры:
        >>> table = Table("Wood", 3)
        >>> table.resize_plus(1)
        """
        if not isinstance(leg, int):
            raise TypeError("Добавляемая ножка должна быть типа int")
        if leg < 0:
            raise ValueError("Добавляемая ножка должна положительным числом")
        ...

    def resize_minus(self, leg: int) -> None:
        """Уменьшает кол-во ножек стола.

        :param leg: Кол-во уабвляемых ножек

        :raises ValueError: Если кол-во убавляемых ножек отрицательное.

        Примеры:
        >>> table = Table("Wood", 5)
        >>> table.resize_minus(1)
        """
        if not isinstance(leg, int):
            raise TypeError("Убавляемая ножка должна быть типа int")
        if leg < 0:
            raise ValueError("Убавляемая ножка должна положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass





class Fork:

    def __init__(self, material: str, prong_count: int):
        """
        Инициализация вилки.

        :param material: Материал вилки, должно быть непустой строкой.
        :param prong_count: Количество зубцов вилки, должно быть положительным целым числом и не еденицей.

        :raises ValueError: Если material пустая или prong_count <= 2.

        Примеры:
        >>> fork = Fork("Сталь", 4)
        >>> fork.material
        'Сталь'
        """
        if not material:
            raise ValueError("Материал вилки, должно быть непустой строкой.")
        if prong_count <= 2:
            raise ValueError("Количество зубцов вилки, должно быть положительным целым числом, больше единицы.")

        self.material = material
        self.prong_count = prong_count

    def is_steel(self) -> bool:
        """
        Проверяет, является ли вилка стальной.

        :return: True, если вилка стальная, False в противном случае.

        Примеры:
        >>> fork = Fork("Plastic", 3)
        >>> fork.is_steel()
        """
        ...

    def add_prong(self) -> None:
        """Добавляет зубец к вилке.

        :raises ValueError: Если количество зубцов превышает допустимое значение (допустим 6).

        Примеры:
        >>> fork = Fork("Сталь", 4)
        >>> fork.add_prong()
        """
        if self.prong_count >= 6:
            raise ValueError("Количество зубцов не может превышать 6.")
        ...

    def remove_prong(self) -> None:
        """Удаляет зубец с вилки.

        :raises ValueError: Если количество зубцов менее 2.

        Примеры:
        >>> fork = Fork("Metal", 4)
        >>> fork.remove_prong()
        """
        if self.prong_count <= 2:
            raise ValueError("Количество зубцов не может быть меньше 2")
        ...


class House:
    def __init__(self, material: str, floors_count: int, people: int):
        """
        Инициализация дома.

        :param material: Материал дома, должно быть непустой строкой.
        :param floors_count: Количество этажей, должно быть положительным целым числом.
        :param people: Количество людей в доме

        :raises ValueError: Если material пустая или floors_count и people <= 0.

        Примеры:
        >>> house = House("Brick", 2, 300)
        >>> house.material
        'Brick'
        """
        if not material:
            raise ValueError("Материал дома, должно быть непустой строкой.")
        if floors_count and people <= 0:
            raise ValueError("Количество этажей и людей, должно быть положительным целым числом.")

        self.material = material
        self.floors_count = floors_count
        self.people = people

    def is_populated(self) -> bool:
        """
        Проверяет, является ли дом населенным.

        :return: True, если дом населенным, False в противном случае.

        Примеры:
        >>> house = House("Wood", 1, 300)
        >>> house.is_populated()
        """
        ...

    def add_floor(self) -> None:
        """Добавляет этаж к дому.

        Примеры:
        >>> house = House("Brick", 2)
        >>> house.add_floor()
        """
        ...

    def remove_floor(self) -> None:
        """Удаляет этаж из дома.

        :raises ValueError: Если количество этажей становится отрицательным или нулевым.

        Примеры:
        >>> house = House("Concrete", 2)
        >>> house.remove_floor()
        """
        if self.floors_count <= 1:
            raise ValueError("Количество этажей не может быть меньше 1.")
        ...
