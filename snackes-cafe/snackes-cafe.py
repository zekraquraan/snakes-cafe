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

def menuList():
    for i in menu:
        print(i)
        print("------")
        for x in menu[i]:
            print(x)
        print("")

def order():
    
    order=input("*********************************** \n **What would you like to order?** \n************************************ \n >")
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
                    print("\n**",count , "order of" ,item, "has been added to your meal **\n")
                    break
            else:
                continue
            break
        else:
            print("\n Sorry, we don't have that item on the menu. Please, select from the menu.\n")
        userInput = order()
    end()        
    
             

into() 
menuList()
output()

