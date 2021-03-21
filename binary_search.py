numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]


def binary_search(numbers, left_index, right_index, key):
    if right_index > left_index:
        mid = (left_index + right_index) // 2
        if numbers[mid] == key:
            return mid
        elif numbers[mid] < key:
            return binary_search(numbers, mid + 1, right_index, key)
        else:
            return binary_search(numbers, left_index, mid - 1, key)
    return -1


print(binary_search(numbers_list, 0, len(numbers_list), 67))
