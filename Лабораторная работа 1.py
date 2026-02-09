# TODO Написать 3 класса с документацией и аннотацией типов
# TODO работоспособность экземпляров класса проверить с помощью doctest

from abc import ABC
import doctest

class Pencil(ABC):
    def __init__(self, length: float, color: str):
        if length <= 0: raise ValueError("Длина карандаша > 0")
        self.length = length
        self.color = color
    def write(self, text: str) -> str: ...
    def sharpen(self) -> None: ...

class WoodenPencil(Pencil):
    def write(self, text: str) -> str: return f"Написано '{text}' карандашом {self.color}"
    def sharpen(self) -> None: self.length -= 0.5

class Cup(ABC):
    def __init__(self, volume: int, material: str):
        if volume <= 0: raise ValueError("Объём чашки > 0")
        self.volume = volume
        self.material = material
    def fill(self, liquid: str) -> str: ...
    def empty(self) -> None: ...

class CeramicCup(Cup):
    def fill(self, liquid: str) -> str: return f"Чашка наполнена {liquid}"
    def empty(self) -> None: pass

class FlashDrive(ABC):
    def __init__(self, capacity: int, used: int):
        if capacity <= 0: raise ValueError("Ёмкость > 0")
        if not 0 <= used <= capacity: raise ValueError("Неверный объём данных")
        self.capacity = capacity
        self.used = used
    def save_file(self, size: int) -> bool: ...
    def free_space(self) -> int: ...

class UsbFlashDrive(FlashDrive):
    def save_file(self, size: int) -> bool:
        if self.used + size <= self.capacity:
            self.used += size
            return True
        return False
    def free_space(self) -> int: return self.capacity - self.used

if __name__ == "__main__":
    doctest.testmod()