# this is the "test/stocks_test.py" file...

from app.stocks import format_usd, fetch_stocks_data

from pandas import DataFrame



def test_usd_formatting():

    #assert 2 + 2 == 4

    assert format_usd(4.5) == "$4.50"

    assert format_usd(4.5555555) == "$4.56"

    assert format_usd(1234567890) == "$1,234,567,890.00"

    #assert format_usd("OOPS") == "______"



def test_data_fetching():
    result = fetch_stocks_data("NFLX")
    assert isinstance(result, DataFrame)

    assert "timestamp" in result.columns
    assert "adjusted_close" in result.columns
    assert "high" in result.columns
    assert "low" in result.columns


    assert len(result) >= 100
5:53
# this is the "app/stocks.py" file...


from pandas import read_csv

from app.alpha import API_KEY

def format_usd(my_price):
    return f"${my_price:,.2f}"


def fetch_stocks_data(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv"

    df = read_csv(request_url)

    return df



if __name__ == "__main__":

    print("STOCKS REPORT...")

    symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
    print("SYMBOL:", symbol)

    df = fetch_stocks_data(symbol)

    print(df.columns)
    print(df.head())
    #breakpoint()

    # CHALLENGE A:
    # print the latest closing date and price

    latest = df.iloc[0]

    #print(latest["timestamp"])
    #print(latest["close"])
    print("LATEST:", format_usd(latest["adjusted_close"]), "as of", latest["timestamp"])

    # Challenge B
    #
    # What is the highest high price (formatted as USD)?
    # What is the lowest low price (formatted as USD)?

    print("HIGH:", format_usd(df["high"].max()))
    print("LOW:", format_usd(df["low"].min()))