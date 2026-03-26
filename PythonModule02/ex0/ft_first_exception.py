def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    for value in ["25", "abc"]:
        print(f"Input data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")
