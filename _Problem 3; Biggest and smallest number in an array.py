#!/usr/bin/env python
# coding: utf-8

# In[10]:


n = int(input('Enter the number of elements:'))
numbers = []

for i in range(n):
    num = float(input(f'Enter number {i+1}:'))
    numbers.append(num)

biggest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > biggest:
        biggest = num
    elif num < smallest:
        smallest = num

print('The biggest number is:', biggest)
print('The smallest number is:', smallest)

