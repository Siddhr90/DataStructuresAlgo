#write a recursive function called nested even sum which returns sum of all even numbers in an object


obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}


obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}


def nestedEvenSum(obj, sum=0):
  for key in obj:
    if type(obj[key]) is dict:
      sum += nestedEvenSum(obj[key])
    elif type(obj[key]) is int and obj[key] % 2 == 0:
      sum += obj[key]
  return sum

print(nestedEvenSum(obj1,0))

'''
def nestedEvenSum(obj, sum=0):
    if len(obj)==0:
        print(obj)
        return (obj,sum)
    if type(obj)==dict:
        print(obj)
        if list(obj.values())[0]%2==0:
            return nestedEvenSum(list(obj.values())[1:],sum+1)
        else:
            return  nestedEvenSum(list(obj.values())[1:],sum)



print(nestedEvenSum(obj2,0))

'''