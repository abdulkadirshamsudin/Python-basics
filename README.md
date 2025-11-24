## Printing Messages
#- In Python, we use the `print()` function to display information on the screen.
#- Anything inside quotation marks (" ") is treated as a string (text).
#- Python runs code from top to bottom, so each print statement appears on a new line.

#Example
print("What you want to print")
print("Hello World")


## Variables
#- Variables are containers used to store data values.
#- Think of variables like labeled boxes that hold information.
#- The value inside a variable can change during the program.
#- Python auto-detects the variable type (no need to declare types manually).


## 1. Strings
#- Strings represent text such as names, messages, or sentences.
#- Strings must be inside quotes (" " or ' ').
#- Strings can be joined together using the + operator.

#Example
first_name = "bro"
last_name = "shariff"
full_name = first_name + " " + last_name   # Adds a space between first and last name
print(full_name)


## 2. Integers (int)
#- Integers represent whole numbers (positive, negative, or zero).
#- Useful for counting, math, and calculations.
#- When printing numbers with text, convert the number to a string using str().

#Example
age = 21
age += 1   # Adds 1 to age (same as: age = age + 1)
print("My age is " + str(age))   # str(age) converts the number to a string


## 3. Float
#- Floats represent decimal numbers, e.g., 3.14, 45.9, 178.5.
#- Useful for measurements, height, weight, prices, etc.

#Example
height = 178.5
print("My height is " + str(height))


## 4. Boolean
#- Booleans represent True or False values.
#- Commonly used in conditions to control program behavior.

#Example
human = False
print(human)


## Multiple Assignment
#- You can assign multiple variables in a single line.
#- This helps write cleaner and shorter code.

#Example
name, age, attractive = "shariff", 21, True

#- You can also assign the same value to several variables at once.

#Example
spongebob = 30
patric = 30
garry = 30

#- Same as:
spongebob = patric = garry = 30
