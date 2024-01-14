"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/447/A -------------

DZY has a hash table with p buckets, numbered from 0 to p - 1. 
He wants to insert n numbers, in the order they are given, into the hash table. 
For the i-th number xi, DZY will put it into the bucket numbered h(xi), where h(x) is the hash function. 
In this problem we will assume, that h(x) = x mod p. 
Operation a mod b denotes taking a remainder after division a by b.

However, each bucket can contain no more than one element. 
If DZY wants to insert an number into a bucket which is already filled, we say a "conflict" happens. 
Suppose the first conflict happens right after the i-th insertion, you should output i. 
If no conflict happens, just output -1.

Input
The first line contains two integers, p and n (2 ≤ p, n ≤ 300). 
Then n lines follow. The i-th of them contains an integer xi (0 ≤ xi ≤ 10^9).

Output
Output a single integer — the answer to the problem.

Input:
10 5
0
21
53
41
53

Output:
4
"""
p, n = map(int, input().split())
buckets = set()
founded = False
for i in range(n):
    num = int(input())
    temp = num % p
    if(temp in buckets):
        founded = True
        print(i + 1)
        break
    else:
        buckets.add(temp)
if(not founded):
    print(-1)