M = "".join(input().split())
if M[0] not in ("1", "8"):
    ans = "mixed"
elif M[1:] == "2345678":
    ans = "ascending"
elif M[1:] == "7654321":
    ans = "descending"
else:
    ans = "mixed"
print(ans)