#!/usr/bin/env python
# coding: utf-8

# In[11]:


'''
Problem statement

1. Create a program for a coffee dispenser machine.
2. User can have 3 types of coffee. Latte, Cuppaccino and Espresso
3. There would be an inventory with required ingredients (coffee, water and milk)
4. Once user selects what type of coffee they want, machine would check if there is necessary amount of required ingredients.
5. If ingredients are not available then machine should print an error message and ask user to choose another type of coffee.
4. If ingredients are available the program should make the coffee by deducting the required amount of each ingredient from
the inventory and update amount left in the inventory.
5. Print cost of the coffee and a thank you message.
6. In case a user enteres invalid input they should be given an error message and asked to enter choice again.

Steps followed
1. Created a base class Coffee.
2. Created 3 coffee objects from coffee class i.e. latte, cuppaccino and espresso.
3. Created inventory object from coffee class.
4. Created a function that takes 2 arguments, inventory adn coffee wanted and checks if the amount of proper
ingredients available to make the required cofee
5. Created a function that will take required amount of required ingredients and update inventory (making the coffee)
6. A while loop so program will be running until user shuts it down.
7. Ask user if they want coffee, check inventory or shut down the machine.
8. Ask user what kind of coffee they want and the make the coffee, then check inventory, print coffee cost and make coffee.
9. Print inventory if the user wants to check inventory.
10. Break from the loop if user wants to continue or repeat from step 7


'''


# In[ ]:


#Creating a base class coffee to make other instances from it

class Coffee:
    def __init__(self, name, coffee, milk, water, cost):
        self.name = name
        self.coffee = coffee
        self.milk = milk
        self.water = water
        self.cost = cost

     #A function within coffee class to be called when user wants to check inventory
    def check_inventory(self):
        print("Coffee powder left: ", self.coffee, "gm")
        print("Milk powder left: ", self.milk, "l")
        print("Water left: ", self.water, "l")





#Making 3 instances of the class Coffee
latte = Coffee("Latte", 10, 10, 20, 80)
cuppaccino = Coffee("Latte", 15, 15, 10, 100)
espresso = Coffee("Latte", 20, 10, 10, 120)


#Creating inventory from Coffee class
inventory = Coffee("Inventory", 1000, 1000, 1000, 0)

#A function that will check if there is proper amount of proper ingredients available to make required cofee
def can_make_coffee(inventory, coffee_wanted):
  if inventory.coffee > coffee_wanted.coffee:
    if inventory.milk > coffee_wanted.milk:
      if inventory.water > coffee_wanted.water:
        return True
      else:
        return False
    else:
      return False
  else:
    return False


#A function that will take required amount of required ingredients and update inventory
def make_coffee(inventory, coffee_wanted):
  inventory.coffee = inventory.coffee - coffee_wanted.coffee
  inventory.milk = inventory.milk - coffee_wanted.milk
  inventory.water = inventory.water - coffee_wanted.water


while True:
  print("Welcome!")   #Welcome message

  #Asking user if they want to make coffee or check inventory
  print("Make coffee/Check inventory")
  print("Press '1' to make Coffee")
  print("Press '2' to check inventory")
  print("Press '3' to turn off machine")
  coffee_inventory_turnoff = int(input("What would you like to do?(1/2/3): "))

  #Checking if user entered a valid input

  #If valid input
  if coffee_inventory_turnoff == 1 or coffee_inventory_turnoff == 2 or coffee_inventory_turnoff == 3:

    #If user wants coffee
    if coffee_inventory_turnoff == 1:

      #Ask user what kind of coffee they want
      print("Press '1' for Latte")
      print("Press '2' for Cuppaccino")
      print("Press '3' for Espresso")
      coffee_wanted = int(input("Please select type of coffee: "))


      #Check if user enterd a valid coffee type
      if coffee_wanted == 1 or coffee_wanted == 2 or coffee_wanted == 3:
        if coffee_wanted == 1:
          coffee_wanted = latte
        elif coffee_wanted == 2:
          coffee_wanted = cuppaccino
        else:
          coffee_wanted = espresso


        #Check if there is necessery ingredients to make coffee
        can_make = can_make_coffee(inventory, coffee_wanted)
        if can_make == True:


          #Mention cost of the coffee and ask for payment
          print("Coffee cost is: ", coffee_wanted.cost)

          #Make the coffee
          make_coffee(inventory, coffee_wanted)
          print("Enjoy your coffee!!!")
          continue

        else:
          print("Sorry ingredients not available! please try something else.")
          continue

      #error message if user entered invalid coffee type
      else:
        print("Invalid Input!!! Please try again!!!")
        continue

    #If user wants to check inventory
    elif coffee_inventory_turnoff == 2:
      inventory.check_inventory()

    #If user wants to turn off machine
    else:
      break

  #If invalid input
  else:
    print("Invalid Input!!! Please try again!!!")
    continue


