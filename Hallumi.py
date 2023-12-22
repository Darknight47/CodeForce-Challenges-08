"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1903/A ---------------

Theofanis is busy after his last contest, as now, he has to deliver many halloumis all over the world. 
He stored them inside n boxes and each of which has some number ai written on it.

He wants to sort them in non-decreasing order based on their number, however, 
his machine works in a strange way. It can only reverse any subarray† of boxes with length at most k.

Find if it's possible to sort the boxes using any number of reverses.

† Reversing a subarray means choosing two indices i and j (where 1 ≤ i ≤ j ≤ n) 
and changing the array a1,a2,…,an to a1,a2,…,ai−1,aj,aj−1,…,ai,aj+1,…,an−1,an. 
The length of the subarray is then j−i+1.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

Each test case consists of two lines.

The first line of each test case contains two integers n and k (1 ≤ k ≤ n ≤ 100) 
— the number of boxes and the length of the maximum reverse that Theofanis can make.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the number written on each box.

Output
For each test case, print YES (case-insensitive), if the array can be sorted in non-decreasing
order, or NO (case-insensitive) otherwise.

Input:
5
3 2
1 2 3
3 1
9 9 9
4 4
6 4 2 1
4 3
10 3 830 14
2 1
3 1

Output:
YES
YES
YES
YES
NO
"""
cases = int(input())
for i in range(cases):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    alreadySorted = True
    for j in range(n - 1):
        first = lst[j]
        second = lst[j + 1]
        if(second < first):
            alreadySorted = False
            break
    if(k == 1 and alreadySorted):
        print("YES")
    elif(k == 1 and not alreadySorted):
        print("NO")
    elif(k >= 2):
        print("YES")