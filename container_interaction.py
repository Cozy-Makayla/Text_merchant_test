from shop import (
    shop_menu_top,
    shop_buy,
    shop_sell,
    shop_list_all,
    shop_list_wealth,
    shop_list_weapon,
    shop_list_armor,
    shop_list_food,
    shop_list_junk,
    shop_gold,
)
from inventory import (
    inv_menu_top,
    inv_list_all,
    inv_list_wealth,
    inv_list_weapon,
    inv_list_armor,
    inv_list_food,
    inv_list_junk,
    inv_gold,
)

text_avoid_interaction = "I see, another time prehaps."
text_error_interaction = "Sorry I didn't catch that."
text_endquery_interaction = "Will that be all today?"
text_end_interaction = "Goodbye for now traveler."


def start_trade():
    global inv_gold
    global shop_gold
    while True:
        print("                                         SHOP INVENTORY")
        shop_list_all()
        print("                                         YOUR INVENTORY")
        inv_list_all()
        print(
            f"Would you like to sell or buy? {inv_gold:10}G : Your Wealth {shop_gold:10}G : Merchant"
        )
        print(f"{inv_gold:10}G : Your Wealth {shop_gold:10}G : Merchant")
        print("(S)ell / (B)uy / (E)xit")
        player_choice = input()
        match player_choice.capitalize():
            case "S" | "Sell":
                print("Choose a catogory:")
                print("(We)alth / (W)eapon / (A)rmor / (F)ood / (J)unk / (E)xit")
                user_select_list = input().capitalize()
                match user_select_list:
                    case "Wealth" | "We":
                        gold_list = shop_sell(inv_list_wealth, shop_list_wealth)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case "Weapons" | "W":
                        gold_list = shop_sell(inv_list_weapon, shop_list_weapon)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case "Armor" | "A":
                        gold_list = shop_sell(inv_list_armor, shop_list_armor)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case "Food" | "F":
                        gold_list = shop_sell(inv_list_food, shop_list_food)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case "Junk" | "J":
                        gold_list = shop_sell(inv_list_junk, shop_list_junk)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case _:
                        print(
                            f"""
                        Merchant:
                        {text_error_interaction}
                        """
                        )
                        input()
            case "B" | "Buy":
                print("Choose a catogory:")
                print("(We)alth / (W)eapon / (A)rmor / (F)ood / (J)unk / (E)xit")
                user_select_list = input().capitalize()
                match user_select_list:
                    case "Wealth" | "We":
                        gold_list = shop_buy(inv_list_wealth, shop_list_wealth)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case "Weapons" | "W":
                        gold_list = shop_buy(inv_list_weapon, shop_list_weapon)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case "Armor" | "A":
                        gold_list = shop_buy(inv_list_armor, shop_list_armor)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case "Food" | "F":
                        gold_list = shop_buy(inv_list_food, shop_list_food)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case "Junk" | "J":
                        gold_list = shop_buy(inv_list_junk, shop_list_junk)
                        inv_gold = gold_list[0]
                        shop_gold = gold_list[1]
                    case _:
                        print(
                            f"""
                            Merchant:
                            {text_error_interaction}
                            """
                        )
                        input()
            case "E" | "Exit":
                break
            case _:
                print(
                    f"""
                    Merchant:
                    {text_error_interaction}
                    """
                )
                input()


def enter_shop():
    shop_loop = True
    print(
        """
You enter the general store,
inside there are many trinkets,
a gruff looking merchant stares at you from across the room
"""
    )
    input()
    while shop_loop == True:
        print(
            """
        Merchant:
            "Would you like to trade stranger?
            (Y)es // (N)o
        """
        )
        player_choice = input()
        print(player_choice)
        match player_choice.capitalize():
            case "Y" | "Yes":
                start_trade()
                print(
                    f"""
                Merchant:
                {text_endquery_interaction}
                """
                )
                player_choice = input().capitalize()
                match player_choice:
                    case "Y" | "Yes":
                        shop_loop = False
                    case "N" | "No":
                        shop_loop = False
            case "N" | "No":
                print(
                    f"""
                Merchant:
                {text_avoid_interaction}
                """
                )
                break
            case _:
                print(
                    f"""
                Merchant:
                {text_error_interaction}
                """
                )
    print(
        f"""
    Merchant:
    {text_end_interaction}
    """
    )
