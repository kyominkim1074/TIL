#회문은 동일한 앞뒤로 읽는 단어 (예: eye, level)
#list slicing 메서드 활용
T = int(input())
for tc in range(1, T+1):
    word = input()
    if str(word) == str(word)[::-1]: # 문자열과 거꾸로 뒤집은 문자열이 같은 경우
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')