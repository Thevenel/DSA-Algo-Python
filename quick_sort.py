def quick_sort(arr):
    """
    Input: Unsorted list of integers 
    Returns sorted list of integers using Quicksort
    Note: This is not an in-place implementation.
    """
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
        # We can call quicsort on the smaller and larger list
        # and add it to the equal list and we'll get the sorted list
        return quick_sort(smaller) + equal + quick_sort(larger) #return a list by change , to +

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(quick_sort(l))