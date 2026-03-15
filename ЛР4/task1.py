class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.
    """

    def __init__(self, brand: str, speed: int) -> None:
        """
        Аргументы:
            brand: марка
            speed: максимальная скорость
        """
        self._brand = brand
        self._speed = speed

    def __str__(self) -> str:
        """
        читаемое представление
        """
        return f"Транспорт: {self._brand}, скорость: {self._speed} км/ч"

    def __repr__(self) -> str:
        """
        Официальное представление для воссоздания объекта
        """
        return f"Vehicle('{self._brand}', {self._speed})"

    def move(self) -> str:
        """
        Действие движения
        """
        return f"{self._brand} движется со скоростью {self._speed} км/ч"

    def info(self) -> str:
        """
        Информация о транспортном средстве
        """
        return f"Марка: {self._brand}, макс. скорость: {self._speed} км/ч"


class Car(Vehicle):
    """
    Дочерний класс, представляющий автомобиль.
    """

    def __init__(self, brand: str, speed: int, fuel: str) -> None:
        """
        Аргументы:
            brand: марка автомобиля
            speed: максимальная скорость
            fuel: тип топлива
        """
        super().__init__(brand, speed)
        self._fuel = fuel

    def __str__(self) -> str:
        """
        Переопределённое строковое представление с учётом типа топлива
        """
        return f"Автомобиль: {self._brand}, скорость: {self._speed} км/ч, топливо: {self._fuel}"

    def __repr__(self) -> str:
        """
        Переопределённое официальное представление
        """
        return f"Car('{self._brand}', {self._speed}, '{self._fuel}')"

    def move(self) -> str:
        """
        Причина переопределения:
        добавляем детали в описание движения
        """
        return f"{self._brand} едет на {self._fuel} со скоростью {self._speed} км/ч"

if __name__ == "__main__":
    # Write your solution here
    pass
