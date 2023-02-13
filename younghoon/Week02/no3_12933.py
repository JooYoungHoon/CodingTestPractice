# 백준 12933 오리

import sys

def find_duck(record: list):
    # 오리 울음소리를 저장할 2차원 배열(row: 최대 오리 수, column: 녹음된 울음 소리 길이)
    duck_max = [['_' for _ in range(len(record))] for _ in range(len(record)//5)]

    # 오리가 발음한 단어(duck)와 그때까지 말했어야할 단어(duck_said) 배열
    duck_said = ['', 'q', 'qu', 'qua', 'quac']
    duck = ['q', 'u', 'a', 'c', 'k']

    # 찾은 오리 수 (-1인 경우 잘못 녹음)
    ducks = 0
    
    # 잘못 녹음 된 경우 체크
    if record[-1] == 'k':
        wrong_record = False
    else:
        wrong_record = True

    # 녹음파일 확인
    for idx, duck_say in enumerate(record):
        # 녹음 오류 확인용 임시 변수
        check = 0

        # 오리 발음에 해당하는 duck index 확인
        duck_idx = duck.index(duck_say)
        # print(idx, duck_idx, duck_said[duck_idx], ''.join(duck_max[0]).replace('_', ''))
        for i, row in enumerate(duck_max):
            if duck_said[duck_idx] == ''.join(row).replace('_', '').replace('quack', ''):
                duck_max[i][idx] = duck_say
                check += 1
                # 오리 마리수 확인
                if ducks <= i+1:
                    ducks = i+1
                break
            else:
                check = 0

        # 잘못 녹음된 경우 확인
        if check == 0:
            wrong_record = True

        # 잘못 녹음된 경우 break
        if wrong_record:
            ducks = -1
            break
    return ducks

if __name__ == "__main__":
    # 입력
    record = list(str(input()))
    
    # 정답 확인
    answer = find_duck(record)

    # 정답 출력
    print(answer)