#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Random Password Generator

'''
1. This program will generate a random password which is either a combination of alphabets or a combination
of alphabets and numbers or alphabets, numbers and special characters.
2. User should be able to choose how long they want their password but it has to be between 7 characters
and 15 characters in length.
3. User can choose if the password should be 'not so strong', 'mildly strong' or 'strong'.
4. User can generate as many random passwords they want without having to re-run the program.
5. For every invalid input user will get a error message and a chance to re-enter their choice.
'''


# In[ ]:


#Importing random module to use choice and shuffle function
import random

#Creating lists of Engligh alphabets, Numbers and Special characters
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','n','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
sp_char = ['~','!','@','#','$','%','^','&','*','(',')','_','+']


#Creating a function to choose the correct combination as user requires
def combination_of_list(wanted):
    charset_list = []

    if wanted == 1:               #If user requires not very strong password
        charset_list = alphabets
    elif wanted == 2:             #If user requires mildy strong password
        charset_list = alphabets + numbers
    else:                         #If user requires strong password
        charset_list = alphabets + numbers + sp_char

    random.shuffle(charset_list)  #Shuffle content of the list to increase randomness
    return charset_list           #Return the list



#Outer while loop if first input is given wrong by user
while True:


    print("Welcome to Pseudo-password generator!!!") #Welcome message
    #Asking user they want to generate random password

    want_to_generate = input("Do you want to generate a Pseudo-Password?(Y/N): ")

    #check if user entered a valid input
    if want_to_generate == "Y" or want_to_generate == "y":

        #Ask user if how many characters they want their pseudo username to be (First input)
        length_wanted = int(input("How long do you want your Pseudoname to be?(min 7 chars - max 12 chars): "))

        #Making sure if user has entered a number between 7 and 15
        if length_wanted < 7 or length_wanted > 15:

          #Error message
          print("Invalid Input!!!")
          print("Length has to be between 7 and 15")
          print("Try Again!!!")
          continue  #Will start another iteration of Outer while loop

        else:

          #Inner while loop
          while True:

            #Ask user to choose strength of the password (second input)
            print("Choose password strength")
            print("Not very strong (combination of alphabets only)")
            print("Mildly strong (combination of alphabets and numbers)")
            print("Strong (combination of alphabets, numbers, special charaters)")

            print("Press:")
            print("'1' for Not very strong")
            print("'2' for mildly strong")
            print("'3' for strong")

            strength_wanted = int(input("How strong should be your password?: "))

            #TO check if user entered a valid input

            #If input is correct
            if strength_wanted == 1 or strength_wanted == 2 or strength_wanted ==3:

              #Calling function combination of list and passing second
              #and assigning it to a variable charset_list
              charset_list = combination_of_list(strength_wanted)

              #Creating an empty variable which we will fill with random characters
              pseudo_password = ""

              #For loop to iterate as charaters user wants
              for i in range(length_wanted):

                #choose a random letter from combination of list of characters and add to empty variable
                char = random.choice(charset_list)
                pseudo_password += char

              #print the result and exit the program
              print("Your random password is", pseudo_password)
              break


            #If user enters an invalid second input
            #Error message
            else:
              print("Invalid Input!!!")
              print("Press Y/N")
              print("Try Again!!!")
              continue


    #If user doesnot wants to generate anymore password
    elif want_to_generate == "N" or want_to_generate == "n":
      break

    #If user enters an invalid second input
    #Error message
    else:
      print("Invalid Input!!!")
      print("Press Y/N")
      print("Try Again!!!")
      continue


# In[ ]:




