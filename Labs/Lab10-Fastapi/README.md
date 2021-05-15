## Big Data Systems and Int Analytics

## Lab 10 - Fast API

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001443824     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |

#### CLAAT Link

https://codelabs-preview.appspot.com/?file_id=1hPD8rfvHgngYOzO6de55sVfP1zi_Herdg5M6y83JCRM#0

### FastAPI

#### What is FastAPI? 

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

#### Requirements

```
pip3 install fastapi
pip3 install uvicorn
pip3 install iexfinance
```

#### Getting Started

Basic usage is available in `main.py`. Run the server with `uvicorn main:app --reload`. Go to `http://127.0.0.1:8000/docs` and you should see the interactive API documentation. This is a simple example that demonstrates the created API that can: 

- Receives HTTP requests in the paths / and /items/{item_id}.
- Both paths take GET operations (also known as HTTP methods).
- The path /items/{item_id} has a path parameter item_id that should be an int.
- The path /items/{item_id} has an optional str query parameter q
- By Clicking on the "Execute" button on the API interface, the user interface will communicate with your API, send the parameters, get the results and show them on the screen

#### Level UP! :arrow_up:

Let's work with an API that would potentially be used by a brokerage to keep a track of investors buying and selling on the stock-market, using their website/app. In addition to serving `PUT` and `GET` requests, the endpoint stores all data on DynamoDB. Create a table on DynamoDB with `id` as the primary key before running the server.

- `stock_price.py` - A simple Python script to get the current stock price of a given company. This requires an API token to query IEX Cloud and fetch the current stock price. Create a free developer account [here](https://iexcloud.io/). Once you have the account, go to `Home > API Tokens` and copy the `SECRET` token, and use your token in the `stock_price.py` script. 

- `id_generator.py` - Python script to generate a unique 10 digit alpha-numeric ID

- `trades.py` - Script to deploy the FastAPI endpoint. Use the created DynamoDB table in this script. Contains three routes:


Fetch the price of a given stock:
```
# Get the current stock price
@app.get("/stock_price/{name}")
```

Place Trades - Required params: `customer_id, name, qty, position`

```
# Place trades
@app.put("/trade/{customer_id}")
```

Get all trades for a given customer ID - Required params: `customer_id`
```
@app.get("/get_trades/{customer_id}")
```

Run the server with `uvicorn trades:app --reload`. Go to `http://127.0.0.1:8000/docs` and you should see the interactive API documentation.

