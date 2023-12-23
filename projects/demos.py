# Generate a list of email
# 
import time
from random import choice
from string import ascii_lowercase as letters

def search_email(email, arr_email):
    start = 0
    stop = len(arr_email)-1
    while start <= stop:
        mid = (start + stop) // 2
        if email == arr_email[mid]:
            return mid, f"{arr_email[mid]} is found at index {mid}"
        elif email > arr_email[mid]:
            start = mid + 1
        else:
            stop = mid -1
    return None, f'{email} is not in the list'

# ************* GENERATE EMAIL ADDRESS ******************

def generate_name(name_length):
    return ''.join(choice(letters) for i in range(name_length))

def get_domain(domain_list):
    return choice(domain_list)

def generate_emails_list(name_length, domains_list, total_emails):
    emails = []
    for i in range(total_emails):
        emails.append(generate_name(name_length) + '@' + get_domain(domains_list))
    return emails

# *************** Runtime analysis function ****************

def analyze_func(func_name, *args):
    start_time = time.time()
    func_name(*args)
    stop_time = time.time()
    seconds = stop_time - start_time
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time : {seconds:.5f}")

