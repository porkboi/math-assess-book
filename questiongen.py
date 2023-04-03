# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:56:49 2023

@author: chris
"""

from random import randrange

def qn1a():
    rnd_int1=randrange(1,50)
    rnd_int2=randrange(1,25)
    rnd_int3=randrange(1,25)
    ans = rnd_int1+rnd_int2+rnd_int3
    text = str(rnd_int1) + " + " + str(rnd_int2) + " + " + str(rnd_int3) + "= ?    Ans: " + str(ans)
    return text

def qn1b():
    rnd_int1=randrange(1,100)
    rnd_int2=randrange(1,100)
    
    if (rnd_int1 > rnd_int2):
        ans = rnd_int1-rnd_int2
        text = str(rnd_int1) + " - " + str(rnd_int2) + "= ?    Ans: " + str(ans)
    else:
        ans = rnd_int2-rnd_int1
        text = str(rnd_int2) + " - " + str(rnd_int1) + "= ?    Ans: " + str(ans)
    return text

def qn2a():
    rnd_int1=randrange(10,100)
    rnd_int2=randrange(10,100)
    rnd_int3=randrange(10)
    sub1 = rnd_int1-rnd_int3
    sub2 = rnd_int2+rnd_int3
    text = "John had " + str(sub1) + " apples, and Mary had "+str(sub2) +" apples. If Mary gave "+ str(rnd_int3) + " to John,how many will John and Mary have in the end? Ans: John had " + str(rnd_int1) + ". Mary had " + str(rnd_int2) + "."
    return text

def qn3a():
    rnd_int1=randrange(1,10)
    rnd_int2=randrange(1,10)
    ans = rnd_int1*rnd_int2
    text = "There are " + str(rnd_int1) + " groups of children. Each group has " + str(rnd_int2) + " children. How many children are there?     Ans: " + str(ans)
    return text

def qn3b():
    rnd_int1=randrange(1,6)
    rnd_int2=randrange(1,5)
    ans = rnd_int1*rnd_int2
    text = "Mrs Tan has " + str(ans) + " sweets. If she splits them into bags of  " + str(rnd_int2) + " sweets, how many bags are there?     Ans: " + str(rnd_int1)
    return text

def qn4a():
    onedollarint = randrange(1,9)
    fiftycentint = randrange(1,9)
    twentycentint = randrange(1,9)
    tencentint = randrange(1,9)
    ans = onedollarint + 0.5*fiftycentint + 0.2*twentycentint + 0.1*tencentint
    ans = round(ans,3)
    text = "How much money is there below? Ans: $" + str(ans)
    return onedollarint, fiftycentint, twentycentint, tencentint, text