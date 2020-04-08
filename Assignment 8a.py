#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')

#import csv dataset
Location = "Anaconda2/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


#create an age histogram, categorized by gender
df.hist(column = "age", by = "gender")

