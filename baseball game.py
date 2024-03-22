ops=[]
n=int(input("no of operation"))
while n>0:
    ops.append(input("enter op"))
    n=n-1
stack=[]
for item in ops:
    if item.isnumeric():
        
        stack.append(int(item))
    elif item=="c":
        stack.pop()
    elif item=="d":
        top=stack[-1]
        stack.append(2*top)
    elif item=="+":
        a=stack[-1]
        b=stack[-2]
        stack.append(a+b)
print(sum(stack))
            
