class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
       """
       Инициализирует объект Book.

       Args:
           name: Название книги.
           author: Автор книги.
       Raises:
           TypeError: если name или author не строки.
       """
       if not isinstance(name, str):
           raise TypeError("Название книги должно быть строкой.")
       if not isinstance(author, str):
           raise TypeError("Автор книги должен быть строкой.")
       self._name = name
       self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f"Книга '{self._name}', автор: {self._author}"

    def __repr__(self) -> str:
        """Возвращает строковое представление для реконструкции объекта."""
        return f"{self.__class__.__name__}(name='{self._name}', author='{self._author}')"


class PaperBook(Book):
    """Класс для бумажных книг."""

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализирует объект PaperBook.

        Args:
            name: Название книги.
            author: Автор книги.
            pages: Количество страниц.
        Raises:
            TypeError: если pages не целое число.
            ValueError: если pages меньше или равно 0.
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """Устанавливает количетсов страниц с проверкой."""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __str__(self) -> str:
        """Возвращает строковое представление бумажной книги."""
        return f"{super().__str__()} ({self._pages} страниц)"

    def __repr__(self) -> str:
        """Возвращает строковое представление для реконструкции объекта."""
        return f"{self.__class__.__name__}(name='{self._name}', author='{self._author}', pages={self._pages})"


class AudioBook(Book):
    """Класс для аудиокниг."""

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализирует объект AudioBook.

         Args:
             name: Название книги.
             author: Автор книги.
             duration: Продолжительность аудиокниги.
         Raises:
             TypeError: если duration не число.
             ValueError: если duration меньше или равно 0.
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """Устанавливает продолжительность с проверкой."""
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = value

    def __str__(self) -> str:
        """Возвращает строковое представление аудиокниги."""
        return f"{super().__str__()} ({self._duration:.1f} часов)"

    def __repr__(self) -> str:
        """Возвращает строковое представление для реконструкции объекта."""
        return f"{self.__class__.__name__}(name='{self._name}', author='{self._author}', duration={self._duration})"


    # Пример использования
if __name__ == "__main__":
    paper_book = PaperBook("Мертвые души", "Николай Гоголь", 352)
    audio_book = AudioBook("Анна Каренина", "Лев Толстой", 39.2)

    print(paper_book)
    print(audio_book)
    print(repr(paper_book))
    print(repr(audio_book))

    try:
        invalid_book = PaperBook("Ошибка", "Автор", -5)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        invalid_book = AudioBook("Ошибка", "Автор", "10")
    except TypeError as e:
        print(f"Ошибка: {e}")

