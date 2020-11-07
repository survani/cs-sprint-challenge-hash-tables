def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    arrays_table = {}
    result = []

    for arr in arrays:
        for i in arr:
            if i in arrays_table:
                arrays_table[i] += 1
            else:
                arrays_table[i] = 1

    for key, value in arrays_table.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
