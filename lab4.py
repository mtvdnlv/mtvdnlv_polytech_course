class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        """Инициализирует объект Vehicle с маркой, моделью и годом выпуска."""
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Vehicle."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Возвращает представление объекта Vehicle для отладки."""
        return f"Vehicle(make={self.make}, model={self.model}, year={self.year})"


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, doors: int) -> None:
        """Инициализирует объект Car с дополнительным атрибутом doors."""
        super().__init__(make, model, year)
        self.__doors = doors  # Инкапсуляция: doors не доступен напрямую

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Car, включая количество дверей."""
        return f"{super().__str__()} with {self.__doors} doors"

    def __repr__(self) -> str:
        """Возвращает представление объекта Car для отладки, включая doors."""
        return f"Car(make={self.make}, model={self.model}, year={self.year}, doors={self.__doors})"

    def get_doors(self) -> int:
        """Возвращает количество дверей у автомобиля.

        Инкапсуляция: метод предоставлен для доступа к приватному атрибуту __doors, 
        чтобы избежать прямого доступа извне.
        """
        return self.__doors

    def set_doors(self, doors: int) -> None:
        """Устанавливает новое количество дверей для автомобиля.

        Если количество дверей меньше 2 или больше 5, вызовет ошибку.
        """
        if doors < 2 or doors > 5:
            raise ValueError("Количество дверей должно быть от 2 до 5.")
        self.__doors = doors


if __name__ == "__main__":
    # Пример создания объектов
    car1 = Car("Toyota", "Camry", 2020, 4)
    print(car1)  # Выводит: 2020 Toyota Camry with 4 doors
    print(repr(car1))  # Выводит: Car(make=Toyota, model=Camry, year=2020, doors=4)