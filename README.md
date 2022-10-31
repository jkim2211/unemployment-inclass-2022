# unemployment-inclass-2022


## Setup


Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```


## Usage

Run an example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
#python app/unemployment.py

# or pass env var from command line:
#ALPHAVANTAGE_API_KEY="______" python app/unemployment.py

python -m app.unemployment
```

Run stocks report:

```sh
#python app/stocks.py

python -m app.stocks
```