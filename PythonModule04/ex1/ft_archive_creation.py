import sys
import typing


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        f: typing.IO[str] = open(sys.argv[1], "r")
        content: str = f.read()
        lines: list[str] = content.split("\n")
        f.close()
        print("---\n")
        for line in lines:
            print(line)
        print("\n---")
        print(f"File '{sys.argv[1]}' closed.")

        new: list[str] = [line + "#" for line in lines]
        print("\nTransform data:")
        print("---\n")
        for line in new:
            print(line)
        print("\n---")

        name: str = input("Enter new file name (or empty): ")
        if name:
            print(f"Saving data to '{name}'")
            f = open(name, "w")
            for line in new:
                f.write(line + "\n")
            f.close()
            print(f"Data saved in file '{name}'.")
        else:
            print("Not saving data.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        sys.exit(1)
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        sys.exit(1)
