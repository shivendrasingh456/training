#Write a Python program to find the closest palindrome from a given string.
def palindrome(strs):
    len_str=len(strs)//2
    strs="".join(strs[i] if i<len_str else strs[~i] for i in range(len(strs)))
    return strs

if __name__=="__main__":
    try:
        strs='cabcvvghjj'
        print(f"test : {palindrome(strs)}")
    except Exception as e1:
        pass



