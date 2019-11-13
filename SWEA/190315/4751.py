import sys
sys.stdin = open("4751.txt")

for t in range(int(input())):
    string = input()
    lens = len(string)

    # 각 값을 리스트에 넣어서 출력하는 방법, 글자까지 출력하는 for문 하나, 블링블링 역으로 출력하는 for문 하나
    ans = []
    ans.append("." + ".#.." * lens)
    ans.append("." + "#." * lens * 2)
    ans.append("#." + ".#.".join(string) + ".#")
    for i in range(3):
        print(ans[i])
    for i in range(1, -1, -1):
        print(ans[i])

    # 1) 일일이 출력하는 방법, print가 많아서 오래 걸리고 메모리도 많이 듦!
    # print(".", end="")
    # for _ in range(lens):
    #     print(".#.", end=".")
    # print()
    # print(".", end="")
    # for _ in range(lens):
    #     print("#.#.", end="")
    # print()
    # print("#", end="")
    # for char in string:
    #     print("." + char, end=".#")
    # print()
    # print(".", end="")
    # for _ in range(lens):
    #     print("#.#.", end="")
    # print()
    # print(".", end="")
    # for _ in range(lens):
    #     print(".#.", end=".")
    # print()
    #
    # # 2) 출력할 값을 변수에 넣어서 출력하는 방법
    # for t in range(int(input())):
    #     string = input()
    #     lens = len(string)
    #
    #     A = "." + ".#.." * lens
    #     B = "." + "#." * lens * 2
    #     string = "#." + ".#.".join(string) + ".#"
    #
    #     print(A)
    #     print(B)
    #     print(string)
    #     print(B)
    #     print(A)