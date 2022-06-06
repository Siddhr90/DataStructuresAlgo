def isPalindrome(strng):
    if len(strng)==0 or len(strng)==1:
        return True
    if strng[0]==strng[-1]:
        return(isPalindrome(strng[1:-1]))
    else:
        return False

print(isPalindrome('MalayalaM'))

strng = 'awesome'
print(strng[0])
print(strng[-1])
print(strng[1:-1])