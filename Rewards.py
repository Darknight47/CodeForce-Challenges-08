"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/448/A -------------

Bizon the Champion is called the Champion for a reason.

Bizon the Champion has recently got a present — a new glass cupboard with n shelves and he decided 
to put all his presents there. All the presents can be divided into two types: medals and cups. 
Bizon the Champion has a1 first prize cups, a2 second prize cups and a3 third prize cups. 
Besides, he has b1 first prize medals, b2 second prize medals and b3 third prize medals.

Naturally, the rewards in the cupboard must look good, that's why Bizon the Champion decided to follow the rules:

any shelf cannot contain both cups and medals at the same time;
no shelf can contain more than five cups;
no shelf can have more than ten medals.

Help Bizon the Champion find out if we can put all the rewards so that all the conditions are fulfilled.

Input
The first line contains integers a1, a2 and a3 (0 ≤ a1, a2, a3 ≤ 100). 
The second line contains integers b1, b2 and b3 (0 ≤ b1, b2, b3 ≤ 100). 
The third line contains integer n (1 ≤ n ≤ 100).

The numbers in the lines are separated by single spaces.

Output
Print "YES" (without the quotes) if all the rewards can be put on the shelves in the described manner. 
Otherwise, print "NO" (without the quotes).

Input:
1 1 1
1 1 1
4

Output:
YES
"""
cups = sum(map(int, input().split()))
medals = sum(map(int, input().split()))
shelves = int(input())
ok = True
if(cups > 0):
    while shelves > 0:
        if(cups > 5):
            cups -= 5
        else:
            cups = 0
        shelves -= 1
        if(shelves <= 0 or cups <= 0):
            break
if((shelves <= 0 and medals > 0) or (shelves <= 0 and cups > 0)):
        ok = False
else:
    if(medals > 0):
        while shelves > 0:
            if(medals > 10):
                medals -= 10
            else:
                medals = 0
            shelves -= 1
            if(shelves <= 0 or medals <= 0):
                break
        if(medals > 0 and shelves <= 0):
            ok = False
print("YES" if ok else "NO")
        