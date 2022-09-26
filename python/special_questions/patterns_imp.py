#Patterns problems


#     *
#   * *
# * * *  
#   * *
#     *

N=3
for i in range(2*N-1):
    if N>i:var=i
    else:var-=1
    for _ in range(N-var-1):print(" ",end=" ")
    for _ in range(var+1):print("*",end=" ")
    print()



#     1
#   2 1 2
#  3 2 1 2 3   
# 4 3 2 1 2 3 4
#5 4 3 2 1 2 3 4 5

N=5
for i in range(N):
    for _ in range(N-i-1):print(" ",end="")
    for _ in range(i+1,0,-1): print(_,end=" ")
    for _ in range(2,i+2): print(_,end=" ")
    print()




#   *
#  * * 
# * * * 
#* * * * 
# * * *
#  * *
#   *

N=4
for i in range(2*N-1):
    if N>i:var=i
    else:var-=1
    for _ in range(N-var-1): print("",end=" ")
    for _ in range(var+1):print("*",end=" ")
    print()


#*
#**
#***
#**
#*

N=3
for i in range(2*N-1):
    if N-1>=i:var=i+1
    else:var-=1
    for _ in range(var): print("*",end=" ")
    print()



#1
#12
#123
#1234
#12345

# lopping in normal order
N=5
for i in range(N):
    for _ in range(i+1): print(_+1,end=" ")
    print()




#4 3 2 1 
#3 2 1 
#2 1 
#1

# looping in reverse order
N=4
for i in reversed(range(N)):
    for _ in reversed(range(i+1)):print(_+1,end=" ")
    print()





