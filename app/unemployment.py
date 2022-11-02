
# this is the "app/unemployment_report.py" file
import json
from pprint import pprint

import requests

from app.alpha import API_KEY


request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)

# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date? 
# Display the unemployment rate using a percent sign.

breakpoint()


data = parsed_response["data"][0]
print(latest)
print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
print(f"{data[0]['value']}%", "as of", data[0]["date"])

#Challenge B
#
#What is the average unemployment rate for all months during this calendar year? How many months are included?
from statistics import mean
this_year = [d for d in data if "2022-" in d["date"]]

rates_this_year = [float(d["value"]) for d in this_year]
print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
print("NO MONTHS:", len(this_year))

# Challenge C
# 
# Plot a line chart of unemployment rates over time.

from plotly.express import line

dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]

fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
fig.show()