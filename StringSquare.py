"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/1619/A --------------

A string is called square if it is some string written twice in a row. 
For example, the strings "aa", "abcabc", "abab" and "baabaa" are square. 
But the strings "aaa", "abaaab" and "abcdabc" are not square.

For a given string s determine if it is square.

Input
The first line of input data contains an integer t (1 ≤ t ≤ 100) —the number of test cases.

This is followed by t lines, each containing a description of one test case. 
The given strings consist only of lowercase Latin letters and have lengths between 1 and 100 inclusive.

Output
For each test case, output on a separate line:

YES if the string in the corresponding test case is square,
NO otherwise.

You can output YES and NO in any case 
(for example, strings yEs, yes, Yes and YES will be recognized as a positive response).

Input:
10
a
aa
aaa
aaaa
abab
abcabc
abacaba
xxyy
xyyx
xyxy

Output:
NO
YES
NO
YES
YES
YES
NO
NO
NO
YES
"""
cases = int(input())
for i in range(cases):
    s = input()
    if(len(s) % 2 == 1):
        print("NO")
    else:
        middle = len(s)//2
        firstHalf = s[:middle]
        secondHalf = s[middle:]
        if(firstHalf == secondHalf):
            print("YES")
        else:
            print("NO")
