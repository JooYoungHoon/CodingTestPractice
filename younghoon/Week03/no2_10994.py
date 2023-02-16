# 백준 10994 별찍기

import sys

def star(N, line):
    if N == 1:
        print("*")
    else:
        stars = ['*' for _ in range(4*N-3)]
        
        # 처음과 마지막 줄
        if line == 0 or line == N-1:
            print(''.join(stars))
        
        # 홀수 번째 줄 and 중간지점 전
        elif line % 2 != 0 and line < 2*N-2:
            stars[]
        
        # 짝수 번째 줄
        else:
            pass
            

if __name__ == "__main__":
    # 입력
    N = int(input())

    # 별그리기
    for i in range(4*N-3):
        star(N, i)
            