## Printing Messages
#- In Python, we use the `print()` function to display information on the screen.
#- Anything inside quotation marks (" ") is treated as text (a string).
#- Python runs code from top to bottom, so each print statement will show its own output line.

#Example
print("What you want to print")
print("Hello World")


## Variables
#- Variables are containers used to store data values.
#- You can think of variables like labeled boxes that hold information.
#- The value inside a variable can change as your program runs.
#- Python does not require you to declare the type first; it figures it out automatically.


## 1. Strings
#- Strings represent text such as names, messages, or sentences.
#- Strings must be inside quotes (" " or ' ').
#- You can join (concatenate) strings using the + operator.

#Example
first_name = "bro"
last_name = "shariff"
full_name = first_name + " " + last_name  #- Adds a space between first and last name
print(full_name)


## 2. Integers (int)
#- Integers represent whole numbers (positive, negative, or zero).
#- You can perform math operations such as +, -, *, / on integers.
#- When mixing text and numbers in print(), convert numbers into strings using str().

#Example
age = 21
age += 1  #- Adds 1 to age (same as: age = age + 1)
print("My age is " + str(age))  #- str(age) converts the number into a string so it can be printed with text


## 3. Float
#- Floats represent decimal numbers (e.g., 3.14, 99.5).
#- Useful for measurements, prices, height, weight, etc.

#Example
height = 178.5
print("My height is " + str(height))


## 4. Boolean
#- Booleans represent True or False values.
#- Often used for conditions (checking if something is true or not).
#- They help in decision-making inside programs.

#Example
human = False
print(human)


## Multiple Assignment
#- Python allows assigning multiple values to multiple variables in a single line.
#- This makes the code cleaner and shorter.

#Example
name, age, attractive = "shariff", 21, True

#- You can also assign the same value to several variables at once:

#Example
spongebob = 30
patric = 30
garry = 30

#- Same as:
spongebob = patric = garry = 30

## Printing Messages
# Python uses the `print()` function to display text or values on the screen.
# Anything inside quotes (" ") is treated as a string.
# Each print statement shows a new line in the output.

```python
print("What you want to print")
print("Hello World")

