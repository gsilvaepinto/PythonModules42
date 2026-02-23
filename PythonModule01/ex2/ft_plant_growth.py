class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self, amount=1) -> None:
        self.height += amount

    def age(self) -> None:
        self.plant_age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


if __name__ == "__main__":
    plant: Plant = Plant("Rose", 25, 30)
    initial_height = plant.height

    print("=== Day 1 ===")
    print(plant.get_info())

    for day in range(1, 7):
        plant.grow()
        plant.age()

    print("=== Day 7 ===")
    print(plant.get_info())
    print(f"Growth this week: +{plant.height - initial_height}cm")
