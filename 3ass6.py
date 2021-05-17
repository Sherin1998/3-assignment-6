#!/usr/bin/env python
# coding: utf-8

# In[20]:


#1
def fibinocci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibinocci(n-1)+fibinocci(n-2)

n = int(input('enter limit'))
for i in range(n+1):
    x=fibinocci(i)
    print(x)
 

    


# In[25]:


#2
def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input('enter no'))
print('Factorial is',factorial(n))



 


# In[22]:


#3
n = int(input('enter weight in Kg'))
m = int(input('enter height in meter'))
if(n<=1) or (m<=1):
    print('invalid')
else:
    x=m*m
    c=n/m
    print('BMI is {}'.format(c))


# In[26]:


#4
import math
n = int(input('enter no'))
math.log(n)


# In[24]:


#5
x=0
n = int(input('enter no'))
if(n>=1):
    for i in range(n+1):
        c=i*i*i
        x+=c
    print(x)
else:
    print('not natural no')
        

