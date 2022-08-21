#!/usr/bin/env python
# coding: utf-8

# # 1.You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

# In[3]:


Length = 92
Width = 48.8
Area = Length*Width
print('Area of the Football field is: ', Area)


# # 2.You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

# In[4]:


Packets = 9
Price = 1.49
Cost = Packets*Price
Given = 20
Return_Amount = Given - Cost
Return_Amount


# # 3.You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

# In[8]:


Length = 5.5
Area = Length**2
Total_cost = 500 * Area
print( 'Cost for replcing tiles is : ',Total_cost)


# # 4.Print binary representation of number 17

# In[9]:


num=17
print('Binary of number 17 is:',format(num,'b'))

