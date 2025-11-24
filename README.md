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

**End of README**
