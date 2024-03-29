MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        for v in self.values():
            if birthday.day == v.day and birthday.month == v.month:
                print(MSG.format(name))
        self.__dict__[name] = birthday

    def values(self):
        return self.__dict__.values()
