if __name__ == "__main__":
    class Pet:
        """
        Базовый класс для домашних животных.
        Содержит общие атрибуты и методы для работы с домашними питомцами.
        """

        def __init__(self, name: str, age: int, species: str) -> None:
            """
            Конструктор для инициализации питомца.

            :param name: Имя питомца.
            :param age: Возраст питомца в годах.
            :param species: Вид животного.
            """
            self._name = name  # защищенный атрибут
            self._age = age  # защищенный атрибут
            self._species = species  # защищенный атрибут

        @property
        def name(self) -> str:
            return self._name

        @property
        def age(self) -> int:
            return self._age

        @property
        def species(self) -> str:
            return self._species

        def speak(self) -> str:
            """
            Возвращает звук, который издает питомец.

            :return: Звук питомца (по умолчанию пустая строка).
            """
            return ""

        def __str__(self) -> str:
            """
            Строковое представление питомца.

            :return: Информация о питомце в виде строки.
            """
            return f'{self.name}, {self.age} лет, {self.species}'

        def __repr__(self) -> str:
            """
            Представление питомца в виде кода.

            :return: Строка, представляющая объект питомца.
            """
            return f'Pet(name={self.name!r}, age={self.age!r}, species={self.species!r})'


    class Dog(Pet):
        """
        Класс для собак.
        Наследует атрибуты и методы базового класса Pet и добавляет дополнительные.
        """

        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            Конструктор для инициализации собаки.

            :param name: Имя собаки.
            :param age: Возраст собаки в годах.
            :param breed: Порода собаки.
            """
            super().__init__(name, age, species="Собака")
            self._breed = breed  # защищенный атрибут

        @property
        def breed(self) -> str:
            return self._breed

        def speak(self) -> str:
            """
            Возвращает звук, который издает собака.

            :return: Звук собаки "Гав".
            """
            return "Гав!"

        def __str__(self) -> str:
            """
            Строковое представление собаки.

            :return: Информация о собаке, включая породу.
            """
            return f'{super().__str__()}, порода: {self.breed}'

        def __repr__(self) -> str:
            """
            Представление собаки в виде кода.

            :return: Строка, представляющая объект собаки.
            """
            return f'Dog(name={self.name!r}, age={self.age!r}, breed={self.breed!r})'


    class Cat(Pet):
        """
        Класс для кошек.
        Наследует атрибуты и методы базового класса Pet и добавляет дополнительные.
        """

        def __init__(self, name: str, age: int, color: str) -> None:
            """
            Конструктор для инициализации кошки.

            :param name: Имя кошки.
            :param age: Возраст кошки в годах.
            :param color: Цвет кошки.
            """
            super().__init__(name, age, species="Кошка")
            self._color = color  # защищенный атрибут

        @property
        def color(self) -> str:
            return self._color

        def speak(self) -> str:
            """
            Возвращает звук, который издает кошка.

            :return: Звук кошки "Мяу".
            """
            return "Мяу!"

        def __str__(self) -> str:
            """
            Строковое представление кошки.

            :return: Информация о кошке, включая цвет.
            """
            return f'{super().__str__()}, цвет: {self.color}'

        def __repr__(self) -> str:
            """
            Представление кошки в виде кода.

            :return: Строка, представляющая объект кошки.
            """
            return f'Cat(name={self.name!r}, age={self.age!r}, color={self.color!r})'

    pass

# Пример использования:
    dog = Dog('Понго', 3, 'Далматин')
    cat = Cat('Салем', 2, 'Чёрный')

    print(dog)
    print(cat)