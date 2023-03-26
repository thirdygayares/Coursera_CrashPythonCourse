def mirrored_string(my_string):
    forward = ""
    backward = ""

    for character in my_string:
        if character.isalpha():
            forward += character
            backward = character + backward
    if forward.lower() == backward.lower():
        return True
    return False

print(mirrored_string("MadaM"))
