"""
-------------- Link for the challenge: https://codeforces.com/problemset/problem/1728/A ----------

The title is a reference to the very first Educational Round from our writers team, Educational Round 18.

There is a bag, containing colored balls. There are n different colors of balls, numbered from 1 to n. 
There are cnt(i) balls of color i in the bag. The total amount of balls in the bag is odd 
(e. g. cnt1 + cnt2 +⋯+ cntn is odd).

In one move, you can choose two balls with different colors and take them out of the bag.

At some point, all the remaining balls in the bag will have the same color. 
That's when you can't make moves anymore.

Find any possible color of the remaining balls.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of testcases.

The first line of each testcase contains a single integer n (1 ≤ n ≤ 20) — the number of colors.

The second line contains n integers cnt1,cnt2,…,cntn (1 ≤ cnt(i) ≤ 100) — 
the amount of balls of each color in the bag.

The total amount of balls in the bag is odd (e. g. cnt1 + cnt2 +⋯+ cntn is odd).

Output
For each testcase, print a single integer — any possible color of the remaining balls, 
after you made some moves and can't make moves anymore.

Input:
3
3
1 1 1
1
9
2
4 7

Output:
3
1
2
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    biggest = 0
    for j in range(sze):
        temp = lst[j]
        if(temp > biggest):
            biggest = temp
            ans = j + 1
    print(ans)