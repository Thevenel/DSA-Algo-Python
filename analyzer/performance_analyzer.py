import time
from demos import quicksort, mergesort, bubblesort
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
    print(f"{func_name.__name__.capitalize()}\t-> Runtime : {seconds}")

size = int(input("What is the size of the list you want to create? "))
max_val = int(input("What is the max value of the range? "))
run_times = int(input("How many times you want it to run? "))

for num in range(run_times):
    print(f"Run: {num+1}")
    l = generate_random_list(size, max_val)
    # Because bubble sort makes in-place sort, we'll call it
    # with a copy to not modify our original list
    analyze_func(bubblesort, l.copy())
    analyze_func(quicksort, l)
    analyze_func(mergesort, l)
    print("-" * 40)

# print(generate_random_list(size, max_val))



