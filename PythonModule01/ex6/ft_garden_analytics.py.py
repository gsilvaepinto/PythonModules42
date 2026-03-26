class Plant:
    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
        
        def increase_grow(self) -> None:
            self._grow_calls += 1

        def increase_age(self) -> None:
            self._age_calls += 1

        def increase_show(self) -> None:
            self._show_calls += 1

        def show_stats(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def height(self) -> float:
        return self._height
    
    @property
    def age(self) -> int:
        return self._age

    @staticmethod
    def check_age(value) -> None:
        print(f"Is {value} days more than a year? -> {value > 365}")

    @classmethod
    def create_anonymous(cls) -> None:
        return cls('Unknown plant', 0, 0)

    def grow(self, value: float) -> None:
        self._height += value
        self._stats.increase_grow()

    def increase_age(self, value: int) -> None:
        self._age += 1
        self._stats.increase_age()

    def display_stats(self):
        self._stats.show_stats(self.name)
    
    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self._stats.increase_show()
    

class Flower(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, color: str):
        super().__init__(name, height, plant_age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to grow and bloom]")
        self.blooming = True
        self.grow(8)

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._producing_shade = 0

        def get_shade(self) -> int:
            return self._producing_shade
        
        def increase_shade(self) -> None:
            self._producing_shade += 1

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self._stats = Tree.Stats()
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        self.producing_shade = True
        print(f"{self.__class__.__name__} {self.name} now produces a shade of "
              f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide")
        self._stats.increase_shade()
    
    def show(self) -> None:
        super().show()
        print(f"Trunk diamater: {self.trunk_diameter:.1f}cm")

    def display_stats(self) -> None:
        super().display_stats()
        print(f"{self._stats.get_shade()} shade")


class Seed(Flower):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._seeds = 0

        def get_seeds(self) -> int:
            return self._seeds
        
        def increase_seeds(self, value: int) -> None:
            self._seeds += value

    def __init__(self, name: str, height: float, 
                 plant_age: int, color: str, seeds: int):
        super().__init__(name, height, plant_age, color)
        self._stats = Seed.Stats()
        self.seeds = seeds
    
    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._stats.get_seeds()}")

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to grow, age and bloom]")
        self.blooming = True
        self.grow(30)
        self.increase_age(20)
        self._stats.increase_seeds(self.seeds)

def display_statistics(plant: Plant) -> None:
    plant.display_stats()

def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)

    plant_list: list[Plant] = [
        Flower('Rose', 15, 10, 'red'),
        Tree('Oak', 200, 365, 5),
        Seed('Sunflower', 80, 45, 'yellow', 42),
        Plant.create_anonymous()
    ]
    for plant in plant_list:
        if isinstance(plant, Seed):
             print(f"\n=== {plant.__class__.__name__}")
             plant.show()
             plant.bloom()
             plant.show()
             display_statistics(plant)
        elif isinstance(plant, Flower):
            print(f"\n=== {plant.__class__.__name__}")
            plant.show()
            display_statistics(plant)
            plant.bloom()
            plant.show()
            display_statistics(plant)
        elif isinstance(plant, Tree):
            print(f"\n=== {plant.__class__.__name__}")
            plant.show()
            display_statistics(plant)
            plant.produce_shade()
            display_statistics(plant)
        elif isinstance(plant, Plant):
            print(f"\n=== Anonymous")
            plant.show()
            display_statistics(plant)

if __name__ == "__main__":
    main()