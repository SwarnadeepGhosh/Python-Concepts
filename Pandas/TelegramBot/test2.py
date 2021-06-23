#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import pandas as pd
import itertools


# In[2]:


def telegram_bot_sendtext(bot_message):
    
    bot_token = '1813999813:AAGk8lvH54zhWQoAYJbGMcAvEtCiLLhP0pg'
    bot_chatID = '643069057'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    


# In[ ]:



def telegram_bot_sendtext1(bot_message):
    
    bot_token = '1813999813:AAGk8lvH54zhWQoAYJbGMcAvEtCiLLhP0pg'
    bot_chatID = '960919064'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    


# In[3]:


#test = telegram_bot_sendtext("Testing Telegram bot")
#print(test)


# In[6]:


df = pd.read_excel (r'C:\Users\Sayan\Desktop\marks.xlsx')


# In[7]:


df.head()


# In[8]:


list1 = df.values.tolist()


# In[9]:


list1


# In[16]:


li2 = list(itertools.chain(*list1))


# In[17]:


li2


# In[19]:


str1 = ''.join(str(e) for e in li2)


# In[21]:


str1


# In[ ]:





# In[22]:


test1 = telegram_bot_sendtext(str1)
test2 = telegram_bot_sendtext1(str1)


# In[ ]:




