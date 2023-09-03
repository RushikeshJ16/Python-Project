#!/usr/bin/env python
# coding: utf-8

# # Libraries in Data Analytics
# 
# 1. Pandas(Python Data Analysis)
# 2. Numpy(Numerical Python)
# 3. Matplotlib(Library used to visualize the plots)
# 4. Seaborn(Its also a visualization library but more colorful and interactive)
# 
# 
# 

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


df=pd.read_csv("cab_rides.csv")
print(type(df))

#data frame


# In[6]:


df


# In[7]:


df.shape #every row is corresponding to one uber trip
#(no_of_rows,no_of_columns)


# In[8]:


df.columns


# In[9]:


df['date_time'] = pd.to_datetime(df['time_stamp']/1000, unit='s')


# In[10]:


print(dir(df))


# In[11]:


df.columns


# In[12]:


# to check if there are duplicates in my data

df.duplicated().sum() 


# In[13]:


df=df.drop_duplicates()


# In[14]:


df


# In[15]:


df.isnull().sum()


# In[16]:


df['distance'].describe()


# In[17]:


df.distance.describe()


# In[18]:


value_distance=df.distance.value_counts()
value_distance


# In[19]:


print(len(value_distance))


# In[20]:


top_10_value_dis=value_distance.iloc[:10] 
top_10_value_dis


# In[21]:


df1=df.iloc[:,0:2]
df1


# In[22]:


df1=df.iloc[0:5,0:2]
df1


# In[23]:


df1=df.iloc[:,:]
df1


# In[24]:


df2=df.loc[df.distance==0.44]
df2


# In[25]:


df2=df.loc[df.distance==1.0][0:10]    # like where condition in sql server
df2


# In[26]:


df3=df[(df.distance==0.44) & (df.price==5.0)]
df3


# In[27]:


df4=df[(df.distance==0.44) | (df.price==5.0)]
df4


# In[28]:


df5=df.loc[(df.destination=="South Station") & (df.surge_multiplier==1.0) & (df.cab_type=="Lyft")][5:10]
df5


# In[29]:


df2=df[(df.price>20) & (df.price<40)]
df2


# In[30]:


df["name"].value_counts()


# In[31]:


df.sort_values(by=['distance'],ascending=False)


# In[32]:


df.sort_values(by=['price'])


# In[33]:


df.sort_values(by=['price'],ascending=False)


# In[34]:


df.sort_values(by=['distance','price'],ascending=False)


# In[35]:


df.sort_values(by=['price','distance'],ascending=False)


# In[36]:


df_new=df.loc[~df.price.isnull()]
df_new


# In[37]:


df_new.isnull().sum()


# In[38]:


df7 = df[(df.source=="West End") & (df.destination=="North End") & (df.price >= 10)]
df7
df7.count()


# In[39]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[40]:


plt.hist(df.distance)


# In[41]:


plt.hist(df.price)


# In[42]:


plt.hist(df.price)


# # Observations
# 1. the highest number of trips in range between 0$ and 10$ having more than 2.5 lacs count
# 2. the increasing in price the number of trips are decreasing

# In[43]:


df.price


# In[44]:


import warnings
warnings.filterwarnings("ignore")
sns.FacetGrid(df, hue="cab_type" ,size=5).map(sns.distplot, "distance").add_legend()
plt.show()


# In[45]:


sns.FacetGrid(df,size=5).map(sns.distplot, "price").add_legend()
plt.show()


# # observations
# 1. for the lowest price public preference is Uber
# 
# 

# In[46]:


# Syntax
# sns.FacetGrid(df, hue="cab_type" ,size=5).map(sns.distplot, "price").add_legend()
# facetgrid is a function by which we can make distribution slots.
# df is a dataframe


# # questions to solve
# 1. what is the percentage distribution of lyft and uber 

# In[47]:


perct_dist = df.cab_type.value_counts()
perct_dist


# In[48]:


index = perct_dist.index
sizes = perct_dist.values
print(index)
print(sizes)


# In[49]:


plt.pie(sizes, labels=index, autopct='%1.2f%%',shadow=True)


# In[50]:


perct_dist_src = df.source.value_counts()
perct_dist_src


# In[51]:


index1=perct_dist_src.index
sizes1=perct_dist_src.values
print(index1)
print(sizes1)


# In[52]:


plt.pie(sizes1, labels=index1, autopct='%1.1f%%', shadow=True)


# In[53]:


perct_dist_dest=df.destination.value_counts()
perct_dist_dest


# In[54]:


index2=perct_dist_dest.index
sizes2=perct_dist_dest.values


# In[55]:


plt.pie(sizes2, labels=index2, autopct='%1.2f%%', shadow=True)


# In[56]:


new_df = df[["source","destination"]]
new_df


