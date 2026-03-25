class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0
        self._plant_age = 0
        self.set_height(height, silent=True)
        self.set_age(age, silent=True)
        print(f"Plant created: {self}")

    def get_height(self):
        return self._height

    def set_height(self, value: float, silent=False):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            if not silent:
                print(f"Height updated: {value}cm")

    def get_age(self):
        return self._plant_age

    def set_age(self, value: float, silent=False):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._plant_age = value
            if not silent:
                print(f"Age updated: {value} days")

    def __str__(self):
        return f"{self.name}: {self._height:.1f}cm, {self._plant_age} days old"


def main():
    print("=== Garden Security System ===")
    plant: Plant = Plant('Rose', 15, 10)
    print("")

    plant.set_height(25)
    plant.set_age(30)
    print("")

    plant.set_height(-5)
    plant.set_age(-5)

    print(f"\nCurrent state: {plant}")


if __name__ == "__main__":
    main()
