#Write a Python program to find all n-digit integers that start or end with 2.

from collections import Counter
import time

def test(n):
    ans = []
    for i in range(10 ** (n - 1), 10 ** n):
        assert len(str(i)) == n
        if str(i).startswith("2") or str(i).endswith("2"):
            ans.append(i)
    return True


def starts_or_ends_with2(N):
    digit={'endswith2':(1,3,4,5,6,7,8,9),'startswith2':(0,1,3,4,5,6,7,8,9)}
    l1=[]
    if N==1:return [2]
    else:
        for _ in ['endswith2','startswith2']:
            for num in digit['endswith2']:
                number=num*pow(10,N-1)+2 if _=='endswith2' else 2*pow(10,N-1)+num
                for _ in range(pow(10,N-2)):
                    l1.append(number)
                    number=number+10
        special_condition=''.join('2' for _ in range(N))
        l1.append(special_condition)
        return l1

if __name__=="__main__":
    try:
        N=2
        print(f"1st program  {starts_or_ends_with2(N)}")
        print(f"2nd program: {test(N)}")
    except Exception as e1:
        raise e1



