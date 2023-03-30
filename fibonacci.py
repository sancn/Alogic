
nterms = int(input("How many terms you want? "))
num1, num2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter greater than zero value")
elif nterms == 1:
   print(f"Fibonacci sequence upto{nterms}:")
   print(num1)
else:
   print("Fibonacci series is:")
   while count < nterms:
       print(num1)
       nth = num1 + num2
       num1 = num2
       num2 = nth
       count += 1