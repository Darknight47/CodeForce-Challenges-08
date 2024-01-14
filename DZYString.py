"""
------------ Link for the challenge: https://codeforces.com/contest/447/problem/B ---------------

DZY loves collecting special strings which only contain lowercase letters. 
For each lowercase letter c DZY knows its value wc. For each special string s = s1s2... s|s| 
(|s| is the length of the string) he represents its value with a function f(s), where

Now DZY has a string s. He wants to insert k lowercase letters into this string in order 
to get the largest possible value of the resulting string. Can you help him calculate the 
largest possible value he could get?

Input
The first line contains a single string s (1 ≤ |s| ≤ 10^3).

The second line contains a single integer k (0 ≤ k ≤ 10^3).

The third line contains twenty-six integers from wa to wz. 
Each such number is non-negative and doesn't exceed 1000.

Output
Print a single integer — the largest possible value of the resulting string DZY could get.

Input:
abc
3
1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

Output:
41
"""
s = input()
k = int(input())
values = list(map(int, input().split()))
sorted_values = sorted(values)
max_value = sorted_values[-1]
diction = {}
asc = 97
for i in values:
    tk = chr(asc)
    asc += 1
    diction[tk] = i
#sorted_dict = {k: v for k, v in sorted(diction.items(), key=lambda item: item[1], reverse=True)}
ans = 0
for j in range(len(s)):
    tv = diction[s[j]]
    ans += (j + 1) * tv
extended = len(s) + k
for j in range(len(s), extended):
    ans += (j + 1) * max_value
print(ans)