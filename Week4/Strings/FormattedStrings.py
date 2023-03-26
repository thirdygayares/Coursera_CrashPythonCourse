name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name,number))
# Hello Manny, your lucky number is 15
# Second Method
print(f"Hello {name}, your lucky number is {number}")
#thirdy Method
print("Your lukcy number is {number}, {name}".format(name=name, number=len(name)*3))

# Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
def student_grade(name, grade):
	return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 7.5
with_tax = price * 1.09
# default code
print(price, with_tax)
# format two decimal only
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price,with_tax))
# Base price: $7.50. With Tax: $8.18


# Format organized text
def to_celcius(x):
    return (x-32)*5/9

for x in range(0,100,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))

