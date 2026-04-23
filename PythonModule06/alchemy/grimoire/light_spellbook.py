def light_spell_allowed_ingredients() -> list:
    return ['earth', 'air', 'fire', 'water']


def light_spell_record(spell_name: str, ingredients: str):
    from .light_validator import validate_ingredients
    result = validate_ingredients(ingredients)
    if 'VALID' in result:
        return f"Spell '{spell_name}' recorded with ingredients: {result}"
    return f"Spell '{spell_name}' rejected with ingredients: {result}"
