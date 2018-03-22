
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# In[3]:

data = pd.read_csv('data_task3.csv', sep='\t')


# In[4]:

data.head()


# In[5]:

data['mark'] = np.where((data['jud'] == data['cjud']), 1, 0)


# In[6]:

data.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1,  inplace=True)


# In[7]:

data_new = data.groupby(['login'], axis=0, as_index=False)['mark'].sum()


# Выведем топ-5 асессоров, которые сделали меньше всего ошибок

# In[8]:

data_new.sort_values('mark', ascending=False).head(5) 


# In[ ]:



