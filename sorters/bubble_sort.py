with open('random_numbers.txt', 'r') as f:
    to_sort = []
    for line in f:
        line = line.strip()
        line = int(line)
        to_sort.append(line)

for i in range(to_sort.__len__()):
    if i == to_sort.__len__() - 1:
        next = i
    else:
        next = i + 1
    if to_sort[i] > to_sort[next]:
        to_sort[i], to_sort[next] = to_sort[next], to_sort[i]
    else:
        pass

print(to_sort)