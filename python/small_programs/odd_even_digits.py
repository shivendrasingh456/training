
#Write a Python program to find an integer (n >= 0) with the given number of even and odd digits.

def odd_even_digits(even,odd):
    # return "".join('2' for _ in range(even)) + "".join("3" for _ in range(odd))
    return "2"*even+"3"*odd
    
if __name__=="__main__":
    try:
        even=4
        odd=7
        print(f"{odd_even_digits(even,odd)}")     
    except Exception as e1:
        raise e1
