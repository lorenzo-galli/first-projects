with open('random_numbers.txt', 'r') as f:
    to_sort = []  # initialize an empty array
    for line in f: # and fill it with the numbers from the text file
        line = line.strip()
        line = int(line)
        to_sort.append(line)


def bubble_sort(to_sort):
    i = 0 # use this condition to make sure it doesn't go out of index
    while i < to_sort.__len__() - 1: 
        if to_sort[i] > to_sort[i + 1]: # if the second is bigger swap them 
            to_sort[i], to_sort[i + 1] = to_sort[i + 1], to_sort[i]
        i += 1
    return to_sort  # return the array


def is_sorted(to_sort):
    o = 0  # use this condition to make sure it doesn't go out of index
    while o < to_sort.__len__() - 1:
        if to_sort[o] > to_sort[o + 1]:  # if one element is bigger than the next
            return False  # the array is not sorted
        else:
            o += 1
    return True  # if it loops in the whole array it means it's sorted


print(to_sort) # print the unsorted array

while is_sorted(to_sort) is False: # continue to loop in the array if it
    bubble_sort(to_sort)  # isn't sorted

print(to_sort)  # print the sorted array
