current_users = ['admin', 'Mark', 'PAUL', 'john', 'ringo']

new_users = ['george', 'mark', 'britney', 'christine', 'christopher', 'darryl']

lower_current_users = []
for user in current_users:
    lower_current_users.append(user.lower())

print(lower_current_users)

for user in new_users:
    if user.lower() in lower_current_users:
        print(f'{user} is not available. Please choose a new username')
    else:
        print(f'{user} is available!')
