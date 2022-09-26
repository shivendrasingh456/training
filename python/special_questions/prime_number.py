#finding the prime number

import math

def prime_number(inp):
    check=2
    inp_sqrt=   math.sqrt(inp)
    while check< inp_sqrt:
        if inp%check==0:return True
        check+=1
    return False

if __name__=="__main__":
    try:
        inp=31
        print(f"is prime number: {prime_number(inp)}")
    except Exception as e1:
        raise e1
