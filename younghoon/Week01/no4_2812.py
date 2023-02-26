# 백준 2812 크게 만들기

# 내 풀이 (시간초과)
# def make_large(num):
#     answer = ''

#     # 처음부터 K+1개씩 확인하면서 가장 큰 값을 반환
#     for idx in range(N-K):
#         max_num = max(num[idx:idx+K+1])
#         max_num_idx = num.index(max_num)
#         answer += max_num
#         # 가장 큰 값을 찾으면 앞의 숫자는 무시
#         for i in range(idx, max_num_idx+1):
#             num[i] = '0'
        
#     print(answer)

# 해설 참고
def make_large(num):
    find_large = []
    dump = 0
    # 숫자 탐색
    for n in num:
        # 찾은 바로 이전 수와 현재 수를 비교하여 현재 수가 더 크면 이전 수를 제외 (단, 버린 수가 K개 이상이면 확인 X)
        while dump < K and find_large and find_large[-1] < n:
            find_large.pop()
            dump += 1

        # 숫자 K개를 버려 N-K의 숫자를 얻을 때 까지 원래 숫자에서 하나씩 append
        if len(find_large) < N-K:
            find_large.append(n)
    print("".join(find_large))
    exit(0)
        

if __name__ == "__main__":
    # 입력
    N, K = map(int, input().split())

    # 입력 N자리수
    num = list(input())

    # 정답 출력
    make_large(num)
