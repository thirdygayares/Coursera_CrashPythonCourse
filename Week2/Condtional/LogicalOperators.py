# PART 1: The and Logical Operator
# In Python, you can use the logical operator and to connect more than one comparison. This type of complex comparison is used to check if two comparison statements are both True or not. You might use the and operator when you need to execute a block of code, but only if two different conditions are true. For example, you might want to write a script  that automates sending you an emergency alert if a server stops responding and there is an unusual increase in employees opening trouble tickets.
#
# Example 1:
#
# The following model demonstrates the use of the and logical operator to join comparisons between two mathematical expressions. The description below the example explains the order in which Python will process the line of code.

# Example 1

print((6*3 >= 18) and (9+9 <= 36/2))

# Example 2:
#
# In this next example, "Nairobi" < "Milan" and "Nairobi" > "Hanoi", the and logical operator is connecting two string comparison statements. You learned previously that using the greater than and less than operators on strings will test the alphabetical order (technically Unicode values) of the strings. So, this complex comparison is checking if "Nairobi" is alphabetized before "Milan" (False) AND after "Hanoi" (True).
#
# This comparison returns a False result because both sides of the logical operator are not True. A comparison statement like this might be used to iterate through a list of names to check if they are alphabetized in the correct order.

# Example 2

print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")

# PART 2: The or Logical Operator
# The or logical operator tests two conditions to determine if at least one side of the or logical operator is True. The result of the test can be used to trigger a block of code if at least one condition is present

# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))


country = "New yorl"
city = "dsd"
# False or True returns True
print(country == "New York City" or city == "New York City")


# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)


# False or False returns False
print("B_name" > "C_name" or "B_name" < "A_name")


# PART 3: The not Logical Operator
# The not logical operator inverts the value of the comparison expression. This is a helpful tool when you want to execute a block of code as long as a certain condition is not present.
#
# If the conditional  expression is True, the not logical operator can be added to make the expression not True (False).
#
# If the conditional  expression is False, the not logical operator can be added to make the expression not False (True).

# Test Example 1:

x = 2*3 > 6
print("The value of x is:")
print(x)

print("")  # Prints a blank line

print("The inverse value of x is:")
print(not x)

# Example 2:
#
# Can you determine the result of the following comparison?

# What happens when you negate a False statement?
# Click Run when you are ready to check your answer.
today = "Monday"
print(not today == "Tuesday")
# The "today" variable states today is Monday. This makes the comparison
# "today == Tuesday" False. The logical operator "not" inverts the False
# result to become True. In other words, this expression asks if it is
# false that today is not Tuesday. More succinctly, "not False" means
# True."

