from math import *

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:32:38 2020

@author: maryann
"""
name = "Nelson"
age = "30"

print("there was once a man named " + name + ",")
print("he was " + age +"years old,")
print("he really liked the name " +  name)
print(name + " did not like being age years of age")
print("for now we will try to make " + name +" accept his " + age + "\n")

################ Working with STRINGS in python#########

#string go between quotaion marks

print("This is a string inside a quotation mark \n")

# using variables

sentence = "This is a string inside a quotation mark"
print(sentence)
############ WORKING WITH len() #####
phrase = "\n*****  working with len() ******"
print(phrase.upper())

# showing the length of the sentence or the characters of a sentence

print (len(sentence))

# getting a specific charaters
print(sentence[0])
# you can get the position of a specific character 
print(sentence.index("i"))
# using REPLACE functions when working with strings
print (sentence.replace("string", "phrase"))

############ WORKING WITH NUMBERS #####
phrase = "\n*****  working with numbers ******"
print(phrase.upper())
print("+ addition\n * -multiplication \n / - divide \n % -modulus")
topic1 = "changing numbers to strings using  STR(5)"
print(topic1)
print("example One")
num1 = 5
print(str(num1))
#---------------------------------------------------
print(abs(num1))#absolute
#---------------------------------------------------
print("\n workng with POW")# 3^2 power of a number
num2 = pow(3,2)
print("pow(3,2\n")
print(num2)
#------------------------------------------------------

print("\n workng with MAX \n example 3,2")# 3,2 to show greater number
print(max(3,2)) #the greatest number
print("\n workng with MIN \n example 3,2")# 3,2 to show lesser number
print(min(3,2)) # the leatst number
#------------------------------------------------------------------

print("\n workng with ROUND() \n example 3.2")# 3.2 to show lesser number
print(round(3.2))
#------------------------------------------------------------------
print("\n workng with FLOOR \n example 3.8")# 3.8 to show lesser number
print(floor(3.8))
#------------------------------------------------------------------
print("\n workng with CEIL \n example 3.8")# 3.8 to show highest number
print(ceil(3.8))
#------------------------------------------------------------------

print("\n workng with SQRT \n example 16")# 16 to show square root number
print(int(sqrt(16)))
#------------------------------------------------------------------
print ("\n getting user information from user")

name = str(input("Enter your name? "))
day = int(input("Enter the day of your birth? "))
month = int(input("Enter the month of birth? "))
year = int(input("Enter the year of your birth? "))


print("Hello " + name + "Your date of birth is" + name, day , month ,year)

#--------------------------------------------------------------------

