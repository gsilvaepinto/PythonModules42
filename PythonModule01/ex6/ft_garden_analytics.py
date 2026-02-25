class Plant:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height
		
    def description(self) -> str:
        return f"- {self.name}: {self.height}cm"
    
    def grow(self, height):
        self.height += height
    

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def description(self) -> str:
        return f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)"
    

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize

    def description(self) -> str:
        name = self.name
        height = self.height
        color = self.color
        prize = ("Prize points: " + str(self.prize))
        return f"- {name}: {height}cm, {color} flowers (blooming), {prize}"
    

class Garden:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.plants = []

    def add_plants(self, plant) -> str:
        self.plants.append(plant)
        return f"Added {plant.name} to {self.owner}'s garden"

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")  
        for plant in self.plants:
            print(plant.description())


class GardenManager:
    def __init__(self):
        self.network = {}

    def get_garden(self, owner):
        return self.network[owner]
    
    @classmethod
    def create_garden_network(cls, owners):
        manager = cls()
        for owner in owners:
            manager.network[owner] = Garden(owner)
        return manager
    
    @staticmethod
    def validate_height(height):
        return height > 0
    
    def garden_score(self, owner):
        garden = self.network[owner]
        total = 0
        for plant in garden.plants:
            total += plant.height
        return total + 40
    
    class GardenStats():
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
            return {"regular": regular, "flowering": flowering, "prize": prize}
        
if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    
    manager = GardenManager.create_garden_network(["Alice", "Bob"])
    
    alice_garden = manager.get_garden("Alice")
    bob_garden = manager.get_garden("Bob")
    
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    lavender = FloweringPlant("Lavender", 20, "purple")
    corn = Plant("Corn", 32)
    
    print(alice_garden.add_plants(oak))
    print(alice_garden.add_plants(rose))
    print(alice_garden.add_plants(sunflower))
    
    bob_garden.add_plants(corn)
    bob_garden.add_plants(lavender)
    
    print()
    alice_garden.grow_all()
    print()
    alice_garden.report()
    print()
    
    stats = GardenManager.GardenStats.calculate(alice_garden)
    print(f"Plant types: {stats['regular']} regular, {stats['flowering']} flowering, {stats['prize']} prize flowers")
    
    print(f"Height validation test: {GardenManager.validate_height(10)}")
    
    alice_score = manager.garden_score("Alice")
    bob_score = manager.garden_score("Bob")
    print(f"Garden scores - Alice: {alice_score} - Bob: {bob_score}")