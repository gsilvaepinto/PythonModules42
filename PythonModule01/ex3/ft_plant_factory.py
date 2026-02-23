class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.plant_age = age


if __name__ == "__main__":
    plants_list = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    plants = []

    print("=== Plant Factory Output ===")
    for data in plants_list:
        plant: Plant = Plant(*data)
        plants.append(plant)
        print(
            f"Created: {plant.name} ({plant.height}cm, {plant.plant_age} days)"
        )
    print(f"\nTotal plants created: {len(plants)}")
