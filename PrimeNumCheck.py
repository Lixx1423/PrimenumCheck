
num = int(input("Give me a number you think is prime: "))

if num > 1:

   for i in range(2,num):
       if (num % i) == 0:
           print(num,"Is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"Is indeed a prime number")
       
else:
   print(num,"Will never be prime")