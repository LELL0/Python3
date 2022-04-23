x= int(input("enter first value: "))

y= int(input("enter second value: "))

z= int(input("enter third value: "))

def triangle(x,y,z):
    if(x<= y+z and y<=x+z and z<=x+y):
        return True
    else:
        return False

print(triangle(x,y,z))
