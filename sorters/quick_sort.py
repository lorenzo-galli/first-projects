from math import pi
import random
with open('random_numbers.txt', 'r') as f:
    unsorted = []
    for line in f:
        line = line.strip()
        line = int(line)
        unsorted.append(line)


def quicksort(to_sort): 
    list_len = to_sort.__len__()
    i_pivot = random.randint(0, list_len - 1)
    pivot = to_sort[i_pivot]
    i = 0
    print(pivot)
    while i < list_len:
        if to_sort[i] > pivot and i < i_pivot:
            to_sort.append(to_sort[i])
            to_sort.pop(i)
            i_pivot -= 1
        elif to_sort[i] < pivot and i > i_pivot:
            to_sort.insert(0, to_sort[i])
            to_sort.pop(i + 1)
            i += 1
        elif to_sort[i] == pivot:
            i += 1
        else:
            i += 1
    i_pivot = to_sort.index(pivot)
    sort1 = to_sort[0:i_pivot]
    sort2 = to_sort[i_pivot + 1:list_len]
    return sort1, sort2

def is_sorted(to_sort):
    list_len = to_sort.__len__()
    o = 0
    while o < list_len - 1:
        if to_sort[o] > to_sort[o + 1]:
            return False
        elif to_sort[o] == to_sort[o + 1]:
            o += 1
        else:
            o += 1
    return True

print(unsorted)
print(quicksort(unsorted))
print(is_sorted(unsorted))