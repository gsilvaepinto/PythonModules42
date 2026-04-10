import sys

if __name__ == '__main__':
    print("=== Inventory System Analysis ===")
    inventory = {}
    for item in sys.argv[1:]:
        data = item.split(':')
        if len(data) != 2:
            print(f"Error - invalid parameter '{item}'")
        elif data[0] in inventory:
            print(f"Redundant item '{data[0]}' - discarding")
        else:
            try:
                inventory[data[0]] = int(data[1])
            except ValueError as e:
                print(f"Quantity error for '{data[0]}': {e}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: "
          f"{sum(inventory.values())}")
    print(f"Item sword represents "
          f"{inventory['sword'] / sum(inventory.values()) * 100:.1f}%")
    print(f"Item potion represents "
          f"{inventory['potion'] / sum(inventory.values()) * 100:.1f}%")
    print(f"Item shield represents "
          f"{inventory['shield'] / sum(inventory.values()) * 100:.1f}%")
    print(f"Item armor represents "
          f"{inventory['armor'] / sum(inventory.values()) * 100:.1f}%")
    print(f"Item helmet represents "
          f"{inventory['helmet'] / sum(inventory.values()) * 100:.1f}%")
    most = None
    for item in inventory:
        if most is None or inventory[most] < inventory[item]:
            most = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    least = None
    for item in inventory:
        if least is None or inventory[least] > inventory[item]:
            least = item
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({'magic_item': 1})
    print(inventory)
