from src.model.creature import Creature
from src.service import creature as code

sample = Creature(
    name="Yeti",
    country="CN",
    area="Him",
    description="rip",
    aka="Snowman",
    )

def test_create():
    resp = code.create(sample)
    assert resp == sample
    
def test_get_exists():
    resp = code.get_one("Yeti")
    assert resp == sample
    
def test_get_missing():
    resp = code.get_one("boxturtle")
    assert resp is None
    
# python3 -m pytest -v src/test/unit/service/test_creature.py