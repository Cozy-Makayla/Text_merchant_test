from random import randint as r
class Wealth():
    def __init__(self, name: str, desc: str, value: int, weight: float, amount: int):
        self.name = name
        self.desc = desc
        self.value = value
        self.weight = weight
        self.amount = amount
class Weapons():
    def __init__(self, name: str, desc: str, damage: int, value: int, weight: float, amount: int):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.value = value
        self.weight = weight
        self.amount = amount
class Armor():
    def __init__(self, name: str, desc: str, protection: int, value: int, weight: float, amount: int):
        self.name = name
        self.desc = desc
        self.protection = protection
        self.value = value
        self.weight = weight
        self.amount = amount
class Food():
    def __init__(self, name: str, desc: str, health: int, value: int, weight: float, amount: int):
        self.name = name
        self.desc = desc
        self.health = health
        self.value = value
        self.weight = weight
        self.amount = amount
class Junk():
    def __init__(self, name: str, desc: str, value: int, weight: float, amount: int):
        self.name = name
        self.desc = desc
        self.value = value
        self.weight = weight
        self.amount = amount

def pstart_wealth_list(start_list: list):
    start_list.append(Wealth('Diamond', 'A precious gem stone said to be quite rare in these parts', 1500, 0.3, 0))
    start_list.append(Wealth('Emerald', 'The vales name sake, shines with a deep viridescent tone', 750, 0.3, 0))
    start_list.append(Wealth('Ruby', 'The deep crimson leaves you feeling wonderful', 500, 0.3, 100))
    start_list.append(Wealth('Shappire', 'As blue as the ocean and just as deep in colour', 200, 0.3, 0))
    start_list.append(Wealth('Platinum Bar', 'A rare gaia mineral, mined by experts and smithed by the wealthy', 5000, 1.0, 0))
    start_list.append(Wealth('Gold Bar', 'It never rusts!', 2500, 1.0, 0))
def pstart_weapon_list(start_list: list):
    start_list.append(Weapons('Bronze Dagger', 'A short bronze stabby weapon', 1, 5, 5.0, 1))
    start_list.append(Weapons('Iron Dagger', 'A short Iron stabby weapon', 5, 15, 5.0, 0))
    start_list.append(Weapons('Steel Dagger', 'A short Steel stabby weapon', 10, 25, 5.0, 0))
    start_list.append(Weapons('Bronze Short Sword', 'A bronze short sword, held in one hand', 10, 15, 10.0, 0))
    start_list.append(Weapons('Iron Short Sword', 'A iron short sword, held in one hand', 17, 35, 10.0, 0))
    start_list.append(Weapons('Steel Short Sword', 'A steel short sword, held in one hand', 22, 50, 10.0, 0))
    start_list.append(Weapons('Bronze Spear', 'A bronze spear, held in both hands', 17, 25, 25.0, 0))
    start_list.append(Weapons('Iron Spear', 'A iron spear, held in both hands', 25, 25, 25.0, 0))
    start_list.append(Weapons('Steel Spear', 'A steel spear, held in both hands', 35, 25, 25.0, 0))
def pstart_armor_list(start_list: list):
    start_list.append(Armor('Bronze Chestplate', 'A strudy bronze chestplate', 10, 65, 35.0, 0))
    start_list.append(Armor('Bronze Plate Gaurds', 'Thick bronze leg protection', 8, 60, 30.0, 0))
    start_list.append(Armor('Bronze Chainmail', 'Interconnected bronze rings form the chainmail', 7, 30, 15.0, 0))
    start_list.append(Armor('Bronze Chain Skirt', 'Dense bronze rings used for light leg protection', 6, 25, 10.0, 1))
    start_list.append(Armor('Iron Chestplate', 'A strudy iron chestplate', 15, 80, 35.0, 0))
    start_list.append(Armor('Iron Plate Gaurds', 'Thick iron leg protection', 12, 75, 30.0, 0))
    start_list.append(Armor('Iron Chainmail', 'Interconnected iron rings form the chainmail', 10, 50, 15.0, 0))
    start_list.append(Armor('Iron Chain Skirt', 'Dense iron rings used for light leg protection', 8, 45, 10.0, 0))
    start_list.append(Armor('Steel Chestplate', 'A strudy steel chestplate', 25, 100, 35.0, 0))
    start_list.append(Armor('Steel Plate Gaurds', 'Thick steel leg protection', 20, 85, 30.0, 0))
    start_list.append(Armor('Steel Chainmail', 'Interconnected steel rings form the chainmail', 15, 60, 15.0, 0))
    start_list.append(Armor('Steel Chain Skirt', 'Dense steel rings used for light leg protection', 12, 55, 10.0, 0))
def pstart_food_list(start_list: list):
    start_list.append(Food('Victoria Sponge', 'A tasty spponge cake filled with jam and cream, best served with a cuppa', 50, 200, 0.1, 0))
    start_list.append(Food('Toffee Pudding', 'Very sticky and sweet, usually served with custard or ice cream', 25, 125, 0.1, 0))
    start_list.append(Food('Green Apple', 'Fresh! might go well in a pie or crumble', 15, 75, 0.5, 3))
    start_list.append(Food('Smoked Salmon', 'Salmon which is super soft and has a rich smoked flavour, feels delicate in your mounth', 25, 500, 0.1,0))
    start_list.append(Food('Small Health Potion', 'A vial of viscus red fluid, you are not sure how this works but it tastes tingly', 25, 250, 0.35, 5))
    start_list.append(Food('Standard Health Potion', 'A vial of viscus red fluid, you are not sure how this works but it tastes tingly', 50, 250, 0.35, 0))
    start_list.append(Food('Large Health Potion', 'A vial of viscus red fluid, you are not sure how this works but it tastes tingly', 100, 250, 0.35, 0))
    start_list.append(Food('Grand Health Potion', 'A vial of viscus red fluid, you are not sure how this works but it tastes tingly', 250, 250, 0.35, 0))
def pstart_junk_list(start_list: list):
    start_list.append(Junk('Rusty Spoon', 'Past its glory days, thats for sure', 5, 0.1, 0))
    start_list.append(Junk('Faded Newspaper', 'You can make out "The Daily ... Post"', 5, 0.2, 0))
    start_list.append(Junk('Cracked Mirror', 'Said to bring bad luck', 5, 0.4, 0))
    start_list.append(Junk('Empty Vial', 'The liquid has vacated', 5, 0.3, 0))
    start_list.append(Junk('Pie Tin', 'Empty except for a few crumbs', 5, 0.5, 0))

def append_wealth_list(start_list: list):
    start_list.append(Wealth('Diamond', 'A precious gem stone said to be quite rare in these parts', 1500, 0.3, r(0,7)))
    start_list.append(Wealth('Emerald', 'The vales name sake, shines with a deep viridescent tone', 750, 0.3, r(0,7)))
    start_list.append(Wealth('Ruby', 'The deep crimson leaves you feeling wonderful', 500, 0.3, r(0,7)))
    start_list.append(Wealth('Shappire', 'As blue as the ocean and just as deep in colour', 200, 0.3, r(0,7)))
    start_list.append(Wealth('Platinum Bar', 'A rare gaia mineral, mined by experts and smithed by the wealthy', 5000, 1.0, r(0,7)))
    start_list.append(Wealth('Gold Bar', 'It never rusts!', 2500, 1.0, r(0,7)))
def append_weapon_list(start_list: list):
    start_list.append(Weapons('Bronze Dagger', 'A short bronze stabby weapon', 1, 5, 5.0, r(0,2)))
    start_list.append(Weapons('Iron Dagger', 'A short Iron stabby weapon', 5, 15, 5.0, r(0,2)))
    start_list.append(Weapons('Steel Dagger', 'A short Steel stabby weapon', 10, 25, 5.0, r(0,2)))
    start_list.append(Weapons('Bronze Short Sword', 'A bronze short sword, held in one hand', 10, 15, 10.0, r(0,2)))
    start_list.append(Weapons('Iron Short Sword', 'A iron short sword, held in one hand', 17, 35, 10.0, r(0,2)))
    start_list.append(Weapons('Steel Short Sword', 'A steel short sword, held in one hand', 22, 50, 10.0, r(0,2)))
    start_list.append(Weapons('Bronze Spear', 'A bronze spear, held in both hands', 17, 25, 25.0, r(0,2)))
    start_list.append(Weapons('Iron Spear', 'A iron spear, held in both hands', 25, 25, 25.0, r(0,2)))
    start_list.append(Weapons('Steel Spear', 'A steel spear, held in both hands', 35, 25, 25.0, r(0,2)))
