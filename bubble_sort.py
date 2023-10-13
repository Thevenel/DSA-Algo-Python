def bubble_sort(arr):
    swapped = True
    while swapped:
        print(f"Bubble sort status : {str(arr)}")
        swapped = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swapped = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
                
    

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)
