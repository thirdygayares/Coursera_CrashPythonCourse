def username(last_name, birthyear):
    return ("{}{}".format(last_name[0:3], birthyear))

print(username("Ivanov", "1985"))
print(username("Gayares", "2002"))
print(username("Gasidan", "2002"))

