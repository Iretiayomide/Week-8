#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "Anaconda2/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


#sort data
df = df.sort_values(by=['fname', 'age', 'grade'],
        ascending=[True, True, True])
df.head()

