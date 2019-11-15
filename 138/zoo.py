class Animal:

    sequence = 10000
    animals = list()

    def __init__(self, name):
        self.name = name.title()
        Animal.sequence += 1
        self.index = self.sequence
        Animal.animals.append((self.index, self.name))

    def __str__(self):
        return f"{self.index}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join([f"{a[0]}. {a[1]}" for a in cls.animals])


dog = Animal('dog')
cat = Animal('cat')
fish = Animal('fish')
lion = Animal('lion')
mouse = Animal('mouse')
print(Animal.zoo())