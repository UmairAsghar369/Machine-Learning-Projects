isprime = True
i=2
n=int(input("Enter a number"))
while i<n:
    remainder=n%i
    if remainder ==0:
        isprime=False
        break
    else:
        i=i+1

if isprime:
    print("NUmber is prime")
else:
    print("Number is not prime")