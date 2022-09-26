# Write a Python program to find the vowels from each of the original texts 
# (y counts as a vowel at the end of the word) from a given list of strings.

import re

def vowel_string_func1(strs):
    strs=strs.lower()
    return ''.join(re.findall('[aeiou]+',strs) + re.findall('y$',strs))

def vowel_string_func2(strs):
    strs=strs.lower()
    dct={char : 0 for char in ("aeiou")}
    res="".join( char if char in dct.keys() else '' for char in strs)+('y' if strs[-1]=='y' else '')
    return res

if __name__=="__main__":
    try:
        lst=['aeiou', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
        print(f"{list(map(vowel_string_func2,lst))}")       
    except Exception as e1:
        raise e1
