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

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    pass


class Seed(Flower):
    def __init__(self, name: str, height: float, 
                 plant_age: int, color: str):
        super().__init__(name, height, plant_age)
        self.color = color
    

def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)

    plant_list: list[Flower | Tree | Seed] = [
        Flower('Rose', 15, 10, 'red')
    ]
    for plant in plant_list:
        if isinstance(plant, Flower):
            print(f"\n=== {plant.__class__.__name__}")
            plant.show()
            plant.display_stats()


if __name__ == "__main__":
    main()