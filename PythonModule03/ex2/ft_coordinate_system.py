import math


def get_player_pos() -> tuple:
    while True:
        try:
            coordinates = input("Enter new coordinates "
                                "as floats in format 'x,y,z': ")
            data = coordinates.split(",")
            if len(data) != 3:
                raise ValueError("Invalid syntax")
            parsed = []
            for value in data:
                try:
                    parsed.append(float(value.strip()))
                except ValueError:
                    raise ValueError(
                        f"Error on parameter '{value.strip()}': could"
                        f" not convert string to float: '{value.strip()}'")
            x, y, z = parsed
            return (x, y, z)
        except ValueError as e:
            print(e)


def calculate_distance(a: tuple, b: tuple) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def first_set() -> tuple:
    print("Get a first set of coordinates")
    coordinates = get_player_pos()
    print(f"Got a first tuple: {coordinates}")
    x, y, z = coordinates
    print(f"It includes: X={x}, Y={y}, Z={z}")
    distance = calculate_distance(coordinates, (0, 0, 0))
    print(f"Distance to center: {distance:.4f}")
    return coordinates


def second_set(first_coordinate) -> None:
    print("\nGet a second set of coordinates")
    coordinates = get_player_pos()
    distance = calculate_distance(coordinates, first_coordinate)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    first_data = first_set()
    second_data = second_set(first_data)
