#!/usr/bin/env python
# coding: utf-8

# # Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,area = (1/2)*base*height

# In[1]:


def calculate_area(d1,d2,shape):

    if shape == "triangle":
        area = 1/2*(d1*d2)
    return area   

base = 5
height = 10
triangle_area=calculate_area(base,height,"triangle")
print("Area of triangle is : ",triangle_area)


# # Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,rectangle area=length*width.If no shape is supplied then it should take triangle as a default shape

# In[3]:


def calculate_area(d1,d2,shape):

    if shape == "triangle":
        area = 1/2*(d1*d2)
    elif shape == "rectangle":
        area = d1*d2
    else:
        print("Error: Input shape is neither triangle nor rectangle")
        area = none
    return area   

base = 5
height = 10
triangle_area=calculate_area(base,height,"triangle")
print("Area of triangle is : ",triangle_area)          

width = 4
breadth = 5
rectangle_area = calculate_area(width,breadth,"rectangle")
print("Area of rectangle is : ",rectangle_area)

triangle_area = calculate_area(base,height)
print("Area of triangle with no shape supplied : ",triangle_area)


# # Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
# 
# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number.

# In[8]:


def print_pattern(n=5): 

    for i in range (n):
        s = ''
        for j in range (i+1):
            s = s + '*'
        print (s)

print ("Print pattern with input = 3")
print_pattern(n=3)
print ("Print pattern with input = 4")
print_pattern(n=4)   
print ("Print pattern with no input") 
print_pattern()


# In[ ]:




