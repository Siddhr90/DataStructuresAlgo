def capitalizeWords(arr):
    if len(arr)==0:
        return arr
    else:
        return [arr[0].upper()] + capitalizeWords(arr[1:])


arr = ['sid', 'bharat','neena','raja']
print(capitalizeWords(arr))
