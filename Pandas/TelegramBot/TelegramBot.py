#!/usr/bin/env python
# coding: utf-8

# # Sending Data to Telegram

import requests
import pandas as pd
import os


def telegram_bot_sendtext(bot_message,bot_chatID):
    bot_token = '1811972683:AAH8RHie2JXsHsiJMhShhkQaHEr0C-gEvsA'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    
    return response.json()


# test = telegram_bot_sendtext("Testing Telegram bot")
# print(test)

# df = pd.read_excel (r'D:\COURSE Modules\My Courses\Python Concepts\Pandas\TelegramBot\ekyc_data.xlsx')
# print(df)

# have to install openpyxl through : "pip install openpyxl"
df1 = pd.read_excel( r'D:\COURSE Modules\My Courses\Python Concepts\Pandas\TelegramBot\ekyc_data.xlsx', engine='openpyxl')
df1.head()

myList = df1.values.tolist()
print(myList)

# myList[1][1]
# len(myList)

message = ''

for item in range(len(myList)):
    for j in range(len(myList[item])):
        message += str(myList[item][j]) + " "
    message += '\n'


test = telegram_bot_sendtext(message, '960919064' )
print(test)


test = telegram_bot_sendtext(message, '1038370384' )
print(test)

test = telegram_bot_sendtext(message, '406661666' )
print(test)
