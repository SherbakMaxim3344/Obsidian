from src.model.creature import Creature

_creatures = [
    Creature(
        name="Yeti",
        country="CN",
        area="Him",
        description="rip",
        aka="Snowman"
    ),
    Creature(
        name="Bigfoot",
        description="HZZZZZ",
        area="*",
        aka="Sas",
        country="USA"
    ),
]

def get_all() -> list[Creature]:
    return _creatures

def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    return creature

def modify(creature: Creature) -> Creature:
    return creature

def replace(creature: Creature) -> Creature:
    return creature

def delete(name: str):
    return None