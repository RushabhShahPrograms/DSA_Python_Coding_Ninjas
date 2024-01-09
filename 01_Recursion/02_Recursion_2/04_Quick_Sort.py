'''
Quick Sort Code

Sort an array A using Quick Sort.
Change in the input array itself. So no need to return or print anything.

Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)
Output format :
Array elements in increasing order (separated by space)
Constraints :
1 <= n <= 10^3
Sample Input 1 :
6 
2 6 8 5 4 3
Sample Output 1 :
2 3 4 5 6 8
Sample Input 2 :
5
1 5 2 7 3
Sample Output 2 :
1 2 3 5 7 
'''

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the index of the pivot element
        pivot_index = partition(arr, low, high)

        # Recursively sort the sub-arrays on both sides of the pivot
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # Choose the first element as the pivot
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            # Swap elements at left and right indices
            arr[left], arr[right] = arr[right], arr[left]

    # Swap pivot with the element at right index
    arr[low], arr[right] = arr[right], arr[low]

    return right

# Input: Array size
n = int(input())

# Input: Array elements
array_elements = list(map(int, input().split()))

# Sorting the array using Quick Sort
quick_sort(array_elements, 0, n - 1)

# Printing the sorted array
print(*array_elements)