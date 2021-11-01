def Hundreds(n):
    n/=100
    return int (n)

def Tens(n):
    n/=10
    n%=10
    return int (n)

def Ones(n):
    n%=10
    return int (n)

def Cube(n):
    n=n**3
    return int(n)

def IsArmstrong(n):
    if Cube(Hundreds(n))+Cube(Tens(n))+Cube(Ones(n))==n:
        return 1
    else: return 0

def PrintCalculation(n):
#    if IsArmstrong(n)==1:
#        v="="
#    else: v="#"
    v="="
    print(n,":",sep="")
    print("(",Ones(n),")","^",3,"+","(",Tens(n),")","^",3,"+","(",Hundreds(n),")","^",3,v,n,"\n",sep="")
    
def NbArmstrong():
    A=-1
    B=-1
    k=-1
    
    print("\n################################################################################\n")
    
    print("-enter two integers to check all Armstrong numbers between them.\n"
          "-enter the two values between 0 and 1000")
    
    print("\n################################################################################\n")
    
    while(A>1000 or A<0):
        try:
            A=int(input("-enter the first integer: "))
        except:
            print("\n!!! Enter An Integer !!!")
            
    while(B>1000 or B<0):
        try:
            B=int(input("-enter the second integer: "))
        except:
            print("\n!!! Enter An Integer !!!")
    if (B<A):
        A,B=B,A
        
    print("\n################################################################################")
    
    while(k!=1 and k!=2):
        try:
            k=int(input("\n-Option 1 for the detailled equation\n"
                    "-Option 2 for the Armstrong number Only!\n"
                    ">>Option: "))
        except:
            print("\n!!! Enter An Integer !!!")
            
    print("\n################################################################################\n")

    if k==1:
        for n in range(A,B+1):#check for Armstrong numbers from A to B including A and B
            if IsArmstrong(n)==1:
                PrintCalculation(n)
                
    flag=1                      #the flag is for the output so the list of Armstrong numbers dosn't start with ','
    if k==2:
        for n in range(A,B+1):#check for Armstrong numbers from A to B including A and B
            if IsArmstrong(n)==1:
                if (flag==0): print(", ",end='')
                print(n,end='')
                flag=0
            
    print("\n################################################################################\n")


NbArmstrong()
