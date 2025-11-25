# Python Basics — Full Beginner Reference

This README provides a complete overview of fundamental Python concepts.  
All examples are clean, simple, and practical for revision.

---

## 1. Printing Output
Python displays text using the `print()` function.

```python
print("What you want to print")
print("Hello World")
```

---

## 2. Variables
Variables store values. Python uses dynamic typing, so you don’t declare types manually.

Common variable types:

- **String** → text  
- **Integer (int)** → whole numbers  
- **Float** → decimal numbers  
- **Boolean (bool)** → True/False  

```python
name = "Shariff"
age = 21
height = 178.5
human = True
```

---

## 3. Strings
Strings hold text. You can combine them (concatenate).

```python
first_name = "bro"
last_name = "shariff"
full_name = first_name + " " + last_name
print(full_name)
```

---

## 4. Integers (int)
Integers represent whole numbers and support arithmetic.

```python
age = 21
age += 1   # increment age by 1
print("My age is " + str(age))
```

### Type Casting
Convert numbers to strings when concatenating:

```python
str(age)
```

---

## 5. Floats
Floats represent decimal values.

```python
height = 178.5
print("My height is " + str(height))
```

---

## 6. Booleans
Booleans represent truth values: `True` or `False`.

```python
human = False
print(human)
```

---

## 7. Multiple Assignment
Assign multiple variables at once.

### Example 1 — Different values
```python
name, age, attractive = "shariff", 21, True
```

### Example 2 — Same value
```python
spongebob = patrick = gary = 30
```

---

## 8. Summary Table of Concepts

| Concept             | Description               | Example                     |
|--------------------|---------------------------|-----------------------------|
| Print statements    | Display text              | `print("Hello")`            |
| Strings             | Text values               | `"Shariff"`                 |
| Integers            | Whole numbers             | `21`                        |
| Floats              | Decimal values            | `178.5`                     |
| Booleans            | True/False values         | `True`                      |
| Type Casting        | Convert types             | `str(21)`                   |
| Multiple Assignment | Set many values at once   | `a, b = 1, 2`               |

---

*
## Python String Methods — Quick Reference

This table summarizes commonly used string methods with examples and explanations.

| Method / Operator       | Example Code                     | Explanation |
|-------------------------|---------------------------------|-------------|
| `find()`                | `name.find("o")`                | Returns the **index of the first occurrence** of the specified character. If not found, returns -1. |
| `capitalize()`          | `name.capitalize()`             | Capitalizes the **first letter** of the string. |
| `upper()`               | `name.upper()`                  | Converts all characters in the string to **uppercase**. |
| `lower()`               | `name.lower()`                  | Converts all characters in the string to **lowercase**. |
| `isalpha()`             | `name.isalpha()`                | Returns `True` if **all characters** in the string are letters. Otherwise `False`. |
| `replace()`             | `name.replace("o", "a")`        | Replaces **specified substring** with another substring. |
| `*` (repetition)        | `name * 3`                      | Repeats the string **3 times**. |

### Notes
- `name` should be a string variable, e.g., `name = "Shariff"`.  
- Always remember string methods **do not modify the original string** unless assigned to a variable. For example:  
```python
new_name = name.upper()  # stores the uppercase version
```
## Python Type Casting (Conversion)

Type casting (or type conversion) is the process of **converting a value from one data type to another**.

| Conversion Function | Example Code                  | Explanation |
|--------------------|-------------------------------|-------------|
| `int()`            | `int("21")`                   | Converts a string or float to an integer. Decimals are truncated. |
| `float()`          | `float("21.5")`               | Converts a string or integer to a floating-point number. |
| `str()`            | `str(21)`                      | Converts an integer, float, or boolean to a string. |
| `bool()`           | `bool(0)` / `bool(1)`         | Converts a value to a boolean. Zero or empty values → `False`; all others → `True`. |
| `complex()`        | `complex(2,3)`                 | Converts numbers to a complex number (real + imaginary). |

### Notes
- Type casting is **explicit**, meaning you must call the conversion function.  
- Python also performs **implicit type conversion** in some cases, e.g., combining int and float in arithmetic.  
- Example of explicit casting:
```python
age_str = "21"
age_int = int(age_str)  # Converts string "21" to integer 21
print(age_int + 5)      # Output: 26
```

