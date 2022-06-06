#find all numbers and convert them to strings

def stringifyNumbers(obj):
    for key in obj:
        if type(obj[key]) == int:
            obj[key] = str(obj[key])
        if type(obj[key]) == dict:
            obj = stringifyNumbers(obj[key])
    return obj



