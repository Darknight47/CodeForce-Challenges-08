"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/1411/A ----------------

You have been assigned to develop a filter for bad messages in the in-game chat. 
A message is a string S of length n, consisting of lowercase English letters and characters ')'. 
The message is bad if the number of characters ')' at the end of the string strictly greater 
than the number of remaining characters. For example, the string ")bc)))" has three parentheses 
at the end, three remaining characters, and is not considered bad.

Input
The first line contains the number of test cases t (1 ≤ t ≤ 100). Description of the t test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 100). 
The second line of each test case contains a string Sof length n, consisting of lowercase English letters and characters ')'.

Output
For each of t test cases, print "Yes" if the string is bad. Otherwise, print "No".

You can print each letter in any case (upper or lower).

Input:
5
2
))
12
gl))hf))))))
9
gege)))))
14
)aa))b))))))))
1
)

Output:
Yes
No
Yes
Yes
Yes
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    s = input()
    parns = 0
    for j in range(sze - 1, -1, -1):
        t = s[j]
        if(t == ')'):
            parns += 1
        else:
            break
    beforeParns = sze - parns
    print("YES" if parns > beforeParns else "NO")