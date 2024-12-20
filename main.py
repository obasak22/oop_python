class Player:
    def __init__(self, name, health, damage=40, armor=15, healing_power=10):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.healing_power = healing_power
        self.current_weapon = None
    def show_name(self):
        return self.name
    def show_health(self):
        return self.health
    def show_damage(self):
        return self.damage
    def show_armor(self):
        return self.armor
    def show_healing_power(self):
        return self.healing_power
    def update_name(self, name):
        self.name = name
    def update_health(self, health):
        self.health = health
    def update_damage(self, damage):
        self.damage = damage
    def update_armor(self, armor):
        self.armor = armor
    def update_healing_power(self, healing_power):
        self.healing_power = healing_power
    def equip(self, weapon):
        if weapon.can_use(self):
            self.current_weapon = weapon
class Ninja(Player):
    def __init__(self, name, health, damage=40, armor=15, healing_power=10):
        super().__init__(name, health, damage, armor, healing_power)
        if self.name == "Itachi":
            self.damage *= 2
            self.armor *= 2
            self.healing_power *= 2
class Warrior(Player):
    def __init__(self, name, health, damage=60, armor=15, healing_power=10):
        super().__init__(name, health, damage, armor, healing_power)
        if self.name == "Curry":
            self.damage *= 2
            self.armor *= 2
            self.healing_power *= 2
class Shaman(Player):
    def __init__(self, name, health, damage=40, armor=15, healing_power=20):
        super().__init__(name, health, damage, armor, healing_power)
        if self.name == "Melisandre":
            self.damage *= 2
            self.armor *= 2
            self.healing_power *= 2
class Sura(Player):
    def __init__(self, name, health, damage=40, armor=30, healing_power=10):
        super().__init__(name, health, damage, armor, healing_power)
        if self.name == "Geralt":
            self.damage *= 2
            self.armor *= 2
            self.healing_power *= 2
class Weapon:
    def __init__(self, name, durability, damage, user_list=[]):
        self.name = name
        self.durability = durability
        self.damage = damage
        self.user_list = user_list
    def used(self):
        self.durability -= 1
class Sword(Weapon):
    def __init__(self, name, durability, damage, armor_penetration=0, poisonous=False, user_list=["Warrior","Ninja"]):
        super().__init__(name, durability, damage, user_list)
        self.armor_penetration = armor_penetration
        self.poisonous = poisonous
    def can_use(self, player):
        if isinstance(player, Warrior) or isinstance(player, Ninja):
            return True
        else:
            return False
class Mace(Weapon):
    def __init__(self, name, durability, damage, armor_reduction=0, user_list=["Warrior"]):
        super().__init__(name, durability, damage, user_list)
        self.armor_reduction = armor_reduction
    def can_use(self, player):
        if isinstance(player, Warrior):
            return True
        else:
            return False
class Shuriken(Weapon):
    def __init__(self, name, durability, damage, user_list=["Ninja"]):
        super().__init__(name, durability, damage, user_list)
    def can_use(self, player):
        if isinstance(player, Ninja):
            return True
        else:
            return False
class PowderBomb(Weapon):
    def __init__(self, name, durability=1, damage=0, user_list=["Shaman","Sura"]):
        super().__init__(name, durability, damage, user_list)
    def can_use(self, player):
        if isinstance(player, Shaman) or isinstance(player, Sura):
            return True
        else:
            return False
class Arena():
    @staticmethod
    def fight(player1, player2, commands):
        i = 0
        player1_poisoned = False
        player2_poisoned = False
        while player1.health > 0 and player2.health > 0 and i < len(commands):
            if i % 2 == 0:
                if commands[i] == "attack" and isinstance(player1.current_weapon, PowderBomb) and player1.current_weapon.durability > 0:
                    player1.current_weapon.used()
                    i += 1
                elif commands[i] == "attack" and isinstance(player1.current_weapon, Sword) and player1.current_weapon.durability > 0:
                    player1.current_weapon.used()
                    if player1.current_weapon.poisonous:
                        player2_poisoned = True
                    if player2.armor > player1.current_weapon.armor_penetration:
                        if player2.armor - player1.current_weapon.armor_penetration >= player1.damage + player1.current_weapon.damage:
                            pass
                        else:
                            player2.health -= -player2.armor + player1.current_weapon.armor_penetration + player1.damage + player1.current_weapon.damage
                    else:
                        player2.health -= player1.damage + player1.current_weapon.damage
                elif commands[i] == "attack" and isinstance(player1.current_weapon, Mace) and player1.current_weapon.durability > 0:
                    player1.current_weapon.used()
                    if player2.armor >= player1.current_weapon.armor_reduction:
                        if player2.armor > player1.damage + player1.current_weapon.damage:
                            pass
                        else:
                            player2.health -= -player2.armor + player1.damage + player1.current_weapon.damage
                        player2.armor -= player1.current_weapon.armor_reduction
                    else:
                        player2.health -= player1.damage + player1.current_weapon.damage
                        player2.armor = 0
                elif commands[i] == "attack" and isinstance(player1.current_weapon, Shuriken) and player1.current_weapon.durability > 0:
                    player1.current_weapon.used()
                    if player2.armor > player1.damage + player1.current_weapon.damage:
                        pass
                    else:
                        player2.health -= -player2.armor + player1.damage + player1.current_weapon.damage
                elif commands[i] == "heal":
                    if player1_poisoned:
                        pass
                    else:
                        player1.health += player1.healing_power
                    player1_poisoned = False
                else:
                    if commands[i] == "attack" and player2.armor >= player1.damage:
                        pass
                    elif commands[i] == "attack" and player2.armor < player1.damage:
                        player2.health -= player1.damage - player2.armor
            else:
                if commands[i] == "attack" and isinstance(player2.current_weapon, PowderBomb) and player2.current_weapon.durability > 0:
                    player2.current_weapon.used()
                    i += 1
                elif commands[i] == "attack" and isinstance(player2.current_weapon, Sword) and player2.current_weapon.durability > 0:
                    player2.current_weapon.used()
                    if player2.current_weapon.poisonous:
                        player1_poisoned = True
                    if player1.armor > player2.current_weapon.armor_penetration:
                        if player1.armor - player2.current_weapon.armor_penetration >= player2.damage + player2.current_weapon.damage:
                            pass
                        else:
                            player1.health -= -player1.armor + player2.current_weapon.armor_penetration + player2.damage + player2.current_weapon.damage
                    else:
                        player1.health -= player2.damage + player2.current_weapon.damage
                elif commands[i] == "attack" and isinstance(player2.current_weapon, Mace) and player2.current_weapon.durability > 0:
                    player2.current_weapon.used()
                    if player1.armor > player2.current_weapon.armor_reduction:
                        if player1.armor >= player2.damage + player2.current_weapon.damage:
                            pass
                        else:
                            player1.health -= -player1.armor + player2.damage + player2.current_weapon.damage
                        player1.armor -= player2.current_weapon.armor_reduction
                    else:
                        player1.health -= player2.damage + player2.current_weapon.damage
                        player1.armor = 0
                elif commands[i] == "attack" and isinstance(player2.current_weapon, Shuriken) and player2.current_weapon.durability > 0:
                    player2.current_weapon.used()
                    if player1.armor > player2.damage + player2.current_weapon.damage:
                        pass
                    else:
                        player1.health -= -player1.armor + player2.damage + player2.current_weapon.damage
                elif commands[i] == "heal":
                    if player2_poisoned:
                        pass
                    else:
                        player2.health += player2.healing_power
                    player2_poisoned = False
                else:
                    if commands[i] == "attack" and player1.armor >= player2.damage:
                        pass
                    elif commands[i] == "attack" and player1.armor < player2.damage:
                        player1.health -= player2.damage - player1.armor
            i += 1
        if player1.health <= 0:
            return player2.name
        elif player2.health <= 0:
            return player1.name
        else:
            return "Draw"
