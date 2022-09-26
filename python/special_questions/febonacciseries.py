
#find the febonacci series of first N numbers

def febonacci_series(N):
    if N==0: return 0
    elif N==1: return 1
    else: return febonacci_series(N-1)+ febonacci_series(N-2)

if __name__=="__main__":
    try:
        N=10
        print(f"start")
        print(f"output of febonacci series : {list(map(febonacci_series,range(N)))}")
    except Exception as e1:
        pass
