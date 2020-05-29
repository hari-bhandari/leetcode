
def bubbleSort(arr):
    isSorted = False
    counter=0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1 - counter):
            if (arr[i] > arr[i + 1]):
                swap(i, i + 1, arr)
                isSorted = False
        counter += 1
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


# nth fibbonacci uneffective
def nthFibonacci(number):
    if number <= 0:
        return -1
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return nthFibonacci(number - 2) + nthFibonacci(number - 1)


def nthFibonacciv2(number, memoize={1: 0, 2: 1}):
    if number in memoize:
        return memoize[number]
    else:
        memoize[number] = nthFibonacciv2(number - 1, memoize) + nthFibonacciv2(number - 2, memoize)
        return memoize[number]


def nthFibonacciv3(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
       nextFib=lastTwo[0]+lastTwo[1]
       lastTwo[0]=lastTwo[1]
       lastTwo[1]=nextFib
       counter+=1
    return lastTwo[1]  if n>1 else lastTwo[0]
##find three largest number in an array

def largestNumber(array):
    largestNumbers=[None,None,None]
    for i,number in enumerate(array):
        updateLargest(largestNumbers,number)
    return largestNumbers
def updateLargest(largestNumbers,number):
    if largestNumbers[2] is None or number>largestNumbers[2]:
        shiftAndUpdate(largestNumbers,number,2)
    elif largestNumbers[1] is None or number>largestNumbers[1]:
        shiftAndUpdate(largestNumbers,number,1)
    elif largestNumbers[0] is None or number>largestNumbers[0]:
        shiftAndUpdate(largestNumbers,number,0)
def shiftAndUpdate(array,num,idx):
    for i in range(idx+1):
        if(i==idx):
            array[i]=num
        else:
            array[i]=array[i+1]
print(largestNumber([1,2,11,212,122,231,12]))