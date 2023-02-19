# 백준 10994 별찍기

import sys

if __name__ == "__main__":
    # 입력
    N = int(input())

    # 별그리기
    if N == 1:
        print("*")
    else:
        stars = ['*' for _ in range(4*N-3)]
        last = 4*N - 3
        mid = 2*N - 2
        for line in range(4*N-3):
            # 처음 줄
            if line == 0:
                print(''.join(stars))
                
            # 중간 이전 and 홀수 번째 줄
            elif line <= 2*N - 2 and line % 2 != 0:
                stars[line:last-line] = " "*(last-2*line)
                print(''.join(stars))

            # 중간 이전 and 짝수 번째 줄
            elif line <= 2*N - 2 and line % 2 == 0:
                stars[line:last-line] = "*"*(last-2*line)
                print(''.join(stars))
            
            # 중간 이후 and 홀수 번째 줄
            elif line > 2*N - 2 and line % 2 != 0:
                stars[2*mid-line:line] = " "*(2*(line-mid))
                print(''.join(stars))
            
            # 중간 이후 and 짝수 번째 줄
            elif line > 2*N -2 and line % 2 == 0:
                stars[2*mid-line:line] = "*"*(2*(line-mid))
                print(''.join(stars))