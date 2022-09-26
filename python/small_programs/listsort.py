

#Write a Python program to find the following strange sort of list of numbers: the first element is the smallest, the second is the largest of the remaining, the third is the smallest of the remaining, the fourth is the smallest of the remaining, etc.



def strange_sort_list(l1):
        l1.sort()
        l2,condition=[],0
        for _ in range(len(l1)):   
            l2.append(l1.pop(condition))
            condition=-1 if not condition else 0
        return l2

if __name__=="__main__":
        try:
            l1=[27, 3, 8, 5, 1, 31]
            print(f"not -1 : {not -1}")
            print(f"list : {strange_sort_list(l1)}")

        except Exception as e1:
            raise e1

