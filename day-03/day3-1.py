#!/usr/bin/env python
# coding: utf-8

# In[11]:


with open('input.txt' , 'r')as infile:
    lines = infile.read().strip().split()

total = 0
for line in lines:
    front,back = line[:len(line)//2], line[len(line)//2:]
    for ch in front:
        if ch in back: break
    if ord(ch) >= 96:
        total += ord(ch) - 96
    else:
        total += ord(ch) -38
print(total)
        

