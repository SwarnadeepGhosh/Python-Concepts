# Create a function called remove_substring that takes a string and removes all instances of an undesirable substring.
# This is the basic concept used in WEB SCRAPPING :
# Here are some strings you can test your function:
# print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
# print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
# print(remove_substring('I am NOT learning to code.', 'NOT '))
def remove_substring(string,substring):
    output=[]
    index=0
    while index < len(string):
        if string[index : index+len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return ("".join(output))

string=input('Enter the main string : ')
substring=input('Enter the substring which has to be removed : ')
print(remove_substring(string,substring))

'''
Input Example
Enter the main string : SPAM!HelloSPAM! worldSPAM!!
Enter the substring which has to be removed : SPAM!

Output Example
Hello world!
'''