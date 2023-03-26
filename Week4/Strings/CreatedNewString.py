message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)


pets = "Cats & Dogs"
pets.index("&")
pets.index("C")
pets.index("Dog")

# python firts get tje he one first
pets.index("s")


# now check if the keyword is on the string
print("Dragons" in pets)
# print false
print("Cats" in pets)
#print true


# Real World problem

# Scenario - Change the old email to new email

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

new_domain = "thirdygraphics"

email1 = replace_domain("gayaresthird@graphicsthirdy", "graphicsthirdy", new_domain)
email2 = replace_domain("juan@thirdygraphics", "graphicsthirdy", new_domain)


print(email1)
print(email2)





