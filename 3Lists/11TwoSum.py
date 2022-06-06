# indices of missing number

def missingnum(mylist,n):
    sum1 = n*(n+1)/2
    sum2 = sum(mylist)

    return sum1-sum2

print(missingnum([1,2,3,4,6,7,8,9],9))

# pairs or two sum:
# return indices of numbers that add up to given sum
# ask if  there can be negative indices, same num can be repeated, (4,1) and (1,4) for 5? etc..

def twopair(mylist, target):
    pair = []
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if (mylist[i]+mylist[j]) == target:
                print([i,j])
    #return(pair)
twopair([1,2,3,4,5,6,7],9)
