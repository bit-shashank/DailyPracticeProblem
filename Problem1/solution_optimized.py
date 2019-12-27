
#Tutorial on:- https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

# Inputting a list of numbers
lst=[int(i) for i in input().split(" ")]

# Inputting the required number k
k=int(input())

#creating an empty hash set
s=set()

found=False
for i in range(len(lst)):
    temp=k-lst[i]
    if temp in s:
        found=True
        break
    s.add(lst[i])
    
if found:
    print("Pair Exists")

else:
    print("Pair does not Exists")