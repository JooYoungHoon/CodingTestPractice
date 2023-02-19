# 백준 25046 기적의 매매법

import sys

def BNP(cash: int, stocks: list):
    my_stocks = 0
    for stock in stocks:
        # 주가가 보유 현금 보다 싼 경우 풀매수
        if stock <= cash:
            my_stocks += (cash // stock)
            cash -= (cash // stock)*stock
    return cash + my_stocks*stocks[-1]

def Timing(cash: int, stocks: list):
    my_stocks = 0
    uds = [0, 0, 0]
    for idx in range(0, 11):
        # 3일연속 상승
        if stocks[idx] < stocks[idx+1] and stocks[idx+1] < stocks[idx+2] and stocks[idx+2] < stocks[idx+3]:
            uds.append(-1)
        # 3일연속 하락
        elif stocks[idx] > stocks[idx+1] and stocks[idx+1] > stocks[idx+2] and stocks[idx+2] > stocks[idx+3]:
            uds.append(1)            
        # 그 외
        else:
            uds.append(0)
            
    for idx, stock in enumerate(stocks):
        # 3일연속 상승? 이건 풀매도
        if uds[idx] == -1 and my_stocks:
            cash += my_stocks*stock
            my_stocks = 0
        
        # 3일연속 하락? 이건 풀매수
        if uds[idx] == 1 and stock <= cash:
            my_stocks += (cash // stock)
            cash -= (cash // stock)*stock
    
    return cash + my_stocks*stocks[-1]

if __name__ == "__main__":
    # 준현이와 성민이의 보유 현금
    cash = int(input())
    # 머신덕 주가 리스트
    stocks = list(map(int, sys.stdin.readline().split()))

    # print(f'BNP: {BNP(cash, stocks)}    TIMING: {Timing(cash, stocks)}')

    if BNP(cash, stocks) > Timing(cash, stocks):
        print("BNP")
    elif BNP(cash, stocks) < Timing(cash, stocks):
        print("TIMING")
    else:
        print("SAMESAME")