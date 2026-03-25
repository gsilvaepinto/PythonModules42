class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")

    def age(self, value: int) -> None:
        self.plant_age += value

    def grow(self, value: float) -> None:
        self.height += value


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, color: str) -> None:
        super().__init__(name, height, plant_age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter
        self.producing_shade = False

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        self.producing_shade = True
        print(f"{self.__class__.__name__} {self.name} now produces a shade of "
              f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, harvest_season: str) -> None:
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self, value: int) -> None:
        super().age(value)
        self.nutritional_value += value

    def update(self, value: int) -> None:
        print(f"[make {self.name.lower()} grow and age for {value} days]")
        for _ in range(value):
            self.age(1)
            self.grow(2.1)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season.capitalize()}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    plant_list: list[Flower | Tree | Vegetable] = [
        Flower('Rose', 15, 10, 'red'),
        Tree('Oak', 200, 365, 5),
        Vegetable('Tomato', 5, 10, 'april')
    ]
    for plant in plant_list:
        if isinstance(plant, Flower):
            print(f"=== {plant.__class__.__name__}")
            plant.show()
            plant.bloom()
            plant.show()
        elif isinstance(plant, Tree):
            print(f"\n=== {plant.__class__.__name__}")
            plant.show()
            plant.produce_shade()
        elif isinstance(plant, Vegetable):
            print(f"\n=== {plant.__class__.__name__}")
            plant.show()
            plant.update(20)
            plant.show()


if __name__ == "__main__":
    main()
