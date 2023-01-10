#!/usr/bin/env python
# coding: utf-8

# In[2]:


count = 10  
transactions = 0
while count >= 0:
    
    num = int(input("\nEnter the amount: "))
    
    if num > 5 and num < count:
        count -= 0 
        print("\nSorry ! You can only buy 5 at a time. We have", count, "ticket." "How many do you want to buy?")
        transactions += 0
        
    if num <= 5 and num < count:
        count -= num      
        print("\nWe have", count,"tickets. How many do you want to buy? ")
        transactions +=1
        continue
    if count - num == 0:
        count -= num
        print("\nWe gave you the maximum we could") 
        print("\nWe have", count , "tickets left. Good bye !")
        transactions +=1
        break
    
print("\nYou had",transactions, "transactions.")   
            


# In[ ]:





# In[ ]:




