def divide_arr(arr):
    if len(arr) < 2:
        print(f"Base case condition reached with: {arr[:]}")
        return arr[:]
    else:
        middle = len(arr)// 2 # divide the array into 2 part
        # print(f"Current list to work with: {arr}")
        # print(f"Left split: {arr[:middle]}")
        # print(f'Right split: {arr[middle:]}')
        l1 = divide_arr(arr[:middle]) # take the left part 
        l2 = divide_arr(arr[middle:]) # take the right part
    


# xxxxxxxxx Programe execution xxxxxxxxxxxxx

l = [1, 4, 6, 8, 10]
# l2 = [2, 3, 5, 7, 8, 9]
divide_arr(l)