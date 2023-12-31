"""
------------- Link for the challenge: https://codeforces.com/problemset/problem/1844/A ---------------

You are given two positive integers, a and b (a < b).

For some positive integer n, two players will play a game starting with a pile of n stones. 
They take turns removing exactly a or exactly b stones from the pile. 
The player who is unable to make a move loses.

Find a positive integer n such that the second player to move in this game has a winning strategy. 
This means that no matter what moves the first player makes, the second player can carefully choose their 
moves (possibly depending on the first player's moves) to ensure they win.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). 
The description of the test cases follows.

The only line of each test case contains two integers, a and b (1 ≤ a < b ≤ 100).

Output
For each test case, output any positive integer n (1≤n≤10^6) such that the second player to move wins.

It can be proven that such an n always exists under the constraints of the problem.

Input:
3
1 4
1 5
9 26

Output:
2
6
3
"""
cases = int(input())
for i in range(cases):
    a, b = map(int, input().split())
    print(a + b)