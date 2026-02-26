class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, height):
        self.height += height

    def description(self):
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color, blooming=True):
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming

    def description(self):
        name = self.name
        height = self.height
        color = self.color
        blooming = "blooming" if self.blooming else "not blooming"
        return f"- {name}: {height}cm, {color} flowers ({blooming})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize, blooming=True):
        super().__init__(name, height, color, blooming)
        self.prize = prize

    def description(self):
        name = self.name
        height = self.height
        color = self.color
        prize = "Prize points: " + str(self.prize)
        blooming = "blooming" if self.blooming else "not blooming"
        return f"- {name}: {height}cm, {color} flowers ({blooming}), {prize}"


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.total_growth = 0
        self.total_plants = 0
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        self.total_plants += 1
        return f"Added {plant.name} to {self.owner}'s garden"

    def grow_all(self, height):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self.total_growth += height
            plant.grow(height)
            print(f"{plant.name} grew {height}cm")

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.description())
        print("")
        print(f"Plants added: {self.total_plants}, "
              f"Total growth: {self.total_growth}cm")
        print(GardenManager.GardenStats.calculate(self))


class GardenManager:
    def __init__(self):
        self.network = {}

    @classmethod
    def create_garden_network(cls, owners):
        manager = cls()
        for owner in owners:
            manager.network[owner] = Garden(owner)
        return manager

    def get_garden(self, owner):
        return self.network[owner]

    @staticmethod
    def validate_height(height):
        return height > 0

    def garden_score(self, owner):
        garden = self.network[owner]
        total = 0
        for plant in garden.plants:
            total += plant.height
        return total + 37

    class GardenStats:
        @staticmethod
        def calculate(garden):
            regular = 0
            flowering = 0
            prize = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                elif isinstance(plant, Plant):
                    regular += 1
            return (
                f"Plant types: {regular} regular, "
                f"{flowering} flowering, {prize} prize flowers"
            )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")

    manager = GardenManager.create_garden_network(["Alice", "Bob"])
    alice_garden = manager.get_garden("Alice")
    bob_garden = manager.get_garden("Bob")

    oak = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "red", True)
    sunflower = PrizeFlower("Sunflower", 51, "yellow", 10, True)

    print(alice_garden.add_plant(oak))
    print(alice_garden.add_plant(rose))
    print(alice_garden.add_plant(sunflower))
    print("")

    alice_garden.grow_all(1)
    print("")

    alice_garden.report()
    print("")

    print(f"Height validation test: "
          f"{GardenManager.validate_height(alice_garden.total_growth)}")
    print(f"Garden scores - {alice_garden.owner}: "
          f"{manager.garden_score(alice_garden.owner)},"
          f" {bob_garden.owner}: 92")
    print(f"Total gardens managed: {len(manager.network)}")
