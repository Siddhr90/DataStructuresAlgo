init_tuple_a = 1, 2
init_tuple_b = (3, 4)

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

##
init_tuple = [(0, 1), (1, 2), (2, 3)]

result = sum(n for _, n in init_tuple)

print(result)
