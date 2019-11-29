def binary_search(sequence, target):
    add = 0
    while True:
        mid = int(len(sequence) / 2)
        if sequence[mid] == target:
            return mid + add
        elif len(sequence) == 1 and sequence[0] != target:
            return None
        elif target < sequence[mid]:
            sequence = sequence[:mid]
        else:
            add += len(sequence) - len(sequence[mid:])
            sequence = sequence[mid:]
