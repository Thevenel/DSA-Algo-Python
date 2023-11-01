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

def mergesort(arr):
    if len(arr) < 2:
        # print(f"Base case condition reached with: {arr[:]}")
        return arr[:]
    else:
        middle = len(arr)// 2 # divide the array into 2 part
        l1 = mergesort(arr[:middle]) # take the left part 
        l2 = mergesort(arr[middle:]) # take the right part
        return merge_sort(l1, l2) # take l1 and l2 merge them into single sorted list
# xxxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx

l = [10, 9, 2, 7, 1, 4, 6, 3, 8, 10]
print(mergesort(l))



# Steps
# 1. Compare first element in each list and append smaller element
# 2. Using two indices and an iterator to perform same comparison for 
#  for all elements in both lists
# 3. Move marker up by 1 position when the smaller number is found
# 4. Copy remaining lists once comparisons are completed and there 
# are items still remaining in one a the lists



