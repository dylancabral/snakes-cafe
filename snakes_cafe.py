from textwrap import dedent
def hello_world():
    print("Hello World!")

def menu_display():
    """
    menu function!
    """
    print(dedent("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************"""))
    your_order = input("> ")
    print(f"{your_order} was added to the bill!")

    ask_again = True
    while ask_again:
        choice = input("Are You Still Hungry?")
        if choice == "y:":
            print(dedent("""**************************************
                     **    Welcome to the Snakes Cafe!   **
                     **    Please see our menu below.    **
                     **
                     ** To quit at any time, type "quit" **
                     **************************************

                     Appetizers
                     ----------
                     Wings
                     Cookies
                     Spring Rolls

                     Entrees
                     -------
                     Salmon
                     Steak
                     Meat Tornado
                     A Literal Garden

                     Desserts
                     --------
                     Ice Cream
                     Cake
                     Pie

                     Drinks
                     ------
                     Coffee
                     Tea
                     Unicorn Tears

                     ***********************************
                     ** What would you like to order? **
                     ***********************************"""))
            your_order = input("> ")
            print(f"{your_order} was added to the bill!")
        else:
            break


if __name__ == "__main__":
    hello_world()
    menu_display()