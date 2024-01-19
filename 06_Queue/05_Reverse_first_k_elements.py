'''
Reverse the First K Elements in the Queue

For a given queue containing all integer data, reverse the first K elements.
You have been required to make the desired change in the input queue itself.
Example:
 
For the above input queue, if K = 4 then after reversing the first 4 elements, the queue will be updated as:
 
Input Format :
The first line of input would contain two integers N and K, separated by a single space. They denote the total number of elements in the queue and the count with which the elements need to be reversed respectively.

The second line of input contains N integers separated by a single space, representing the order in which the elements are enqueued into the queue.
Output Format:
The only line of output prints the updated order in which the queue elements are dequeued, all of them separated by a single space. 
Note:
You are not required to print the expected output explicitly, it has already been taken care of. Just make the changes in the input queue itself.
Contraints :
1 <= N <= 10^6
1 <= K <= N
-2^31 <= data <= 2^31 - 1

 Time Limit: 1sec
Sample Input 1:
5 3
1 2 3 4 5
Sample Output 1:
3 2 1 4 5
Sample Input 2:
7 7
3 4 2 5 6 7 8
Sample Output 2:
8 7 6 5 2 4 3
'''

from queue import Queue

def reverse_k_elements(queue, k):
    stack = []

    # Push the first K elements into a stack
    for i in range(k):
        stack.append(queue.get())

    # Pop elements from the stack and enqueue them back to the queue
    while stack:
        queue.put(stack.pop())

    # Enqueue the remaining elements
    for i in range(queue.qsize() - k):
        queue.put(queue.get())

# Driver code
if __name__ == "__main__":
    n, k = map(int, input().split())
    elements = list(map(int, input().split()))

    # Create a queue and enqueue the elements
    input_queue = Queue()
    for element in elements:
        input_queue.put(element)

    # Reverse the first K elements in the queue
    reverse_k_elements(input_queue, k)

    # Print the updated queue
    while not input_queue.empty():
        print(input_queue.get(), end=" ")
    print()