"""
------------- Link for the challenge: https://codeforces.com/problemset/problem/1894/A --------------

Let's consider a game in which two players, A and B, participate. 
This game is characterized by two positive integers, X and Y.

The game consists of sets, and each set consists of plays. In each play, exactly one of the players, either A or B, 
wins. A set ends exactly when one of the players reaches X
wins in the plays of that set. This player is declared the winner of the set. 
The players play sets until one of them reaches Y wins in the sets. 
After that, the game ends, and this player is declared the winner of the entire game.

You have just watched a game but didn't notice who was declared the winner. You remember that during the game, n
plays were played, and you know which player won each play. However, you do not know the values of X and Y. 
Based on the available information, determine who won the entire game — A or B. 
If there is not enough information to determine the winner, you should also report it.

Input
Each test contains multiple test cases. The first line contains a single integer t
(1 ≤ t ≤ 10^4) - the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 20) - the number of plays played during the game.

The second line of each test case contains a string s
of length n, consisting of characters A and B. If s(i)=A, 
it means that player A won the i-th play. If s(i)=B, it means that player B won the i-th play.

It is guaranteed that the given sequence of plays corresponds to 
at least one valid game scenario, for some values of X and Y.

Output
For each test case, output:

A — if player A is guaranteed to be the winner of the game.
B — if player B is guaranteed to be the winner of the game.
? — if it is impossible to determine the winner of the game.

Input:
7
5
ABBAA
3
BBB
7
BBAAABA
20
AAAAAAAABBBAABBBBBAB
1
A
13
AAAABABBABBAB
7
BBBAAAA

Output:
A
B
A
B
A
B
A
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    game = input()
    print(game[-1])