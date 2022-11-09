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


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage (i.e. `ALPHAVANTAGE_API_KEY`).

Also sign up for the [SendGrid Service](https://sendgrid.com/), verify your single sender address (i.e. `SENDER_EMAIL_ADDRESS`), and obtain an API Key (i.e. `SENDGRID_API_KEY`). See these [setup notes](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md#setup) for more details.

Then create a local ".env" file and provide the keys like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
SENDER_EMAIL_ADDRESS="you@example.com"
SENDGRID_API_KEY="__________"
```


## Usage

Run an example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
python -m app.unemployment
```

Run stocks report:

```sh
python -m app.stocks
```


### Email Sending

Run the email service to send an example email and see if everything is working:

```sh
python -m app.email_service
```

Send the unemployment report via email:

```sh
python -m app.unemployment_email
```

Send the stocks report via email:

```sh
python -m app.stocks_email

# or in production mode:
APP_ENV="production" DEFAULT_SYMBOL="GOOGL" python -m app.stocks_email
```

## Testing

Run tests:

```sh
pytest
```