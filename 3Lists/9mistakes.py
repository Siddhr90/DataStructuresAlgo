a = [1,2,3,4,5,6]
print(a[3:0:-1])

# expected output?
# [4,3,2,1] Wrong
# [4,3,2] Correct, last index is not considered!

'''
What will be the output of the following code block?

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
    for row in m:
        for element in row:
            if v < element: v = element
    return v

print(fun(data[0]))

'''
data[0] = [[1, 2], [3, 4]]