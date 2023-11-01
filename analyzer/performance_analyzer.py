import demos
from random import randint

def generate_random_list(size, max_val):
    
    rand_list = []
    for num in range(size):
        rand_list.append(randint(1, max_val))
    return rand_list


size = int(input("What is the size of the list you want to create "))
max_val = int(input("What is the max value of the range "))
print(generate_random_list(size, max_val))