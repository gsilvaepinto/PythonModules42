from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print("")


def test_battle(factory1, factory2):
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(f"{c1.describe()} vs. {c2.describe()} fight!")
    print(c1.attack())
    print(c2.attack())


flame_factory = FlameFactory()
aqua_factory = AquaFactory()

test_factory(flame_factory)
test_factory(aqua_factory)
test_battle(flame_factory, aqua_factory)