import time
from demos import quick_sort, mergesort
from random import randint

def generate_random_list(size, max_val):
    
    rand_list = []
    for num in range(size):
        rand_list.append(randint(1, max_val))
    return rand_list

def analyze_func(func_name, arr):
    start_time = time.time()
    func_name(arr)
    end_time = time.time()
    seconds = end_time - start_time
    print(f"{func_name} -> Runtime : {seconds}")

size = int(input("What is the size of the list you want to create "))
max_val = int(input("What is the max value of the range "))

# print(generate_random_list(size, max_val))

l = generate_random_list(size, max_val)

analyze_func(quick_sort, l)
analyze_func(mergesort, l)


