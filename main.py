import inventory
import shop
import items
import container_interaction

def build_lists():
    items.pstart_wealth_list(inventory.inv_list_wealth)
    items.pstart_weapon_list(inventory.inv_list_weapon)
    items.pstart_armor_list(inventory.inv_list_armor)
    items.pstart_food_list(inventory.inv_list_food)
    items.pstart_junk_list(inventory.inv_list_junk)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    items.append_wealth_list(shop.shop_list_wealth)
    items.append_weapon_list(shop.shop_list_weapon)
    items.append_armor_list(shop.shop_list_armor)
    items.append_food_list(shop.shop_list_food)
    items.append_junk_list(shop.shop_list_junk)

def main():
    build_lists()
    container_interaction.start_trade()


main()

