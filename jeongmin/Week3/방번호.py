"""

    방번호를 플라스틱 숫자로 나타냄
    필요한 세트의 최소숫자를 출력

    6은 9를 뒤집어서 이용가능 9는 6을 뒤집어서 이용가능

    9696 => 9, 6 두개 사용
    96 => 1개
    9999 => 1개 => 9, 6

"""


def add_card(card):
    for k in card.keys():
        card[k].append(k)
    return card


def solve(number):
    card = {x: [x] for x in range(10)}
    # card[6].append(9)
    # card[9].append(6)
    # visited = [0] * 11
    count = 1
    while number:
        num = number.pop(0)
        if num == 6:
            if card[6]:
                card[6].pop(0)
                continue
            elif card[9]:
                card[9].pop(0)
                continue
            card = add_card(card)
            card[num].pop(0)
            count += 1
            continue
        if num == 9:
            if card[9]:
                card[9].pop(0)
                continue
            elif card[6]:
                card[6].pop(0)
                continue
            card = add_card(card)
            card[num].pop(0)
            count += 1
            continue
        if card[num]:
            card[num].pop(0)
        else:
            card = add_card(card)
            card[num].pop(0)
            count += 1

    return count


if __name__ == '__main__':
    N = list(map(int, input()))

    print(solve(N))
