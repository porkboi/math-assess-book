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

def qn1c():
    rnd_int1=randrange(2,6)
    rnd_int2=randrange(1,3)
    common_point=rnd_int1*rnd_int2*5
    s = ""
    counter = 0
    while counter in range(rnd_int1):
        t = str(str(rnd_int2*5) + " + ")
        s = s + t
        counter += 1
    lhs = s[:-3]
    rhs = " = ____ + " + str(rnd_int2*5)
    text = "Fill in the blank: \n" + lhs + rhs + "    Ans: " + str(rnd_int1)
    return text

def qn1d():
    rnd_int1=randrange(11,100)
    lst = []
    for i in str(rnd_int1):
        lst.append(i)
    a = int(lst[0])
    b = int(lst[1])
    
    if b != 0 and a % b == 0 and a != b:
        c = a/b
        c = int(c)
        d = randrange(1,a+1)
        e = a - d
        text = "Ahmad is thinking of a 2 digit number.\nThe number in the tens place is " + str(e) + " more than " + str(d) + ".\nThe number in the ones place is the digit in the tens place divided by "+ str(c) +".\nWhat is the number?       Ans: " + str(rnd_int1)
    elif b != 0 and b % a == 0 and a != b:
        c = b/a
        c = int(c)
        d = randrange(1,a+1)
        e = a - d
        text = "Ahmad is thinking of a 2 digit number.\nThe number in the tens place is " + str(e) + " more than " + str(d) + ".\nThe number in the ones place is the digit in the tens place multiplied by "+ str(c) +".\nWhat is the number?       Ans: " + str(rnd_int1)
    elif a > b:
        c = a - b
        d = randrange(0,b+1)
        e = b - d
        text = "Ahmad is thinking of a 2 digit number.\nThe number in the ones place is " + str(e) + " more than " + str(d) + ".\nThe number in the tens place is "+ str(c) +" more than the digit in the ones place.\nWhat is the number?       Ans: " + str(rnd_int1)
    elif b > a:
        c = b - a
        d = randrange(0,b+1)
        e = b - d
        text = "Ahmad is thinking of a 2 digit number.\nThe number in the ones place is " + str(e) + " more than " + str(d) + ".\nThe number in the tens place is "+ str(c) +" less than the digit in the ones place.\nWhat is the number?       Ans: " + str(rnd_int1)
    elif a == b:
        c = randrange(1,a+1)
        d = a - c
        text = "Ahmad is thinking of a 2 digit number.\nThe number in the ones place and the tens place are the same.\nThey are " + str(d) + " more than " + str(c) + "\nWhat is the number?       Ans: " + str(rnd_int1)
    return text
    

def qn2a():
    rnd_int1=randrange(10,100)
    rnd_int2=randrange(10,100)
    rnd_int3=randrange(10)
    sub1 = rnd_int1-rnd_int3
    sub2 = rnd_int2+rnd_int3
    text = "John had " + str(sub1) + " apples, and Mary had "+str(sub2) +" apples.\nIf Mary gave "+ str(rnd_int3) + " to John,\nhow many will John and Mary have in the end? \nAns: John had " + str(rnd_int1) + ". Mary had " + str(rnd_int2) + "."
    return text

def qn2b():
    rnd_int1=randrange(0,31)
    rnd_int2=randrange(0,71)
    sub1 = rnd_int2+rnd_int1
    text = f"Charlie obtained {rnd_int1} birds.\nIf he had {rnd_int2} birds at first,\nhow many birds did he have in the end?     Ans: {sub1} birds"
    return text

def qn3a():
    rnd_int1=randrange(1,10)
    rnd_int2=randrange(1,10)
    ans = rnd_int1*rnd_int2
    text = "There are " + str(rnd_int1) + " groups of children. \nEach group has " + str(rnd_int2) + " children. \nHow many children are there?     Ans: " + str(ans)
    return text

def qn3b():
    rnd_int1=randrange(1,6)
    rnd_int2=randrange(1,5)
    ans = rnd_int1*rnd_int2
    text = "Mrs Tan has " + str(ans) + " sweets. \nIf she splits them into bags of  " + str(rnd_int2) + " sweets, \nhow many bags are there?     Ans: " + str(rnd_int1)
    return text

def qn4a():
    onedollarint = randrange(1,9)
    fiftycentint = randrange(1,9)
    twentycentint = randrange(1,9)
    tencentint = randrange(1,9)
    ans = onedollarint + 0.5*fiftycentint + 0.2*twentycentint + 0.1*tencentint
    ans = round(ans,3)
    text = "How much money is there below?     Ans: $" + str(ans)
    return onedollarint, fiftycentint, twentycentint, tencentint, text

def qn4b():
    twentycentint = randrange(1,9)
    tencentint = randrange(1,9)
    ans = 0.2*twentycentint + 0.1*tencentint
    ans = round(ans,3)
    text = "How much money is there below?     Ans: $" + str(ans)
    return twentycentint, tencentint, text

def qn4c():
    rnd_int1 = randrange(1,99)
    rnd_int2 = randrange(2,100)
    if (rnd_int1 > rnd_int2):
        ans = rnd_int1-rnd_int2
        text = "Charlie bought a bird. \nHe gave the cashier $" + str(rnd_int1) + ".\nHe got back $" + str(rnd_int2) + ".\nHow much was the bird?    Ans: $" + str(ans)
    else:
        ans = rnd_int2-rnd_int1
        text = "Charlie bought a bird. \nHe gave the cashier $" + str(rnd_int2) + ".\nHe got back $" + str(rnd_int1) + ".\nHow much was the bird?    Ans: $" + str(ans)
    return text

def qn4d():
    rnd_int1=randrange(0,31)
    rnd_int2=randrange(0,71)
    sub1 = rnd_int2+rnd_int1
    text = f"Charlie spent ${rnd_int1} on a bird.\nIf he received ${rnd_int2} as change,\nhow much money did he have at first?     Ans: ${sub1}"
    return text

def printWords(h, m): 

    nums = ["zero", "one", "two", "three", "four", 
        "five", "six", "seven", "eight", "nine", 
        "ten", "eleven", "twelve", "thirteen", 
        "fourteen", "fifteen", "sixteen",  
        "seventeen", "eighteen", "nineteen",  
        "twenty", "twenty one", "twenty two",  
        "twenty three", "twenty four",  
        "twenty five", "twenty six", "twenty seven", 
        "twenty eight", "twenty nine"]
    
    if (m == 0): 
        ans = f"{nums[h]} o' clock"
    elif (m == 1): 
        ans = f"one minute past {nums[h]}"
    elif (m == 59): 
        ans = f"one minute to {nums[h+1]}" 
    elif (m == 15): 
        ans = f"quarter past {nums[h]}"
    elif (m == 30): 
        ans = f"half past {nums[h]}"
    elif (m == 45): 
        ans = f"quarter to {nums[h+1]}"
    elif (m <= 30): 
        ans = f"{nums[m]} minutes past {nums[h]}"
    elif (m > 30): 
        ans = f"{nums[60-m]} minutes to {nums[h+1]}" 
    return ans

def qn5a():
    rnd_int1 = randrange(0,13)
    rnd_int2 = randrange(-1,60)
    ans = "What is the time shown below?\nAns: " + str(printWords(rnd_int1, rnd_int2))
    return rnd_int1, rnd_int2, ans