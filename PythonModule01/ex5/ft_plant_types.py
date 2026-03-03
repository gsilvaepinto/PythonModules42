class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        classname = self.__class__.__name__
        return f"{self.name} ({classname}): {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")

    def __str__(self):
        return super().__str__() + f", {self.color} color"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade\n")

    def __str__(self):
        return super().__str__() + f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self):
        print(f"{self.name} is rich in vitamin C")

    def __str__(self):
        return super().__str__() + f", {self.harvest_season} harvest"


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    '#ROSE'
    rose = Flower("Rose", 25, 30, "red")
    print(rose)
    rose.bloom()
    '#OAK'
    oak = Tree("Oak", 500, 1825, 50)
    print(oak)
    oak.produce_shade()
    '#TOMATO'
    tomato = Vegetable("Tomato", 80, 90, "summer")
    print(tomato)
    tomato.nutritional_value()
