"""
------------- Link for the challenge: https://codeforces.com/contest/1878/problem/B --------------

After the Serbian Informatics Olympiad, Aleksa was very sad, because he didn't win a medal (he didn't know stack), 
so Vasilije came to give him an easy problem, just to make his day better.

Vasilije gave Aleksa a positive integer n
(n ≥ 3) and asked him to construct a strictly increasing array of size n of positive integers, such that

3⋅ai+2 is not divisible by ai+ai+1 for each i (1 ≤ i ≤ n−2).
Note that a strictly increasing array a of size n is an array where ai<ai+1 for each i (1 ≤ i ≤ n−1).
Since Aleksa thinks he is a bad programmer now, he asked you to help him find such an array.

Input
Each test consists of multiple test cases. The first line contains a single integer t
(1 ≤ t ≤ 10^4) — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 2⋅10^5) — the number of elements in array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output n integers a1,a2,a3,…,an (1 ≤ ai ≤ 10^9).

It can be proved that the solution exists for any n. 
If there are multiple solutions, output any of them.

"""
cases = int(input())
for i in range(cases):
    n = int(input())
    tempSum = 0
    indx = 1
    while n > 0:
        print(indx, end= ' ')
        n -= 1
        indx += 2
    print()