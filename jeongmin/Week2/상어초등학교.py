"""

    [Baekjoon] https://www.acmicpc.net/problem/21608

    교실은 N×N 크기의 격자

     학생의 수는 N**2명

     학생은 1번부터 N**2번까지 번호

     (r, c)는 r행 c열을 의미한다.

     교실의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)

     배열 상으로 나타낸다면 (0, 0) ~ (N-1, N-1)

     학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사

     정해진 순서대로 학생의 자리

     한 칸에는 학생 한 명의 자리

     |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)

     이 인접한다고한다.

     r1, c1 <=> r2, c2

     위 아래 오른쪽 왼쪽

    맨하탄거리
     https://ko.wikipedia.org/wiki/%EB%A7%A8%ED%95%B4%ED%8A%BC_%EA%B1%B0%EB%A6%AC

     1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
     2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리
     3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
        그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.


    모든 자리에 대해 인접한 자리의 개수를 구하는 함수 (nearby)
    위치 인접한 자리의 개수

    가장 자리 => 2
    모서리를 제외한 가장자리 => 3
    가운데 N-1, N-1 의 정사각형 지역 => 4

"""
from collections import defaultdict


def get_nearby(room_size):
    """
        room_size : 교실의 크기
        return 교실 안 자리의 인접한 자리의 개수를 담은 2차원 배열
    """

    room = [[4] * room_size for _ in range(room_size)]

    # 모서리 부분
    for x in [0, room_size - 1]:
        for y in [0, room_size - 1]:
            room[y][x] = 2

    for x in range(1, room_size - 1):
        for y in [0, room_size - 1]:
            room[y][x] = 3

    for x in [0, room_size - 1]:
        for y in range(1, room_size - 1):
            room[y][x] = 3

    return room


def update(student_loc):
    global classroom, dx, dy

    r = student_loc[0]
    c = student_loc[0]

    classroom[r][c] = 0
    for idx, idy in zip(dx, dy):
        y = idy + r
        x = idx + x
        classroom[y][x] -= 1


def set_seat(student, init_flag, used):
    global student_in_room, student_info, dx, dy
    if init_flag:
        used[1][1] = 1
        r = 1
        c = 1
        init_flag = 0
        student_in_room.append(student)
        update([r, c])
        return [r, c], init_flag

    likes = student_info[student]

    for like in likes:
        if like in student_in_room:
            like_r = student_seat_info[like][0]
            like_c = student_seat_info[like][1]

            for idx, idy in zip(dx, dy):
                y = like_r + idy
                x = like_c + idx


    return [r, c], init_flag


if __name__ == '__main__':
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    N = int(input())
    classroom = get_nearby(N)
    used = [[0] * N for _ in range(N)]
    student_info = defaultdict(list)
    student_seat_info = defaultdict(list)
    student_in_room = []
    init = 1
    for _ in range(N ** 2):
        info = list(map(int, input().split()))
        student_info[info[0]] = info[1:]
        student_seat_info[info[0]], init = set_seat(info[0], init, used)
