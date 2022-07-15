def recursionSum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursionSum(arr[1:])

print(recursionSum([2,4,6]))