# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:09:14 2019

@author: Arsalan Ashraf
"""


import numpy as np
import pandas as pd
import math
types = {"Refund": str,"Marital_Status": str,"Taxable_Income": float,"Evade":str}
names = ["Refund","Marital_Status","Taxable_income","Evade"]
dataset = pd.read_csv("E:\Laptop Stuff 2020\DS\XYZ\Data Science Assignments\Labs\Lab_6\\datafile.csv", dtype=types)
print(dataset)
def prob_2(s_col,s_flag,s_class):
    prob_arr = np.where((dataset[s_col] == s_flag) & (dataset[s_class] == 'Yes'))
    result = dataset[s_class].value_counts()
    p1 = len(prob_arr[0])/result[0]
    prob_arr = np.where((dataset[s_col] == s_flag) & (dataset[s_class] == 'No'))
    p2 = len(prob_arr[0])/(result[1])
    p = [p1,p2]
    return p           
def prob_con(s_col,dp,s_class):
    list1 = dataset[s_col]
    
    prob_arr = np.where((dataset[s_class] == 'Yes'))
    var= np.var(list1[prob_arr[0].tolist()],ddof=1)
    m = np.mean(list1[prob_arr[0].tolist()])
    p1 = ((1/math.sqrt(2*math.pi*var)) * math.exp(-(float(dp)-float(m))**2/(2*var)))
    
    prob_arr = np.where((dataset[s_class] == 'No'))
    var= np.var(list1[prob_arr[0].tolist()],ddof=1)
    print(var)
    m = np.mean(list1[prob_arr[0].tolist()])
    p2 = ((1/math.sqrt(2*math.pi*var)) * math.exp(-(float(dp)-float(m))**2/(2*var)))
    
    p = [p1,p2]
    return p
def naiveB(l1,s_class):
    p = []
    p_yes = 1
    p_no = 1
    for x,y in l1:
        if type(y) != float:
          p.append(prob_2(x,y,s_class))
        else:
          p.append(prob_con(x,y,s_class))   
    for x,y in p:
        
        p_yes = p_yes * x
        p_no = p_no * y
   
    if(p_yes>p_no):
        print("This data point has Evade = Yes with a probablity of ",p_yes)
    else:
        print("This data point has Evade = No with a probablity of ",p_no)
     

l1 = [("Refund", "Yes"), ("Marital_Status", "Married"),("Taxable_Income", 120.0)]
naiveB(l1,"Evade")  


