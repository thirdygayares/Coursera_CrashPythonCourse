counts = {"mov": 20, "mp4":14}
for extension in counts:
    print(extension)

for ext, amount in counts.items():
    print("There are {} files with the . {} extension".format(amount, ext))

# content and values
print(counts.keys())
print(counts.values())

# get all values
for value in counts.values():
    print(value)