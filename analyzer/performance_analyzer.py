import time
from demos import quick_sort, mergesort
from random import randint

def generate_random_list(size, max_val):
    
    rand_list = []
    for num in range(size):
        rand_list.append(randint(1, max_val))
    return rand_list


size = int(input("What is the size of the list you want to create "))
max_val = int(input("What is the max value of the range "))

# print(generate_random_list(size, max_val))

l = generate_random_list(size, max_val)
start_time = time.time()
quick_sort(l)
end_time = time.time()
print(f"QS Elapse time : {end_time - start_time}")

start_time = time.time()
mergesort(l)
end_time = time.time()
print(f"MS Elapse time : {end_time - start_time}")
