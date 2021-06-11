with open('random_numbers.txt', 'r') as f:
    to_sort = []
    for line in f:
        line = line.strip()
        line = int(line)
        to_sort.append(line)

for i in range(to_sort.__len__()):
    if i == to_sort.__len__() - 1:
        p = i
    else:
        p = i + 1
    if to_sort[i] > to_sort[p]:
        to_sort[i], to_sort[p] = to_sort[p], to_sort[i]
    else:
        pass
    

def is_sorted(array):
    pass


array = [1, 3, 4]
is_sorted = True
for i in (0, array.__len__()):
    p = i + 1
    if is_sorted:
        if array[i] == array[p]:
            pass
        else:
            is_sorted = False
    else:
        break

print(zip(array))

print(is_sorted)
            
