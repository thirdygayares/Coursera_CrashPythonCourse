# 1
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
print("Total characters: {}, Average Length: {}".format(chars, chars/len(animals)))

# 2
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index+1, person))

# 3
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([('gayaresthird@gmail.com', 'Thirdy Gayares'), ("mariellezbl@gmail.com", "Marielle Zabala")]))


# Sample Activity
def skip_elements(elements):
    # Initialize an empty list to store the elements to be skipped
    skipped_elements = []

    # Iterate through the input list using a for loop with a step of 2
    for i in range(0, len(elements), 2):
        # Append the element at the current index to the skipped_elements list
        skipped_elements.append(elements[i])

    # Return the skipped_elements list
    return skipped_elements
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
