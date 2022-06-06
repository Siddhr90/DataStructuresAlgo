#Write a recursive function to capitalize first letter of each string of Array
# capitalizeF(['car','jeep','truck'] = ['Car','Jeep','Truck']


def capitalizeF(arr):
    if len(arr) == 0:
        return arr
    else:
        return [arr[0][0].upper()+arr[0][1:]] + capitalizeF(arr[1:])

print(capitalizeF(['car','jeep','truck']))



