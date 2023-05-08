menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}


def intro():
    print(
        '''
        **************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        **
        ** To quit at any time, type "quit" **
        **************************************
        '''
    )
    print_menu()


def print_menu():
    print("\nMenu")
    print("----------")
    for category, items in menu.items():
        print(category)
        for item in items:
            print(item)


def take_order():
    order_count = {}

    while True:
        order = input("What would you like to order? \n> ")

        if order.lower() == "quit":
            break

        found_item = False

        for category, items in menu.items():
            for item in items:
                if order.lower() == item.lower():
                    found_item = True
                    order_count[item] = order_count.get(item, 0) + 1
                    count = order_count[item]
                    print(f"{count} order{'s' if count > 1 else ''} of {item} has been added to your meal.")
                    break

            if found_item:
                break

        if not found_item:
            print("Sorry, we don't have that item on the menu. Please, select from the menu.")

    print("Thanks for visiting!!")


def run_snakes_cafe():
    intro()
    take_order()


if __name__ == "__main__":
    run_snakes_cafe()
