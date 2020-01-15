#!/usr/bin/env python
# coding: utf-8

# In[272]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#pull necessary date from the csv file 
DF= pd.read_csv('master.csv', usecols=[0,1,2,3,4,5,6,10])
DF.columns = ['country', 'year', 'sex', 'age','suicides_no', 'population', 'suicides/100k pop', 'gdp_per_capita($)']   

#clean the data to the ones needed for research 
df = DF.loc[DF['country'] == 'United Kingdom']
df_uk = df_uk

df = df.append(DF.loc[DF['country'] == 'United States'], ignore_index=True)
df = df.append(DF.loc[DF['country'] == 'Lithuania'], ignore_index=True)
#delete variables that are missing other variables 
first10 = df[df['year'] <= 1994].index
df = df.drop(first10)

#organize data 
df = df.sort_values(by=['country','year','sex','age'])
df = df.reset_index()
df = df.drop(columns='index')

#delete variables that are missing other variables 
first10 = df_uk[df_uk['year'] <= 1994].index
df_uk = df_uk.drop(first10)

#organize data 
df_uk = df_uk.reset_index()
df_uk = df_uk.sort_values(by=['country','year','sex','age'])
df_uk = df_uk.drop(columns='index')
df_uk.head(8)


# In[419]:


#pivot table for the number of suicide in order to create graph
uk_suicides = pd.pivot_table(df_uk, index = 'year', values = ['suicides_no'], aggfunc='sum')
uk_suicides = uk_suicides.dropna()

#create scatter point with line for easier pattern analysis 
ax = uk_suicides.plot(figsize=(15,8))
uk_suicides.reindex(uk_suicides.index).plot(marker='o',linestyle='none',color='g', ax=ax).grid()
plt.xlabel('Year')
plt.ylabel('Number of suicides')
plt.title('U.K. number of suicides 1995-2015')
plt.show()


# In[417]:


#pivot table for the suicide rates in order to create graph
uk_rate = pd.pivot_table(df_uk, index = 'year', values = ['suicides/100k pop'], aggfunc='sum')
uk_rate = uk_rate.dropna()

#create scatter point with line for easier pattern analysis 
ax = uk_rate.plot(figsize=(15,7))
uk_rate.reindex(uk_rate.index).plot(marker='o',linestyle='none',color='g', ax=ax).grid()
plt.xlabel('Year')
plt.ylabel('Suicides/ 100k population')
plt.title('U.K. suicide rates/ 100k population 1995-2015')
plt.show()


# In[426]:


#pivot table for the number of suicides in order to create graph
uk_genn = pd.pivot_table(df_uk, index = ['sex'],values = ['suicides_no'], aggfunc='sum')

#uniform color for gender 
g_colors = ['r','blue']

#plot pie graph
ax = uk_genn.plot.pie(y = 'suicides_no',colors=g_colors, title = 'Number of suicides 1995-2015',autopct='%1.1f%%')




# In[427]:


#pivot table for the number of suicides in order to create graph
uk_genr = pd.pivot_table(df_uk, index = ['year'],values = ['suicides/100k pop'],columns=['sex'], aggfunc='sum')

#plot line graph 
uk_genr.plot(figsize=(15,7),color=g_colors).grid()
plt.xlabel('Year')
plt.ylabel('Suicides/ 100k population')
plt.title('U.K. suicide rates/ 100k population 1995-2015')
plt.show()


# In[278]:


#create box graph by gender 
ax = uk_genr.boxplot(figsize = (5,10))
plt.title('Average rate of suicides/ 100k population 1995-2015')


# In[377]:


#pivot table for the number of suicides in order to create graph
uk_age = pd.pivot_table(df_uk, index = ['year'],values = ['suicides/100k pop'],columns=['age'], aggfunc='sum')

#create bar graph by age group 
ax = uk_age.plot.barh(stacked=True, figsize=(18,10),rot=0)
plt.xlabel('Year')
plt.ylabel('Suicides/ 100k population')
plt.title('U.K. suicide rates/ 100k population 1995-2015')
plt.show()


# In[371]:


#pivot table for the number of suicides in order to create graph
uk_ageSpecific = uk_age.drop(['5-14 years','15-24 years'],axis=1)

#graph line graph by age group
uk_ageSpecific.plot(figsize=(15,10)).grid()
plt.xlabel('Year')
plt.ylabel('Suicides/ 100k population')
plt.title('U.K. suicide rates/ 100k population 1995-2015')
plt.show()


# In[356]:


#pivot table for the number of suicides in order to create graph
uk_age = pd.pivot_table(df_uk, index = ['year'],values = ['suicides/100k pop'],columns=['age'], aggfunc='sum')
#relabel column names 
uk_age.columns = ['15-24 years', '25-34 years', '35-54 years', '5-14 years', '55-74 years', '75+ years']

#graph box graph by age group 
ax = uk_age.boxplot(figsize = (10,13))
plt.title('Average rate of suicides/ 100k population 1995-2015')


# In[389]:


#pivot table for the number of suicides in order to create graph
uk_demo = pd.pivot_table(df_uk, index = 'age', values = ['suicides_no'],columns='sex', aggfunc='sum')
uk_demo.columns = ['female','male']

#create heatmap by demographics
ax = sns.heatmap(uk_demo, annot=True,linewidths = 2)
ax.set_ylim(0, 5) 
ax.set_title('Number of suicide 1995-2015') 
ax.set_xlabel('Sex')
ax.set_ylabel('Age Group')
plt.show()


# In[273]:


#pivot table for the number of suicides in order to create graph
df_all = pd.pivot_table(df, index = 'year', values = ['suicides/100k pop'], columns='country', aggfunc='sum')
df_all = df_all.dropna()

#create line graph by the country 
df_all.plot(figsize=(10,7)).grid()
plt.xlabel('year')
plt.ylabel('suicides/ 100k population')
plt.title('countrys suicide rates/ 100k population')
plt.show()


# In[425]:


#organize for explicit data on U.K. and U.S.
df_two = DF.loc[DF['country'] == 'United Kingdom']
df_two = df_two.append(DF.loc[DF['country'] == 'United States'], ignore_index=True)
df_two = pd.pivot_table(df_two, index = 'year', values = ['suicides/100k pop'], columns='country', aggfunc='sum')

#graph line graph for specified variables 
df_two.plot(figsize=(10,7), color=['orange','green']).grid()
plt.xlabel('year')
plt.ylabel('suicides/ 100k population')
plt.title('countrys suicide rates/ 100k population')
plt.show()


# In[403]:


#organize data only for necessary data 
df_gdp = df.drop(columns='sex')
df_gdp = df_gdp.drop(columns='age')
df_gdp = df_gdp.drop(columns='population')
df_gdp = df_gdp.drop(columns='suicides_no')
df_gdp = df_gdp.drop(columns='suicides/100k pop')
df_gdp = df_gdp.drop_duplicates()

#pivot table for the number of suicides in order to create graph
df_gdp = pd.pivot_table(df_gdp, index = 'year', values = ['gdp_per_capita($)'], columns='country')
df_gdp = df_gdp.dropna()

#create line graph by country's economy 
df_gdp.plot(figsize=(10,7)).grid()
plt.xlabel('Year')
plt.ylabel('gdp_per_capita($)')
plt.title('countrys gdp_per_capita($)')
plt.show()


# In[ ]:




