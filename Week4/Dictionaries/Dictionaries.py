thirdy_files = {"name": "thirdy", "surname": "gayares", "age": 20}
print(type(thirdy_files))
print(thirdy_files)

# print only my name
print(thirdy_files["name"])

# dictionares is mutable

#check if have value or title in dictionaries
print( "name" in thirdy_files)

# add elements in dictionaries
thirdy_files["school"] = "University of Makati"
print(thirdy_files)

# change value in dictionaries
thirdy_files["name"] = "jose"
print(thirdy_files)

# delete in dictionaries
del thirdy_files["age"]
print(thirdy_files)