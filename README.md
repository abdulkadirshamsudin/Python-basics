## Printing Messages
# How to print output in Python
#- Use the print() function to display text or values on the screen.

#Example
print("What you want to print")
print("Hello World")

## Variables
# What are variables?
#- Variables are containers that hold values such as integers, strings, floats, and booleans.

## 1. Strings
#- Strings represent text values.

#Example
first_name = "bro"
last_name = "shariff"
full_name = first_name + " " + last_name
print(full_name)

## 2. Integers (int)
#- Integers represent whole numbers.

#Example
age = 21
age += 1   # incrementing age
print("My age is " + str(age))
#- Converting age to a string above is called type casting (str(age)).

## 3. Floats
#- Floats represent decimal numbers.

#Example
height = 178.5
print("My height is " + str(height))

## 4. Boolean
#- Booleans represent True or False values.

#Example
human = False
print(human)

## Multiple Assignment
#- Assign multiple variables in a single line.

#Example
name, age, attractive = "shariff", 21, True

#Example
spongebob = 30
patrick = 30
garry = 30
#- Same as:
spongebob = patrick = garry = 30
