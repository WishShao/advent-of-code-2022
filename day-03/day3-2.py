#!/usr/bin/env python
# coding: utf-8

# In[3]:


with open('input.txt' , 'r')as infile:
    parts = infile.read().strip().split()

total = 0
for i in range(0,len(parts),3):
    for ch in parts[i]:
        if ch in parts[i+1] and ch in parts[i+2]: break
    if ord(ch) >= 96:
        total += ord(ch) - 96
    else:
        total += ord(ch) -38
    
print(total)
        

