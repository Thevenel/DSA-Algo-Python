records = [ ('mashrur@example.com', 'hello world'),
            ('sultan@example.com', 'how are you?'),
            ('mohammad@example.com', "I'm fine, thanks."),
            ]

for index, record in enumerate(records):
    key, value = record
    if key == 'sultan@example.com':
        break
    # print(index, key, value)

print(records[index])