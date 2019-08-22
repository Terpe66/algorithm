import sys
sys.stdin = open("4865.txt", "r")

for T in range(int(input())):
    str1 = input()
    str2 = input()
    chardict = {}
    for char in str1:
        if char not in chardict:
            chardict[char] = 0
    for char in chardict:
        for i in range(len(str2)):
            if char == str2[i]:
                chardict[char] += 1
    val = 0
    for char in chardict:
        if chardict[char] > val:
            val = chardict[char]
    print("#{} {}".format(T+1, val))