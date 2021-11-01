# complexity: O(n2) 

x=int(input("complexity: O(n2)\nenter a value: "))

for i in range(1,x+2):
    
    for k in range(i,x+1):
        print(" ",end="")
        
    for j in range(2,i*2):
        print("*",end="")
    print("\n")


for i in range(x+1,1,-1):
    
    for k in range(x-i+1,0,-1):
        print(" ",end="")
        
    for j in range(i*2,2,-1):
        print("*",end="")
    print("\n")


########################################
# complexity: O(n)

x=int(input("complexity: O(n)\nenter a value: "))

for i in range(0,x+1):
    print(" "*(x-i),end="")
    print("*"*(i*2),end="")
    print("\n")


for i in range(x,0,-1):
    print(" "*(x-i),end="")
    print("*"*(i*2),end="")
    print("\n")
