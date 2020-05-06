

def Prime_numbers(m,n):

    for i in range(m,n+1):
        flag = False
        for j in range(2,i):
            if(i%j==0):
                flag = True
                break

        if(flag):
            continue
        else:
            print(i,end=" ")



m=int(input("Enter first number:"))
n=int(input("Enter second number:"))
if m > n:
    print("Invalid entry")
Prime_numbers(m,n)
