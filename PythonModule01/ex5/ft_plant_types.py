class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def show(self):
        print (f"{self.name}: {self.height:.1f}cm, {self.age} days old")
    

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False
    
    def bloom(self):
        print(f"[asking the {self.name.lower()} to bloom]")
        self.blooming = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if not self.blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season


def main():
    print("=== Garden Plant Types ===")
    plant_list: list[Flower, Tree, Vegetable] = [
        Flower('Rose', 15, 10, 'red')
    ]
    for plant in plant_list:
        if isinstance(plant, Flower):
            print(f"=== {plant.__class__.__name__}")
            plant.show()
            plant.bloom()
            plant.show()


if __name__ == "__main__":
    main()