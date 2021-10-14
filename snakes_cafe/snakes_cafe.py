# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

print(
"""
  
**************************************
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
***********************************

"""
)
menu={
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cookies": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
}
def customer_ordering():
    """
    command line utility which will mimic the functionality of a point of sale restaurant system using your basic Python tools and understanding of the basics of the language.
    """
    summary =0
    flag=True
    order = input("> ")
    while flag:
        if order == "quit":
            flag = False
            break
        else:
            for i in menu:
                if i.lower() == order.lower():
                    menu[i]+=1
                    formatted_string = f"** {menu[i]} order of {i} have been added to your meal ** . Great choice!"
                    print(formatted_string)
                    order = input("> ")

    for k in menu.keys():
            summary +=menu.get(k)

    print(summary)

customer_ordering()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    