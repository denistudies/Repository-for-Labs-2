# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class ParkingSpace:
    def __init__(self, total_number: int, occupied_places: int):
        """
        Создание и подготовка к работе объекта "Парковка"

        :param total_number: Общее количество парковочных мест
        :param occupied_places: Количество занятых парковочных мест

        >>> parking_space = ParkingSpace(250, 186) # инициализация экземпляра класса
        """
        if not isinstance(total_number, int):
            raise TypeError("Общее количество парковочных мест должно быть типа int")
        if total_number <= 0:
            raise ValueError("Общее количество парковочных мест должно быть больше 0")
        self.total_number = total_number

        if not isinstance(occupied_places, int):
            raise TypeError("Количество занятых мест должно быть типа int")
        if occupied_places < 0:
            raise ValueError("Количество занятых мест не может быть отрицательным числом")
        if occupied_places > total_number:
            raise ValueError("Количество занятых мест не может быть больше общего количества мест")
        self.occupied_places = occupied_places

    def is_parkingspace_empty(self) -> bool:
        """
        Функция, которая проверяет является ли парковка пустой

        :return: Является ли стакан пустым

        >>> parking_space = ParkingSpace (250, 0)
        >>> parking_space.is_parkingspace_empty()
        """
        ...
    def add_cars_to_parkingspace(self, cars: int) -> None:
        """
        Приезд на парковку новых машин

        :param cars: Количество приехавших машин
        :return: Если количество приехавших машин превышает свободное количество парковочных мест, вызываем ошибку

        >>> parking_space = ParkingSpace (250, 186)
        >>> parking_space.add_cars_to_parkingspace(92)
        """
        if not isinstance(cars, int):
            raise TypeError("Количество приехавших машин должно быть типа int")
        if cars < 0:
            raise ValueError("Количество приехавших машин должно быть положительным числом")
        ...

class Pencil:
    def __init__(self, color: str, length_in_cm: float, sharpness: int):
        """
        Создание и подготовка к работе объекта "Карандаш"

        :param color: Цвет карандаша
        :param length_in_cm: Длина карандаша (в см)
        :param sharpness: Острота (в %)

        >>> pencil = Pencil ('фиолетовый', 18, 100) # инициализация экземпляра класса
        """
        self.color = color
        if length_in_cm < 0:
            raise ValueError("Длина карандаша (в см) не может быть отрицательным числом")
        self.length_in_cm = length_in_cm
        self.sharpness = sharpness

    def draw(self, line_length):
        """Метод для рисования линии. Уменьшает степень заточенности в зависимости от длины линии."""
        if self.sharpness <= 0 :
            print("Карандаш затупился. Заточите его перед рисованием.")
        else:
            print(f"Рисуем линию длиной {line_length} см цветом {self.color}.")
            # Предполагаем, что каждые 10 см линии уменьшают заточенность на 10 едениц
            self.sharpness -= line_length // 10
            if self.sharpness < 0:
                self.sharpness = 0

    def sharpen(self):
        """Метод для заточки карандаша. Восстанавливает заточенность до 100."""
        self.sharpness = 100
        print("Карандаш заточен.")
        ...

class Book:
    def __init__(self, author: str, title: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param author: Автор книги
        :param title: Название книги
        :param pages: Количество страниц

        >>> book = Book('Алескандр Сергеевич Пушкин','Капитанская дочка', 256) # инициализация экземпляра класса
        """
        self.author = author
        self.title = title
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def compare(self, other: 'Book') -> str:
        """Сравнивает текущую книгу с другой книгой по названию.
        :param other: Другая книга для сравнения.
        :return: Строка с результатом сравнения.
        """
        if not isinstance(other, Book):
            return "Можно сравнивать только с другими книгами."
        if self.name == other.name and self.author == other.author:
            return "Эти книги идентичны."
        return "Эти книги разные."

    def get_summary(self) -> str:
        """Возвращает краткое содержание книги."""
        return f"Краткое содержание книги \"{self.title}\" автор: {self.author}."

if __name__ == "__main__":
    doctest.testmod()
# TODO работоспособность экземпляров класса проверить с помощью doctest