- Example of combining int and float:
```python
x = 5       # int
y = 2.5     # float
z = x + y   # Python implicitly converts x to float
print(z)    # Output: 7.5
```



## Python Conditional Statements

Conditional statements allow your program to **make decisions** based on conditions.  
Python provides `if`, `elif`, and `else` statements, along with logical operators and nested conditions.

---

### 1. Basic `if` Statement

- Executes a block of code **only if the condition is True**.
- Use `else` to handle the case when the condition is False.

```python
age = int(input("What is your age? "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor.")
```

**Explanation:**  
- `if age >= 18:` checks if the user is 18 or older.  
- If True → prints “You are an adult”.  
- If False → the `else` block runs, printing “You are a minor.”

---

### 2. `elif` (Else-If) Statement

- Use `elif` to check **multiple conditions** in sequence.

```python
age = int(input("What is your age? "))

if age >= 18:
    print("You are an adult")
elif age < 0:
    print("You are still in your father's nut sack!")  # humorous invalid input
else:
    print("You are a minor.")
```

**Explanation:**  
- The first `if` checks if age ≥ 18.  
- `elif` checks another condition (age < 0) — useful for invalid input.  
- `else` handles all remaining cases.

---

### 3. Logical Operators (`and`, `or`, `not`)

- Combine multiple conditions in a single `if` statement.

```python
temp = int(input("What is the temperature today? "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today")
    print("Go outside")
elif temp < 0 or temp > 30:
    print("The temperature is bad today")
    print("Stay inside")
else:
    print("Unable to detect temperature")
```

**Explanation:**  
- `and` → both conditions must be True.  
- `or` → at least one condition must be True.  
- `not` → reverses the Boolean value.  
- Helps handle multiple scenarios in one check.

---

### 4. Nested `if` Statements

- An `if` statement inside another `if` statement.
- Useful for **hierarchical or dependent conditions**.

```python
age = int(input("Enter your age: "))

if age >= 0:  # Outer if: check valid age
    if age >= 18:  # Inner if: check adult
        print("You are an adult")
    else:  # Inner else: not adult
        print("You are a minor")
else:  # Outer else: invalid age
    print("Invalid age")
```

**Explanation:**  
- Outer `if` ensures age is valid (≥ 0).  
- Inner `if` distinguishes between adult and minor.  
- Outer `else` handles invalid input.

---

**Key Points to Remember:**  
- Conditions are **Boolean expressions** (True/False).  
- Python uses **indentation** to define blocks.  
- `if`, `elif`, `else` are evaluated **in order**; only the first True block executes.  
- Logical operators can combine multiple conditions efficiently.  
- Nested `if` statements allow more precise checks within broader conditions.


## Python Loops

Loops allow your program to **repeat code multiple times**.  
Python provides `for` loops and `while` loops, which are used depending on the situation.

---

### 1. `for` Loops

- Used to iterate over a **sequence** (list, tuple, string, range, etc.).  
- Executes a block of code for each item in the sequence.

```python
# Example 1: Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Example 2: Using range() to iterate over numbers
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# Example 3: Sum numbers using a for loop
total = 0
for i in range(1, 6):  # 1 to 5
    total += i
print("Sum:", total)
# Output:
# Sum: 15
```

### Countdown Timer Using `range()` and `time.sleep()`

This example shows how to create a countdown timer in Python.  
It uses:

- `range(start, stop, step)` → counts from 10 down to 1 in steps of -2  
- `time.sleep(1)` → pauses the program for 1 second between each number

```python
import time

for seconds in range(10, 0, -2):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
# Output:
# 10
# 8
# 6
# 4
# 2
# Happy New Year!
```

This is useful whenever you need delays, countdowns, or timed operations in your programs.



**Key Points for `for` loops:**
- `range(start, stop, step)` generates numbers: `start` inclusive, `stop` exclusive.  
- Loops can iterate over **any iterable**: strings, lists, tuples, sets, dictionaries (keys or values).  
- Use `break` to exit the loop early and `continue` to skip the current iteration.

---

### 2. `while` Loops

- Repeats a block of code **as long as a condition is True**.  
- Useful when the number of iterations is **not known in advance**.

```python
# Example 1: Simple while loop
count = 0
while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4

# Example 2: Using break
count = 0
while True:
    print(count)
    count += 1
    if count == 3:
        break
# Output:
# 0
# 1
# 2

# Example 3: Using continue
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip printing when count is 3
    print(count)
# Output:
# 1
# 2
# 4
# 5
```

**Key Points for `while` loops:**
- Make sure the **condition will eventually become False**, otherwise the loop will run forever.  
- `break` exits the loop immediately.  
- `continue` skips the rest of the current iteration and moves to the next check.  

---

### 3. Nested Loops

- Loops inside loops are called **nested loops**.  
- Useful for **2D structures** like grids, matrices, or tables.

```python
# Example: Nested for loop
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i={i}, j={j}")
# Output:
# i=1, j=1
# i=1, j=2
# i=1, j=3
# i=2, j=1
# i=2, j=2
# i=2, j=3
# i=3, j=1
# i=3, j=2
# i=3, j=3
```

**Tips:**
- Nested loops can be `for` inside `for`, `while` inside `while`, or mixed.  
- Be careful: nested loops can **increase execution time** quickly.  

---

✅ **Summary:**
- **`for` loop** → best for iterating over sequences with a known length.  
- **`while` loop** → best for repeating until a condition is met.  
- Use **`break`** and **`continue`** to control loop execution.  
- **Nested loops** allow multi-level iteration for more complex logic.





## Python Functions

Functions are **blocks of reusable code** that run when called.  
They help organize your code, avoid repetition, and make programs easier to read and maintain.

---

### 1. Basic Function

```python
# Define a function
def hello(name):
    print("Hello " + name)
    print("How are you?")

# Call the function
hello("Bro")
# Output:
# Hello Bro
# How are you?
```

**Explanation:**  
- `def hello(name):` → defines a function named `hello` with one parameter `name`.  
- The function code executes **only when called**: `hello("Bro")`.  
- Functions can take **parameters** (inputs) and optionally **return values**.

---

### 2. Function with Return Value

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
# Output:
# 8
```

**Notes:**  
- `return` sends a value back to the caller.  
- Without `return`, the function returns `None` by default.

---

### 3. Function with Default Parameter

```python
def greet(name="Guest"):
    print("Hello " + name)

greet("Shamsudin")  # Output: Hello Shamsudin
greet()              # Output: Hello Guest
```

**Explanation:**  
- Parameters can have **default values**.  
- If no argument is provided, the default is used.

---

### 4. Function with Multiple Parameters

```python
def introduce(name, age, country):
    print(f"My name is {name}, I am {age} years old, and I live in {country}.")

introduce("Shamsudin", 21, "Kenya")
# Output:
# My name is Shamsudin, I am 21 years old, and I live in Kenya.
```

**Notes:**  
- Python supports **positional** and **keyword arguments**.  
- Example of keyword arguments:
```python
introduce(age=21, country="Kenya", name="Shamsudin")
```

---

### 5. Function with Multiple Return Values

```python
def arithmetic(a, b):
    return a+b, a-b, a*b, a/b

sum_, diff, prod, quot = arithmetic(10, 2)
print(sum_, diff, prod, quot)
# Output:
# 12 8 20 5.0
```

**Explanation:**  
- Functions can return **multiple values** as a tuple.  
- You can unpack them into separate variables.

---

### 6. Functions with Conditional Logic

```python
def check_age(age):
    if age >= 18:
        return "Adult"
    elif age < 0:
        return "Invalid age"
    else:
        return "Minor"

print(check_age(21))  # Output: Adult
print(check_age(-5))  # Output: Invalid age
```

**Notes:**  
- Functions can include **loops, conditionals, and other logic**.  
- They are not limited to a single operation.

---

### 7. Complex Function Example — Countdown Timer with Optional Step

```python
import time

def countdown(start, stop=0, step=-1, message="Time's up!"):
    """
    Countdown timer that prints numbers from start to stop using a custom step.
    Pauses 1 second between numbers and prints a final message.
    """
    for seconds in range(start, stop, step):
        print(seconds)
        time.sleep(1)
    print(message)

# Example 1: default countdown
countdown(10, 0, -2, "Happy New Year!")
# Output:
# 10
# 8
# 6
# 4
# 2
# Happy New Year!

