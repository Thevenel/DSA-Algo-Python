from demos import search_email, generate_emails_list, analyze_func

# List of domains to create email with
list_of_domains = ['thev.com', 'example.com', 'thevacademy.com', 'annouaprann.net', 'thevservices.com']

# Generate email
emails = generate_emails_list(10, list_of_domains, 1000000)

# Add the email to test in the email list
email = 'thev@example.com'
emails.append(email)

# Sort the email list to perform bineray search
sorted_emails = sorted(emails)

# Run the binary search over the emails to find the element
index, found = search_email(email, sorted_emails)

# Print search result
print(found)

# Print index returned by function on the list of sorted email
if index: print(f"element at index : {index}, is {sorted_emails[index]}")

# Analyze the functions runtime
analyze_func(search_email, email, sorted_emails)
analyze_func(generate_emails_list, 10, list_of_domains, 1000000 )

