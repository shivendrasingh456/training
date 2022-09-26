
# Write a Python program to find a valid substring of a given string 
# that contains matching brackets, at least one of which is nested.
import re

def is_Valid_string(strs):
    isValid=re.search(r"\[(\[\])+\]",strs).group()
    return isValid

if __name__=="__main__":
    try:
        strs="]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[["
        print(f"{is_Valid_string(strs)}")     
    except Exception as e1:
        raise e1
