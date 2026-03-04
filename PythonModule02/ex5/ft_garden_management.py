class GardenError(Exception):
    def __init__(self):
        super().__init__("Not enough water in tank")


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant, water, sun):
        try:
            if not plant:
                raise ValueError("Plant name cannot be empty!")
            info = {"plant": plant, "water": water, "sun": sun}
            self.plants.append(info)
            print(f"Added {plant} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def watering(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise ValueError("Garden is empty!")
            for plant in self.plants:
                print(f"Watering {plant['plant']} - success")
        except ValueError as e:
            print(f"Error watering plants: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant):
        try:
            if plant['water'] > 10:
                raise ValueError(
                    f"Water level {plant['water']} is too high (max 10)")
            print(f"{plant['plant']}: healthy "
                  f"(water: {plant['water']}, sun: {plant['sun']})")
        except ValueError as e:
            print(f"Error checking {plant['plant']}: {e}")


def test_garden_management():
    print("=== Garden Management System ===\n")

    garden = GardenManager()
    print("Adding plants to garden...")
    garden.add_plant("tomato", 10, 0)
    garden.add_plant("lettuce", 15, 0)
    garden.add_plant("", 30, 0)

    print("\nWatering plants...")
    garden.watering()

    print("\nChecking plant health...")
    for plant in garden.plants:
        garden.check_plant_health(plant)

    print("\nTesting error recovery...")
    try:
        raise GardenError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
