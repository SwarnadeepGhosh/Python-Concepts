number = input('> ')
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight"
}
output = ""

for i in number:
    output += digits_mapping.get(i, '!') + " "  # '!' is default if match not found 
print(output)