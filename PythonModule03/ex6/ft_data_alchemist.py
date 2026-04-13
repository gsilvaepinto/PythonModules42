import random

ALL_NAME: list[str] = ['Alice', 'bob', 'Charlie',
                       'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']


if __name__ == '__main__':
    print("=== Game Data Alchemist ===\n")
    players: list[str] = list(ALL_NAME)
    print("Initial list of players:", players)

    capitalized = [name.capitalize() for name in ALL_NAME]
    print("New list with all names capitalized:", capitalized)
    unique = [name for name in ALL_NAME if name == name.capitalize()]
    print("New list of capitalized names only:", unique)

    scores = {name: random.randint(0, 1000) for name in capitalized}
    print("\nScore dict:", scores)
    average = sum(scores.values()) / len(scores)
    print(f"Score average: {average:.2f}")
    high = {name: score for name, score in scores.items() if score > average}
    print(f"High scores: {high}")
