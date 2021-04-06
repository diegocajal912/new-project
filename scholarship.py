#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("scholarship program 2021")

distance_university=int(input("Enter the distance to the university in km: "))
print(distance_university)

Number_of_brothers=int(input("Enter the number of siblings: "))
print(Number_of_brothers)

family_salary=int(input("Enter gross monthly family salary: "))
print(family_salary)

if distance_university > 40  and Number_of_brothers > 2 and family_salary <= 1000:
    print("has access to the scholarship")

else:
    print("does not have access to the scholarship")


# In[ ]:




