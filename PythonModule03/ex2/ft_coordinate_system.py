import math


def create_coordinate(x, y, z):
    try:
        return int(x), int(y), int(z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}")')


def calculate_distance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    )


def parse_coordinate(coordinate):
    parsed = create_coordinate(*coordinate.split(","))
    if parsed:
        print(f"Parsed position: {parsed}")
    return parsed


if __name__ == '__main__':
    print("=== Game Coordinate System ===\n")

    coordinate = create_coordinate(10, 20, 5)
    null_coordinate = create_coordinate(0, 0, 0)

    print(f"Position created: {coordinate}")
    print(f"Distance between {null_coordinate} and {coordinate}: "
          f"{calculate_distance(null_coordinate, coordinate):.2f}\n")

    data = "3,4,0"
    print(f'Parsing coordinates: "{data}"')
    parsed = parse_coordinate(data)
    print(f"Distance between {null_coordinate} and {parsed}: "
          f"{calculate_distance(null_coordinate, parsed):.1f}\n")

    invalid = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid}"')
    invalid_parsed = parse_coordinate(invalid)

    print("\nUnpacking demonstration...")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates:  X={x}, Y={y}, Z={z}")
