def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1,len(customList)):
            if customList[min_index] > customList[j]:
                customList[i], cust omList[j] = customList[j], customList[i]

