#program to print all prime factors of a given number

#Time complexity :O(sqrt(n))
#Auxilory space : 0(n)

import math
def prime_factors(n):
    l1=[]

    #Testing for divisibility of 2 and diving recursively until it's not divided
    while n%2==0:
        l1.append(2)
        n=n/2

    #Testing for 3 and odd numbers upto square roots
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            l1.append(i)
            n=n/i

    if n>2:l1.append(int(n))
    return l1

if __name__=="__main__":
    try:
        inp=355
        print(f"res: {prime_factors(inp)}")
    except Exception as e1:
        raise e1
