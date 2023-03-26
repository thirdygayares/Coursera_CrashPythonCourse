def lucky_number(name):
    number = len(name) * 9
    lucky_number = "Hello " + name + ". Your lucky number is " + str(number)
    return lucky_number


print(lucky_number("Kay"))
print(lucky_number("Cameron"))