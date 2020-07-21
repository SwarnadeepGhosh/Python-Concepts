'''
Write a python code which takes input from words.py and return a random sentence with random verbs and nouns.

Output example:
The octopus hacked the king.
The goat uplifted the dog.
'''
import random
import words

def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a while loop here.
    while index < len(template):
        if template[index : index+len('{{noun}}')] == '{{noun}}':
            noun_ = random.choice(nouns)
            output.append(noun_)
            index += len('{{noun}}')

        elif template[index : index+len('{{verb}}')] == '{{verb}}':
            verb_ = random.choice(verbs)
            output.append(verb_)
            index += len('{{verb}}')

        else:
            output.append(template[index])
            index += 1

    # After the loop has finished, join the output and return it.
    return "".join(output)

if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
        words.templates))