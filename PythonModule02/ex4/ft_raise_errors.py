def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")
        return f"Plant '{plant_name}' is healthy!"
    except ValueError as e:
        return f"Error: {e}"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    print(check_plant_health("tomato", 10, 2))

    print("\nTesting empty plant name...")
    print(check_plant_health("", 10, 2))

    print("\nTesting bad water level...")
    print(check_plant_health("tomato", 15, 3))

    print("\nTesting bad sunlight hours...")
    print(check_plant_health("tomato", 10, 0))

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
