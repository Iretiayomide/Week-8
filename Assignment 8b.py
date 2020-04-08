#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import libraries
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

#create dataset
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']

#create dataframe
df = pd.DataFrame(data = GradeList, columns=columns)

#create a new column called TotalDemerits
df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']


# In[4]:


#create a customized pie chart
plt.pie(df['TotalDemerits'],
labels=df['Names'],
explode=(0,0,0,0.35,0),
startangle=180,
autopct='%1.1f%%',)
plt.axis('equal')
plt.show()

