
for i in range(dump):
    while cnt[MinIdx] == 0:
        MinIdx += 1
    while cnt[MaxIdx] == 0:
        MaxIdx -= 1
    if i == dump:
        break
    cnt[MinIdx] -= 1
    cnt[MinIdx + 1] += 1
    cnt[MaxIdx] -= 1
    cnt[MaxIdx - 1] += 1          