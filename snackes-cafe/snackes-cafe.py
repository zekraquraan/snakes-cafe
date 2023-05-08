
menu={
    "Appetizers":["Wings","Cookies","Spring Rolls"],
    "Entrees":["Salamon","Steak","Meat Tornado","A Literal Garden"],
    "Desserts":["Ice Cream","Cake","Pie"],
    "Drinks":["Coffee","Tea","Unicorn Tears"]
   }


# FUNCTION

def into():
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

def order():
    
    order=input("What would you like to order? \n >")
    return order

def end():
   print("Thanks for visiting !!")
    
def output():
    userInput = order()
    count = 0
    while userInput.lower() != "quit":
        for x in menu:
            for item in menu[x]:
                if userInput.lower() == item.lower():
                    count += 1
                    print(count , "order of" ,item, "has been added to your meal")
                    break
            else:
                continue
            break
        else:
            print("Sorry, we don't have that item on the menu. Please, select from the menu.")
        userInput = order()
    end()        
    
             

into() 
output()



    
    