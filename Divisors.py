"""
--------------- Link for the challenge: https://codeforces.com/problemset/problem/1916/B -----------

A certain number 1 ≤ x ≤ 10^9 is chosen. You are given two integers a and b, 
which are the two largest divisors of the number x.
At the same time, the condition 1 ≤ a < b < x is satisfied.

For the given numbers a, b, you need to find the value of x.

† The number y is a divisor of the number x if there is an integer k such that x=y⋅k.

Input
Each test consists of several test cases. The first line contains a single integer t
(1 ≤ t ≤ 10^4) — the number of test cases. Then follows the description of the test cases.

The only line of each test cases contains two integers a, b (1 ≤ a < b ≤ 10^9).

It is guaranteed that a, b are the two largest divisors for some number 1 ≤ x ≤ 10^9.

Output
For each test case, output the number x, such that a and b are the two largest divisors of the number x.

If there are several answers, print any of them.

Input:
8
2 3
1 2
3 11
1 5
5 10
4 6
3 9
250000000 500000000

Output:
6
4
33
25
20
12
27
1000000000
"""
from math import gcd
cases = int(input())
for i in range(cases):
    a, b = map(int, input().split())
    if(b % a == 0):
        div = b // a
        ans = b * div
    else:
        ans = b * (a // gcd(a, b))
    print(ans)