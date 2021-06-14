'''
ATTENTION!!!
this was my attempt to recreate the quick sort algorithm. this code has a lot of bugs
but i didn't bothered to fix it. i know this isn't the fastest way to implement this 
algorithm. my goal was to comprehend how this sorting alg works and i think i reached it
i still think that the idea is right.
it once worked now it just doesn't. i'm giving up :/
'''
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
    if len(to_sort) == 1 or is_sorted(to_sort) is True: # we return the array if it's sorted
        return to_sort
    else:
        i_pivot = random.randint(0, to_sort.__len__() - 1) # we take a random pivot and we assign the value to pivot
        pivot = to_sort[i_pivot] # !!! if there are same numbers the code will break
        i = 0
        while i < len(to_sort):
            if to_sort[i] > to_sort[i_pivot] and i < i_pivot:  # this is easy to understand when you start 
                if to_sort[i] == pivot: # to think with indexes. if the num is equal to pivot we put it directly after
                    to_sort.insert(i_pivot + 1, to_sort[i])
                else:
                    to_sort.append(to_sort[i])  
                to_sort.pop(i)
                i_pivot -= 2
            elif to_sort[i] < to_sort[i_pivot] and i > i_pivot:
                if to_sort[i] == pivot:
                    to_sort.insert(i_pivot + 1, to_sort[i])
                else:
                    to_sort.insert(0, to_sort[i])
                to_sort.pop(i + 1)
            i += 1

        i_pivot = to_sort.index(pivot)
        sort1 = to_sort[0:i_pivot]  # we create two different arrays
        sort2 = to_sort[i_pivot + 1:len(to_sort)]
        if is_sorted(to_sort):
            to_sort = sort1 + sort2  
            to_sort.insert(i_pivot, pivot)
            return to_sort
        else:
            sor1 = quicksort(sort1)
            sor2 = quicksort(sort2)
            to_sort = sor1 + sor2
            to_sort.insert(i_pivot, pivot)
            return to_sort

print(unsorted)
unsorted = quicksort(unsorted)
print(unsorted)
print(is_sorted(unsorted))