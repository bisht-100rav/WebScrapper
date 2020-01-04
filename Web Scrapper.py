#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client


# In[2]:


my_url = 'http://punjabiuniversity.ac.in/Pages/Department.aspx?dsenc=3'


# In[3]:


my_url


# In[4]:


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


# In[5]:


page_soup = soup(page_html, "html.parser")


# In[6]:


page_soup.p


# In[7]:


#grabs all the required teachers item
teachers = page_soup.findAll("div", {"class" : "col-md-6 col-sm-6 text-center"})
            


# In[9]:


teach = teachers[0]


# In[10]:


teachers[0]


# In[82]:


#teacher_name = teach.h5.text.replace("\r\n","").replace(" ","")
#teacher_email = teach.a['href'].replace('mailto:','').replace('?Subject=Hello','') 
#teacher_designation = teach.h6.text.replace(', ','').replace('  ','')

emails_bas


# In[78]:


names_bas = []
designation_bas = []
emails_bas = []


# In[79]:


for teach in teachers:
    teacher_name = teach.h5.text.replace("\r\n","").replace(" ","")
    teacher_designation = teach.h6.text.replace(', ','').replace('  ','')
    teacher_email = teach.a['href'].replace('mailto:','').replace('?Subject=Hello','')
    names_bas.append(teacher_name)
    designation_bas.append(teacher_designation)
    emails_bas.append(teacher_email)


# In[83]:


import pandas as pd
from pandas import DataFrame


# In[85]:


teachers_list_bas = {'Name': names_bas,
                     'Designation': designation_bas,
                     'Email': emails_bas}


# In[ ]:





# In[86]:


df = DataFrame(teachers_list_bas, columns = ['Name','Designation','Email'])


# In[87]:


df.to_csv('C:/Users/Acer/Desktop/New folder/teacher_database/Bas_Teachers_data.csv')


# In[ ]:




