"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/1604/A --------------

Shohag has an integer sequence a1,a2,…,an. 
He can perform the following operation any number of times (possibly, zero):

Select any positive integer k (it can be different in different operations).
Choose any position in the sequence (possibly the beginning or end of the sequence, 
or in between any two elements) and insert k into the sequence at this position.
This way, the sequence a changes, and the next operation is performed on this changed sequence. 
For example, if a=[3,3,4] and he selects k=2, then after the operation he can obtain one of the sequences [2,3,3,4], [3,2,3,4], [3,3,2,4], or [3,3,4,2].

Shohag wants this sequence to satisfy the following condition: for each 1≤i≤|a|, ai≤i. 
Here, |a| denotes the size of a.

Help him to find the minimum number of operations that he has to perform to achieve this goal. 
We can show that under the constraints of the problem it's always possible to achieve this goal 
in a finite number of operations.

Input
The first line contains a single integer t (1 ≤ t ≤ 200)  — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the initial length of the sequence.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the elements of the sequence.

Output
For each test case, print a single integer  — the minimum number of operations needed to 
perform to achieve the goal mentioned in the statement.

Input:
4
3
1 3 4
5
1 2 5 7 4
1
1
3
69 6969 696969

Output:
1
3
0
696966
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    indx = 1
    ans = 0
    for j in range(sze):
        temp = arr[j]
        if(temp > indx):
            diff = temp - indx
            if(diff > ans):
                ans = diff
        indx += 1
    print(ans)