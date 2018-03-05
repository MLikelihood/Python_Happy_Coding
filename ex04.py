num = int(input("enter a number: "))
divisorList = [x for x in range(1,num+1,1) if num % x ==0]
print(divisorList)
