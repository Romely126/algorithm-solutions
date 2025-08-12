import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline())) 

num.sort()

for i in num:
    print(i)

#기존 방식대로 구현하면 시간 초과가 발생한다
#최대조건에서는 수가 매우 크기 때문.
#input()은 개행문자를 삭제한 값을 리턴, 작은 부하가 될 수 O
#따라서 sys.stdin.readline()을 사
