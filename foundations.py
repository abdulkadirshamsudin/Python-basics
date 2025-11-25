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

# age = int(input("what is your age?"))

# if age >= 18:
#     print("you are an adult")
# else:
#     print("you are minor.")


# ## else-if (elif) statements
# age = int(input("what is your age?"))

# if age >= 18 :
#     print("you are an adult")
# elif age < 0:
#     print("Your are stiill in your father's nut sack!")
# else:
#     print("you are minor.")


# ## Logical operators with if statements and, or, not.
# temp = int(input("what is the temperature today?"))

# if temp >= 0 and temp <= 30:
#     print("the temperature is good today")
#     print("go outside")
# elif temp < 0 or temp > 30:
#     print("the temperature is bad today")
#     print("stay inside")
# else:
#     print("unable to detect temperature")

# ## nested if statements
# age = int(input("Enter your age: "))

# if age >= 0:  # Outer if: check valid age
#     if age >= 18:  # Inner if: check adult
#         print("You are an adult")
#     else:  # Inner else: not adult, must be minor
#         print("You are a minor")
# else:  # Outer else: invalid age
#     print("Invalid age")


## While loops.

#example one

# name = ""
# while len(name) == 0:
#     name = input("Etner your name:")
# print("Hello " + name)


# #Example two
# count = 0
# while count < 5:
#     print("bro code")
#     count += 1

# # # example three
# count = 0

# for i in range(10):
#     print(i)

# Fruites = {"apple", "banana", "cherry"}
# for i in Fruites:
#     print(i)

# total = 0
# for i in range(100):
#     total += i
# print(total)

# import time

# for seconds in range(10,0, -2):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# # functions - block of code which is executed when it is called
# def hello (name):
#     print("hello " + name)
#     print("How are you?")
    

# hello("bro  ")

# import time

# def countdown(start, stop=0, step=-1, message="Time's up!"):
#     """
#     Countdown timer that prints numbers from start to stop using a custom step.
#     Pauses 1 second between numbers and prints a final message.
#     """
#     for seconds in range(start, stop, step):
#         print(seconds)
#         time.sleep(1)
#     print(message)

# # Example 1: default countdown
# countdown(10, 0, -2, "Happy New Year!")
# # Output:
# # 10
# # 8
# # 6
# # 4
# # 2
# # Happy New Year!

# # Example 2: custom step countdown
# countdown(5, -1, -1, "Blast off!")
# # Output:
# # 5
# # 4
# # 3
# # 2
# # 1
# # 0
# # Blast off!


# return statement - used to exit a function and return a value.
# def multiply (number1, number2):
#     result = number1 * number2
#     return result
#     # print(result)  # This line will not be executed
# # print(multiply(3, 5)) # this will not print anything.
 
# x = multiply(3, 5)
# print(x) # this will print 15

# # SIMPER WAY WITH LESS LINES OF CODE.
# def multiply(number1, number2):
#     return number1 * number2
# result = multiply(4, 6)
# print(result)  # This will print 24 

# Keyword arguments - arguments that are passed to a function by explicitly naming each parameter and its corresponding value.


# def hello (first,middle,last):
#     print("hello " + first + " " + middle + " " + last) 

# hello(last="bro", middle="the", first="shariff") # this will print hello shariff the bro

# neste function calls - function calls made within other functions.

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)
# # The above code can be simplified using nested function calls as follows:

# print(round(abs(float(input ("Enter a whole positive number: ")))))
# # This single line of code achieves the same result by nesting the function calls.

#Default arguments - arguments that take a default value if no value is provided in the function call.
def hello (name = "bro"):
    print("hello " + name)
hello()
hello("shariff")