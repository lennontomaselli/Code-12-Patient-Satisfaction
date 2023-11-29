#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Checking working directory
import os
import pandas as pd

current_directory = os.getcwd()
print(current_directory)


# In[2]:


# Change working directory
new_directory_path = r'/Users/lennontomaselli'
os.chdir(new_directory_path)


# In[5]:


updated_dir = os.getcwd()
print(updated_dir)


# In[6]:


file_path = "Week14Assignment.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except filenotFoundError:
        print(f"file '{file_path}' not found.")
except IOError:
        print("An error occurred while reading this file.")


# In[17]:


# Number of patients readmitted
df = pd.read_csv(file_path)
Readmission = (df[' Readmission'] == 1).sum()

print(f"The number of readmission patients is {Readmission}.")


# In[19]:


# Staff satisfaction
df = pd.read_csv(file_path)
StaffSatisfaction = (df[' StaffSatisfaction']).mean()

print(f" The Staff satisfaction is {StaffSatisfaction}")


# In[32]:


# Overall satisfaction
df['OverallSatisfaction'] = df[[' StaffSatisfaction', ' CleanlinessSatisfaction',
                          ' FoodSatisfaction', ' ComfortSatisfaction',
                          ' CommunicationSatisfaction']].mean(axis = 1)



# In[40]:


# Logistic Regression

import sklearn.linear_model

X = df['OverallSatisfaction'].values.reshape(-1,1)
Y = df[' Readmission']

log_reg = sklearn.linear_model.LogisticRegression().fit(X, Y)



# In[41]:


# Correlation coefficient 

correlation_coefficient = log_reg.coef_[0][0]


# In[47]:


# Plot CC

import matplotlib.pyplot as plt

plt.plot(X, log_reg.predict(X), label = "Regression Line", color= "pink")
plt.scatter(df['OverallSatisfaction'], df[' Readmission'], color= "green")
plt.show()


# In[ ]:




