x1=int(input("enter the x1: "))
y2=int(input("enter the y1: "))
x2=int(input("enter the x2: "))
y2=int(input("enter the y2: "))
x3=int(input("enter the x3: "))
y3=int(input("enter the y3: "))

area=1/2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
print("(x1,y1)=",x1,y1)
print("(x2,y2)=",x2,y2)
print("(x3,y3)=",x3,y3)
print("area=",area)