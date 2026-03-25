class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.plant_age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def main():
    print("=== Garden Plant Registry ===")

    plants: list[Plant] = [
        Plant('Rose', 25, 30),
        Plant('Sunflower', 80, 45),
        Plant('Cactus', 15, 120)
    ]

    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
