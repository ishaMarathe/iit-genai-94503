# Q3:
# Given a CSV file Products.csv with columns:
# Write a Python program to:

# a) Read the CSV

# b) Print each row in a clean format

# c) Total number of rows

# d) Total number of products priced above 500
# e) Average price of all products
# f) List all products belonging to a specific category (user input)
# g) Total quantity of all items in stock

import csv

with open("Products.csv") as f:
    data=list(csv.reader(f))
header=data[0]
rows=data[1:]

for r in rows:
    print(r)
print("Total rows:",len(rows))

count=0
total=0
for r in rows:
    price=float(r[3])
    total+=price
    if price>500:
        count+=1
avg=total/len(rows)
print("Products above 500:",count)
print("Average price:",avg)

cat=input("Enter category:")
for r in rows:
    if r[2].lower()==cat.lower():
        print(r[1])

qty=sum(int(r[4]) for r in rows)
print("Total quantity:",qty)
