import sys
sys.stdin = open("2304.txt")

N = int(input())

# tmp : 임시로 입력을 받기 위한 list, 전체 list의 길이를 모르기 때문에 임시로 저장한 뒤 최대 길이를 찾는다!
tmp = []
# n : 최대 길이를 비교하기 위한 변수
n = 0
for _ in range(N):
    # x : index, y : 높이, 여기서는 x가 중요
    x, y = map(int, input().split())
    if n < x:
        n = x
    tmp.append((x, y))

# 가장 큰 index 값만큼 list를 만들어준다
warehouse = [0] * (n + 1)

# tmp에 있는 값을 pop해서 warehouse의 x index값을 y로 변경
while tmp:
    x, y = tmp.pop()
    warehouse[x] = y

i = 1
# 최대 높이의 왼쪽과 오른쪽의 계산 방법이 정 반대이기 때문에 최대 높이를 구한다
m = warehouse.index(max(warehouse))
# i가 최대 높이 이전이라면
# 현재 위치의 왼쪽에 있는 값과 비교, 왼쪽 값이 클 경우 현재 위치의 값을 왼쪽 값으로 변경해준다.
while i < m:
    if warehouse[i] < warehouse[i-1]:
        warehouse[i] = warehouse[i-1]
    i += 1

# i가 최대 높이 이후라면
# 현재 위치의 오른쪽에 있는 값과 비교, 오른쪽 값이 클 경우 현재 위치의 값을 오른쪽 값으로 변경해준다.
i = n - 1
while m < i:
    if warehouse[i] < warehouse[i+1]:
        warehouse[i] = warehouse[i+1]
    i -= 1

print(sum(warehouse))
