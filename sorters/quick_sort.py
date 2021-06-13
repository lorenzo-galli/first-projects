import random
with open('random_numbers.txt', 'r') as f:
    unsorted = []  # initialize an empty array
    for line in f: # and fill it with the numbers from the text file
        line = line.strip()
        line = int(line)
        unsorted.append(line)
def is_sorted(to_sort):
    o = 0  # use this condition to make sure it doesn't go out of index
    while o < to_sort.__len__() - 1:
        if to_sort[o] > to_sort[o + 1]:  # if one element is bigger than the next
            return False  # the array is not sorted
        else:
            o += 1
    return True  # if it loops in the whole array it means it's sorted

def quicksort(to_sort): 
    if len(to_sort) == 1 or is_sorted(to_sort) is True:
        print("There ain't nothing to sort XD")
        return to_sort
    else:
        i_pivot = random.randint(0, to_sort.__len__() - 1)
        pivot = to_sort[i_pivot]
        i = 0
        print(pivot)
        while i < len(to_sort):
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
        sort2 = to_sort[i_pivot + 1:len(to_sort)]
        pivot_list = [pivot]
        if is_sorted(to_sort):
            to_sort = sort1 + pivot_list + sort2
            print(str(to_sort) + "FINAL")
            return to_sort
        else:
            print(to_sort)
            sor1 = quicksort(sort1)
            sor2 = quicksort(sort2)
            to_sort = sort1 + pivot_list + sort2
            if is_sorted(to_sort):
                print(to_sort)   

print(quicksort(unsorted))