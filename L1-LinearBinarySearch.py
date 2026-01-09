'''
Docstring for DSA Python.L1-LinearBinarySearch

In this module, we implement both Binary Search and Linear Search algorithms in Python.
We also compare their time complexities by measuring the time taken to search for an element in a sorted array.

First we import the time and random module to measure execution time and generate random numbers.
Second, we define an unsorted array and sort it, and set the target number to be found. 
Then, we implement the binary_search function that performs binary search on the array.

How is binary search implemented?
1. Initialize two pointers, left and right, to the start and end of the array.
2. While left is less than or equal to right:
   a. Calculate the mid index.
   b. If the middle element is equal to the target, return the mid index.
   c. If the middle element is less than the target, move the left pointer to mid + 1.
   d. If the middle element is greater than the target, move the right pointer to mid - 1.
3. If the target is not found, return -1.

Next, we implement the linear_search function that performs linear search on the array.
1. Iterate through each element in the array.
2. If the current element is equal to the target, return the index.
3. If the target is not found after checking all elements, return -1.

Finally, we measure and print the time taken for both search algorithms to find the target element in the array.

The final time taken for each search method is printed to the console and shows the efficiency difference between not only binary search and linear search but also between O(log n) and O(n).
Through this we can clearly see that binary search is significantly faster than linear search for large datasets.
'''
import time,random
#`Implementing Binary and Linear Search in Python
unsorted_list = [random.randint(1, 10000) for _ in range(10000)]
arr1=sorted(unsorted_list)
num_to_b_found=arr1[random.randint(0,9999)]
def binary_search(arr:list,target:int)->int:
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

# Linear Binary Search Implementation
def linear_search(arr:list,target:int)->int:
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

# Checking the time complexity of both algorithms
# Time Complexity of Binary Search: O(log n)
time_start=time.time()
result=binary_search(arr1,num_to_b_found)
print(f"Element found at index: {result}" if result!=-1 else "Element not found")
time_end=time.time()
print(f"Time taken for Binary Search: {time_end-time_start} seconds")

# Time Complexity of Linear Search: O(n)
time_start=time.time()
result=linear_search(arr1,num_to_b_found)
print(f"Element found at index: {result}" if result!=-1 else "Element not found")
time_end=time.time()
print(f"Time taken for Linear Search: {time_end-time_start} seconds")
