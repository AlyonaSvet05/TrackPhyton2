from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

class Publication(ABC):
    def __init__(self, title: str, author: str, publication_date: datetime):
        if not isinstance(title, str):
            raise TypeError("Название публикации должно быть строкой.")
        if not isinstance(author, str):
            raise TypeError("Автор публикации должен быть строкой.")
        if not isinstance(publication_date, datetime):
            raise TypeError("Дата публикации должна быть объектом datetime")
        if not title:
            raise ValueError("Название публикации не может быть пустым.")
        if not author:
            raise ValueError("Имя автора публикации не может быть пустым.")
        self._title = title
        self._author = author
        self._publication_date = publication_date

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def publication_date(self) -> datetime:
        return self._publication_date

    def __str__(self) -> str:
        formatted_date = self._publication_date.strftime("%Y-%m-%d")
        return f"'{self._title}', автор: {self._author}, дата публикации: {formatted_date}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(title='{self._title}', author='{self._author}', "
            f"publication_date=datetime.fromisoformat('{self._publication_date.isoformat()}'))"
        )

    @abstractmethod
    def display(self) -> str:
        pass


class BlogPost(Publication):
    def __init__(self, title: str, author: str, publication_date: datetime, content: str, tags: List[str]):
        super().__init__(title, author, publication_date)
        if not isinstance(content, str):
            raise TypeError("Содержание блог-поста должно быть строкой.")
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            raise TypeError("Теги блог-поста должны быть списком строк.")
        if not content:
            raise ValueError("Содержание блог-поста не может быть пустым.")
        if not tags:
            raise ValueError("Теги блог-поста не могут быть пустым списком.")
        self._content = content
        self._tags = tags

    @property
    def content(self) -> str:
        return self._content

    @property
    def tags(self) -> List[str]:
        """Returns list of tags of the BlogPost"""
        return self._tags

    def __str__(self) -> str:
        formatted_date = self._publication_date.strftime("%Y-%m-%d")
        return f"Блог-пост '{self._title}', автор: {self._author}, дата публикации: {formatted_date}, теги: {', '.join(self._tags)}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(title='{self._title}', author='{self._author}', "
            f"publication_date=datetime.fromisoformat('{self._publication_date.isoformat()}'), content='{self._content}',"
            f"tags={self._tags})"
        )

    def display(self) -> str:
        formatted_date = self._publication_date.strftime("%Y-%m-%d")
        return f"Блог-пост: {self._title}  Автор: {self._author} Дата публикации: {formatted_date}. Содержание: {self._content}. Теги: {', '.join(self._tags)}"


if __name__ == "__main__":
    try:
        publication = Publication("Тестовая публикация", "Иванов И.И.", datetime(2025, 10, 26))
        print(publication)
        print(repr(publication))

        blog_post = BlogPost("Мой первый блог-пост", "Петров П.П.", datetime(2025, 10, 25),
                             "Содержание моего блог-поста.", ["блог", "тест"])
        print(blog_post)
        print(repr(blog_post))
        print(blog_post.display())

        publication1 = Publication("Ошибка1", "", datetime(2025, 10, 26))
    except TypeError as e:
        print(f"Error:{e}")
    except ValueError as e:
        print(f"Error:{e}")
    try:
        blog_post1 = BlogPost("Ошибка", "Автор", datetime(2025, 10, 25), 123, ["тест"])
    except TypeError as e:
        print(f"Error:{e}")
    try:
        blog_post1 = BlogPost("Ошибка", "Автор", datetime(2025, 10, 25), "", ["тест"])
    except ValueError as e:
        print(f"Error:{e}")
    try:
        blog_post1 = BlogPost("Ошибка", "Автор", datetime(2025, 10, 25), "контент", [])
    except ValueError as e:
        print(f"Error:{e}")
    try:
        blog_post1 = BlogPost("Ошибка", "Автор", datetime(2025, 10, 25), "контент", 123)
    except TypeError as e:
        print(f"Error:{e}")