def bubbleSort(arr):
    isSorted = False
    counter=0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1-counter):
            if (arr[i] > arr[i + 1]):
                swap(i, i + 1, arr)
                isSorted = False
        counter+=1
    return arr

def swap(i,j,arr):
    arr[i],arr[j]=arr[j],arr[i]


print(bubbleSort([2,12,3,1,2,1,11,1]))