#!/usr/bin/env python
# coding: utf-8

# # 1.After flipping a coin 10 times you got this result, result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"] Using for loop figure out how many times you got heads

# In[23]:


result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for i in result:
    if i == "heads":
        count += 1
    
print("Count of heads is : ",count)


# # 2.Print square of all numbers between 1 to 10 except even numbers

# In[24]:


for i in range (1,11):
    if i % 2 == 1:
        print ("Square of Odd numbers : ",(i*i))


# # 3.Your monthly expense list (from Jan to May) looks like this,expense_list = [2340, 2500, 2100, 3100, 2980] Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

# In[34]:


month_list = ["Jan","Feb","March","April","May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
expense = input("Enter an expense amount : ")
expense = int(expense)
month = -1
for i in range(len(expense_list)): 
    if expense == expense_list[i]:
        month = i
        break
        
        
if month != -1:
            print(f'You spent {expense} in {month_list[month]}')
else:
            print(f'You didn\'t spend {expense} in any month')


# # 4.Lets say you are running a 5 km race. Write a program that,Upon completing each 1 km asks you "are you tired?" If you reply "yes" then it should break and print "you didn't finish the race" If you reply "no" then it should continue and ask "are you tired" on every km If you finish all 5 km then it should print congratulations message

# In[36]:


for i in range (5):
    print(f"You ran {i+1} km")
    tired = input("Are you tired?")
    if tired == 'yes':
        break
        
if i == 4:
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print(f"You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")    
    


# # 5.Write a program that prints following shape
# *
# **
# ***
# ****
# *****

# In[40]:


for i in range (1,6):
    s = ''
for j in range(i):
        s = s+'*'
        print(s)

