# question16

# Operator Challenge -
# Write a program that calculates the remainder when dividing two numbers. Print both the quotient and remainder.

number1=int(input("enter first number:"))
number2=int(input("enter second number:"))
number_quotient=number1/number2
print("the quotient is:", number_quotient )
number_remainder=number1%number2
print("the remainder is ", number_remainder)

# question17
# 17. Escape Sequences and Print Formatting:
# Create a program that prints a message with a backslash followed by a quote on the same line using escape sequences.

message="i am doing good \n and i always do my best"
print(message)

#question18
# 18. Type Casting and Comments:
# Take the user's height as input (consider it as a float) in centimeters. Convert it to meters and print the result with a comment explaining the conversion.

height=float(input("enter your number in centimeters:"))
height_in_meters= height /100
print("hence the height in meters is :", height_in_meters)

# question19
# 19. Operators and Conditional Print:
# Write a program that takes a number as input and prints "Even" if it's an even number and "Odd" if it's an odd number.

number=int(input("enter your number:"))
if number % 2 ==0:
  print("the number is even")
else:
  print("number is odd")

question19 duplicate
def number_check(number):
  number=int(number)
  if number >20:
    return number*2
  elif number <20:
    if number % 2 == 0:
      return("the number is even")
    else:
      return("the number is odd")
  else:
    return("the number is exactly 20")

user_number=input("enter your number")
number_even_odd=number_check(user_number)
print(number_even_odd)

# 20. Print Formatting and Comments:
# Print a message that includes both single and double quotes. Add comments explaining how to handle quotes in strings.

message=" how are you doing, he replied: 'i am doing good' "
print(message)

# question21

# 21. Operator Challenge - IV:
# Write a program that calculates the area of a circle. Take the radius as input and use the appropriate operator.

radius=int(input("enter the radius:"))
area_of_circle=3.14 * radius ** 2
print(area_of_circle)
question22

# 22. Escape Sequences and Print Formatting:
# Create a program that prints your address with proper line breaks and tabs using escape sequences.

address="fazaia\thousing\tsociety, \n house no 342, \n block b ,\n lahore"

print(address)

# question23
# 23. Type Casting and Operator Challenge:
# Take a number as input (consider it as a float), convert it to an integer, square it, and then print the result.

number=float(input("enter your number : "))
new_number=int(number)
sqaure_new_number=new_number ** 2
print("The square of new number is : " , sqaure_new_number)

question24

# 24. Operators and Print Formatting:
# Write a program that calculates the total cost of items in a shopping cart. Use variables for item prices and quantities.

item_1_price=500
item_1_quantity=2

item_2_price=600
item_2_quantity=3

total_cost_item1=item_1_price * item_1_quantity
total_cost_item2=item_2_price * item_2_quantity

print(total_cost_item1)
print(total_cost_item2)

total_cost=total_cost_item1 + total_cost_item2
print(total_cost)

question25

# 25. Conditional Statements and Comments:
# Create a program that takes a person's age as input and prints "Teenager" if they are between 13 and 19 years old.

age=int(input("enter your age:"))
if age >=13 and age <=19:
  print("teenager")
else:
  print("not teenager")

# question26

# 26. Escape Sequences and Print Formatting:
# Print a message that includes a new line and a backspace character. Add comments explaining their use.

message="hello\n how are you doing \b i am doing good"
print(message)
we use \n to create a new line and \b to create a backspace.

#question27
# 27. Operator Challenge - V:
# Write a program that takes two numbers as input and swaps their values without using a third variable.

number1=int(input("enter first number: "))
number2=int(input("enter second number : "))

print("before swapping")
print("number1 before swapping:", number1)
print("number2 before swapping:", number2)
number1= number1+number2
number2=number1-number2
number1=number1-number2
print("after swapping")

print("number1 after swapping is:" , number1)
print("number2 after swapping is:" , number2)

# question28

# 28. Type Casting and Print Formatting:
# Take a floating-point number as input, convert it to an integer, and then print it in a sentence using formatted print statements.

number=float(input("enter your number : "))
number_to_int=int(number)
print(f"the entered number is {number_to_int}  ". format(number_to_int))

# question29

# 29. Conditional Statements and Comments:
# Create a program that checks if a given number is positive, negative, or zero. Add comments explaining each condition.

number=int(input("enter your number : "))
if number>0:
  print("the number is positive")
elif number<0:
  print("the number is negative")
else:
  print("the number is zero")

question30

# 30. Escape Sequences and Print Formatting:
# Print a message that includes a Unicode character. Add comments explaining the importance of Unicode in programming.

message_with_unicode = "Hello! \u2720 Welcome to the world of Unicode! \u2729"

print(message_with_unicode)

# question31
# 31. Operator Challenge - VI:
# Write a program that calculates the average of four numbers. Use both addition and division operators.

numbers=[1,2,3,4]
sum_numbers=sum(numbers)
length=len(numbers)
average_of_numbers=sum_numbers/ length
print("the average of numbers is : ", average_of_numbers)

# question32
# Take a user's age as input (consider it as a string), convert it to an integer, and print "Child" if the age is below 12.

age_str = input("Enter your age: ")

age = int(age_str)

if age < 12:
    print("Child")

# question33
# Write a program that calculates the area of a triangle. Take the base and height as input and use the appropriate operator.

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height

print("The area of the triangle is:", area)

# question34
# Print a message that includes a percent symbol using escape sequences. Add comments explaining their purpose.

print("You scored 90% on the exam!")

# question35

# Take a decimal number as input, convert it to an integer, and then print both the original and converted values.

decimal_number_str = input("Enter a decimal number: ")

decimal_number = float(decimal_number_str)

print("Original decimal number:", decimal_number_str)
print("Converted integer value:", int(decimal_number))
