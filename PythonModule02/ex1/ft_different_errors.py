def garden_operations():
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        missing = "missing.txt"
        with open(missing) as f:
            f.read()
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{missing}'\n")

    try:
        print("Testing KeyError...")
        plants = {"rose": 30, "yellow": 10}
        missing = plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        print("Testing multiple errors together...")
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == '__main__':
    test_error_types()
