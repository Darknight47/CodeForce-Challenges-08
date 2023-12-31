"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/1916/A ------------

In a sequence a, whose product was equal to 2023, k numbers were removed, leaving a sequence b of length n. 
Given the resulting sequence b, find any suitable sequence a and output which k elements 
were removed from it, or state that such a sequence could not have existed.

Notice that you are not guaranteed that such array exists.

Input
Each test consists of several test cases. The first line contains a single integer t (1 ≤ t ≤ 100) — 
the number of test cases. This is followed by a description of the test cases.

The first line of each test case contains two integers n (1 ≤ n , k ≤ 5) — 
the size of sequence b and the number of numbers removed from sequence a.

The second line contains n integers b1,b2,…,bn (1 ≤ b (i) ≤ 2023) — the remaining sequence. 
The values of bi might not be divisors of 2023.

Output
For each test case, output "YES" if the sequence a exists, and in the following line output 
k non-negative integers that were removed from the sequence a. 
If the sequence a does not exist, output "NO" in a single line.

You can output the answer in any case (uppercase or lowercase). 
For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive answers.

Input:
7
2 2
5 2
3 1
7 17 7
4 2
1 289 1 1
3 1
7 17 17
1 1
289
1 1
2023
1 3
1

Output:
NO
NO
YES
7 1
YES
1
YES
7
YES
1
YES
7 17 17
"""

from functools import reduce
import operator
cases = int(input())
for i in range(cases):
    sze, removed = map(int, input().split())
    lst = list(map(int, input().split()))
    product = reduce(operator.mul, lst)
    if(2023 % product == 0):
        print("YES")
        removedDigits = ""
        first = 2023 // product
        removedDigits += str(first) + " "
        removed -= 1
        for j in range(removed):
            removedDigits += "1 "
        print(removedDigits)
    else:
        print("NO")