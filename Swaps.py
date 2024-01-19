"""
------------------- Link for the challenge: https://codeforces.com/problemset/problem/1353/B --------------

You are given two arrays a and b both consisting of n positive (greater than zero) integers. 
You are also given an integer k.

In one move, you can choose two indices i and j (1 ≤ i,j ≤ n) and swap ai and bj 
(i.e. ai becomes bj and vice versa). Note that i and j
can be equal or different (in particular, swap a2 with b2 or swap a3 and b9 both are acceptable moves).

Your task is to find the maximum possible sum you can obtain in the array a
if you can do no more than (i.e. at most) k such moves (swaps).

You have to answer t independent test cases.

Input
The first line of the input contains one integer t
(1 ≤ t ≤ 200) — the number of test cases. Then t test cases follow.

The first line of the test case contains two integers n
and k (1 ≤ n ≤ 30; 0 ≤ k ≤ n) — the number of elements in a and b and the maximum number of moves you can do. 
The second line of the test case contains n
integers a1,a2,…,an (1 ≤ ai ≤ 30), where ai is the i-th element of a. 
The third line of the test case contains n integers b1,b2,…,bn (1 ≤ bi ≤ 30), where bi is the i-th element of b.

Output
For each test case, print the answer — the maximum possible sum you can obtain in the array a
if you can do no more than (i.e. at most) k swaps.

Input:
5
2 1
1 2
3 4
5 5
5 5 6 6 5
1 2 5 4 3
5 3
1 2 3 4 5
10 9 10 10 9
4 0
2 2 4 3
2 4 2 3
4 4
1 2 2 1
4 4 5 4

Output:
6
27
39
11
17
"""
cases = int(input())
for i in range(cases):
    sze, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    aSum = 0
    aindx = 0
    for j in range(sze - 1, -1, -1):
        temp1 = a[aindx]
        temp2 = b[j]
        if(temp1 > temp2):
            aSum += temp1
        else:
            if(k > 0):
                aSum += temp2
            else:
                aSum += temp1
            k -= 1
        aindx += 1
    print(aSum)