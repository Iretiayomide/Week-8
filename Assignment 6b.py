#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "Anaconda2/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df.gender[df.gender == 'male'] = 0
df.gender[df.gender == 'female'] = 1
print(df)


# In[3]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ age + exercise + hours',
data=df).fit()
result.summary()


# In[4]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ exercise + hours',
data=df).fit()
result.summary()


# In[5]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ gender+ age + exercise + hours',
data=df).fit()
result.summary()

