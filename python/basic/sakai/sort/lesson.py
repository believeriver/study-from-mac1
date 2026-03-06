# Bucket sort
# split bucket and insertion sort in bucket

from typing import List


def insertion_sort(numbers):
    size = len(numbers)
    for i in range(size):
        index = i
        for j in range(i, size):
            if numbers[i] > numbers[j]:
                index = j
        numbers[i], numbers[index] = numbers[index], numbers[i]

    return numbers


def bucket_sort(numbers: List[int]):
    size = len(numbers)
    buckets = [[] for n in range(size)]

    for num in numbers:
        index = num // size
        if index >= size:
            index = size - 1
        buckets[index].append(num)
    print(buckets)


if __name__ == '__main__':
    nums = [1, 5, 28, 25, 100, 52, 27, 91, 22, 99]
    # bucket_sort(nums)
    print(nums)
    print(insertion_sort(nums))



