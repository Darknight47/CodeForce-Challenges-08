"""
---------- Link for the challenge: https://codeforces.com/contest/1915/problem/C -------------

Calin has n buckets, the i-th of which contains a(i) wooden squares of side length 1.

Can Calin build a square using all the given squares?

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains a single integer n
(1 ≤ n ≤ 2⋅10^5) — the number of buckets.

The second line of each test case contains n
integers a1,…,an (1 ≤ a(i) ≤ 10^9) — the number of squares in each bucket.

The sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output "YES" if Calin can build a square using all of the given 1×1
squares, and "NO" otherwise.

You can output the answer in any case 
(for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Input:
5
1
9
2
14 2
7
1 2 3 4 5 6 7
6
1 3 5 7 9 11
4
2 2 2 2

Output:
YES
YES
NO
YES
NO
"""
import math
cases = int(input())
for i in range(cases):
    sze = int(input())
    tempSum = sum(list(map(int, input().split())))
    root = math.sqrt(tempSum)
    print("YES" if root == int(root) else "NO")