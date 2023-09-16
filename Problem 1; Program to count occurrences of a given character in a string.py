#!/usr/bin/env python
# coding: utf-8

# In[12]:


string= input('Enter string:')
character= input('Enter the character to be counted:')
count = 0

for char in string:
    if char == character:
        count += 1

print(character, 'appeared', count, 'times')

