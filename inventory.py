inv_list_wealth = []
inv_list_weapon = []
inv_list_armor = []
inv_list_food = []
inv_list_junk = []
inv_all = [
    inv_list_wealth,
    inv_list_weapon,
    inv_list_armor,
    inv_list_food,
    inv_list_junk,
]

inv_gold = 3000


def inv_menu_top():
    inv_loop = True
    while inv_loop == True:
        print("(A)ll / (We)alth / (W)eapon / (A)rmor / (F)ood / (J)unk / (E)xit")
        print("Please select one: ")
        user_select = input()
        match user_select.capitalize():
            case "All" | "A":
                inv_menu_mid("All")
            case "Wealth" | "We":
                inv_menu_mid("Wealth")
            case "Weapon" | "W":
                inv_menu_mid("Weapon")
            case "Armor" | "A":
                inv_menu_mid("Armor")
            case "Food" | "F":
                inv_menu_mid("Food")
            case "Junk" | "J":
                inv_menu_mid("Junk")
            case "Exit" | "E":
                return
            case _:
                print(f"{user_select.capitalize()} Not found, Try again")
                input("")


def inv_menu_mid(list_selection: str):
    inv_loop = True
    print(f"{list_selection} - (D)escription / (L)ist / (E)xit")
    user_select = input()
    match list_selection.capitalize():
        case "All" | "A":
            match user_select.capitalize():
                case "Description" | "D":
                    inv_desc_all()
                case "List" | "L":
                    inv_list_all()
                case "Exit" | "E":
                    return
        case "Wealth" | "W":
            match user_select.capitalize():
                case "Description" | "D":
                    inv_desc(inv_list_wealth, list_selection)
                case "List" | "L":
                    inv_list(inv_list_wealth, False, list_selection)
                case "Exit" | "E":
                    return
        case "Weapon" | "We":
            match user_select.capitalize():
                case "Description" | "D":
                    inv_desc(inv_list_weapon, list_selection)
                case "List" | "L":
                    inv_list(inv_list_weapon, False, list_selection)
                case "Exit" | "E":
                    return
        case "Armor" | "A":
            match user_select.capitalize():
                case "Description" | "D":
                    inv_desc(inv_list_armor, list_selection)
                case "List" | "L":
                    inv_list(inv_list_armor, False, list_selection)
                case "Exit" | "E":
                    return
        case "Food" | "F":
            match user_select.capitalize():
                case "Description" | "D":
                    inv_desc(inv_list_food, list_selection)
                case "List" | "L":
                    inv_list(inv_list_food, False, list_selection)
                case "Exit" | "E":
                    return
        case "Junk" | "J":
            match user_select.capitalize():
                case "Description" | "D":
                    inv_desc(inv_list_junk, list_selection)
                case "List" | "L":
                    inv_list(inv_list_junk, False, list_selection)
                case "Exit" | "E":
                    return


def inv_list(list: list, is_all: bool, list_selection: str):
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


def inv_list_all():
    print(
        "############################################ WEALTH ################################################"
    )
    inv_list(inv_list_wealth, True, "Wealth")
    print(
        "############################################ WEAPONS ###############################################"
    )
    inv_list(inv_list_weapon, True, "Weapons")
    print(
        "############################################ ARMOR #################################################"
    )
    inv_list(inv_list_armor, True, "Armor")
    print(
        "############################################# FOOD #################################################"
    )
    inv_list(inv_list_food, True, "Food")
    print(
        "############################################# JUNK #################################################"
    )
    inv_list(inv_list_junk, True, "Junk")
    print(
        "####################################################################################################"
    )
    return


def inv_desc(list: list, list_selection: str):
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


def inv_desc_all():
    counter = 1
    for list in inv_all:
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
