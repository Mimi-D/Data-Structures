import random
import time
def binary_Search(array, target, low, high):
    if low > high:
        return False

    middle = (low + high) // 2
    if array[middle] == target:
        return True

    elif array[middle] > target:

        return binary_Search(array, target, low, middle - 1)
    else:
        return binary_Search(array, target, middle + 1, high)


def interpolation_Search(array, target, low, high):

    while low <= high and target>= array[low] and target <= array[high]:
        mid = low + ((high - low) / (array[high] - array[low]) * (target - array[low]))
        middle = int(mid)
        if low == high and array[low]==target:
            return True

        elif array[middle] == target:
            return True

        elif array[middle] < target:
            low =middle +1
        else:
            high = middle + 1
    return False

#Running and timing of Binary Search
print(" Question 2.  Binary search vs Interpolation seacrh \n")
for i in range(15):
    N = int(input("Kindly input the array size"))
    array = []
    for i in range(N):
        n = random.randint(1, 32768)
        array.append(n)
    array.sort()
    print(array)
    target = int(input("Kindly input the target"))
    binary_Search_Start = time.clock()
    state=binary_Search(array, target, 0, len(array) - 1)
    binary_Search_End = time.clock()
    time_taken = binary_Search_End - binary_Search_Start
    if state:
        print("The target is in the array")
    else:
        print("The target is not in the array")
    print("Time taken by binary search is = ", time_taken)
    print("\n")

    interpolation_Search_Start = time.clock()
    statee=interpolation_Search(array, target, 0, len(array) - 1)
    interpolation_Search_End = time.clock()
    time_taken2 = (interpolation_Search_End - interpolation_Search_Start)
    if statee:
        print("The target is in the array")
    else:
        print("The target is not in the array")
    print("Time taken by interpolation search is = ", time_taken2)
    print("\n")

