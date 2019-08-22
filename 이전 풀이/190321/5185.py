import sys
sys.stdin = open("5185.txt")

# book = {
#     '0': '0000',
#     '1': '0001',
#     '2': '0010',
#     'F': '1111',
#     '10': '1010'
# }

for t in range(int(input())):
    N, hex_num = input().split()
    full = ""
    for num in hex_num:
        num = int(num, 16)
        go = ""
        for i in range(3, -1, -1):
            if num & (1 << i):
                go += "1"
            else:
                go += "0"
        full += go

    full2 = ""
    for num in hex_num:
        num = format(int(num, 16), "04b")
        full2 += num

    print(f"#{t + 1} {full} {full2}")
