"""
------------- Link for the challenge: https://codeforces.com/contest/1915/problem/D ----------------

Lura was bored and decided to make a simple language using the five letters 
a, b, c, d, e. There are two types of letters:

vowels — the letters a and e. They are represented by V.
consonants — the letters b, c, and d. They are represented by C.
There are two types of syllables in the language: CV
(consonant followed by vowel) or CVC (vowel with consonant before and after). 
For example, ba, ced, bab are syllables, but aa, eda, baba are not.
A word in the language is a sequence of syllables. Lura has written a word 
in the language, but she doesn't know how to split it into syllables. Help her break the word into syllables.

For example, given the word bacedbab, it would be split 
into syllables as ba.ced.bab (the dot "." represents a syllable boundary).

Input
The input consists of multiple test cases. The first line contains an integer t
(1 ≤ t ≤ 100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n
(1 ≤ n ≤ 2⋅10^5) — the length of the word.

The second line of each test case contains a string consisting of n
lowercase Latin characters  — the word.

All words given are valid words in the language; that is, they only use the letters 
a, b, c, d, e, and each word is made up of several syllables.

The sum of n over all test cases does not exceed 2⋅10^5.

Output
For test case, output a string denoting the word split into syllables by inserting a dot "."
between every pair of adjacent syllables.

If there are multiple possible splittings, output any of them. 
The input is given in such a way that at least one possible splitting exists.

Input:
6
8
bacedbab
4
baba
13
daddecabeddad
3
dac
6
dacdac
22
dababbabababbabbababba

Output:
ba.ced.bab
ba.ba
dad.de.ca.bed.dad
dac
dac.dac
da.bab.ba.ba.bab.bab.ba.bab.ba
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    s = input()
    startIndx = sze - 1
    ans = []
    #output = ''
    while startIndx >= 0:
        first = s[startIndx]
        second = s[startIndx - 1] if startIndx - 1 >= 0 else ''
        third = s[startIndx - 2] if startIndx - 2 >= 0 else ''
        if(first == 'a' or first == 'e'):
            temp = second + first
            ans.append(temp)
            #output = temp + '.' + output if output else temp
            startIndx -= 2
        else:
            temp = third + second + first
            ans.append(temp)
            #output = temp + '.' + output if output else temp
            startIndx -= 3
    print('.'.join(reversed(ans)))