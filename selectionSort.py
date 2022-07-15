def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr



print(selectionSort([2,4,6,1,1,1,1,1,1,10,90,899]))

# this algo sorts an array in O(n^2) time
# technically sorts it in O(n * 1/2 * n) but we drop the constant (1/2)