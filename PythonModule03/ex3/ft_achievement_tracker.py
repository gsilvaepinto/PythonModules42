import random

ALL_ACHIEVEMENTS = [
    "First Steps",
    "Speed Runner",
    "Master Explorer",
    "Treasure Hunter",
    "Crafting Genius",
    "Strategist",
    "Survivor",
    "Boss Slayer",
    "Collector Supreme",
    "Untouchable",
    "World Savior",
    "Sharp Mind",
    "Hidden Path Finder"
]

def gen_player_achievements() -> set:
    return set(random.sample(ALL_ACHIEVEMENTS, random.randint(1, len(ALL_ACHIEVEMENTS))))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    for name in players:
        print(f"Player {name}: {players[name]}")

    distinct = set()
    for name in players:
        distinct = distinct.union(players[name])
    print(f"\nAll distinct achievements: {distinct}\n")

    common = set(ALL_ACHIEVEMENTS)
    for name in players:
        common = common.intersection(players[name])
    print(f"Common achievements: {common}\n")

    for name in players:
        others = set()
        for other in players:
            if other != name:
                others = others.union(players[other])
        unique = players[name].difference(others)
        print(f"Only {name} has: {unique}")
    print("")

    for name in players:
        print(f"{name} is missing: {distinct.difference(players[name])}")
