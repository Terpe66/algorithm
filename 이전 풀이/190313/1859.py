import sys
sys.stdin = open("1859.txt")

def find(i, day):
    max_val = 0
    i = idx
    while i < day:
        new = bs[i]
        if max_val < new:
            max_val = new
        i += 1
    return max_val

for t in range(int(input())):
    day = int(input())
    bs = list(map(int, input().split()))
    ans = idx = m_idx = 0
    max_val = find(idx, day)
    while m_idx < day:
        new = bs[m_idx]
        if new < max_val:
            ans -= new
        elif ans != 0 and new == max_val:
            ans += max_val * (m_idx - idx)
            idx = m_idx + 1
            max_val = find(idx, day)
        m_idx += 1

    if ans < 0:
        ans = 0
    print(f"#{t+1} {ans}")

