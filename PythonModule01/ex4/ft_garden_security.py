class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant: SecurePlant = SecurePlant("Rose", 25, 30)
    print("")

    plant.set_height(-5)

    name = plant.name
    height = plant.get_height()
    age = plant.get_age()
    print(f"\nCurrent plant: {name} ({height}cm, {age} days)")
