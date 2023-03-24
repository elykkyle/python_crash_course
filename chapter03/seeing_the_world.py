# Store locations in a list, make sure list is not in alphabetical order
places = ['london', 'paris', 'tokyo', 'new york', 'bergen', 'vienna']

# print list in original order
print(places)

# use sorted() to print list in alphabetical order w/o modifying original list
print(sorted(places))

# show list is still in original order by printing it
print(places)

# use sorted() to print list in reverse-alpha order w/o modifying original
print(sorted(places, reverse=True))

# show list is still in original order by printing it
print(places)

# use reverse() to change order of list. print list to show order has changed
places.reverse()
print(places)

# use reverse() to change order of list again. print list to show back in original order.
places.reverse()
print(places)

# use sort() to change list so it's stored in alphabetical order. print list to show it has been changed.
places.sort()
print(places)

# use sort() to change your list so it's stored in reverse-alphabetical order. print to show.
places.sort(reverse=True)
print(places)
