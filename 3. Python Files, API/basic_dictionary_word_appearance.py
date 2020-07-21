str = 'it appears that the the appears the most in the sentence'
dict = {}
words = str.split()

for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

for key, value in dict.items():
    print(f"'{key}' appears {value} times in the string.")