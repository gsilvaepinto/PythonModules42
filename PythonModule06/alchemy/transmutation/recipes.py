import elements
from .. import potions
from ..elements import create_air


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and '{potions.strength_potion()}' mixed "
            f"with '{elements.create_fire()}'")
