"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/1915/B -------------

A Latin square is a 3×3 grid made up of the letters A, B, and C such that:

in each row, the letters A, B, and C each appear once, and
in each column, the letters A, B, and C each appear once.

For example, one possible Latin square is shown below

You are given a Latin square, but one of the letters was replaced with a question mark ?. 
Find the letter that was replaced.

Input
The first line of the input contains a single integer t
(1≤t≤108) — the number of testcases.

Each test case contains three lines, each consisting of three characters, 
representing the Latin square. Each character is one of A, B, C, or ?.

Each test case is a Latin square with exactly one of the letters replaced with a question mark ?.

Output
For each test case, output the letter that was replaced.
"""
cases = int(input())
for i in range(cases):
    for j in range(3):
        temp = input()
        if(temp.count("?") > 0):
            if(temp.count("A") == 0):
                ans = "A"
            elif(temp.count("B") == 0):
                ans = "B"
            else:
                ans = "C"
            print(ans)