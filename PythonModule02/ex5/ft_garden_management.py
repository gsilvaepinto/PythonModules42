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

    def water_plants(self):
        try:
            print("Opening watering system")
            if not self.plants:
                raise ValueError("Garden is empty!")
            for plant in self.plants:
                print(f"Watering {plant['plant']} - success")
        except ValueError as e:
            print(f"Error opening watering system: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant):
        try:
            if plant["water"] > 10:
                raise ValueError(
                    f"Water level {plant['water']} is too high (max 10)")
            print(f"{plant['plant']}: healthy (water: {plant['water']}, "
                  f"sun: {plant['sun']})")
        except (ValueError, KeyError) as e:
            print(f"Error checking {plant['plant']}: {e}")


def test_garden_management():
    print("=== Garden Management System ===")

    garden = GardenManager()
    print("\nAdding plants to garden...")
    garden.add_plant("tomato", 5, 8)
    garden.add_plant("lettuce", 15, 20)
    garden.add_plant("", 30, 30)

    print("\nWatering Plants")
    garden.water_plants()

    print("\nChecking plant health...")
    for plant in garden.plants:
        garden.check_plant_health(plant)

    print("\nTesting error recovery...")
    try:
        raise GardenError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
