from app.unemployment import format_pct, fetch_unemployment_data


def test_percent_sign_formatting():

    assert format_pct(3.65554) == '3.66%'

    assert format_pct(25.4) == '25.40%'


def test_fetch_data():
    # this function will return a list of datapoints
    data = fetch_unemployment_data()
    assert isinstance(data, list)

    # how did our program need to be referencing this data?
    # Challenge A seems to take the first item and print its value and date keys
    # the latest values and dates will change, so we can't test the exact values in this case
    # but we can at least test the structure:
    latest = data[0]
    assert isinstance(latest, dict)
    assert "date" in latest.keys()
    assert "value" in latest.keys()
    assert isinstance(latest["date"], str)
    assert isinstance(latest["value"], str) # NOTE: the rates are strings!!!

    # in this case, we do know what the earliest value is, so
    # we can test it for good measure, to give us a sense of the structure of each item in the list
    earliest = data[-1]
    assert earliest == {'date': '1948-01-01', 'value': '3.4'}

    # testing the second to last value could give us some clue about the frequency
    # here it looks like we are expecting monthly frequency
    assert data[-2] == {'date': '1948-02-01', 'value': '3.8'}