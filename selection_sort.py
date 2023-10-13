def selection_sort(arr):
    marker = 0
    while marker < len(arr):
        print(f"Selection sort status : {str(arr)}")
        for num in range(marker, len(arr)):
            if arr[num] < arr[marker]:        
                arr[marker], arr[num] = arr[num], arr[marker]
        marker += 1
        


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)