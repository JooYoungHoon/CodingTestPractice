# 백준 1475 방번호

import sys
import math

if __name__ == "__main__":
    # 입력
    room_num = list(str(input()))

    # 플라스틱 숫자
    nums = [0 for _ in range(10)]
    
    # 방번호 확인
    for num in room_num:
        num = int(num)
        if num == 6 or num == 9:
            nums[6] += 0.5
        else:
            nums[num] += 1
            
    # 6, 9는 중복 가능
    nums[6] = math.ceil(nums[6])
    
    # 정답
    print(max(nums))