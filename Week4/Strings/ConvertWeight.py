def convert_weight(ounces):
    pounds = ounces/16


    result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
    return result

print(convert_weight(12))
print(convert_weight(50.5))