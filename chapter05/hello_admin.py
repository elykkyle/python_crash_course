users = ['admin', 'mark', 'paul', 'john', 'ringo']

for user in users:
    if user == 'admin':
        print(
            f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, welcome back.')
