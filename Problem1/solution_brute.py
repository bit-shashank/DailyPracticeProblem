
# Inputting a list of numbers
lst=[int(i) for i in input().split(" ")]

# Inputting the required number k
k=int(input())

#checking every pair in list to sum upto k

found=False
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==k:
            found=True
            break

if found:
    print("Pair Exists")

else:
    print("Pair does not Exists")