
# Returns the new required list 

def solve(arr):
    # multiplying all the elements in arr
    pro=1
    for i in arr:
        pro*=i
    
    #creating the new list where nlst[i]=pro/arr[i]
    nlst=[pro//i for i in arr]

    return nlst


# Driver program to test above function
A=[1, 2, 3, 4, 5]
print(solve(A))