input_str = list(input())

result = [-1] * 26

for i in range(len(input_str)):   #ord()는 문자의 유니코드 정수값을 반환함
    check = ord(input_str[i]) - ord('a') #각 알파벳을 0~26 인덱스값으로 변경
    if result[check] == -1:
        result[check] = i

print(' '.join(map(str, result)))