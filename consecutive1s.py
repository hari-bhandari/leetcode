def findMaxConsecutiveOnes(nums):
    count = 0
    for i, num in enumerate(nums):
        highest=0
        if num == 1:
            print(count)
            count += 1
        else:
            highest=
            count = 0
    return count


print(findMaxConsecutiveOnes([1,0,1,1,1,0,1,1]))