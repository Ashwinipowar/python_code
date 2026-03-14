a=330
b=3303
 
print("a") if a>b else print("=") if a==b else print("B")


c = 9 if a<b else 0
print(c)


# ​In Python, a shorthand way to write an if...else statement is by using the 
# ternary conditional operator. This allows you to evaluate a condition and return a value 
# based on whether the condition is True or False, all in a single line
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult


# Nested Ternary Operators: 
# While it's possible to nest ternary operators, it can make the code less readable. For instance:
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # Output: B







# How Do I Use the Ternary Operator in Python?
# The ternary operator in Python is a one-line shorthand for an if-else statement.
#  It allows you to quickly test a condition and return a value based on whether that condition is true or false.
x = 10
print('Even' if x % 2 == 0 else 'Odd')
# Output:
# Even





# Exploring Nested Ternary Operations in Python
# As you become more comfortable with the ternary operator, you might find yourself wondering if you can nest them. 
# The answer is yes, you can, but with caution. Nested ternary operations can make your code compact,
#  but they can also make it harder to read if overused.
x = 15
message = 'Divisible by 5' if x % 5 == 0 else 'Even' if x % 2 == 0 else 'Odd'
print(message)
# Output:
# Divisible by 5
