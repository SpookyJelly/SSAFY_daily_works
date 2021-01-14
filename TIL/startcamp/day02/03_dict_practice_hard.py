# 미니 실습2

coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13'
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28'
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51'
    }
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.

max_price = coin['BTC']['max_price']
print(max_price)

max_price_2 = coin.get('BTC').get('max_price') #이런식으로 get 함수를 이용해서 출력해도 된다
#               여기가 BTC.get('max_price')가 된다.

# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.

B_price = int(coin.get('BTC').get('opening_price'))
X_price = float(coin.get('XRP').get('opening_price'))
print(B_price + X_price)