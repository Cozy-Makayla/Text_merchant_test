from random import randint as r
from inventory import inv_gold

shop_list_wealth = []
shop_list_weapon = []
shop_list_armor = []
shop_list_food = []
shop_list_junk = []
shop_all = [
    shop_list_wealth,
    shop_list_weapon,
    shop_list_armor,
    shop_list_food,
    shop_list_junk,
]
# shop_gold = r(499, 500000)
shop_gold = 3000


def shop_menu_top():
    inv_loop = True
    while inv_loop == True:
        print("(A)ll / (We)alth / (W)eapon / (A)rmor / (F)ood / (J)unk / (E)xit")
        print("Please select one: ")
        user_select = input()
        match user_select.capitalize():
            case "All" | "A":
                shop_menu_mid("All")
            case "Wealth" | "We":
                shop_menu_mid("Wealth")
            case "Weapon" | "W":
                shop_menu_mid("Weapon")
            case "Armor" | "A":
                shop_menu_mid("Armor")
            case "Food" | "F":
                shop_menu_mid("Food")
            case "Junk" | "J":
                shop_menu_mid("Junk")
            case "Exit" | "E":
                return
            case _:
                print(f"{user_select.capitalize()} Not found, Try again")
                input("")


def shop_menu_mid(list_selection: str):
    inv_loop = True
    print(f"{list_selection} - (D)escription / (L)ist / (E)xit")
    user_select = input()
    match list_selection.capitalize():
        case "All" | "A":
            match user_select.capitalize():
                case "Description" | "D":
                    shop_desc_all()
                case "List" | "L":
                    shop_list_all()
                case "Exit" | "E":
                    return
        case "Wealth" | "W":
            match user_select.capitalize():
                case "Description" | "D":
                    shop_desc(shop_list_wealth, list_selection)
                case "List" | "L":
                    shop_list(shop_list_wealth, False, list_selection)
                case "Exit" | "E":
                    return
        case "Weapon" | "We":
            match user_select.capitalize():
                case "Description" | "D":
                    shop_desc(shop_list_weapon, list_selection)
                case "List" | "L":
                    shop_list(shop_list_weapon, False, list_selection)
                case "Exit" | "E":
                    return
        case "Armor" | "A":
            match user_select.capitalize():
                case "Description" | "D":
                    shop_desc(shop_list_armor, list_selection)
                case "List" | "L":
                    shop_list(shop_list_armor, False, list_selection)
                case "Exit" | "E":
                    return
        case "Food" | "F":
            match user_select.capitalize():
                case "Description" | "D":
                    shop_desc(shop_list_food, list_selection)
                case "List" | "L":
                    shop_list(shop_list_food, False, list_selection)
                case "Exit" | "E":
                    return
        case "Junk" | "J":
            match user_select.capitalize():
                case "Description" | "D":
                    shop_desc(shop_list_junk, list_selection)
                case "List" | "L":
                    shop_list(shop_list_junk, False, list_selection)
                case "Exit" | "E":
                    return


def shop_list(list: list, is_all: bool, list_selection: str):
    first_print = False
    if is_all == True:
        for obj in list:
            if obj.amount > 0:
                print(
                    f"|{obj.amount:4}|{obj.name:36}|{obj.weight:6}KG|{obj.value:6}G|{round(obj.weight * obj.amount, 2):8}KG / Stack|{obj.amount * (obj.value):11}G / Stack|"
                )
    else:
        has_item = False
        for obj in list:
            if obj.amount > 0:
                if first_print == False:
                    print(
                        f"############################################ {list_selection:7} ###############################################"
                    )
                    first_print = True
                has_item = True
                print(
                    f"|{obj.amount:4}|{obj.name:36}|{obj.weight:6}KG|{obj.value:6}G|{round(obj.weight * obj.amount, 2):8}KG / Stack|{obj.amount * (obj.value):11}G / Stack|"
                )
        if has_item == False:
            print(f"There are no items in you {list_selection} Inventory")
        print(
            "####################################################################################################"
        )


def shop_list_all():
    print(
        "############################################ WEALTH ################################################"
    )
    shop_list(shop_list_wealth, True, "Wealth")
    print(
        "############################################ WEAPONS ###############################################"
    )
    shop_list(shop_list_weapon, True, "Weapons")
    print(
        "############################################ ARMOR #################################################"
    )
    shop_list(shop_list_armor, True, "Armor")
    print(
        "############################################# FOOD #################################################"
    )
    shop_list(shop_list_food, True, "Food")
    print(
        "############################################# JUNK #################################################"
    )
    shop_list(shop_list_junk, True, "Junk")
    print(
        "####################################################################################################"
    )
    return


def shop_desc(list: list, list_selection: str):
    inv_loop = True
    print("Please select one of the following: ")
    for obj in list:
        print(f"- {obj.name}")
    print()
    user_choice = input().title()
    user_choice_check = False
    answer_null = True
    for obj in list:
        if user_choice == obj.name:
            print()
            print(f"{obj.name} : {obj.desc}.")
            print()
            user_choice_check = True
    else:
        print()
        print(f"You don't have any '{user_choice}'")
        print()


def shop_desc_all():
    counter = 1
    for list in shop_all:
        match counter:
            case 1:
                print(
                    "############################################ WEALTH ################################################"
                )
            case 2:
                print(
                    "############################################ WEAPONS ###############################################"
                )
            case 3:
                print(
                    "############################################ ARMOR #################################################"
                )
            case 4:
                print(
                    "############################################# FOOD #################################################"
                )
            case 5:
                print(
                    "############################################# JUNK #################################################"
                )
        counter = counter + 1
        for obj in list:
            if obj.amount > 0:
                print(f"{obj.name:36}{obj.desc}")
        print(
            "####################################################################################################"
        )


def shop_buy(inv_list_selected: list, shop_list_selected: list):
    global shop_gold
    global inv_gold
    int_check = False
    item_check = False
    sale_check = False
    print("Select Item")
    print('info: do not put "S" at the end of your input for mulitples')
    user_select_item = input().title()
    while int_check == False:
        print("How many?")
        user_select_amount = input()
        if user_select_amount.isnumeric():
            user_select_amount = int(user_select_amount)
            int_check = True
        else:
            print(
                f"""
            Merchant:
            {user_select_amount} ins't a numerical amount, are you feeling okay?
            """
            )
    for obj in shop_list_selected:
        if user_select_item == obj.name:
            item_check = True
            if obj.amount >= user_select_amount:
                if obj.value * user_select_amount <= inv_gold:
                    print(
                        f"You're buying {user_select_amount} {obj.name} for a total of -{user_select_amount * obj.value}G"
                    )
                    obj.amount = obj.amount - user_select_amount
                    inv_gold = inv_gold - (user_select_amount * obj.value)
                    shop_gold = shop_gold + (user_select_amount * obj.value)
                    sale_check = True
                else:
                    print(
                        f"""
                    Merchant:
                    I'm sorry you don't have enough gold for this transaction
                    (you're {(obj.value * user_select_amount) - inv_gold}G short.)
                    """
                    )
            else:
                print(
                    f"""
                    Merchant:
                    I don't have enough {user_select_item} to sell
                    My current stock is {obj.amount} {obj.name}
                    """
                )
    if sale_check == True:
        for obj in inv_list_selected:
            if user_select_item == obj.name:
                obj.amount = obj.amount + user_select_amount
    if item_check == False:
        print(
            f"""
        Merchant:
        I don't have any {user_select_item} to sell.
        """
        )
    input()
    return [inv_gold, shop_gold]


def shop_sell(inv_list_selected: list, shop_list_selected: list):
    global shop_gold
    global inv_gold
    int_check = False
    item_check = False
    sale_check = False
    print("Select Item")
    print('info: do not put "S" at the end of your input for mulitples')
    user_select_item = input().title()
    while int_check == False:
        print("How many?")
        user_select_amount = input()
        if user_select_amount.isnumeric():
            user_select_amount = int(user_select_amount)
            int_check = True
        else:
            print(
                f"""
            Merchant:
            {user_select_amount} ins't a numerical amount, are you feeling okay?
            """
            )
    for obj in inv_list_selected:
        if user_select_item == obj.name:
            item_check = True
            if obj.amount >= user_select_amount:
                if obj.value * user_select_amount <= shop_gold:
                    print(
                        f"You're selling {user_select_amount} {obj.name} for a total of +{user_select_amount * obj.value}G"
                    )
                    obj.amount = obj.amount - user_select_amount
                    inv_gold = inv_gold + (user_select_amount * obj.value)
                    shop_gold = shop_gold - (user_select_amount * obj.value)
                    sale_check = True
                else:
                    print(
                        f"""
                    Merchant:
                    I'm sorry I don't have enough gold for this transaction
                    (they're {(obj.value * user_select_amount) - shop_gold}G short.)
                    """
                    )
            else:
                print(
                    f"""
                    Merchant:
                    you don't have enough {user_select_item} to sell.
                    your current stock is {obj.amount} {obj.name}
                    """
                )
                print(f"you do not have enough {user_select_item} to sell")
    if sale_check == True:
        for obj in shop_list_selected:
            if user_select_item == obj.name:
                obj.amount = obj.amount + user_select_amount
    if item_check == False:
        (
            f"""
        Merchant:
        I don't have any {user_select_item} to sell.
        """
        )
    input()
    return [inv_gold, shop_gold]
