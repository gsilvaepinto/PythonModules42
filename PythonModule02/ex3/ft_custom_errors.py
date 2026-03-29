class GardenError(Exception):
    def __init__(self, msg="Unknown plant error"):
        super().__init__(msg)

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass


def test_plant_errors():
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

test_plant_errors()