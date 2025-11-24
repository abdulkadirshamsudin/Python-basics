# # to print a message syntax:
# # -we use print key word for print statement Example.
# print ("What you want to print")
# print ("hello World")

# # variiables
# ## - They are containters for valuse. eg int, stings, floats, bulleans etc

# ## 1. Strings
# # Example
# # first_name = "bro"
# # last_name = "shariff"
# # full_name = first_name + " " + last_name
# # print(full_name)

# ## 2. Int
# # Example
# age = 21
# age += 1
# print ("my age is " + str (age))
# # type catting is  displayed above. str (age)

# ## 3. float
# height = 178.5
# print("my height is " + str(height))

# ## 4. bullean
# human = False
# print(human)

# ## multipe assignment
# # example one
# name, age, attractive = "shariff" , 21 , True

# #example 2:
# spongebob = 30
# patric = 30
# garry = 30
# #- is the same as saying:
# sopngebob = patric = garry = 30

# # useful string method.
# #len allows us to see the length of a variable.
# name = "len(bro)"

# #find used to find character possitions
# print(name.find ("o"))
# print(name.capitalize)
# print(name.upper())
# print(name.lower())
# print(name.isalpha())
# print(name.replace())
# print(name*3) # prints name 3 times.

# Conditional stateemnts.
#if statements

age = int(input("what is your age?"))

if age >= 18:
    print("you are an adult")
else:
    print("you are minor.")


## else-if (elif) statements
age = int(input("what is your age?"))

if age >= 18 :
    print("you are an adult")
elif age < 0:
    print("Your are stiill in your father's nut sack!")
else:
    print("you are minor.")


## Logical operators with if statements and, or, not.
temp = int(input("what is the temperature today?"))

if temp >= 0 and temp <= 30:
    print("the temperature is good today")
    print("go outside")
elif temp < 0 or temp > 30:
    print("the temperature is bad today")
    print("stay inside")
else:
    print("unable to detect temperature")

## nested if statements
age = int(input("Enter your age: "))

if age >= 0:  # Outer if: check valid age
    if age >= 18:  # Inner if: check adult
        print("You are an adult")
    else:  # Inner else: not adult, must be minor
        print("You are a minor")
else:  # Outer else: invalid age
    print("Invalid age")



