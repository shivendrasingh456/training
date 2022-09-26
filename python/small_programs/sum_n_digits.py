
#finding the sum of N digits

def digit_sum(x):
    if x==0: return 0
    else: return x%10 +digit_sum(x//10)

if __name__=="__main__":
    try:
        N=1234567
        print(f"res : {digit_sum(N)}")
    except Exception as e1:
        pass
