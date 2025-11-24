## Printing Messages
#- In Python, we use the `print()` function to display information on the screen.
#- Anything inside quotation marks (" ") is treated as a string (text).
#- Python runs code from top to bottom, so each print statement appears on a new line.

#Example
```python
print("What you want to print")
print("Hello World")
Variables
#- Variables are containers that store data values.
#- Think of them like labeled boxes that hold information.
#- The value inside a variable can change during program execution.
#- Python automatically detects the type of data stored (you do NOT declare types manually).

1. Strings
#- Strings represent text like names or words.
#- They must be enclosed in quotes (" " or ' ').
#- Strings can be joined together (concatenated) using the + operator.

#Example

python
Copy code
first_name = "bro"
last_name = "shariff"
full_name = first_name + " " + last_name   # Adds a space between names
print(full_name)
2. Integers (int)
#- Integers represent whole numbers (positive, negative, or zero).
#- You can perform arithmetic operations: +, -, *, /, etc.
#- When mixing numbers and text in print(), convert numbers to strings using str().

#Example

python
Copy code
age = 21
age += 1   # Adds 1 to age (same as: age = age + 1)
print("My age is " + str(age))   # str(age) converts the number to a string
3. Float
#- Floats represent decimal numbers such as 3.14 or 178.5.
#- Useful for measurements, prices, or any value needing decimals.

#Example

python
Copy code
height = 178.5
print("My height is " + str(height))
4. Boolean
#- Booleans represent True or False.
#- Used in conditions (if statements) to control program decisions.

#Example

python
Copy code
human = False
print(human)
Multiple Assignment
#- Python allows assigning multiple variables in one line.
#- This makes code shorter and cleaner.

#Example

python
Copy code
name, age, attractive = "shariff", 21, True
#- You can assign the same value to several variables at once:

#Example

python
Copy code
spongebob = 30
patric = 30
garry = 30
#- Same as:

python
Copy code
spongebob = patric = garry = 30