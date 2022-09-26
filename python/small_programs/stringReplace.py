#Write a Python program to find a string such that, when three or more spaces are compacted to a '-' and one or two spaces are replaced by underscores, leads to the target.

def string_modification(strs):
    return strs.replace('-',' '*3).replace('_',' ')


if __name__=="__main__":
        try:
            strs='Python-Exerci-se_s'
            print(f"string : {string_modification(strs)}")

        except Exception as e1:
            raise e1
