#!/usr/bin/env python
# coding: utf-8

# In[48]:


'''
PROGRAM: CEASER'S CIPHER

PROBLEM STATEMENT
Write a python code for encryption or decryption of a given text
1. User would be able to enter the text.
2. For each letter in the user entered text the encrypted text should have the letter that is
   3 letters next to it and reverser for the decryption (the letter 3 letters ahead of the letter
   in the text).
3. Any space in user entered text should be replaced by "@" symbol in the encrypted text and "@"
   symbol replaced by space in the decrypted text.
4. Print the encrypted or decrypted text


STEPS FOLLOWED
1. Create two lists one of English alphabets having the letters a - z and one of numbers having
   the numbers 0-9.
2. Written a program that will accept a text as an argument.
3. Created an empty variable to store the result (the encrypted/decrypted text).
4. A for loop to iterate through each letter and find if it's in alphabets list or numbers list
   or a space.
5. Added (in case of encryption) or substracted (in case of edecryption) the index number by 3
   and added the letter in the empty variable which is in the new index.
6. returned the empty string which is now filled.
7. Created an input variable which will accept the text from the user to encrypt or decrypt.
8. Called the encryption / decryption function and passed on the input variable as an argument.
9. Printed the result.


'''


# In[49]:


#Creating two lists to refer to
alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

#Writing encryption program
def encryption_code(text):

  #An empty variable to add the encrypted letters
  converted_text = ""

  #A for loop to iterate through each letter in the given text
  for letter in text:

    #To check if the lettet is an alphabet, number or space

    #If letter in an alphabet
    if letter in alphabets:

      #Find the index of the letter
      index_of_letter = alphabets.index(letter)

      #Add 3 to index to create new index
      new_index = index_of_letter + 3

      #Check to see if new index is within the length of the list

      #If  not within then bring index to start from zero
      if new_index > len(alphabets) - 1:
        new_index -= len(alphabets)

        #Add the new letter to the empty variable
        converted_text += alphabets[new_index]
      else:
        converted_text += alphabets[new_index]

    #If letter in number list
    elif letter in numbers:

      #Find the index of the letter
      index_of_letter = numbers.index(letter)

      #Add 3 to index to create new index
      new_index = index_of_letter + 3

      #Check to see if new index is greater the length of th list

      #If  not within then bring index to start from zero
      if new_index > len(numbers) - 1:
        new_index -= len(numbers)

        #Add the new letter at the new index to the empty variable
        converted_text += numbers[new_index]
      else:
        converted_text += numbers[new_index]

    #If letter is a space then replace with "@"
    else:
      converted_text += '@'

  #Return the converted text
  return converted_text


#Accpet text from user to encrypt
to_encrypt = input("Enter: ").lower()

#Calling the encryption function and passing the text to it
encrypted = encryption_code(to_encrypt)


#Printing the result
print(encrypted)



# In[50]:


#Creating two lists to refer to
alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"


#Writing decryption program
def decryption_code(text):

  #An empty variable to add the decrypted letters
  converted_text = ""

  #A for loop to iterate through each letter in the given text
  for letter in text:

    #To check if the lettet is an alphabet, number or space

    #If letter in an alphabet
    if letter in alphabets:

      #Find the index of the letter
      index_of_letter = alphabets.index(letter.lower())

      #Substract 3 to index to create new index
      new_index = index_of_letter - 3

      #Check to see if new index is less than zero

      #If  not within then bring index to start from zero
      if new_index < 0:
        new_index += len(alphabets)

        #Add the new letter at the new index to the empty variable
        converted_text += alphabets[new_index]
      else:
        converted_text += alphabets[new_index]

    #If letter in number list
    elif letter in numbers:

      #Find the index of the letter
      index_of_letter = numbers.index(letter)

      #Substract 3 to index to create new index
      new_index = index_of_letter - 3

      #Check to see if new index is less than zero

      #If  not within then bring index to start from zero
      if new_index < 0:
        new_index += len(numbers)

        #Add the new letter at the new index to the empty variable
        converted_text += numbers[new_index]
      else:
        converted_text += numbers[new_index]

    #If letter is a "@" then replace with " "
    else:
      converted_text += " "

  #Return the converted text
  return converted_text


#Accpet text from user to decrypt
to_decrypt = input("Enter text to Decrypt: ")


#Calling the decryption function and passing the text to it
decrypted_text = decryption_code(to_decrypt)


#Printing the result
print(decrypted_text)


# In[ ]:




