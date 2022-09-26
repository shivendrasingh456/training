#Sum of first N natural number

def sum_natural(x):
    if x==0: return 0
    else: return x +sum_natural(x-1)

if __name__=="__main__":
    try:
        N=7
        print(f"res : {sum_natural(N)}")
    except Exception as e1:
        pass
