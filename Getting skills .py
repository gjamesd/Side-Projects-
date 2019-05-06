#!/usr/bin/env python
# coding: utf-8

# In[2]:


## importing stuff 

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import random 
from random import sample
import numpy as np

from collections import Counter


# In[3]:


big_data = pd.read_csv("OrderBoard4_29.csv")


# In[4]:


big_data.head()


# In[5]:


smaller = pd.read_csv("smallerstilldirty.csv")


# In[6]:


smaller.head()


# In[7]:


print(smaller.columns)


# In[8]:


smaller.skills_pdl


# In[9]:


smaller.Seniority_james

seniority2 = []

for i in smaller.Seniority_james:
    if i == 1:
        seniority2.append(1)
    else:
        seniority2.append(0)

        
smaller["Seniority2"] = seniority2


# In[10]:


smaller.Modified_title_james.value_counts().plot(kind = "bar")


# In[11]:


print(smaller.Modified_title_james.value_counts())


# In[12]:


smaller.skills_pdl[0]


# In[13]:


mylist = smaller.skills_pdl
mylist


# In[14]:


len(mylist)

mylist[0]


# def unique(list1):
#     
#     #initialize a null list
#     
#    unique_list = []
#     
#     #traverse for all elements 
#     
#    for x in list1:
#        if x not in unique_list:
#        unique_list.append(x)
#    for x in unique_list:
#         print(x)
# 
#         
# unique(mylist)

# In[15]:


len(mylist)


# In[16]:


type(mylist)


# In[17]:


unique = []
for i in mylist:
    if i not in unique:
        unique.append(i)
        
unique
    


# In[18]:


len(unique)


# In[19]:


mydf = smaller[['skills_pdl', 'Modified_title_james']]

mydf


# In[20]:


bidf = mydf[mydf["Modified_title_james"]== "BI"]

Consultant = mydf[mydf["Modified_title_james"]== "Consultant"]
Software = mydf[mydf["Modified_title_james"]== "Software"]
Other = mydf[mydf["Modified_title_james"]== "Other"]
Engineer = mydf[mydf["Modified_title_james"]== "Engineer"]
GIS = mydf[mydf["Modified_title_james"]== "GIS"]
Developer = mydf[mydf["Modified_title_james"]== "Developer"]
Security = mydf[mydf["Modified_title_james"]== "Security"]
Data = mydf[mydf["Modified_title_james"]== "Data"]
IT = mydf[mydf["Modified_title_james"]== "IT"]
Analytics = mydf[mydf["Modified_title_james"]== "Analytics"]
Administrator = mydf[mydf["Modified_title_james"]== "Administrator"]
ML = mydf[mydf["Modified_title_james"]== "ML"]
Research = mydf[mydf["Modified_title_james"]== "Research"]
Advisory = mydf[mydf["Modified_title_james"]== "Advisory"]
AI = mydf[mydf["Modified_title_james"]== "AI"]
Systems = mydf[mydf["Modified_title_james"]== "Systems"]
IS = mydf[mydf["Modified_title_james"]== "IS"]
Cloud = mydf[mydf["Modified_title_james"]== "Cloud"]
transport = mydf[mydf["Modified_title_james"]== "transport"]
Student = mydf[mydf["Modified_title_james"]== "Student"]
Planner = mydf[mydf["Modified_title_james"]== "Planner"]
Applications = mydf[mydf["Modified_title_james"]== "Applications"]
Java = mydf[mydf["Modified_title_james"]== "Java"]
Archatect = mydf[mydf["Modified_title_james"]== "Archatect"]
QA = mydf[mydf["Modified_title_james"]== "QA"]


bidf


# In[21]:


def skills(dataframe):

    s = []
    for i in dataframe.skills_pdl:
        #print(i)
        s.append(i.split(","))
    merge = s[0]
    for j in range(1,len(s)):
        merge += s[j]


    for k in range(len(merge)):
        merge[k] = merge[k].strip()

    print(merge)

bidf.skills_pdl


# In[22]:


def skills(dataframe):

    s = []
    for i in dataframe.skills_pdl:
        #print(i)
        s.append(i.split(","))
    merge = s[0]
    for j in range(1,len(s)):
        merge += s[j]


    for k in range(len(merge)):
        merge[k] = merge[k].strip()

    #print(merge)
    
    skill_count = Counter(merge)
    
    return skill_count
    
print(skills(bidf))

bi = skills(bidf)


# In[23]:


type(skills(bidf))

count = list(skills(bidf).values())

lables = list(skills(bidf).keys())

top = skills(bidf).most_common(10)

#print(top)

myarray = np.array(top)

#print(myarray)

mydf = pd.DataFrame(myarray)

mydf = mydf.rename(columns = {0: 'Skill', 1:'Count'})

mydf


# In[24]:


mydf.Count


# In[28]:


x = mydf.Count
y = mydf.Skill

plt.bar(x,y)

plt.show()


# In[36]:


mydf.Skill

mydf.Count


# In[33]:


import matplotlib.pyplot as plt
import pandas as pd

data = mydf

plt.bar("Skill", "Count", data=data)

plt.show()


# In[31]:


#plotting 


data =  mydf


#plot = sns.barplot(data = data)
plot = sns.barplot(x = mydf.Count, data = mydf)

#plt.xlabel('Skill', fontsize=12)
#plt.ylabel('Count', fontsize=12)
#plt.title('Most relevant skills', fontsize=15)
#plt.xticks([0, 1,2,3,4,5,6,7,8,9,10],
#           ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
plt.show()


# In[741]:


ax = sns.barplot(x="Skill", y="Count", data=mydf)


# In[ ]:





# In[ ]:





# In[601]:


IS


# In[602]:


IS

IS = skills(IS)

IS


# In[603]:


consultant = skills(Consultant)
software = skills(Software)
other= skills(Other)
engineer = skills(Engineer)
gis = skills(GIS)
developer = skills(Developer)
security = skills(Security)
data = skills(Data)
#it = skills(IT)
analytics = skills(Analytics)
admin = skills(Administrator)
ml = skills(ML)
research = skills(Research)
advis = skills(Advisory)
ai = skills(AI)
cloud = skills(Cloud)
trans = skills(transport)
student = skills(Student)
#planner = skills(Planner)
#app = skills(Applications)
java = skills(Java)
#archatect = skills(Archatect)
#qa = skills(qa)


# In[605]:


bi = skills(bidf)
bi


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




