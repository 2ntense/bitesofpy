from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL


class User:

    def __init__(self, name):
        self.name = name
        self._transactions = []

    @property
    def karma(self):
        return sum(self.points)

    @property
    def points(self):
        return [transaction.points for transaction in self._transactions]

    @property
    def fans(self):
        return len({transaction.giver for transaction in self._transactions})

    def __str__(self):
        return f"{self.name} has a karma of {self.karma} and {self.fans} {'fans' if self.fans > 1 else 'fan'}"

    def __add__(self, other):
        self._transactions.append(other)



bob = User("Bob")
bob + Transaction(giver=bob, points=2)


print(bob.karma)

alice = User("Alice")
alice + Transaction(giver=bob, points=3)

print(alice.karma)