
#For each triple of eaten, need, stock write a Python 
# program to get a pair of total appetite and remaining.

def appetite_and_remaining(l1):
    return [l1[0]+l1[1],l1[2]-l1[1]] if l1[2]>l1[1] else [l1[0]+l1[2],0]

if __name__=="__main__":
    try:
        inp=[[2, 5, 6], [3, 9, 22]]
        print(f"res: {list(map(appetite_and_remaining,inp))}")
    except Exception as e1:
        raise e1
