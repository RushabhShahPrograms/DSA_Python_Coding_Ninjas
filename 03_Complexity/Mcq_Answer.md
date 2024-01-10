#### Efficiency of Algorithm
1. Two main measures for the efficiency of an algorithm are - **Time and Space**

#### Theoretical Analysis
2. In theoretical Analysis the time factor when determining the efficency of algorithm is measured by - **Counting the number of unit operations**

#### Time Complexity
3. If the number of primary operations of an algorithm that takes an array of size $n$ as input are $3n^2$ + $5n$. The worst case time complexity of the algorithm will be? - **$O(n^2)$**

#### Linear Search Time Complexity
4. The worst case time complexity of Linear Search is - **$O(n)$**

#### Insertion Sort Time Complexity
5. Worst case time complexity of insertion sort is? - **$O(n^2)$**

#### Selection Sort
6. Worst case time complexity of selection sort is? - **$O(n^2)$**

#### Time Complexity
7. What will be the Time complexity of following code in terms of 'n'?
Refer the code for C++.

~~~cpp
for(int i=0; i<n ;i++){
    for(; i<n;i++) {
        cout<<i<<endl;
    }
}
~~~

Refer the same code in Java

~~~java
for(int i=0;i<n;i++) {
    for(;i<n;i++){
        System.out.println(i);
    }
}
~~~

Refer the same code in python.

~~~python
i=0
while i<n:
    while i<n:
        print(i)
        i += 1
~~~

Answer - **$O(n)$**

#### Time complexity of code
8. What will be the Time Complexity of following coe in terms of 'n'?
Note: Assume k to be constant value

Refer the code in python.

~~~python
for i in range(n):
    for j in range(k):
        print(i+j)
~~~

Answer - **$O(n)$**

9. What will be the Time complexity of following code in terms of 'n'?
Refer code in Python

~~~python
for i in range(n):
    k = n
    while k>0:
        k//=2
~~~

Answer - **$O(nlogn)$**

10. What will be the Time complexity of following code in terms of 'n'?

Code in python

~~~python
while n>0:
    n=n//4
~~~

Anwser - **$O(log_4n)$**

#### Recursive Time Complexity
11. What is the time complexity of following recursive code?

~~~python
def multiplyRec(m,n):
    if n==1:
        return m
    return m + multiplyRec(m,n-1)
~~~

Answer - **$O(n)$**

12. What is the time complexity of following recursive code?

~~~python
def sumOfDigits(n):
    if n<10:
        return n
    sum = (n%10) + sumOfDigits(n//10)
    return sum
~~~

Answer - **$O(log_{10}n)$**

#### Recurrence For Merge Sort
13. What is the recurrence relation for merge sort? - **$T(n) = 2T(n/2) + O(n)$**

#### Operations For Merging
14. For merging two sorted arrays of size m and n into a sorted array of size m+n, we require operations - **$O(m+n)$**

#### Merge Sort Time Complexity
15. What is the time complexity of merge sort? - **$O(nlog n)$**

#### Fibonacci Time Complexity
16. What is the time complexity of following recursive code?

~~~python
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)
~~~

Answer - $O(2^n)$

#### Space Complexity Analysis
17. What is the space complexity of following recursive code?

~~~python
def multiplyRec(m,n):
    if n==1:
        return m
    return m+multiplyRec(m,n-1)
~~~
Answer - $O(n)$

#### Merge Sort Space Complexity
18. The space complexity for merge sort is? - **$O(n)$**

#### Fibonacci Space Complexity
19. The space complexity for finding nth fibonacci number using recursion is? - $O(n)$