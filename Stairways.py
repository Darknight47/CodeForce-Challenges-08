"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1005/A -------------

Little girl Tanya climbs the stairs inside a multi-storey building. Every time Tanya climbs a stairway, 
she starts counting steps from 1 to the number of steps in this stairway. 
She speaks every number aloud. For example, if she climbs two stairways, the first of which contains 3
steps, and the second contains 4 steps, she will pronounce the numbers 1,2,3,1,2,3,4.

You are given all the numbers pronounced by Tanya. How many stairways did she climb? 
Also, output the number of steps in each stairway.

The given sequence will be a valid sequence that Tanya could have pronounced 
when climbing one or more stairways.

Input
The first line contains n (1 ≤ n ≤ 1000) — the total number of numbers pronounced by Tanya.

The second line contains integers a1,a2,…,an (1 ≤ a(i) ≤ 1000) — 
all the numbers Tanya pronounced while climbing the stairs, in order from the first 
to the last pronounced number. 
Passing a stairway with x steps, she will pronounce the numbers 1,2,…,x in that order.

The given sequence will be a valid sequence that Tanya could have pronounced when 
climbing one or more stairways.

Output
In the first line, output t — the number of stairways that Tanya climbed. In the second line, output t numbers — 
the number of steps in each stairway she climbed. Write the numbers in the correct order of 
passage of the stairways.

Input:
7
1 2 3 1 2 3 4

Output:
2
3 4 
"""
sze = int(input())
lst = list(map(int, input().split()))
stairs = []
for i in range(sze):
    tmp = lst[i]
    if(tmp == 1):
        stairs.append([1])
    else:
        stairs[len(stairs) - 1].append(tmp)
print(len(stairs))
for lst in stairs:
    print(lst[len(lst) - 1], end= " ")