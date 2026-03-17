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


def counting_sort_answer(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    counts = [0] * (max_num + 1)
    result = [0] * len(numbers)

    for num in numbers:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        result[counts[index]-1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


def radix_sort_answer(numbers: List[int]) -> List[int]:
    def _counting_sort(_numbers: List[int], _place: int) -> List[int]:
        counts = [0] * 10
        result = [0] * len(numbers)

        for num in numbers:
            index = int(num / place) % 10
            # print(index)
            counts[index] += 1

        # print(counts)
        for i in range(1, 10):
            counts[i] += counts[i-1]

        # print(counts)
        i = len(numbers) - 1
        while i >= 0:
            index = int(numbers[i]/place) % 10
            result[counts[index]-1] = numbers[i]
            counts[index] -= 1
            i -= 1

        return result

    max_num = max(numbers)
    place = 1
    while max_num > place:
        numbers = _counting_sort(numbers, place)
        place *= 10
    return numbers


def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(_numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(numbers, partition_index+1, high)

    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


def quick_sort_2(numbers: List[int]) -> List[int]:
    def _partition(_numbers: List[int], high: int, low: int) -> int:
        pass

    def _quick_sort(_numbers: List[int], _high: int, _low:int):
        pass




if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5, 7]
    print(nums)
    # print(bucket_sort(nums))
    # print(bucket_sort_answer(nums))
    # print(selection_sort(nums))
    # print(insertion_sort(nums))

    # print(counting_sort(nums))
    # print(counting_sort_answer(nums))

    # print(radix_sort_answer(nums))
    print(quick_sort(nums))



