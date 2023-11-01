import demos
from random import randint

def generate_random_list(size, max_val):
    
    rand_list = []
    for num in range(size):
        rand_list.append(randint(1, max_val))
    return rand_list


print(generate_random_list(10, 10))