integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

binary_dict = dict(zip(integer, binary))
print(binary_dict)


integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-x for x in integer]
print(additive_inverse)


integer = [1, -1, 2, -2, 3, -3]
sq_set = {x ** 2 for x in integer}
print(sq_set)
