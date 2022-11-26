a=0
b=1
fib=[0,1]
for i in range(0,50001):
    sum=a+b
    a=b
    b=sum
    fib.append(sum)
a=[]
while True:
    d=input("Enter input : ")
    if d=='':
        break
    else:
        a.append(int(d))
for i in range(len(a)):
    if a[i] in fib:
        print(a[i],"is in Fibonacci Series")
    else:
        print(a[i],"is not in Fibonacci Series")