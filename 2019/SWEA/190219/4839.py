import sys
sys.stdin = open("4839.txt", "r")

for T in range(int(input())):
    PAB = list(map(int, input().split()))
    Ca, Cb = 0, 0
    Mida, Midb = 0, 0
    starta, startb, enda, endb = 1, 1, PAB[0], PAB[0]
    while Mida != PAB[1] and Midb != PAB[2]:
        Mida = (starta + enda) // 2
        Midb = (startb + endb) // 2
        if Mida > PAB[1]:
            enda = Mida
        elif Mida < PAB[1]:
            starta = Mida
        if Midb > PAB[2]:
            endb = Midb
        elif Midb < PAB[2]:
            startb = Midb
    if Mida == PAB[1] and Midb == PAB[2]:
        print("#{} 0".format(T+1))
    elif Mida == PAB[1]:
        print("#{} {}".format(T+1, "A"))
    else:
        print("#{} {}".format(T+1, "B"))
    