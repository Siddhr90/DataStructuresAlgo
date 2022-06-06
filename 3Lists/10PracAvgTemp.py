# calcuate count of above avg temperatures
import numpy as np

numDays = int(input('Enter num days : '))
temp = []
for i in range(0,numDays):
    temp.append(float(input('Enter temperature foor day' + str(i+1))))

tempAr = np.array(temp)
Average = np.sum(tempAr)/len(tempAr)
print('Average: ' + str(Average))

for i in tempAr:
    if i > Average:
        print(' Temp: '+ str(i))

