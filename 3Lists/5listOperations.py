a = [0, 1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7]

c = a+b

print(c)

d = [1, 0]
d = d * 4
print(d)

# Count elements #helps eliminate a loop to count
print(len(a))

# max min
print(max(a))
print(min(a))

# sum
print(sum(a))

# to print avg
print(sum(a)/len(a))


'''
# Q. Convert the following piece of code using 'list functions' to make it more efficient

total = 0
count = 0
while True:
    inp = input('Enter a number : ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total/count

print('Average: ', average)

'''
inputList = []
while True:
    inp = input('Enter a number:')
    if inp == 'done':
        break
    inputList.append(float(inp))
print('average: ', sum(inputList)/len(inputList))

