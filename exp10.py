#right a program to find sum of array
def sum(arr): 
    #initalize a variable to store the sum while iterating the throgh later
    sum = 0 
    # iterate thought the array and add each element to the one at a time
    for i in arr:
        sum = sum+i

    return(sum)
arr = []
# input values of the list
arr = [12,56,33,98]
# calculatinf length of array
n = len(arr)
ans =sum(arr)
#display sum
print("sum of the array is" , ans)