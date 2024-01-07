"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/1519/B --------------

There is a n×m grid. You are standing at cell (1,1) and your goal is to finish at cell (n,m).

You can move to the neighboring cells to the right or down. 
In other words, suppose you are standing at cell (x,y). You can:

move right to the cell (x,y+1) — it costs x burles;
move down to the cell (x+1,y) — it costs y burles.
Can you reach cell (n,m) spending exactly k burles?

Input
The first line contains the single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first and only line of each test case contains three integers n, m, and k 
(1 ≤ n, m ≤ 100; 0 ≤ k ≤ 10^4) — the sizes of grid and the exact amount of money you need to spend.

Output
For each test case, if you can reach cell (n,m)
spending exactly k burles, print YES. Otherwise, print NO.

You may print every letter in any case you want 
(so, for example, the strings yEs, yes, Yes and YES are all recognized as positive.

Input:
6
1 1 0
2 2 2
2 2 3
2 2 4
1 4 3
100 100 10000

Output:
YES
NO
YES
NO
YES
NO
"""
cases = int(input())
for i in range(cases):
    n, m, k = map(int, input().split())
    totalcost = (n * m) - 1
    if(totalcost == k):
        print("YES")
    else:
        print("NO")