# Example 2: custom step countdown
countdown(5, -1, -1, "Blast off!")
# Output:
# 5
# 4
# 3
# 2
# 1
# 0
# Blast off!
```

**Explanation:**  
- Uses **parameters with default values** (`stop=0`, `step=-1`, `message`).  
- Demonstrates **loops inside functions**.  
- Can be reused with **different start, stop, step, and messages**.  
- Combines **logic, loops, and printing** in one function — a good example of real-world use.

---

✅ **Key Points About Functions:**
- Always define before calling.  
- Parameters make functions flexible.  
- `return` lets functions output values.  
- Functions can contain **loops, conditionals, and other functions**.  
- Properly documented functions (with docstrings) are easier to read and maintain.  


## Advanced Function Concepts in Python

Python functions can be made more powerful and flexible using **return statements, keyword arguments, nested function calls, and default arguments**.  
Below is a detailed guide with examples and outputs.

---

### 1. Return Statement

The `return` statement **exits a function and sends a value back** to the caller.  
Any code after `return` inside the function is **not executed**.

```python
# Example 1: Using return
def multiply(number1, number2):
    result = number1 * number2
    return result
    # print(result)  # This line will NOT be executed

x = multiply(3, 5)
print(x)
# Output:
# 15

# Example 2: Simpler version with fewer lines
def multiply(number1, number2):
    return number1 * number2

result = multiply(4, 6)
print(result)
# Output:
# 24
```

**Notes:**  
- `return` allows you to **store or further process the function’s output**.  
- Without `return`, the function outputs `None`.

---

### 2. Keyword Arguments

Keyword arguments allow you to **pass arguments by explicitly naming parameters**, ignoring their order.

```python
def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(last="Bro", middle="the", first="Shariff")
# Output:
# Hello Shariff the Bro
```

**Notes:**  
- Improves **readability** and avoids errors when calling functions with multiple parameters.  
- Can be combined with **positional arguments**.

---

### 3. Nested Function Calls

You can **call a function inside another function** or **nest multiple calls** for concise code.

```python
# Without nesting
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
# If input: -4.7
# Output:
# 5

# Using nested function calls
print(round(abs(float(input("Enter a whole positive number: ")))))
# If input: -4.7
# Output:
# 5
```

**Explanation:**  
- `float(input(...))` → converts input to float  
- `abs()` → gets absolute value  
- `round()` → rounds to nearest integer  
- Nesting **reduces lines of code** but may reduce readability if overused.

---

### 4. Default Arguments

Default arguments **provide a fallback value** if the caller does not supply one.

```python
# Example 1: Default argument
def hello(name="Bro"):
    print("Hello " + name)

hello()          # Output: Hello Bro
hello("Shariff") # Output: Hello Shariff

# Example 2: Multiple parameters with defaults
def greet(first="John", last="Doe"):
    print(f"Hello {first} {last}")

greet()               # Output: Hello John Doe
greet(first="Shamsudin") # Output: Hello Shamsudin Doe
greet(last="Ali")        # Output: Hello John Ali
```

**Notes:**  
- Default arguments **must come after non-default parameters**.  
- Combine default and keyword arguments for maximum flexibility.

---

### ✅ Key Points

1. **Return statement**: sends a value back and exits the function.  
2. **Keyword arguments**: allow arguments to be passed in any order by naming them.  
3. **Nested function calls**: combine multiple operations in a single expression.  
4. **Default arguments**: provide fallback values, reducing the need for multiple function overloads.  

---

### 5. Complex Function Example — Multi-Operation Calculator

```python
def calculator(a, b, operation="add"):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.
    Defaults to addition if no operation is provided.
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

# Examples
print(calculator(10, 5))              # Output: 15 (default add)
print(calculator(10, 5, "subtract"))  # Output: 5
print(calculator(10, 5, "multiply"))  # Output: 50
print(calculator(10, 5, "divide"))    # Output: 2.0
print(calculator(10, 0, "divide"))    # Output: Cannot divide by zero
```

**Explanation:**  
- Demonstrates **default arguments, conditionals, and return values**.  
- Can handle multiple operations in a **flexible, reusable way**.  
- Shows real-world use of Python functions in a simple calculator.

