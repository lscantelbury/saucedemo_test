from selenium.webdriver.common.by import By

class HomePageLocators:
    menu =  '//*[@id="menu_button_container"]/div/div[2]'
    menu_button =  '//*[@id="react-burger-menu-btn"]'
    amount_of_items_at_cart =  '//*[@id="shopping_cart_container"]/a/span'
    first_inventory_item =  '//*[@id="inventory_container"]/div/div[1]/div[2]/div[1]/a/div'
    inventory_items =  '//*[@id="inventory_container"]'
    sort_button =  'product_sort_container'
    selected_option = lambda option : f'''//*[@id="header_container"]/div[2]/div/span/select/option[{option}]'''
    add_to_cart_button =  '//*[@id="add-to-cart-sauce-labs-backpack"]'
    products_label =  '//*[@id="header_container"]/div[2]/span'
