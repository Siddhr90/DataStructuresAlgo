# Strings and Lists

a = 'spam'
b = list(a)
print(b)
# ['s', 'p', 'a', 'm']

a = 'spam spam spam'
b = a.split()
print(b)
# ['spam', 'spam', 'spam']
print(b[1])
# spam

a = 'spam1-spam2-spam3'
delimiter = '-'
b = a.split(delimiter)
print(b)
#['spam1', 'spam2', 'spam3']

delimiter = 'a'
b = a.split(delimiter)
print(b)
#['sp', 'm1-sp', 'm2-sp', 'm3']
print(delimiter.join(b))





