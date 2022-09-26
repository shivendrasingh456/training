#Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.

import sys

def matching_parenthesis(strs):
    strs=strs.replace(' ','')
    strs_res,l1='',[]
    for char in strs:
        strs_res+=char
        if strs_res.count('(')==strs_res.count(')'):
            l1.append(strs_res)
            strs_res=''
    return l1

if __name__=="__main__":
    try:
        strs='( ()) ((()()())) (()) ()'
        print(f"res : {matching_parenthesis(strs)}")

    except Exception as e1:
        pass



