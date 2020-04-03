#!/usr/bin/env python
# coding: utf-8

# In[28]:


#import libraries
import glob
import numpy as np
import pandas as pd
import plotly.express as px

#import and combine data 
all_data = pd.DataFrame()
for f in glob.glob("Anaconda2/archived_daily_case_updates/day*.csv"):
    df = pd.read_csv(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[33]:


# Confirmed
fig = px.choropleth(df, locations="Country/Region", 
                    locationmode='country names', color=np.log(df["Confirmed"]), 
                    hover_name="Country/Region", hover_data=['Confirmed'],
                    color_continuous_scale="Sunsetdark", 
                    title='Countries with Confirmed Cases from Jan 21st to Feb 14th 2020')
fig.update(layout_coloraxis_showscale=False)
fig.show()


# In[ ]:





# In[ ]:




