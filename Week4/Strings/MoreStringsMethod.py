answer = "Mountains"
print(answer.upper())
print(answer.lower())

#strip method
Data = "  sas ss "
print(Data)
print(Data.strip())

# lstrip for left White spaces
print(Data.lstrip())
# rstrip for right White spaces
print(Data.rstrip())


# method count how many times a given substring appers with a string.
data2 = " The number of times e occurs in this string is 4"
print(data2.count("e"))

# method endswith return whether the string ends with a certain substring
data3 = "Forest"
print(data3.endswith("rest"))
# print true
print(data3.endswith("how"))
# print false

# method that check if the string is numeric
print(data3.isnumeric()) #print false
data4 = "2323"
print(data4.isnumeric()) # print true


# Join method
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))

# Spit method like create a list
print("This is another example".split())
# ['This', 'is', 'another', 'example']




