#Write a Python program to get the single digits in numbers sorted backwards and converted to English words.

from collections import defaultdict
def single_digit_numbers(l1):
    l2=[]
    l1.sort(reverse=True)
    dict1=defaultdict(int,{
        1:'one',2:'two',3:'three',
        4:'four',5:'five',6:'six',
        7:'seven',8:'eight',9:'nine',
        0:'zero'
        })
    for digit in l1:
        if dict1[digit]:l2.append(dict1[digit])
    return l2

if __name__=="__main__":
        try:
            l1=[27, 3, 8, 5, 1, 31]
            print(f"list : {single_digit_numbers(l1)}")

        except Exception as e1:
            raise e1

