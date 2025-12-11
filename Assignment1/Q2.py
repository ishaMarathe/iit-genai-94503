numbers=input("Enter numbers: ").split(",")
even=0
odd=0
for x in numbers:
    n=int(x)
    if n%2==0:
        even+=1
    else:
        odd+=1
print("Even:",even)
print("Odd:",odd)
