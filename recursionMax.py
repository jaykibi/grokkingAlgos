def recursiveMax(arr):
    if len(arr) == 1: 
        return arr[0]
    else: 
        return max(arr[0], recursiveMax(arr[1:]))

currArr = [2,4,6,1,1,1,1,1,1,10,90,899,788,512,123456789,256,128,1,1,0,6,9]
print("currArr currently has a max value of 123456789")
print(recursiveMax(currArr))
