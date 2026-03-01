def check_temperature(temp_str):
    try:
        print(f"Testing temperature: {temp_str}")
        value = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    try:
        if value > 40:
            raise ValueError(
                f"Error: {value}°C is too hot for plants (max 40°C)")
        if value < 0:
            raise ValueError(
                f"Error: {value}°C is too cold for plants (min 0°C)")
    except ValueError as e:
        print(e)
        return None

    print(f"Temperature {value}°C is perfect for plants!")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")

    values = ["25", "abc", "100", "-50"]
    for value in values:
        check_temperature(value)
        print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
