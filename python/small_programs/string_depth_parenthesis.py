#Finding the depth of parenthesis 


def parenthesis_depth(strs):
    return list(map(lambda x : len(x)//2,strs.split(' ')))
    

if __name__=="__main__":
        try:
            strs='(()) (()) () ((()()()))'
            print(f"string : {parenthesis_depth(strs)}")
        except Exception as e1:
            raise e1
