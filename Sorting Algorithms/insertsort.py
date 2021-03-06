def inSort(arr):
    '''Insertion Sort Algorithm'''
    '''Average Case: O(n^2)'''
    '''Best Case: Ω(n)''' #Occurs when data is already sorted (passes through array once)
    '''Worst Case: Θ(n^2)'''
    for i in range(1, len(arr)):
        toSwap = arr[i]
        index = i
        while arr[index-1] > toSwap and index != 0: #go back and shift elements forward by one until it finds the correct pos
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = toSwap
    return arr
A = [64, 25, 12, 22, 11] 
print(inSort(A))