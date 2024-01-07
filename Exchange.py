"""
---------- Link for the challenge: https://codeforces.com/contest/1919/problem/A ---------------

Alice and Bob are bored, so they decide to play a game with their wallets. Alice has a
coins in her wallet, while Bob has b coins in his wallet.

Both players take turns playing, with Alice making the first move. 
In each turn, the player will perform the following steps in order:

Choose to exchange wallets with their opponent, or to keep their current wallets.
Remove 1 coin from the player's current wallet. 
The current wallet cannot have 0 coins before performing this step.
The player who cannot make a valid move on their turn loses. 
If both Alice and Bob play optimally, determine who will win the game.

Input
Each test contains multiple test cases. The first line contains a single integer t
(1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The first and only line of each test case contains two integers a and b (1 ≤ a, b ≤ 10^9) — 
the number of coins in Alice's and Bob's wallets, respectively.

Output
For each test case, output "Alice" if Alice will win the game, and "Bob" if Bob will win the game.

Input:
10
1 1
1 4
5 3
4 5
11 9
83 91
1032 9307
839204 7281
1000000000 1000000000
53110 2024

Output:
Bob
Alice
Bob
Alice
Bob
Bob
Alice
Alice
Bob
Bob
"""
cases = int(input())
for i in range(cases):
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print("Bob")
    else:
        print("Alice")