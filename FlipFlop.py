"""
----------------- Link for the challenge: https://codeforces.com/problemset/problem/1778/A -------------

You are given an array of n integers a1,a2,…,an. The integers are either 1 or −1. 
You have to perform the following operation exactly once on the array a:

Choose an index i (1 ≤ i < n) and flip the signs of a(i) and a(i)+1. 
Here, flipping the sign means −1 will be 1 and 1 will be −1.
What is the maximum possible value of a1+a2+…+an after applying the above operation?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). 
Description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 10^5), the length of the array a.

The next line contains n integers a1,a2,…,an (a(i)=1 or a(i)=−1).

The sum of n over all cases doesn't exceed 10^5.

Output
For each test case, print the maximum possible sum of the array a you can get in a separate line.

Input:
4
5
-1 1 1 -1 -1
5
1 1 -1 -1 -1
2
1 1
4
1 -1 -1 1

Output:
3
3
-2
4
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    fw = False
    for j in range(sze - 1):
        first = lst[j]
        second = lst[j + 1]
        if(first == -1 and second == -1):
            lst[j] = 1
            lst[j + 1] = 1
            fw = True
            break
    if(not fw):
        for j in range(sze - 1):
            first = lst[j]
            second = lst[j + 1]
            if((first == 1 and second == -1) or (first == -1 and second == 1)):
                lst[j] = 1 if lst[j] < 0 else -1
                lst[j + 1] = 1 if lst[j + 1] < 0 else -1
                fw = True
                break
        if(not fw):
            lst[0] = 1 if lst[0] < 0 else -1
            lst[1] = 1 if lst[1] < 0 else -1
    ans = sum(lst)
    print(ans)