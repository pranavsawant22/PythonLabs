def pair(n):
   a=b=1
   for a in range(1,n):
       for b in range(1,n):
           if a**2 +b**2 == n and a<=b:
               print (a,b)


pair(int(input("enter a number : ")))
