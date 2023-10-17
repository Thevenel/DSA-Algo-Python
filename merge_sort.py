def merge_sort(arr1, arr2):
    print("Merge function with lists bellow:")
    print(f"left: {arr1} and right {arr2}")
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
        print(sorted_array)
    return sorted_array


# xxxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx

l1 = [1, 4, 6, 8, 10]
l2 = [2, 3, 5, 7, 8, 9]

print(f"Merged-list: {merge_sort(l1, l2)}")


# Steps
# 1. Compare first element in each list and append smaller element
# 2. Using two indices and an iterator to perform same comparison for 
#  for all elements in both lists
# 3. Move marker up by 1 position when the smaller number is found
# 4. Copy remaining lists once comparisons are completed and there 
# are items still remaining in one a the lists



