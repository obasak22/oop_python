try:
    from main import Player, Ninja, Warrior, Shaman, Sura, Arena, Weapon, Sword, Shuriken, Mace, PowderBomb
except ImportError:
    pass

def test_metin2_1():
    ninja1 = Ninja("Itachi", 100)
    warrior1 = Warrior("Thompson", 120)
    commands = [
      "attack", "heal", "attack", "attack", "heal", "attack", "attack", "heal"
    ]
    assert Arena.fight(ninja1, warrior1, commands) == "Itachi"


def test_metin2_2():
    shaman1 = Shaman("Gandalf", 110)
    sura1 = Sura("Ragnar", 125)
    commands = [
      "attack", "attack", "heal", "attack", "heal", "attack", "attack", "heal"
    ]
    assert Arena.fight(shaman1, sura1, commands) == "Draw"


def test_metin2_3():
    sura2 = Sura("Geralt", 100)
    warrior3 = Warrior("Draymond", 120)
    commands = [
      "attack", "attack", "heal", "attack", "heal", "attack", "attack",
      "attack", "heal"
    ]
    assert Arena.fight(sura2, warrior3, commands) == "Geralt"

# Armor reduction test
def test_metin2_4():
    mace1 = Mace("Bone Breaker", 1, 20, 15)
    shurinken1 = Shuriken("7th Star", 2, 10)

    ninja1 = Ninja("Donatello", 106)
    warrior1 = Warrior("Mordekaiser", 120)

    warrior1.equip(mace1)
    ninja1.equip(shurinken1)
    commands = ["attack", "heal", "attack", "attack"]
    assert Arena.fight(warrior1, ninja1, commands) == "Mordekaiser"

# Powder test
def test_metin2_5():
    PowderBomb1 = PowderBomb("Smoke", 2)
    shaman1 = Shaman("Gandalf", 110)
    sura1 = Sura("Ragnar", 125)
    shaman1.equip(PowderBomb1)
    commands = ["attack", "attack", "attack", "attack", "attack", "attack", "attack", "attack", "attack", "attack", "attack", "attack"]
    assert Arena.fight(shaman1, sura1, commands) == "Draw"

# Poison test
def test_metin2_6():
    pois_sword = Sword("Snake", 2, 50, 0, True)
    ninja2 = Ninja("Kakashi", 90)

    ninja2.equip(pois_sword)
    warrior2 = Warrior("Curry", 110)

    commands = ["attack", "heal", "attack"]
    assert Arena.fight(ninja2, warrior2, commands) == "Kakashi"

# Armor penetration test
def test_metin2_7():
    powder1 = PowderBomb("Sand", 1)
    sword2 = Sword("Katana", 3, 1, 14)

    ninja3 = Ninja("Itachi", 150)
    shaman2 = Shaman("Merlin", 115)

    ninja3.equip(sword2)
    shaman2.equip(powder1)
    commands = ["attack", "attack", "heal", "heal", "attack", "heal", "attack", "attack", "heal"]
    assert Arena.fight(ninja3, shaman2, commands) == "Itachi"


# Changing weapon test.
def test_metin2_8():

    Mace1 = Mace("Spatula", 2, 10, 15)
    Sword2 = Sword("The Finisher", 1, 100, 1)
    Sword3 = Sword("My Little Friend", 1, 20, 1)

    warrior3 = Warrior("Spongebob", 90)
    warrior2 = Warrior("Squidward", 190)

    warrior3.equip(Mace1)
    warrior2.equip(Sword2)
    warrior2.equip(Sword3)

    commands = ["attack", "attack", "attack", "heal", "attack", "heal"]
    assert Arena.fight(warrior3, warrior2, commands) == "Draw"


if __name__ == '__main__':
    tests = [
      test_metin2_1, test_metin2_2, test_metin2_3, test_metin2_4,
      test_metin2_5, test_metin2_6, test_metin2_7, test_metin2_8
    ]

    print('Points:')
    for t in tests:
        try:
          t()
          print(str(t).split()[1], 1)
        except AssertionError:
          print(str(t).split()[1], 0)
