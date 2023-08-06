   #!/bin/bash
   # This script calculates simple interest given principal,
   # annual rate of interest and time period in years.

   # Do not use this in production. Sample purpose only.

   # Author: Upkar Lidder (IBM)
   # Additional Authors:
   # <your GitHub username>

   # Input:
   # p, the principal amount
   # t, time period in years
   # r, annual rate of interest

   # Output:
   # simple interest = p*t*r

p = int(input("Enter the value of principal"))
r = int(input("Enter the value of rate of return"))
t = int(input("Enter the value of time"))

print("The simple interest for the {0} years".format(t))
print("SI = {0}".format(p*r*t/100))
