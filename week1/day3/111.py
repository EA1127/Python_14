""" Множественное присвоение """

a, b, c = 'one', 'two', 'three'
print(a, b, c) # -> one two three


a, b, *c = 'one', 'two', 'three', 'four', 'five'
print(a, b, c)  # -> one two ['three', 'four', 'five']