print("=== Garden Temperature Checker ===\n")


def check_temperature(temp_str):
    try:
        print(f"Testing temperature: {temp_str}")
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    try:
        if temp > 40:
            raise ValueError(
                f"Error: {temp}°C is too hot for plants (max 40°C)")
        if temp < 0:
            raise ValueError(
                f"Error: {temp}°C is too cold for plants (min 0°C)")
    except ValueError as e:
        print(e)
        return None

    print(f"Temperature {temp}°C is perfect for plants!")


def test_temperature():
    numbers = ["25", "abc", "100", "-50"]

    for number in numbers:
        check_temperature(number)
        print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
