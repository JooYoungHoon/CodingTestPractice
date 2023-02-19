"""

    [Baekjoon] https://www.acmicpc.net/problem/20546

    준현이는

    주식 매수 후 오로지 기도만 하는 전략 => BNP

    주식을 살 수 있다면 무조건 매수한다.

    성민이는
    => 33 매매법

    모든 거래는 전량 매수와 전량 매도로 이루어짐

    빚을 내서 주식을 하지않는다.

    100 주가 11원 => 99원 전량 매수

    3일 연속 가격이 전일 대비 상승하는 주식은 다음날 무조건 가격이 하락한다고 가정함

    소유한 주식의 가격이 3일째 상승한다면 전량 매도


    3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가겨이 상승한다고 가정한다.

    이러한 경향이 나타나면 전량 매수한다.

    전일과 오늘의 주가가 동일하다면 가격이 상승한 것도 하락한것도 아니다.

    기간은 1월 1일 ~ 1월 14일까지

    자산 평가 방법은 ( 현금 + 1월 14일의 주가 + 주식 수)

"""


class Asset:
    invest_cond = 'Unknown'

    def __init__(self, money, count):
        """
        준현이와 성민이가 가지는 주식의 정보
        :param money:
        :param count:
        """
        self.stock_count = count
        self.cash = money
        self._price = None

    def set_price(self, stock_price):
        """
        현재 주식의 가격을 설정해주는 함수
        :param stock_price: 현재 주식 가격
        :return:
        """
        self._price = stock_price

    def buy(self, stock_price):
        """
        주식 cash내에서 전량 매수
        :param stock_price: 현재 주식 가격
        :return:
        """
        count = self.cash // stock_price

        self.cash -= (stock_price * count)
        self.stock_count += count

    def sell(self, stock_price):
        """
        가지고 있는 주식을 현재 주가에 맞춰 전량 매도
        :param stock_price: 현재 주가
        :return:
        """
        if not self.stock_count:
            return
        self.cash += (self.stock_count * stock_price)
        self.stock_count = 0
        return self.cash

    def total_asset(self):
        """
        가지고 있는 전 재산을 반환하는 함수
        :return: 전 재산
        """
        total = self.cash + (self.stock_count * self._price)
        return total

    """ 비교 함수 """
    def __lt__(self, other):
        return self.total_asset() < other.total_asset()

    def __eq__(self, other):
        return self.total_asset() == other.total_asset()

    def __gt__(self, other):
        return self.total_asset() > other.total_asset()

    def echo(self, other):
        """ 다른 자산과 비교하기 위한 방법 """
        if self > other:
            print(self.__class__.invest_cond)
        elif self < other:
            print(other.__class__.invest_cond)
        else:
            print("SAMESAME")


class Bnp(Asset):
    invest_cond = "BNP"

    def __init__(self, money, count):
        """
        Buy and Pray 투자 방법
        :param money: 초기 자본
        :param count: 초기 주식 수
        """
        self.buy_condition = 1
        self.cash = money
        self.stock_count = count

    def is_to_buy(self, stock_price):
        """
        BNP에 따라 살 수 있는 지 여부 반환
        :param stock_price: 현재 주가
        :return: True or False
        """
        if not self.buy_condition:
            return False

        if self.cash < stock_price:
            return False
        else:
            self.buy_condition = 0
            return True


class Timing(Asset):
    invest_cond = "TIMING"

    def __init__(self, money, count):
        """
        Timing 3일 주가 증가 감소 추세를 이용한 주식 매매 방법
        :param money: 초기 자본
        :param count: 초기 주가 수
        """
        self.cash = money
        self.stock_count = count
        self.is_up = 0
        self.price = None
        self.day = 0

    def update(self, stock_price):
        """
        매일마다 바뀌는 주가를 보며 주가 증가 감소 추세정보를 업데이트
        :param stock_price: 현재 주가
        :return:
        """
        if self.price is None:
            self.price = stock_price
            self.day = 0
            return

        if self.price < stock_price:
            if self.is_up <= 0:
                self.day = 0
                self.is_up = 1
            else:
                self.day += 1

        elif self.price > stock_price:
            if self.is_up >= 0:
                self.day = 0
                self.is_up = -1
            else:
                self.day += 1

        else:
            if self.is_up != 0:
                self.is_up = 0
            self.day = 0

        self.price = stock_price

    def is_to_buy(self, stock_price):
        """
        Timing 방법에 따른 매수 여부
        :param stock_price: 현재 주가
        :return: True or False
        """
        if self.cash < stock_price:
            return False
        if self.is_up == -1:
            if self.day == 2:
                return True

        return False

    def is_to_sell(self):
        """
        Timing 방법에 따른 매도 여부
        :return: True False
        """
        if self.is_up == 1:
            if self.day == 2:
                return True
        return False


if __name__ == "__main__":
    cash = int(input())
    stocks = list(map(int, input().split()))

    jun = Bnp(cash, 0)
    sung = Timing(cash, 0)

    for i in range(14):

        if jun.is_to_buy(stocks[i]):
            jun.buy(stocks[i])

        sung.update(stocks[i])

        if sung.is_to_buy(stocks[i]):
            sung.buy(stocks[i])

        if sung.is_to_sell():
            sung.sell(stocks[i])

    jun.set_price(stocks[-1])
    sung.set_price(stocks[-1])
    jun.echo(sung)
