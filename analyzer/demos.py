print("Algorithms file load")

#Quick sort
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)
    
# Merge Sort
def merge_sort(arr1, arr2):
# print("Merge function with lists bellow:")
# print(f"left: {arr1} and right {arr2}")
    sorted_array = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        # print(f"Left list index i is {i} and has value {arr1[i]}")
        # print(f"Right list index j is {j} and has value {arr2[j]}")
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1
        # print(sorted_array)
    while i < len(arr1):
        sorted_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_array.append(arr2[j])
        j += 1
    return sorted_array
# the function to call
def mergesort(arr):
    if len(arr) < 2:
        # print(f"Base case condition reached with: {arr[:]}")
        return arr[:]
    else:
        middle = len(arr)// 2 # divide the array into 2 part
        l1 = mergesort(arr[:middle]) # take the left part 
        l2 = mergesort(arr[middle:]) # take the right part
        return merge_sort(l1, l2) # take l1 and l2 merge them into single sorted list

# Buble sort
def bubblesort(arr):
    swapped = True
    while swapped:
        swapped = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swapped = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
                
    

