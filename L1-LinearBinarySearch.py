'''
L1-LinearBinarySearch

This module provides robust Binary Search and Linear Search implementations
with explicit handling for common edge cases:

- empty input (`arr` is empty)
- single-element arrays
- target at first/second/middle positions
- target not present
- arrays with repeating elements (returns first index or all indices)

Functions:
- `binary_search(arr, target)` -> int
    Returns any index where `target` is found, or -1 if not found.

- `binary_search_first(arr, target)` -> int
    Returns the first (leftmost) index of `target` in a sorted array, or -1.

- `binary_search_all(arr, target)` -> list[int]
    Returns a list of all indices where `target` occurs (sorted, empty if none).

- `linear_search(arr, target)` -> int
    Returns the first index of `target` (scans left-to-right), or -1.

- `linear_search_all(arr, target)` -> list[int]
    Returns a list of all indices where `target` occurs (empty if none).

All functions gracefully handle empty input and single-element arrays.
'''
import time
import random

# Example data used later for timing/demo
unsorted_list = [random.randint(1, 10000) for _ in range(10000)]
arr1 = sorted(unsorted_list)
num_to_b_found = arr1[random.randint(0, len(arr1) - 1)]


def binary_search(arr: list, target: int) -> int:
    """Standard binary search.

    Returns any index where `target` is found (in a sorted array),
    or -1 if not found. Handles empty arrays.
    """
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_first(arr: list, target: int) -> int:
    """Return the first (leftmost) index of `target` in `arr`, or -1.

    Useful when `arr` may contain repeated elements.
    """
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            res = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return res


def binary_search_all(arr: list, target: int) -> list:
    """Return a list of all indices where `target` occurs in the sorted `arr`.

    Returns an empty list if `target` is not present.
    This finds one occurrence then expands left/right to collect the full block
    (efficient because equal elements are contiguous in a sorted array).
    """
    idx = binary_search(arr, target)
    if idx == -1:
        return []
    l = idx
    while l - 1 >= 0 and arr[l - 1] == target:
        l -= 1
    r = idx
    while r + 1 < len(arr) and arr[r + 1] == target:
        r += 1
    return list(range(l, r + 1))


def linear_search(arr: list, target: int) -> int:
    """Return the first index of `target` by scanning left-to-right, or -1.

    Works for unsorted arrays and handles empty inputs.
    """
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def linear_search_all(arr: list, target: int) -> list:
    """Return all indices where `target` occurs (left-to-right scan).

    Returns an empty list if not found.
    """
    return [i for i, v in enumerate(arr) if v == target]


if __name__ == "__main__":
    # Demo: simple timing using the randomly generated sorted array
    print("-- Demo: timing on a large random sorted array --")
    time_start = time.time()
    result = binary_search(arr1, num_to_b_found)
    print(f"Binary search: Element found at index: {result}" if result != -1 else "Binary search: Element not found")
    time_end = time.time()
    print(f"Time taken for Binary Search: {time_end - time_start} seconds")

    time_start = time.time()
    result = linear_search(arr1, num_to_b_found)
    print(f"Linear search: Element found at index: {result}" if result != -1 else "Linear search: Element not found")
    time_end = time.time()
    print(f"Time taken for Linear Search: {time_end - time_start} seconds")

    # Explicit edge-case checks
    print("\n-- Edge-case checks --")
    tests = [
        ([], 5, "empty array"),
        ([7], 7, "single-element array where element is target"),
        ([7], 3, "single-element array where element is not target"),
        ([1, 2, 3, 4, 5], 1, "target is first element"),
        ([1, 2, 3, 4, 5], 2, "target is second element"),
        ([1, 2, 3, 4, 5], 3, "target in middle"),
        ([1, 2, 2, 2, 3, 4], 2, "repeating elements, multiple positions"),
        ([1, 3, 5, 7], 4, "target not present"),
    ]

    for arr, t, desc in tests:
        print(f"\nTest: {desc} -> arr={arr}, target={t}")
        print("binary_search:", binary_search(arr, t))
        print("binary_search_first:", binary_search_first(arr, t))
        print("binary_search_all:", binary_search_all(arr, t))
        print("linear_search:", linear_search(arr, t))
        print("linear_search_all:", linear_search_all(arr, t))
