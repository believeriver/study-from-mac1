from typing import List, NewType


IndexNum = NewType("IndexNum", int)


def linear_search(numbers: List[int], value: int) -> IndexNum:
    cnt = 0
    for i in range(len(numbers)):
        cnt += 1
        if numbers[i] == value:
            print(f"counter: {cnt}")
            return i
    return -1


def binary_search(numbers: List[int], value: int) -> IndexNum:
    left, right = 0, len(numbers) - 1
    cnt = 0
    while left <= right:
        cnt += 1
        mid = (left + right) // 2
        if numbers[mid] == value:
            print(f"counter: {cnt}")
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_rec(numbers: List[int], value: int) -> IndexNum:
    def _binary_search(_numbers: List[int], _value: int,
                       left: IndexNum, right: IndexNum) -> IndexNum:
        if left > right:
            return -1

        mid = (left + right) // 2

        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(_numbers, _value, mid+1, right)
        else:
            return _binary_search(_numbers, _value, left, mid-1)

    return _binary_search(numbers, value, 0, len(numbers)-1)


if __name__ == '__main__':
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    print(linear_search(nums, 15))
    print(binary_search(nums, 15))
    print(binary_search_rec(nums, 15))

