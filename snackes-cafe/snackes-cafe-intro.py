Appetizers = ["Wings",'Cookies',"Spring Rolls"]
Entrees = ["Salmon","Steak","Meat Tornado","A Literal Garden"]
Desserts = ["Ice Cream","Cake","Pie"]
Drinks = ["Coffee","Tea","Unicorn Tears"]

def intro():
    print('''
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
''')

def user_insertion():
    user_input=input(">")  
    return user_input.capitalize()        

def main():
    user_input = user_insertion()
    while(user_input.lower() != "quit"):
        if user_input in Appetizers :
            print("** 1 order of", user_input ,"has been added to your meal **")
            #TODO: handle the order numbers
               
        elif user_input in Entrees:
            print("** 1 order of", user_input, "has been added to your meal **")
            # TODO: handle the order numbers

        elif user_input in Desserts:
            print("** 1 order of", user_input, "has been added to your meal **")
            # TODO: handle the order numbers

        elif user_input in Drinks:
            print("** 1 order of", user_input, "has been added to your meal **")
            # TODO: handle the order numbers

        else:
            print("Sorry, we don't have this item!")
                
        user_input = user_insertion()    

    end_application()


def end_application():
    print("Thanks for using Snakes Cafe application!")          

#invoke the function 
if __name__=="__main__": 
    intro()  
    main()
