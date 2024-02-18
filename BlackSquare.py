"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/1028/A -------------

Consider a table of size n×m, initially fully white. Rows are numbered 1 through n from top to bottom, 
columns 1 through m from left to right. Some square inside the table with odd side length was painted black. 
Find the center of this square.

Input
The first line contains two integers n
and m (1 ≤ n, m ≤ 115) — the number of rows and the number of columns in the table.

The i-th of the next n lines contains a string of m characters si1 si2 …sim 
(sij is 'W' for white cells and 'B' for black cells), describing the i-th row of the table.

Output
Output two integers r and c (1 ≤ r ≤ n, 1 ≤ c ≤ m) separated by a space — 
the row and column numbers of the center of the black square.

Input:
5 6
WWBBBW
WWBBBW
WWBBBW
WWWWWW
WWWWWW

Output:
2 4
"""
n , m = map(int, input().split())
arr = []
firstIndx = -1
lastIndx = -1
for i in range(n):
    arr.append(input())
firstFound = False
for j in range(n):
    tempLine = arr[j]
    if("B" in tempLine and not firstFound):
        firstIndx = j + 1
        firstFound = True
    elif("B" in tempLine and firstFound):
        lastIndx = j + 1
if(lastIndx > -1):
    row = (lastIndx + firstIndx) // 2
else:
    row = firstIndx
temp = arr[firstIndx - 1]
bsHalf = (temp.count("B") // 2 ) + 1
for c in range(m):
    tc = temp[c]
    if(tc == "B"):
        bsHalf -= 1
    if(bsHalf <= 0):
        col = c + 1
        break
print(row, col)