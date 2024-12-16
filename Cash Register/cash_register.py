#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Problem statement
1. Create a program for a cashier machine.
2. The program will log entries of total cash received by calculating total number of units of different denominations.
3. In the same way machine can return balance by calculating total number of units of different denominations.
4. Machine would be able to log all transaction in the day and print a report at the end of day.



Steps followed
1. Created a function that will have the following.
  i. A list with all available denominations of currency in it.
  ii. A for loop that will iterate through the denomination list and take input from
      user for each denomination how many notes or coins were accepted/given and
      return a total of money received/given.
2. Created two lists 'Credits and 'Debits' to log in the credit and debit amount accordingly
   and a variable 'Beginning balance' to check the balance at the beginning and closing of the day.
3. A while loop to keep the program running as long as the user wants.
4. If-else statement coupled with while loop to throw user an error when an invalid input
   is received.
'''


# In[2]:


def count_money():
  denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500]

  total_money = 0

  for denomination in denominations:
    number = input(f"Number of {denomination} rupee: ")
    if number != "":
      total_count = int(number) * denomination
      total_money += total_count

  return total_money

credits = []
debits = []

beginning_balance = int(input("Enter beginning balance: "))

cash_register_on = True

while cash_register_on:
  print("Press '1' to enter transaction")
  print("Press '2' to check balance")
  print("Press '3' to print statement")
  print("Press '4' to turn off machine")
  enter_or_check = int(input("Enter Transaction or Check Balance (1/2): "))
  if enter_or_check in range(1, 5):
    if enter_or_check == 1:
      print("Enter cash amount received:")
      cash_received = count_money()
      beginning_balance += cash_received
      credits.append(cash_received)

      print("Enter cash amount given:")
      cash_returned = count_money()
      beginning_balance -= cash_returned
      debits.append(cash_returned)

      print(f"Updated balance is: {beginning_balance}")
    elif enter_or_check == 2:
      print(f"Total balance is {beginning_balance}")
    elif enter_or_check == 3:
      print("Today's activities")
      for i in range(1, len(credits)+1):
        print(f"Tranaction number ", i)
        print(f"Credit {credits[i]}")
        print(f"Debit {debits[i]}")
        print(f"Closing balance is {sum(credits)-sum(debits)}")
    elif enter_or_check == 4:
      cash_register_on = False
    else:
      print("Invalid Input!!! Please try again!!!")
      continue





# In[ ]:


def count_money():
  denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500]

  total_money = 0

  for denomination in denominations:
    number = input(f"Number of {denomination} rupee: ")
    if number != "":
      total_count = int(number) * denomination
      total_money += total_count

  print(total_money)

count_money()


# In[ ]:




