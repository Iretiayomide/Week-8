#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

#import csv dataset
Location = "Anaconda2/gradedata.csv"
df = pd.read_csv(Location)

#create scatterplot
plt.scatter(df.hours, df['grade'])


# In[ ]:


# Conclusion - From the scatterplot above, there is an obvious pattern. We can therefore conclude that the as the number of hours increase, the grades also increase.