def append_armor_list(start_list: list):
    start_list.append(Armor('Bronze Chestplate', 'A strudy bronze chestplate', 10, 65, 35.0, r(0,2)))
    start_list.append(Armor('Bronze Plate Gaurds', 'Thick bronze leg protection', 8, 60, 30.0, r(0,2)))
    start_list.append(Armor('Bronze Chainmail', 'Interconnected bronze rings form the chainmail', 7, 30, 15.0, r(0,2)))
    start_list.append(Armor('Bronze Chain Skirt', 'Dense bronze rings used for light leg protection', 6, 25, 10.0, r(0,2)))
    start_list.append(Armor('Iron Chestplate', 'A strudy iron chestplate', 15, 80, 35.0, r(0,2)))
    start_list.append(Armor('Iron Plate Gaurds', 'Thick iron leg protection', 12, 75, 30.0, r(0,2)))
    start_list.append(Armor('Iron Chainmail', 'Interconnected iron rings form the chainmail', 10, 50, 15.0, r(0,2)))
    start_list.append(Armor('Iron Chain Skirt', 'Dense iron rings used for light leg protection', 8, 45, 10.0, r(0,2)))
    start_list.append(Armor('Steel Chestplate', 'A strudy steel chestplate', 25, 100, 35.0, r(0,2)))
    start_list.append(Armor('Steel Plate Gaurds', 'Thick steel leg protection', 20, 85, 30.0, r(0,2)))
    start_list.append(Armor('Steel Chainmail', 'Interconnected steel rings form the chainmail', 15, 60, 15.0, r(0,2)))
    start_list.append(Armor('Steel Chain Skirt', 'Dense steel rings used for light leg protection', 12, 55, 10.0, r(0,2)))
def append_food_list(start_list: list):
    start_list.append(Food('Victoria Sponge', 'A tasty spponge cake filled with jam and cream, best served with a cuppa', 50, 200, 0.1, r(0,10)))
    start_list.append(Food('Toffee Pudding', 'Very sticky and sweet, usually served with custard or ice cream', 25, 125, 0.1, r(0,10)))
    start_list.append(Food('Green Apple', 'Fresh! might go well in a pie or crumble', 15, 75, 0.5, r(10,76)))
    start_list.append(Food('Smoked Salmon', 'Salmon which is super soft and has a rich smoked flavour, feels delicate in your mounth', 25, 500, 0.1,r(0,10)))
    start_list.append(Food('Small Health Potion', 'A vial of viscus red fluid, you are not sure how this works but it tastes tingly', 25, 250, 0.35, r(0,15)))
    start_list.append(Food('Standard Health Potion', 'A vial of viscus red fluid, you are not sure how this works but it tastes tingly', 50, 250, 0.35, r(0,12)))
    start_list.append(Food('Large Health Potion', 'A vial of viscus red fluid, you are not sure how this works but it tastes tingly', 100, 250, 0.35, r(0,7)))
    start_list.append(Food('Grand Health Potion', 'A vial of viscus red fluid, you are not sure how this works but it tastes tingly', 250, 250, 0.35, r(0,3)))
def append_junk_list(start_list: list):
    start_list.append(Junk('Rusty Spoon', 'Past its glory days, thats for sure', 5, 0.1, r(0,7)))
    start_list.append(Junk('Faded Newspaper', 'You can make out "The Daily ... Post"', 5, 0.2, r(0,7)))
    start_list.append(Junk('Cracked Mirror', 'Said to bring bad luck', 5, 0.4, r(0,7)))
    start_list.append(Junk('Empty Vial', 'The liquid has vacated', 5, 0.3, r(0,7)))
    start_list.append(Junk('Pie Tin', 'Empty except for a few crumbs', 5, 0.5, r(0,7)))
