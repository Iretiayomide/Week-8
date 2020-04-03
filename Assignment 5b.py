#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=GradeList, columns=['Names','Grades','BS','MS','PhD'])
df


# In[3]:


df.median()


# In[4]:


df.var()


# In[5]:


df.mean()


# In[6]:


df.count()


# In[7]:


df.std()


# In[8]:


df.min()


# In[9]:


df.max()


# In[10]:


df.quantile(.25)


# In[11]:


df.quantile(.50)


# In[12]:


df.quantile(.75)


# In[13]:


df.describe()


# In[ ]:




