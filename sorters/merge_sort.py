with open('random_numbers.txt', 'r') as f:
    to_sort_to_sort = []
    for line in f:
        line = line.strip()
        line = int(line)
        to_sort_to_sort.append(line)

