"""

    [baekjoon] https://www.acmicpc.net/problem/12933

    울음 소리 'quack'

    순서는 quack
     quqacukqauackck와 같은 경우 두 오리가 울었다.

     qu qacuk qa uack ck
     quack
     quqauackck
     quack



"""
duck = {'q': 'u', 'u': 'a', 'a': 'c', 'c': 'k', 'k': 'q'}
full_sound = ['q', 'u', 'a', 'c', 'k']


def find_duck(s):
    cnt = 0
    i = 0
    temp = []
    flag = 0

    # 처음 소리가 q가 아닌 경우 -1 반환
    if s[i] != 'q':
        return -1

    while i < len(s):
        key = s[i]

        # temp가 비어있을 경우 처음 오는 소리가 q가 되도록함
        if not temp:
            if key == 'q':
                temp.append(s.pop(i))
            else:
                i += 1
            continue

        # temp에 소리가 있다면 다음 소리로 이어지는 소리가 차례로 오는지 확인
        if duck[temp[-1]] == key:
            temp.append(s.pop(i))
        else:
            i += 1

        # idx가 s의 마지막에 있을 경우 다음과 같이 확인
        if i == len(s):
            if len(temp) % 5 == 0:
                if temp[-1] == 'k':
                    cnt += 1
                    temp = []
                    i = 0
                else:
                    temp = []
                    i = 0
                    flag = 1
            else:
                temp = []
                i = 0
                flag = 1
    if s:
        return -1
    if temp:
        if temp != full_sound:
            return -1
    if flag:
        return -1

    return cnt


if __name__ == '__main__':
    sound = list(input())

    count = find_duck(sound)

    print(count)
