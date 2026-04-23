from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    return ['bats', 'frogs', 'arsenic', 'eyeball']


def dark_spell_record(spell_name: str, ingredients: str):
    result = validate_ingredients(ingredients)
    if 'VALID' in result:
        return f"Spell '{spell_name}' recorded with ingredients: {result}"
    return f"Spell '{spell_name}' rejected with ingredients: {result}"
