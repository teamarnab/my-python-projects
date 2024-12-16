#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Love Calculator

'''
PROBLEM STATEMENT
-----------------
Create a love calculator using Python coding that takes two names (his name and her name) as input 
and compare each letter present in both the names to see if the letter is present in the word "True Love".
If present the count would go up by 1 and if not the count remain unchanged.

Steps used
----------------
1. Creating a variable with the word 'truelove' to refer to and calculate.
2. Create two input options to take two names (his and her) and converting to lower case.
3. Create a function that will take two names as a input and then inside the function will be a for-loop
that will check how many letters in the names are in the word 'TrueLove' if there is a match the count variable
will have an increment of 1 if not then no changes to the count variable
4. Finally the function will return the count
5. print an output statement displaying the result
'''


# In[14]:


#creating a variable to refer to for calculating percentage
true_love = 'truelove'

#input for her name and assign to a variable after converting into lower case
her_name = input("Enter Her fullname: ").lower() 

#input for his name and assign to a variable after converting into lower case
his_name = input("Enter His fullname: ").lower()

#creating a function for caluculating percentage by seeing how many letters of the name is in true love
def count_love(name1, name2):   # function takes two names as input
    love_count = 0              # a count variable innitalized with 0
    for letter in name1:        # a for loop to check if each letter is present in the word 'true love'
        if letter in true_love:
            love_count += 1     # if letter is present count increases by one
    for letter in name2:        # a for loop to check if each letter is present in the word 'true love'
        if letter in true_love: 
            love_count += 1     # if letter is present count increases by one
    
    return love_count           # function returns count



#assigning the result of the function to a variable
count = str(count_love(her_name, his_name))



# output display statement showing result
print(her_name + "'s and " + his_name + "'s love count is: " + count + "/10")


# In[ ]:





# In[ ]:





# In[ ]:




