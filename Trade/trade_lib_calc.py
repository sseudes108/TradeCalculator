from trade_lib_view import (Header)

def PrintSellPoints(sellPoints, header, amountToSell, price, tradeType):
    index = 1
    profits = 0
    cost = amountToSell * price

    Header(header)
    print("Amount to sell each target:", amountToSell)
    print("Paid Price: ", cost)
    print(" ")

    for sellpoint in sellPoints:
        faturado = amountToSell * sellpoint
        profit = faturado - cost

        if tradeType != 1:
            profit *= -1
        
        profits += profit

        profit = '${:,.6f}'.format(profit)

        print("Target",index,":", '${:,.9f}'.format(sellpoint))
        print("Faturado: ${}. Profit: {}".format(faturado, profit))
        print("Profits til this moment: ",'${:,.4f}'.format(profits))
        index += 1

        print(" ")