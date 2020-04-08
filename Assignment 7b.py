#!/usr/bin/env python
# coding: utf-8

# In[9]:


#import libraries
import matplotlib.pyplot as plt
import pandas as pd

#create dataset 
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior', 'Junior']
grades = [76,95,77,78,99]
GradeList = zip(status,grades)

#create dataframe
df = pd.DataFrame(data = GradeList, columns=['Status', 'Grades'])

#plot graph
get_ipython().magic(u'matplotlib inline')
df.plot(kind='bar')


# In[10]:


#add code to plot dataset, replacing x-axis with Names column
df2 = df.set_index(df['Status'])
df2.plot(kind="bar")

