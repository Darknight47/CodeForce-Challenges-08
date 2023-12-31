"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/426/A -----------

Sereja showed an interesting game to his friends. The game goes like that. 
Initially, there is a table with an empty cup and n water mugs on it. 
Then all players take turns to move. During a move, a player takes a non-empty 
mug of water and pours all water from it into the cup. If the cup overfills, 
then we assume that this player lost.

As soon as Sereja's friends heard of the game, they wanted to play it. 
Sereja, on the other hand, wanted to find out whether his friends can play the game 
in such a way that there are no losers. You are given the volumes of all mugs and the cup. 
Also, you know that Sereja has (n - 1) friends. Determine if Sereja's friends can play 
the game so that nobody loses.

Input
The first line contains integers n and s (2 ≤ n ≤ 100; 1 ≤ s ≤ 1000) — the number of mugs and 
the volume of the cup. The next line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 10). 
Number ai means the volume of the i-th mug.

Output
In a single line, print "YES" (without the quotes) if his friends can play in the described manner, 
and "NO" (without the quotes) otherwise.

Input:
3 4
1 1 1

Output:
YES
"""
n, s = map(int, input().split())
lst = sorted(list(map(int, input().split())))
friendSum = sum(lst)
friendSum -= lst[n - 1]
if(friendSum <= s):
    print("YES")
else:
    print("NO")