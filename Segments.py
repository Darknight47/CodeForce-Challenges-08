"""
-------------- Link for the challenge: https://codeforces.com/problemset/problem/1015/A ------------------

You are given a set of n segments on the axis Ox, each segment has integer endpoints between 1 and m inclusive. 
Segments may intersect, overlap or even coincide with each other. 
Each segment is characterized by two integers li and ri (1 ≤ li ≤ ri ≤ m) — 
coordinates of the left and of the right endpoints.

Consider all integer points between 1 and m inclusive. 
Your task is to print all such points that don't belong to any segment. 
The point x belongs to the segment [l;r] if and only if l ≤ x ≤ r.

Input
The first line of the input contains two integers n and m (1 ≤ n, m ≤ 100) — 
the number of segments and the upper bound for coordinates.

The next n lines contain two integers each li and ri (1 ≤ li ≤ ri ≤m) — the endpoints of the i-th segment. 
Segments may intersect, overlap or even coincide with each other. 
Note, it is possible that li=ri, i.e. a segment can degenerate to a point.

Output
In the first line print one integer k — the number of points that don't belong to any segment.

In the second line print exactly k integers in any order — 
the points that don't belong to any segment. All points you print should be distinct.

If there are no such points at all, print a single integer 0
in the first line and either leave the second line empty or do not print it at all.

Input:
3 5
2 2
1 2
5 5

Output:
2
3 4
"""
segments, upperBound = map(int, input().split())
interval = set(range(0,0))
orig = set(range(1, upperBound + 1))
for i in range(segments):
    a, b = map(int, input().split())
    if(a == b):
        interval.add(a)
    else:
        interval.update(range(a,b + 1))
if(upperBound - len(interval) == 0):
    print(0)
else:
    print(upperBound - len(interval))
    misssing = orig - interval
    print(*misssing)