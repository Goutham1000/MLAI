#!/usr/bin/env python
# coding: utf-8

# # Python problem solving

# In[2]:


set_1={2,5,7,88,99,33,67}
set_2={55,5,88,44,64,89,3}
if set_1.intersection(set_2):
    print(set_1&set_2)
else:
    print(set_1.union(set_2))


# In[3]:


D={'john' :[25,32,43],'peter':[87,55,96],'ram':[58,55,43],'meena':[63,79,85]}
n =input('Enter the name to be updated')
if n in D:
   D[n]=[88,77,99]
   print(D)
else:
    print('Name not Found')


# In[ ]:




