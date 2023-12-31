"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/1634/A ---------------

You are given a string s of length n and a number k. 
Let's denote by rev(s) the reversed string s (i.e. rev(s)=snsn−1...s1). 
You can apply one of the two kinds of operations to the string:

replace the string s with s+rev(s) replace the string s with rev(s)+s

How many different strings can you get as a result of performing exactly k
operations (possibly of different kinds) on the original string s?

In this statement we denoted the concatenation of strings s and t as s+t. 
In other words, s+t=s1s2...snt1t2...tm, where n and m are the lengths of strings s and t respectively.

Input
The first line contains one integer t (1 ≤ t ≤ 100) — number of test cases. Next 2⋅t lines contain t test cases:

The first line of a test case contains two integers n and k (1 ≤ n ≤ 100, 0 ≤ k ≤ 1000) — 
the length of the string and the number of operations respectively.

The second string of a test case contains one string s of length n consisting of lowercase Latin letters.

Output
For each test case, print the answer (that is, the number of different strings that you can get after exactly k
operations) on a separate line.

It can be shown that the answer does not exceed 10^9 under the given constraints.

Input:
4
3 2
aab
3 3
aab
7 1
abacaba
2 0
ab

Output:
2
2
1
1
"""
cases = int(input())
for i in range(cases):
    sze, ops = map(int, input().split())
    s = input()
    revS = s[::-1]
    if(s == revS or ops == 0):
        print(1)
    else:
        print(2)