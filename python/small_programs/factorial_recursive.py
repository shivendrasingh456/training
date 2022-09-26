#find factorial of a given Number N



def factorial(N):
    if N==1:return 1
    else: return factorial(N-1)*N

if __name__=="__main__":
    try:
        N=4
        print(f"start")
        print(f"factorial : {factorial(N)}")
    except Exception as e1:
        pass
