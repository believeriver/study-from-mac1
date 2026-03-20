from typing import List, NewType


IndexNum = NewType("IndexNum", int)


def linear_search(numbers: List[int], value: int) -> IndexNum:
    cnt = 0
    for i in range(len(numbers)):
        cnt += 1
        if numbers[i] == value:
            print(cnt)
            return i
    return -1


def binary_search(numbers: List[int], value: int) -> IndexNum:
    pass


if __name__ == '__main__':
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    print(linear_search(nums, 15))

