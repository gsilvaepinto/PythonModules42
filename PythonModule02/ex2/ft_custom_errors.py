class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant):
        super().__init__(f"The {plant} plant is wilting!")
        self.plant = plant


class WaterError(GardenError):
    def __init__(self, liters):
        super().__init__("Not enough water in the tank!")
        self.liters = liters


def wilting(plant, is_wilting=False):
    try:
        print("Testing PlantError...")
        if is_wilting:
            raise PlantError(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")


def watering(liters):
    try:
        print("Testing WaterError...")
        if liters < 25:
            raise WaterError(liters)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")


def raise_errors():
    errors = [
        PlantError("tomato"),
        WaterError(10),
    ]
    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def test_all_errors():
    print("=== Custom Garden Errors Demo ===\n")
    wilting("tomato", True)
    watering(10)
    print("Testing catching all garden errors...")
    raise_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_all_errors()
