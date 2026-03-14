from typing import List


def selection_sort(numbers):
    size = len(numbers)
    for i in range(size):
        index = i
        for j in range(i, size):
            if numbers[index] > numbers[j]:
                index = j
        numbers[i], numbers[index] = numbers[index], numbers[i]

    return numbers


def insertion_sort(numbers: List[int]) -> List[int]:
    size = len(numbers)
    for i in range(1, size):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            # print(j, end=' ')
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers


def bucket_sort(numbers: List[int]):
    """
    # Bucket sort
    # split bucket and insertion sort in bucket
    """

    size = len(numbers)
    buckets = [[] for _ in range(size)]

    for num in numbers:
        index = num // size
        if index >= size:
            index = size - 1
        buckets[index].append(num)

    result = []
    for items in buckets:
        res_items = insertion_sort(items)
        for res in res_items:
            result.append(res)

    return result


def bucket_sort_answer(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    buckets = [[] for _ in range(size)]
    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size-1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]

    return result


def counting_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    counters = [0 for _ in range(len_numbers+1)]
    # print(len(counters))
    for num in numbers:
        counters[num] += 1

    for index in range(1, len(counters)):
        counters[index] += counters[index - 1]

    # print(counters)
    result = [0 for _ in range(len_numbers)]
    for num in numbers:
        # print("counter index", counters[num])
        result[counters[num]-1] = num
        # print("result", result)
        counters[num] -= 1
        # print("counters", counters)

    return result


if __name__ == '__main__':
    nums = [4, 3, 6, 2, 3, 4, 7]
    print(nums)
    # print(bucket_sort(nums))
    # print(bucket_sort_answer(nums))
    # print(selection_sort(nums))
    # print(insertion_sort(nums))

    print(counting_sort(nums))



