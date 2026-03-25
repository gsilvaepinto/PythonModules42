class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.plant_age = age
        self.initial_height = height

    def grow(self, height: float):
        self.height += height

    def age(self):
        self.plant_age += 1

    def __str__(self):
        return f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old"


def main():
    print("=== Garden Plant Growth ===")
    plant: Plant = Plant('Rose', 25, 30)
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        print(plant)
        plant.grow(0.8)
        plant.age()
    print(f"Growth this week: {round(plant.height - plant.initial_height)}cm")


if __name__ == "__main__":
    main()
