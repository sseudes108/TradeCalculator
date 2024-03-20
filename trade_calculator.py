from trade_lib_view import (Header, DrawLine, GetInteger, GetFloat, GetText)
from trade_lib_calc import (PrintSellPoints)

Header("Trade Target Calculator")

tradeType = GetInteger("(1) Long (2) Short")

coin = GetText("What is the Coin?")
price = GetFloat("What is the price?")
amount = GetFloat("What is the amount of {} ?".format(coin))
lavarage = GetFloat("Whats is the Lavarage?")

amountToSell = amount * 0.25

#50%, 100%, 150% Roi
target501 = 50 / lavarage / 100
target502 = 100 / lavarage / 100
target503 = 150 / lavarage / 100

#75%, 125%, 200% Roi
target751 = 75 / lavarage / 100
target752 = 125 / lavarage / 100
target753 = 200 / lavarage / 100

if tradeType == 1:
    sellPoint501 = price + (price * target501)
    sellPoint502 = price + (price * target502)
    sellPoint503 = price + (price * target503)

    sellPoint751 = price + (price * target751)
    sellPoint752 = price + (price * target752)
    sellPoint753 = price + (price * target753)

else:
    sellPoint501 = price - (price * target501)
    sellPoint502 = price - (price * target502)
    sellPoint503 = price - (price * target503)

    sellPoint751 = price - (price * target751)
    sellPoint752 = price - (price * target752)
    sellPoint753 = price - (price * target753)

sellPoints50 = [sellPoint501, sellPoint502, sellPoint503]
sellPoints75 = [sellPoint751, sellPoint752, sellPoint753]

PrintSellPoints(sellPoints50, "50s", amountToSell, price, tradeType)

PrintSellPoints(sellPoints75, "75s", amountToSell, price, tradeType)

DrawLine()
