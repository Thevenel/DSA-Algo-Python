def binary_search_rec(n, arr, start, stop):
    if start > stop:
        return f"{n} not found in the list."
    else:
        mid = (start + stop)//2
        if n == arr[mid]:
            return f"{n} found at index {mid}"
        elif n > arr[mid]:
            return binary_search_rec(n, arr, mid+1, stop)
        else:
            return binary_search_rec(n, arr, start, mid-1)

def create_list(max_val):
    arr = []
    for num in range(max_val):
        arr.append(num)
    return arr

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#ind 0  1  2  3  4  5  6  7  8  9
num_to_search = 8
for num in  range(16):
    print(binary_search_rec(num, l, 0, len(l)-1))