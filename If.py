#!/usr/bin/env python
# coding: utf-8

# # 1.Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# i.Write a program that asks user to enter a city name and it should tell which country the city belongs to
# ii.Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

# In[24]:


#i
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city = input("Enter a city name : ")
if city in india:
    print("City belongs to India")
elif city in pakistan:
        print("City belongs to pakistan")
elif city in bangladesh:
            print("City belongs to bangladesh")
else:
                print("City doesn't belong to any above countries")


# In[27]:


#ii
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city1 = input("Enter city1 : ")
city2 = input("Enter city2 : ")
if city1 in india and city2 in india:
    print("Cities belongs to India")
elif city1 in pakistan and city2 in pakistan:
    print("Cities belongs to pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Cities belongs to bangladesh")
else:
    print("They don't belong to same country")


# # 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

# In[16]:


i = (input("Fasting Sugar level : "))
i=int(i)
if i in range(80,100):
    print ("Sugar is low")
elif i > 100:
    print ("Sugar is high")
else:
    print ("Sugar is normal") 

