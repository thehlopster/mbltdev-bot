﻿import random as rand


class gen:

    _nick_name = ("Александр", "Алексей", "Анатолий", "Андрей", "Антон", "Аркадий", "Борис", "Вадим", "Валентин", "Валерий", "Василий", "Виктор", "Виталий", "Владимир",
                  "Вячеслав", "Геннадий", "Георгий", "Глеб", "Григорий", "Данила", "Дмитрий", "Евгений", "Егор", "Ефим", "Захар", "Иван", "Игорь", "Илья", "Кирилл", "Константин", "Лев", "Леонид",
                  "Максим", "Матвей", "Михаил", "Никита", "Николай", "Олег", "Павел", "Петр", "Платон", "Прохор", "Роман", "Руслан", "Савва", "Сергей", "Станислав", "Степан", "Тимофей", "Тихон", "Федор", "Юрий", "Ярослав", "Яков")

    _mail = ("a", "b", "c", "d", "f", "g", "h", "j", "k", "l",
             "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

    _host = ("@pay-mon.com", "@zep-hyr.com", "@travala10.com", "@zippiex.com", "@poly-swarm.com",
             "@1shivom.com", "@fidelium10.com", "@hubii-network.com", "@hurify1.com", "@bit-degree.com")

    _spec = ("ИБ", "Информационная безопасность", "веб-дизайнер", "верстальщик", "тестировщик", "системный администратор", "Программист Swift", "Программист Python", "Программист C#", "iOS-разработчик", "Android-разработчик", "Программист Java", "Программист Ruby", "Программист PHP", "Архитектор баз данных", "Разработчик баз данных",
             "Сетевой администратор", "Програмист", "Разработчик игр", "gamedev", "Системный инженер", "Flash-аниматор", "3D-Дженералист", "Архитектор VR", "Веб-аналитик", "Юзабилити-специалист", "Мобильный разработчик", "Бэк-энд разработчик", "Frontend разработчик", "3D-аниматор", "Гейм-дизайнер", "Программист 1С", "Веб-программист", "верстальщик", "Web-дизайнер")

    def __init__(self):
        pass

    def get_nick(self):
        return rand.choice(self._nick_name)

    def get_mail(self):
        _temp = []
        for _ in range(10):
            _temp.append(rand.choice(self._mail))
        return ''.join(_temp) + ''.join(rand.choice(self._host))

    def get_spec(self):
        return rand.choice(self._spec)
#
