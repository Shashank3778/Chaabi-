fact = lambda num: 1 if num == 0 else num * fact(num - 1)

num = int(input("enter the number "))
res =fact(num)
print("The factorial of the given number =",res)


