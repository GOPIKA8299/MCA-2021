#factorial of a number

n=int(input("enter the number:"))
fact=1
i=1
while i<=n:
 fact=fact*i
 i=i+1
print(n,'! is',fact)

