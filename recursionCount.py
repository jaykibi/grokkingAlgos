def recursiveCount(arr):
    if len(arr) == 1:
        return 1
    else: 
        return 1 + recursiveCount(arr[1:])

currArr = [2,4,6,1,1,1,1,1,1,10,90,899]
print(f"currArr currently has {len(currArr)} elements")
print(recursiveCount(currArr))