def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😥",
        ":o": "😮"
    }
    result = ""
    for word in words:
        # We are using dictianary.get(match With This, Default Value), if match found, return respective value, else return default value.
        result += emojis.get(word, word) + " "
    return result


message = input('> ')
result = emoji_converter(message)
print(result)
