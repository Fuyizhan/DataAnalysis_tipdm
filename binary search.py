import random
import time


def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    len_mid = (low + high) // 2
    if target == l[len_mid]:
        return len_mid
    if target > l[len_mid]:
        low = len_mid + 1
        return binary_search(l, target, low, high)
    if target < l[len_mid]:
        high = len_mid - 1
        return binary_search(l, target, low, high)

if __name__ == '__main__':
    length = 10000
    sorted_l = set()
    for i in range(length):
        sorted_l.add(random.randint(-3 * length, 3 * length))
    sorted_l = sorted(list(sorted_l))

    start = time.time()
    for target in sorted_l:
        naive_search(sorted_l, target)
    end = time.time()
    print(f"naive search spend {(end - start) / length} seconds")

    start = time.time()
    for target in sorted_l:
        binary_search(sorted_l, target)
    end = time.time()
    print(f"binary search spend {(end - start) / length} seconds")