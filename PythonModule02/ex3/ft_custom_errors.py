class GardenError(Exception):
    def __init__(self, msg="Unknown plant error"):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg="The tomato plant is wilting!"):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg="Not enough water in the tank!"):
        super().__init__(msg)


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    for error in [PlantError, WaterError]:
        print(f"Testing {error.__name__}...")
        try:
            raise error()
        except error as e:
            print(f"Caught {error.__name__}: {e}\n")
    print("Testing catching all garden errors...")
    for error in [PlantError, WaterError]:
        try:
            raise error()
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")
