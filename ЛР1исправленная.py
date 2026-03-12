# TODO Написать 3 класса с документацией и аннотацией типов

from abc import ABC, abstractmethod
import doctest


class Pencil(ABC):
    """Абстрактный класс Карандаш"""

    def __init__(self, length: float, color: str):
        """
        Инициализация карандаша.
        :param length: Длина карандаша
        :param color: Цвет карандаша
        """
        if length <= 0:
            raise ValueError("Длина карандаша > 0")
        self.length = length
        self.color = color

    @abstractmethod
    def write(self, text: str) -> str:
        """Метод для письма"""
        ...

    @abstractmethod
    def sharpen(self) -> None:
        """Метод для заточки"""
        ...


class WoodenPencil(Pencil):
    """Класс Деревянный Карандаш"""

    def write(self, text: str) -> str:
        """
        Метод для письма карандашом.
        :param text: Текст для записи
        :return: Строка с результатом

        Пример:
        >>> pencil = WoodenPencil(15.0, "Красный")
        >>> pencil.write("Привет")
        "Написано 'Привет' карандашом Красный"
        """
        return f"Написано '{text}' карандашом {self.color}"

    def sharpen(self) -> None:
        """
        Метод для заточки карандаша (уменьшает длину).

        Пример:
        >>> pencil = WoodenPencil(10.0, "HB")
        >>> pencil.sharpen()
        >>> pencil.length
        9.5
        """
        self.length -= 0.5


class Cup(ABC):
    """Абстрактный класс Чашка"""

    def __init__(self, volume: int, material: str):
        """
        Инициализация чашки.
        :param volume: Объём чашки
        :param material: Материал чашки
        """
        if volume <= 0:
            raise ValueError("Объём чашки > 0")
        self.volume = volume
        self.material = material

    @abstractmethod
    def fill(self, liquid: str) -> str:
        """Метод для наполнения чашки"""
        ...

    @abstractmethod
    def empty(self) -> None:
        """Метод для опустошения чашки"""
        ...


class CeramicCup(Cup):
    """Класс Керамическая Чашка"""

    def fill(self, liquid: str) -> str:
        """
        Метод для наполнения чашки жидкостью.
        :param liquid: Название жидкости
        :return: Строка с результатом

        Пример:
        >>> cup = CeramicCup(300, "Керамика")
        >>> cup.fill("Чай")
        'Чашка наполнена Чай'
        """
        return f"Чашка наполнена {liquid}"

    def empty(self) -> None:
        """
        Метод для опустошения чашки.

        Пример:
        >>> cup = CeramicCup(250, "Глина")
        >>> cup.empty()
        >>> cup.volume
        250
        """
        ...


class FlashDrive(ABC):
    """Абстрактный класс Флешка"""

    def __init__(self, capacity: int, used: int):
        """
        Инициализация флешки.
        :param capacity: Общая ёмкость
        :param used: Занятое место
        """
        if capacity <= 0:
            raise ValueError("Ёмкость > 0")
        if not 0 <= used <= capacity:
            raise ValueError("Неверный объём данных")
        self.capacity = capacity
        self.used = used

    @abstractmethod
    def save_file(self, size: int) -> bool:
        """Метод для сохранения файла"""
        ...

    @abstractmethod
    def free_space(self) -> int:
        """Метод для получения свободного места"""
        ...


class UsbFlashDrive(FlashDrive):
    """Класс USB Флешка"""

    def save_file(self, size: int) -> bool:
        """
        Метод для сохранения файла на флешку.
        :param size: Размер файла
        :return: True если успешно, иначе False

        Пример:
        >>> usb = UsbFlashDrive(100, 50)
        >>> usb.save_file(30)
        True
        >>> usb.save_file(50)
        False
        """
        if self.used + size <= self.capacity:
            self.used += size
            return True
        return False

    def free_space(self) -> int:
        """
        Метод для получения свободного места.
        :return: Свободное место в единицах

        Пример:
        >>> usb = UsbFlashDrive(100, 50)
        >>> usb.free_space()
        50
        """
        return self.capacity - self.used


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()