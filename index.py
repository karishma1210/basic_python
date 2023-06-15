a=int(input("enter a number"))
if a>1:
  for i in range(2,a):
    if(a % i) == 0:
      print(a,"the number is not a prime number")
      break
  else:
    print("the number is prime")  
else:
  print("the number is not prime")