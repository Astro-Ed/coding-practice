# -*- coding: utf-8 -*-
# code challenge from https://www.coderbyte.com/editor/guest:Questions%20Marks:Python3
"""
Created on Mon Sep 23 21:06:17 2019

@author: Astro.Ed
"""                

def QuestionsMarks(str):
    sum_digit = 0
    for x in str: # creating a loop to check each char in the string
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
            if sum_digit == 10:
                break     
    if "???" in str:
        print('True')
    else:
        print('False')
    return str
# keep this function call here  
QuestionsMarks(input()) 
