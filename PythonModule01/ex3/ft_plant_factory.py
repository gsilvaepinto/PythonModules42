class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self, height: float):
        self.height += height

    def show(self):
        return(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")


def main():
    print("=== Plant Factory Output ===")
    plants_list: list[tuple[str, float, int]] = [
        ('Rose', 25, 30),
        ('Oak', 200, 365),
        ('Cactus', 5, 90),
        ('Sunflower', 80, 45),
        ('Fern', 15, 120)
    ]

    plants: list[Plant] = []

    for data in plants_list:
        plant: Plant = Plant(*data)
        plants.append(plant)
        print(f"Created: {plant.show()}")


if __name__ == "__main__":
    main()
    
