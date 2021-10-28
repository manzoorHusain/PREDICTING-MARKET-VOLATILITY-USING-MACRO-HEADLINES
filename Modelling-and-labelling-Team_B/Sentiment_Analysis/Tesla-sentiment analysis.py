#!/usr/bin/env python
# coding: utf-8

# # Tesla
# 

# In[8]:


import pandas as pd
import numpy as np 
import pandas as pd 
import re
import nltk 
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
global str



# In[9]:


df = pd.read_csv(r'C:\Internship\Datasets_Stocks\TSLA.csv')

print(df.shape)


# In[3]:


# let's get a randome sample of data; previously tried to run some analysis and  
# system was running out of memory
df = df.fillna(0)
#df = df.sample(frac=0.1, replace=True, random_state=1)
print(df.shape)


# In[5]:


# let's experiment with some sentiment analysis concepts
# first we need to clean up the stuff in the independent field of the DF we are workign with
df['Text'] = df[['Text']].astype(str)
df['Text'] = df[['Text']].astype(str)

df['Text'] = df['Text'].str.replace('\d+', '')
df['Text'] = df['Text'].str.replace('\d+', '')
# get rid of special characters
df['Text'] = df['Text'].str.replace(r'[^\w\s]+', '')
df['Text'] = df['Text'].str.replace(r'[^\w\s]+', '')
# get rid fo double spaces
df['Text'] = df['Text'].str.replace(r'\^[a-zA-Z]\s+', '')
df['Text'] = df['Text'].str.replace(r'\^[a-zA-Z]\s+', '')
# convert all case to lower
df['Text'] = df['Text'].str.lower()
df['Text'] = df['Text'].str.lower()


# In[7]:


# Here we are doing some sentiment analysis, and distilling the 'Tweet' field into positive, neutral, or negative, 
# based on the tone of the text in each record.  Also, we are filtering out the records that have <.2 negative score; 
# keeping only those that have >.2 negative score. This is interesting, but this can contain some non-intitive results.  
# For instance, one record in 'Tweet' literally says 'no issues'.  This is probably positive, but the algo sees the
# word 'no' and interprets the comment as negative.  I would argue that it's positive.  We'll circle back and resolve 
# this potential issue a little later.
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')


from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
df['sentiment'] = df['Text'].apply(lambda x: sid.polarity_scores(x))
def convert(x):
    if x < -0.5:
        return "negative"
    elif x > 0.5:
        return "positive"
    else:
        return "neutral"
df['result'] = df['sentiment'].apply(lambda x:convert(x['compound']))


# In[10]:


df.head()


# In[10]:


df.to_csv('TSLA_dataset.csv')


# In[ ]:




