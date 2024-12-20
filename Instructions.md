# PS4 - Object-Oriented Programming (OOP)

### Deadline: January 7, 2024 23:59

In this assignment, you will learn how to use object-oriented programming paradigm to create a game simulation. Note that this assignment, like any other assignment, will be graded with additional different test cases.

### Important Note
The constructor parameters and the methods you should implement is listed for each class. However, *you will likely need to add more attributes and methods to make the whole simulation work*. These additional features will depend on the specific requirements of your game.



## Description:
Welcome to the realm of Metin2.0, a mystical domain where warriors engage in epic battles! You're tasked with creating an immersive battle simulation involving valiant players: Ninjas, Warriors, Shamans, and Suras. Each player possesses unique attributes like health, damage, armor, and healing power.


## Character Classes

Create the following classes for characters.

### 1. Player Class
This is a parent class for all type of players in the game. The constructor parameters are listed below in order.

- **Parameters/Attributes**:
  - `name`: String
  - `health`: Integer, starts with the given value and decreases/increases as player plays rounds
  - `damage`: Integer (default: 40), representing the damage given to the opponent player
  - `armor`: Integer (default: 15), representing the protective power of the player. 
  - `healing_power`: Integer (default: 10)
- **Methods**:
  - Access and update methods for attributes

    
### 2. Ninja Class 

This is a subclass of the Player class.

- Inherits attributes and methods from Player

- **Special Rule**:
  - If a Ninja's name is "Itachi" their abilities mysteriously double, increasing damage, armor, and healing power. 

### 3. Warrior Class

This is a subclass of the Player class.

- Inherits attributes and methods from Player
  
- **Special Rule**:
  - Warriors are powerful beings; those named "Curry" possess doubled attributes
  - Default damage is set to 60 for others

### 4. Shaman Class 
This is a subclass of the Player class.

- Inherits attributes and methods from Player
- **Special Rule**:
  - If name is "Melisandre", attributes are doubled
  - Default healing power is 20 for others

### 5. Sura Class 
This is a subclass of the Player class.

- Inherits attributes and methods from Player
- **Special Rule**:
  - If name is "Geralt", attributes are doubled
  - Default armor is 30 for others


## Weapon Classes

Now, there is a blacksmith in the town! Characters can equip weapon and use its special powers! However, **a weapon can only be acquired by certain player types.** If a player tries to equip a weapon they cannot request, their request will be invalid and they will continue without the weapon. Also, a player can equip with only one weapon and test cases will be according to this. 

Now, implement the following weapons. Also do not forget to add attributes and methods to `Player` class so that they can equip with the weapons.

After implementation, the weapons should be ready for testing in the arena!

### 1. Weapon Class

This is a parent class for all weapons. Constructor parameters are listed below in order.

- **Parameters/Attributes**:
  - `name`: String
  - `durability`: Integer, representing the number of rounds that this weapon can be used. 
  - `damage`: Integer, representing the additional damage that the player will gain by using this weapon. 
  - `user_list`: List of `Character` types. It includes all the character types that can equip this weapon. 
- **Methods**:
  - `can_use(Player)`: Returns True if the player can use the weapon
  - `used()`: Decreases durability by one after each use

### 2. Sword Class 

**Sword** is a weapon _(Oh really?)_ that can be used only by *warriors or ninjas*.

- **Additional Parameters/Attributes**:
  - `armor_penetration`: Integer, representing the _temporary_ damage that the player can do on the opponent's armor **(only on armor)**. It is temporary because this damage does not break the armor permanently _(see Mace in comparison)_. *It breaks the armor only for the current round.*
  - `poisonous`: Boolean, representing whether this sword has been covered with a special poison _(Hamlet would like that)_ or not. If it is covered, the opponent who is taken damage by that sword will not be able to heal him/herself on his/her first try, i.e., his/her first heal move will be skipped, after that the effect of being poisoned will disappear. 

### 3. Mace Class 
Mace is a heavy weapon for breaking armor _(or bones...)_ ! It can be used only by *warriors*.

- **Additional Parameters/Attributes**:
  - `armor_reduction`: Integer, representing the _permanent_ damage that the player can do on the opponent's armor **(only on armor)**. It is permanent because once a player's armor is damaged by a Mace, the protection capability of the armor is diminished for all following rounds! It can even be totally broken!
    Notice that, *opponent's armor is damaged after the player's attack*. In the current round, opponent uses its original armor power. Its armor will be damaged for the next rounds. 

### 4. Shuriken Class 
Shuriken is a ranged small weapon that can be used only by *ninjas*.

### 5. Powder Bomb Class 
Powder bomb is a strategic weapon that can create wonders in a talented hand. It can be used only by *shamans and suras*.


- **Functionality**:
  - It deals no damage; however, it gives the player who used it a chance to disappear! That is, once it is used, the player can dodge the next attack of the opponent and will take no damage! After the opponent attacks, this effect disappears, i.e., the disappearing effect is not permanent.



## Battle Arena

### Arena Class
The Arena Class serves as the virtual battleground where two characters face off in exciting combat. It's like the director of a battle, applying the game's fight rules and deciding who wins based on the strategies and moves of the players. This class makes sure each clash is fair, thrilling, and follows the story of the battle, considering everything from the characters' skills to the mighty weapons they wield. They can choose to launch a fierce *"attack"* to conquer their opponent or choose to *"heal"* and mend their wounds.

**Note:** As a battle in the arena can be lethal, ** no player fights more than once.**
 
- **Method**: `fight(player1, player2, commands)`
  - **Parameters**:
    - `player1`: Player
    - `player2`: Player
    - `commands`: List of strings ("attack" or "heal")
  - **Functionality**:
    - Iterates through commands and performs actions. Player 1 will follow commands with even indexes and player 2 will follow commands with odd indexes.
    - *"attack"*: Reduces opponent's health by attacker's damage minus opponent's armor
    - *"heal"*: Increases the healer's health by their healing power
    - The battle progresses until one warrior's health drops below or equal to zero or all commands are executed.
  - **Returns**:
    - The name of the victorious warrior or "Draw" if neither's health drops to zero

Examples without Weapons: 
```
ninja1 = Ninja("Itachi", 100)
warrior1 = Warrior("Enes", 120)
shaman1 = Shaman("Melisandre", 110)
sura1 = Sura("Geralt", 100)

ninja2 = Ninja("Kakashi", 70)
warrior2 = Warrior("Conan", 110)
shaman2 = Shaman("Taha", 105)
sura2 = Sura("Ege", 80)

Arena.fight(ninja1, warrior1, ["attack", "heal", "attack", "attack"]) --> Itachi

Arena.fight(shaman2, sura2,["attack", "attack", "heal", "attack"]) --> Draw

Arena.fight(ninja2, sura1, ["heal", "attack", "attack", "attack", "heal", "attack"]) --> Geralt

Arena.fight(shaman1, warrior2,["attack", "attack", "heal", "heal", "attack", "attack"]) --> Melisandre

```

An example with Weapons: 
```
mace1 = Mace("Bone Breaker", 1, 20, 15)
shurinken1 = Shuriken("7th Star", 2, 10)

ninja1 = Ninja("Donatello", 106)
warrior1 = Warrior("Mordekaiser", 120)

warrior1.equip(mace1)
ninja1.equip(shurinken1)

Arena.fight(warrior1, ninja1, ["attack", "heal", "attack", "attack"]) -->  "Mordekaiser"
```

**Please refer to test_samples.py for more examples.**


