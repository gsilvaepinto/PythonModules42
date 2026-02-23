class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.plant_age = age


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.plant_age} days old")
