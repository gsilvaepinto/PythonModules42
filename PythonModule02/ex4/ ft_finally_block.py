class PlantError(Exception):
    def __init__(self, msg="Unknow plant error"):
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f" Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for plant in ["Tomato", "Lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")

    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for plant in ["Tomato", "lettuce"]:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")

    print("Cleanup always happens, even with errors!")
