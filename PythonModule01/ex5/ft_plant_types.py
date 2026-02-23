class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.plant_age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        return f"{self.name} provides 78 square meters of shade"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self):
        return f"{self.name} is rich in vitamin C"


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    flower: Flower = Flower("Rose", 25, 30, "red")
    name = flower.name
    height = flower.height
    age = flower.plant_age
    color = (flower.color + " color")
    print(f"{name} (Flower): {height}cm, {age} days, {color}")
    print(flower.bloom())
    print("")

    tree: Tree = Tree("Oak", 500, 1825, 50)
    name = tree.name
    height = tree.height
    age = tree.plant_age
    diameter = tree.trunk_diameter
    print(f"{name} (Tree): {height}cm, {age} days, {diameter}cm diameter")
    print(tree.produce_shade())
    print("")

    vegetable: Vegetable = Vegetable("Tomato", 80, 90, "summer")
    name = vegetable.name
    height = vegetable.height
    age = vegetable.plant_age
    season = (vegetable.harvest_season + " harvest")
    print(f"{name} (Vegetable): {height}cm, {age} days, {season}")
    print(vegetable.nutritional_value())
