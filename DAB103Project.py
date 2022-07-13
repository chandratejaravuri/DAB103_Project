#!/usr/bin/env python
# coding: utf-8

# In[210]:


import pandas as pd
import numpy as np
from itertools import chain
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings


# In[211]:


IT_EU_US = pd.read_csv("E:\study\DAB103\IT_Salary_EU&US.csv")


# In[ ]:





# In[212]:


IT_EU_US


# In[213]:


type(IT_EU_US)


# In[214]:


IT_EU_US.shape


# In[215]:


print(IT_EU_US.columns.tolist())


# In[216]:


dataTypeSeries = IT_EU_US.dtypes

print(dataTypeSeries)


# In[217]:


IT_EU_US.head(6)


# In[218]:


IT_EU_US.tail(5)


# In[219]:


IT_EU_US.isnull().sum()


# In[220]:


IT_EU_US.nunique()


# In[221]:


IT_EU_US.corr()


# In[222]:


fig=px.box(IT_EU_US,y="Age")
fig.show()


# In[223]:


sns.set()
ax = sns.countplot(x="Contract duration",data=IT_EU_US)

plt.xlabel('Сontract duration',fontsize = 15) 
plt.ylabel('Count', fontsize = 15) 
plt.title("COUNT OF PEOPLE WHO ARE HAVING DIFFERENT CONTRACTS", fontsize = 15)


# In[224]:


IT_EU_US.Gender.str.get_dummies().sum().plot.pie(label='', autopct='%1.0f%%',figsize=(10, 7) , fontsize = 20)
plt.title("PROPORTION OF GENDERS", fontsize = 20)


# In[225]:


sns.set_theme(style="darkgrid")
p8= plt.hist(IT_EU_US['Age'],bins=10)
plt.xlabel('Age') 
plt.ylabel('Count') 
plt.title("COUNT OF DIFFERENT AGE")
plt.show(p8)


# In[226]:


sns.set_theme(style="darkgrid")
ax = sns.boxplot(x="Age", y="Gender", data=IT_EU_US)
plt.xlabel('Age') 
plt.ylabel('Gender') 
plt.title("GENDERS RESPECTIVE TO THEIR AGES")


# In[227]:


plt.figure(figsize = (11,8))
sns.set_theme(style="darkgrid")
ax = sns.countplot(x="Company size",data=IT_EU_US)
plt.xlabel('Company size') 
plt.ylabel('count') 
plt.title("DIFFERENT COMPANY SIZES AND ITS COUNT")


# In[ ]:





# In[228]:


# Distribution of Yearly Salaries with countries
plt.figure(figsize=(15,8))

sns.histplot(x='Yearly salary range',data=IT_EU_US,
             bins=20, kde=True, hue='Countries',multiple="stack",palette='inferno')
plt.xticks(fontsize=13)
plt.xlabel("Yearly salary range",fontsize=14)
plt.yticks(fontsize=15)
plt.ylabel("Count",fontsize=15)
plt.title("Yearly Salaries With countries",fontsize=15)
plt.show()


# In[236]:


IT_EU_US.drop(IT_EU_US[IT_EU_US['Age'] == 0 ].index, inplace = True)
IT_EU_US.plot.scatter(x = 'Age', y = 'Yearly salary range')



# In[237]:


plt.figure(figsize=(15,8))
sns.countplot(data=IT_EU_US,x='Seniority level',
              order=IT_EU_US['Seniority level'].value_counts().iloc[:10].index,
              palette='Pastel2')
plt.xticks(rotation=70,fontsize=13)
plt.xlabel("Seniority level",fontsize=14)
plt.yticks(fontsize=13)
plt.ylabel("Count",fontsize=14)
plt.title("Positions Are In Trend In Year 2020 ",fontsize = 15)
plt.show()


# In[241]:


plt.figure(figsize=(15,8))
sns.countplot(data=IT_EU_US,x='Position ',
              order=IT_EU_US['Position '].value_counts().iloc[:20].index,
              palette='Pastel2')
plt.xticks(rotation=70,fontsize=13)
plt.xlabel("Position ",fontsize=14)
plt.yticks(fontsize=13)
plt.ylabel("Count",fontsize=14)
plt.title("Positions Are In Trend In Year 2020 ",fontsize = 15)
plt.show()


# In[ ]:




