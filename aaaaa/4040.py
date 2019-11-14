T = int(input())
for t in range(T):
    string = input()
    length = len(string)

    if string == "":
        print("#{} {}".format(t + 1, 0))
        continue
    if length == 1:
        print("#{} {}".format(t + 1, 1))
        continue

    mul = length
    i = 1
    while i < length + 1:
        cut = string[:i]
        if cut * mul == string:
            print("#{} {}".format(t + 1, mul))
            break
        i += 1
        while length % i:
            i += 1
        mul = length // i