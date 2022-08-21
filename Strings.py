#!/usr/bin/env python
# coding: utf-8

# # Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line

# In[5]:


Street = 'Street'
City = 'City'
Country = 'Country'
Address = Street + '\n' + City + '\n' + Country
print('Address using + sign: ',Address)
Adress = f'{Street}\n{City}\n{Country}'
print ('Adress using f-string: ',Adress)


# # 2.Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index

# In[9]:


a = 'Earth revolves around the sun'
print (a[6:13])
print (a[-3:])


# # 3.Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

# In[12]:


vegetables = 6
fruits = 8
print (f"I eat {vegetables} veggies and {fruits} fruits daily")


# # 4.I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

# In[15]:


s = 'maine 200 banana khaye'
s = s.replace('200','10')
s = s.replace('banana', 'samosa')
print ("Using two lines : ",s)
s = s.replace('banana', 'samosa').replace('200','10')
print ("Using single line : ",s)

