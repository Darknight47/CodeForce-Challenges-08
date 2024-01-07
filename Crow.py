"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/712/A -------------

There are n integers b1, b2, ..., bn written in a row. For all i from 1 to n, values a(i) 
are defined by the crows performing the following procedure:

The crow sets ai initially 0.
The crow then adds bi to ai, subtracts bi + 1, adds the bi + 2 number, and so on until the n'th number. 
Thus, ai = bi - bi + 1 + bi + 2 - bi + 3....
Memory gives you the values a1, a2, ..., an, and he now wants you to find the initial 
numbers b1, b2, ..., bn written in the row? Can you do it?

Input
The first line of the input contains a single integer n (2 ≤ n ≤ 100 000) — 
the number of integers written in the row.

The next line contains n, the i'th of which is ai ( - 109 ≤ ai ≤ 10^9) — the value of the i'th number.

Output
Print n integers corresponding to the sequence b1, b2, ..., bn. 
It's guaranteed that the answer is unique and fits in 32-bit integer type.

Input:
5
6 -4 8 -2 3

Output:
2 4 6 1 3 
"""
sze = int(input())
arr = list(map(int, input().split()))
s = []
for i in range(len(arr) - 1, 0, -1):
    t = arr[i - 1] + arr[i]
    s.append(t)
    #print(t, end=" ")
s.reverse()
print(*s, end=" ")
print(arr[sze - 1])