# In[57]:


new_df["std"] =df.source + "-" + df.destination    # adding new column std
new_df


# In[58]:


std_value=new_df["std"].value_counts()
std_value


# In[59]:


top_10 = std_value [:10]
top_10


# In[60]:


sns.barplot(top_10.values, top_10.index)


# In[61]:


sm=df.surge_multiplier.value_counts()
sm


# In[62]:


plt.pie(sm.values, labels=sm.index, autopct='%1.2f%%') # plt.pie(size,labels,autopct='%1.1%%')


# In[63]:


nm=df.name.value_counts()
nm


# In[64]:


plt.pie(nm.values, labels=nm.index, autopct='%1.1f%%')


# In[65]:


sns.barplot (nm.values,nm.index)


# In[66]:


df.sort_values(by=['price'],ascending=False)


# In[67]:


pc=df.price.value_counts()
pc


# In[68]:


pc=df.price.value_counts()[:10]
pc


# In[69]:


plt.figure(figsize=(10,5))
sns.barplot(pc.index,pc.values)


# # Group By

# In[70]:


df.isnull().sum()


# In[106]:


df=df.dropna()


# In[107]:


a=df.groupby("name")["price"].max().sort_values(ascending=False)


# In[108]:


b=df.groupby("name")["price"].sum().sort_values(ascending=False)


# In[74]:


print(type(a))
a


# In[75]:


a.sort_values(ascending=False)


# In[76]:


plt.pie(a.values, labels=a.index, autopct='%1.1f%%')


# In[77]:


df


# # To segregate date and time 

# In[78]:


df['date_time'] = pd.to_datetime(df['time_stamp']/1000, unit='s')
df


# In[79]:


df['date']=pd.to_datetime(df['date_time']).dt.date
df['time']=pd.to_datetime(df['date_time']).dt.time
df


# In[80]:


df.groupby("cab_type")["distance"].mean()


# In[81]:


df.groupby("cab_type")["distance"].max()


# In[82]:


df.groupby("cab_type")["distance"].min()


# # Extra Questions with their plots

# 1.Rides of Uber with surge multiplier 1 

# In[83]:


df5=df[(df.surge_multiplier==1.0) & (df.cab_type=="Uber")]
df5


# 2.Rides of car name taxi

# In[84]:


df2=df[df.name=='Taxi']
df2


# 3.Top 10 rides with distance more than 2 miles and price more than 20$

# In[85]:


df2=df[(df.distance>2.0) & (df.price>20)][1:10]
df2


# 4.Sort rides by highest price surge multiplier

# In[86]:


df.sort_values(by=['price','surge_multiplier'],ascending=False)


# 5.Number of rides which have source Boston University,destination Financial District and price less than 15$

# In[87]:


df7 = df[(df.source=="Boston University") & (df.destination=="Financial District") & (df.price <= 15.0)]
df7
df7.count()


# 6.Histogram of date

# In[88]:


plt.figure(figsize=(11,7))
plt.hist(df.date)


# 7.Pie chart of percentage of cab types used

# In[89]:


perct_dist = df.name.value_counts()
perct_dist


# In[90]:


index = perct_dist.index
sizes = perct_dist.values
print(index)
print(sizes)


# In[91]:


plt.pie(sizes, labels=index, autopct='%1.2f%%',shadow=True)


# 8.price bar chart

# In[92]:


pc=df.price.value_counts()


# In[93]:


pc=df.price.value_counts()[:10]
pc


# In[94]:


plt.figure(figsize=(15,5))
sns.barplot(pc.index,pc.values)


# 9.surge multiplier other than 1 bar graph 

# In[95]:


pc=df.surge_multiplier.value_counts()


# In[96]:


pc=df.surge_multiplier.value_counts()[1.25:]
pc


# In[97]:


plt.figure(figsize=(20,5))
sns.barplot(pc.index,pc.values)


# 10.Date bar graph

# In[98]:


pc=df.date.value_counts()


# In[99]:


pc=df.date.value_counts()
pc


# In[100]:


plt.figure(figsize=(20,5))
sns.barplot(pc.index,pc.values)


# 11.Extra money earned from surge

# In[101]:




df2=df[df["surge_multiplier"]>1.0]
df3=df2.price.sum()
df2.shape[0],df3
f=df3-(df3/df2.shape[0])
f


# 12.What is the date when surge was max

# In[102]:


df7 = df[(2018 in df.date) & (df.surge_multiplier==3.0)]
df7


# 13.Group by of destination and price max

# In[103]:


a=df.groupby("destination")["price"].max().sort_values(ascending=False)


# In[104]:


b=df.groupby("destination")["price"].sum().sort_values(ascending=False)


# In[105]:


print(type(a))
a


# In[ ]:




