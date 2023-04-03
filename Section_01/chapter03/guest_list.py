guests = ['Albert Einstein', 'Ada Lovelace', 'Desmond Tutu']

print(f"{guests[0]}, please join me for dinner.")
print(f"{guests[1]}, please join me for dinner.")
print(f"{guests[2]}, please join me for dinner.")

print(f"there are {len(guests)} guests invited to dinner.")

print(f"{guests[0]} is unable to attend.")

guests[0] = 'Robert Oppenheimer'

print(f"{guests[0]}, please join me for dinner.")
print(f"{guests[1]}, please join me for dinner.")
print(f"{guests[2]}, please join me for dinner.")

print(f"there are {len(guests)} guests invited to dinner.")


print('I found a bigger table!')

guests.insert(0, 'Barack Obama')
guests.insert(2, 'Dolly Parton')
guests.append('Tim Cook')

print(f"{guests[0]}, please join me for dinner.")
print(f"{guests[1]}, please join me for dinner.")
print(f"{guests[2]}, please join me for dinner.")
print(f"{guests[3]}, please join me for dinner.")
print(f"{guests[4]}, please join me for dinner.")
print(f"{guests[5]}, please join me for dinner.")

print(f"there are {len(guests)} guests invited to dinner.")


print('I can only invite two people for dinner.')

uninvited = guests.pop()
print(f"Sorry, {uninvited}, I'm not able to invite you to dinner.")
uninvited = guests.pop()
print(f"Sorry, {uninvited}, I'm not able to invite you to dinner.")
uninvited = guests.pop()
print(f"Sorry, {uninvited}, I'm not able to invite you to dinner.")
uninvited = guests.pop()
print(f"Sorry, {uninvited}, I'm not able to invite you to dinner.")

print(f"there are {len(guests)} guests invited to dinner.")

del guests[0]
del guests[0]

print(f"there are {len(guests)} guests invited to dinner.")


print(guests)
