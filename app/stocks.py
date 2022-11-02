# this is the "app/stocks.py" file...

print("STOCKS REPORT...")

from pandas import read_csv
from app.alpha import API_KEY

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
print("SYMBOL:", symbol)

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv"

df = read_csv(request_url)
print(df.columns)
print(df.head())
#breakpoint()

# CHALLENGE A:
# print the latest closing date and price

latest = df.iloc[0]

#print(latest["timestamp"])
#print(latest["close"])
print("LATEST:", '${:,.2f}'.format(latest["adjusted_close"]), "as of", latest["timestamp"])

# Challenge B
#
# What is the highest high price (formatted as USD)?
# What is the lowest low price (formatted as USD)?

print("HIGH:", '${:,.2f}'.format(df["high"].max()))
print("LOW:", '${:,.2f}'.format(df["low"].min()))