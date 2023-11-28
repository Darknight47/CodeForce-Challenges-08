"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/1646/A ------------

Luis has a sequence of n+1 integers a1,a2,…,an+1. 
For each i=1,2,…,n+1 it is guaranteed that 0 ≤ a(i) < n, or a(i) = n^2. 
He has calculated the sum of all the elements of the sequence, and called this value s.

Luis has lost his sequence, but he remembers the values of n and s. 
Can you find the number of elements in the sequence that are equal to n^2?

We can show that the answer is unique under the given constraints.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 2⋅10^4). 
Description of the test cases follows.

The only line of each test case contains two integers n and s (1 ≤ n < 10^6, 0 ≤ s ≤ 10^18). 
It is guaranteed that the value of s is a valid sum for some sequence satisfying the above constraints.

Output
For each test case, print one integer — the number of elements in the sequence which are equal to n^2.

Input:
4
7 0
1 1
2 12
3 12

Output:
0
1
3
1
"""
cases = int(input())
for i in range(cases):
    n, s = map(int, input().split())
    nsquare = n * n
    if(s == 0):
        ans = 0
    else:
        ans = s // nsquare
    print(ans)