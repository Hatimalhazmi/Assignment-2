#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Problem 1:
# Wrtie a python program to check if the numbers "3.5" is positive or negative or zero.


# In[5]:


num = 3.5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[7]:


# Problem 2:
# Wrtie a python program displays the multiplication table of variable nummber (from 1 to 10).
# Input Number = 11.


# In[9]:


num = 11

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# In[ ]:




