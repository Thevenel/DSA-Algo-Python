def binary_search_iter(n, arr):
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        mid = (start + stop)//2
        if arr[mid] == n:
            return f"{n} is found at index {mid}"
        elif arr[mid] > n:
            stop = mid - 1
        else:
            start = mid + 1

    return f"{n} not found in the list"

def create_list(max_val):
    arr = []
    for num in range(max_val):
        arr.append(num)
    return arr



l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#ind 0  1  2  3  4  5  6  7  8  9

num_to_search = 11
print(binary_search_iter(num_to_search, l))