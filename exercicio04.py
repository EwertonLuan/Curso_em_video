n = input("Type something: ")
t = (type(n))

print('the value type it is of type\n{}'.format(t))
print('The value can be a num?\n',n.isnumeric())
print('The value can be a aplha?\n',n.isalpha())
print('The value can be a alphanum?\n',n.isalnum())

