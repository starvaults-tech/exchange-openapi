---
description: >-
  According to the CCXT content of bitwind, the following functional interfaces
  can be used directly
---

# CCXT User Guide

### Public

#### 1. Test connect public\_get\_ping()

Testing REST API connectivity

```
# Test python document (test_bitwind.py)
import ccxt  

# init exchange
exchange = ccxt.bitwind()

# public_get_sapi_v2_ping
 try:
     markets = exchange.public_get_ping()
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_ping:", str(e))
```

{% tabs %}
{% tab title="200: OK " %}
```javascript
{}
```
{% endtab %}
{% endtabs %}

#### 2.Server Time public\_get\_time()

Get server time

```
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()

# public_get_sapi_v2_time
 try:
     markets = exchange.public_get_time()
 except Exception as e:
     print("Error public_get_sapi_v2_time:", str(e))
```

{% tabs %}
{% tab title="200: OK " %}
```javascript
{
    "timezone": "GMT+08:00",
    "serverTime": 1595563624731
}
```
{% endtab %}
{% endtabs %}

#### 3.Currency pair List, fetchMarkets()

The set of currency pairs supported by the exchange

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()

# public_get_sapi_v2_symbol
 try:
     markets = exchange.fetchMarkets()
 except Exception as e:
     print("Error public_get_sapi_v2_symbol:", str(e))
```

{% tabs %}
{% tab title="200: OK " %}
```javascript
{
    "symbols": [
        {
            "quantityPrecision": 3,
            "symbol": "sccadai",
            "pricePrecision": 6,
            "baseAsset": "SCCA",
            "quoteAsset": "DAI",
            "limitAmountMin": "100",
            "limitPriceMin": "123.45",
            "limitVolumeMin": "10",
            "feeRateMaker": "0.002",
            "feeRateTaker": "0.002"
        },
        {
            "quantityPrecision": 8,
            "symbol": "btcusdt",
            "pricePrecision": 2,
            "baseAsset": "BTC",
            "quoteAsset": "USDT",
            "limitAmountMin": "100",
            "limitPriceMin": "123.45",
            "limitVolumeMin": "10",
            "feeRateMaker": "0.002",
            "feeRateTaker": "0.002"
        }
    ]
}
```
{% endtab %}
{% endtabs %}

**Response**

<table><thead><tr><th width="154">Name</th><th>Type</th><th>Example</th><th>Description</th></tr></thead><tbody><tr><td>symbol</td><td>string</td><td><code>BTCUSDT</code></td><td>Currency Pair Name</td></tr><tr><td>baseAsset</td><td>string</td><td><code>BTC</code></td><td>Base currency</td></tr><tr><td>quoteAsset</td><td>string</td><td><code>USDT</code></td><td>Quote currency</td></tr><tr><td>pricePrecision</td><td>integer</td><td><code>2</code></td><td>Price accuracy</td></tr><tr><td>quantityPrecision</td><td>integer</td><td><code>6</code></td><td>Volume accuracy</td></tr><tr><td>limitAmountMin</td><td>String</td><td>100</td><td>Limit Order Minimum Order Amount</td></tr><tr><td>limitPriceMin</td><td>String</td><td>100</td><td>limit order minimum price</td></tr><tr><td>limitVolumeMin</td><td>String</td><td>100</td><td>Minimum order quantity for limit orders</td></tr><tr><td>baseAssetName</td><td>String</td><td>BTC</td><td>Base currency display name</td></tr><tr><td>quoteAssetName</td><td>String</td><td>USDT</td><td>Quote Currency Display Name</td></tr><tr><td>SymbolName</td><td>String</td><td>BTC/USDT</td><td>Currency Pair Display Name</td></tr><tr><td>feeRateMaker</td><td>String</td><td>0.002</td><td>maker handling rate</td></tr><tr><td>feeRateMaker</td><td>String</td><td>0.002</td><td>taker handling rate</td></tr></tbody></table>

#### 4.Order book, fetchOrderBook()

Market order book depth information

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.fetchOrderBook({'symbol':'BTC/USDT'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

Query Parameters

| Name                                     | Type    | Description              |
| ---------------------------------------- | ------- | ------------------------ |
| limit                                    | integer | Default 100; Maximum 100 |
| symbol<mark style="color:red;">\*</mark> | String  | Pair Name e.g. BTC/USDT  |

{% tabs %}
{% tab title="200: OK Successful Obtain info  " %}
```javascript
{
  "bids": [
    [
      "3.90000000",   // price
      "431.00000000"  // volume
    ],
    [
      "4.00000000",
      "431.00000000"
    ]
  ],
  "asks": [
    [
      "4.00000200",  // price
      "12.00000000"  // volume
    ],
    [
      "5.10000000",
      "28.00000000"
    ]
  ]
}
```
{% endtab %}
{% endtabs %}

**Response:**

| time | long | `1595563624731` | Current Time(Unix Timestamp, ms) |
| ---- | ---- | --------------- | -------------------------------- |
| bids | list | as follow       | Order boot buy info              |
| asks | list | as follow       | Order boot sell info             |

The information corresponding to bids and asks represents all the prices of the order book and the quantities corresponding to the prices, sorted from top to bottom by the best price.

| ' ' | float | `131.1` | price                                       |
| --- | ----- | ------- | ------------------------------------------- |
| ' ' | float | `2.3`   | Quantity corresponding to the current price |

#### 5.market ticker, fetchTicker()

24-hour price change data

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.fetchTicker({'symbol':'BTC/USDT'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

Parameters symbol and symbols are both provided, then symbol is preferred. If neither is provided, all ticker data for symbols is returned.

| Name    | Type   | Description                                                                                                                         |
| ------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| symbol  | String | Pair name E.g. `BTC/USDT (if this parameter is not passed, the api takes up a lot of weight and the return structure is different)` |
| symbols | String | Pair names, multiple pairs separated by commas btcusdt,ethusdt                                                                      |

{% tabs %}
{% tab title="200: OK Ticker information retrieved successfully (with symbol)" %}
```javascript
{
    "high": "9279.0301",
    "vol": "1302",
    "last": "9200",
    "low": "9279.0301",
    "rose": "0",
    "time": 1595563624731,
    "symbol": "btcusdt",
    "amount": "3213",
    "askPrice": "123",
    "askVolume": "213213"
    "bidPrice": "12323",
    "bidVolume": "213213"
}
```
{% endtab %}

{% tab title="200: OK Ticker information retrieved successfully (without symbol) " %}
```javascript
[
    {
        "high": "9279.0301",
        "vol": "1302",
        "last": "9200",
        "low": "9279.0301",
        "rose": "0",
        "time": 1595563624731
        "symbol": "btcusdt",
        "amount": "3213",
        "askPrice": "123",
        "askVolume": "213213"
        "bidPrice": "12323",
        "bidVolume": "213213"
    }
]
```
{% endtab %}
{% endtabs %}

**Response:**

| time      | long   | `1595563624731` | timestamp                             |
| --------- | ------ | --------------- | ------------------------------------- |
| high      | float  | `9900`          | highest price                         |
| low       | float  | `8800.34`       | lowest price                          |
| open      | float  | `8700`          | open price                            |
| last      | float  | `8900`          | latest price                          |
| vol       | float  | `4999`          | Trading volume                        |
| rose      | float  | 0               | rise and fall price                   |
| symbol    | String | btcusdt         | currency pair                         |
| amount    | String | 1233            | Turnover, denominated currency volume |
| askPrice  | String | 23321           | First sell price                      |
| askVolume | String | 3321            | First sell volume                     |
| bidPrice  | String | 21              | First buy price                       |
| bidVolume | String | 12              | First buy volume                      |

#### 6.Recent deal, public\_get\_trades()

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.public_get_trades({'symbol':'BTC/USDT','limit':1})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

| Name                                     | Type   | Description                  |
| ---------------------------------------- | ------ | ---------------------------- |
| symbol<mark style="color:red;">\*</mark> | String | Currency pair E.g.`BTC/USDT` |
| limit                                    | String | Default 100 Maximum 1000     |

{% tabs %}
{% tab title="200: OK success" %}
```javascript
{
    "list":[
        {
            "price":"3.00000100",
            "qty":"11.00000000",
            "time":1499865549590,
            "side":"BUY"
        }
    ]
}
```
{% endtab %}
{% endtabs %}

**Response:**

| price | float  | `0.055`         | Trading price     |
| ----- | ------ | --------------- | ----------------- |
| time  | long   | `1537797044116` | Timestamp (ms)    |
| qty   | float  | `5`             | volume            |
| side  | string | `BUY/SELL`      | Active order side |

#### 7.K-line/Candlestick Data fetchOHLCV()

```python
# Test python document (test_bitwind.py)
import ccxt

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.fetchOHLCV({'symbol':'BTC/USDT','interval':'1min'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

| Name                                       | Type   | Description                                                                                                                                   |
| ------------------------------------------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| symbol<mark style="color:red;">\*</mark>   | ​      | currency pair name E.g.`BTC/USDT`                                                                                                             |
| interval<mark style="color:red;">\*</mark> | String | k-chart intervals, the value of the recognizable send is:`1min`,`5min`,`15min`,`30min`,`60min`,`1day`,`1week`,`1month`（min，h, day，week，month） |
| startTime                                  | long   | Start timestamp                                                                                                                               |
| endTime                                    | long   | End timestamp                                                                                                                                 |

{% tabs %}
{% tab title="200: OK success" %}
```javascript
[
    {
        "high": "6228.77",
        "vol": "111",
        "low": "6228.77",
        "idx": 1594640340,
        "close": "6228.77",
        "open": "6228.77"
    }
]
```
{% endtab %}
{% endtabs %}

**Response:**

| `idx` | long  | `1538728740000` | Timestamp（ms）          |
| ----- | ----- | --------------- | ---------------------- |
| open  | float | `36.00000`      | opening price          |
| close | float | `33.00000`      | closing price          |
| high  | float | `36.00000`      | height price           |
| low   | float | `30.00000`      | lowest price           |
| vol   | float | `2456.111`      | <p>Deal volume<br></p> |

### Trading

**Type of security: TRADE**

The interfaces below the transaction all require signatures and API-Key validation

#### 8.Create order, createOrder()

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.createOrder({'symbol':'BTC/USDT','volume':'0.01','side':'BUY','type':'MARKET'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

CommentShare feedback on the editor

| Parameter   | Type    | Description  |
| ----------- | ------- | ------------ |
| X-CH-SIGN   | string  | Signature    |
| X-CH-APIKEY | string  | user API-Key |
| X-CH-TS     | integer | timestamp    |

**Request Body**

|                                          |         |                                                                                                  |
| ---------------------------------------- | ------- | ------------------------------------------------------------------------------------------------ |
| symbol                                   | String  | Currency pair E.g.`BTC/USDT`                                                                     |
| volume<mark style="color:red;">\*</mark> | number  | Order volume                                                                                     |
| side<mark style="color:red;">\*</mark>   | String  | Order side ,`BUY/SELL`                                                                           |
| type<mark style="color:red;">\*</mark>   | String  | Order type,`LIMIT/MARKET/FOK/POST_ONLY/IOC/STOP`                                                 |
| price                                    | number  | Order price, must be sent for LIMIT orders                                                       |
| newClientOrderId                         | String  | Client Order Identification                                                                      |
| recvwindow                               | integer | Time window                                                                                      |
| triggerPrice                             | number  | Take Profit or Stop Loss ,Trigger Price (when type is STOP, price and triggerPrice are required) |

{% tabs %}
{% tab title="200: OK" %}
```javascript
{
    'symbol': 'LXTUSDT', 
    'orderId': '150695552109032492', //Order id(Long type)
    'clientOrderId': '157371322565051',
    'transactTime': '1573713225668', 
    'price': '0.005452', 
    'origQty': '110', 
    'executedQty': '0', 
    'status': '0',
    'type': 'LIMIT', 
    'side': 'SELL',
    "orderIdString": "1642655717519015937" //String type of order number, recommended to use this
}
```
{% endtab %}
{% endtabs %}

**Response:**

| orderId       | long    | `150695552109032492`   | Order ID (system-generated)                                      |
| ------------- | ------- | ---------------------- | ---------------------------------------------------------------- |
| orderIdString | string  | "`150695552109032492"` | Order ID in string format (recommended for use)                  |
| clientOrderId | string  | `213443`               | Client-side Order ID (user-provided)                             |
| symbol        | string  | `BTCUSDT`              | Trading pair name                                                |
| transactTime  | integer | `1273774892913`        | Order creation timestamp                                         |
| price         | float   | `4765.29`              | Order price                                                      |
| origQty       | float   | `1.01`                 | Original order quantity                                          |
| executedQty   | float   | `1.01`                 | Total executed/filled quantity                                   |
| type          | string  | `LIMIT`                | Order type: `LIMIT`, `MARKET`, or `STOP` (Stop-loss/Take-profit) |
| side          | string  | `BUY`                  | Order side. Possible values: `BUY` (Long) and `SELL` (Short)     |
| status        | string  | `0`                    | 0 = New order                                                    |

#### 9.Batch order, private\_post\_batchOrders()

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 try:
     maps = {'price': '0.01', 'side': 'BUY', 'batchType': 'MARKET', 'volume': '0.01'}
     maps2 = {'price': '0.01', 'side': 'BUY', 'batchType': 'MARKET', 'volume': '0.01'}
     orders = [maps,maps2]
     markets = exchange.private_post_batchOrders({'symbol':'BTC/USDT','orders':orders})
     print("Markets:", markets)
 except Exception as e:
     print("Error private_post_sapi_v2_batchOrders:", str(e))
```

**Headers**

|             |        |           |
| ----------- | ------ | --------- |
| X-CH-SIGN   | String | Signature |
| X-CH-APIKEY | String | API-key   |
| X-CH-TS     | String | Timestamp |

**Request Body**

|                                          |        |                                   |
| ---------------------------------------- | ------ | --------------------------------- |
| symbol<mark style="color:red;">\*</mark> | String | Currency pair name E.g.`BTC/USDT` |
| orders                                   | number | Batch order info, maximum 10      |

{% tabs %}
{% tab title="200: OK" %}
```javascript
{
    "idsString": [ //Order id of string type (recommended)
        "165964665990709251",
        "165964665990709252",
        "165964665990709253"
    ],
    "ids": [
        165964665990709251,
        165964665990709252,
        165964665990709253
    ]
}
```
{% endtab %}
{% endtabs %}

**Resquest `orders` field:**

| Name      | Type   | Example        | Description |
| --------- | ------ | -------------- | ----------- |
| price     | folat  | 1000           | Price       |
| volume    | folat  | 20.1           | Volume      |
| side      | String | BUY/SELL       | side        |
| batchType | String | `LIMIT/MARKET` | type        |

**Resquest:**

| idsString | String  | Example | A collection of order numbers of String type |
| --------- | ------- | ------- | -------------------------------------------- |
| ids       | integer | 2100    | Order number collection                      |

#### 10.Order query, fetchOrder()

```python
# Test python document (test_bitwind.py)
import ccxt

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.fetchOrder({'symbol':'BTC/USDT','orderId':'90909'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

|                                           |        |                                   |
| ----------------------------------------- | ------ | --------------------------------- |
| orderId<mark style="color:red;">\*</mark> | String | order id                          |
| newClientOrderId                          | String | Client order identification       |
| symbol<mark style="color:red;">\*</mark>  | String | Currency pair name E.g.`BTC/USDT` |

**Headers**

|             |        |           |
| ----------- | ------ | --------- |
| X-CH-SIGN   | String | Signature |
| X-CH-APIKEY | String | API-key   |
| X-CH-TS     | String | Timestamp |

{% tabs %}
{% tab title="200: OK" %}
```javascript
{
    'orderId': '499890200602846976', 
    'clientOrderId': '157432755564968', 
    'symbol': 'BHTUSDT', 
    'price': '0.01', 
    'origQty': '50', 
    'executedQty': '0', 
    'avgPrice': '0', 
    'status': 'NEW', 
    'type': 'LIMIT', 
    'side': 'BUY', 
    'transactTime': '1574327555669'
}
```
{% endtab %}
{% endtabs %}

**Response:**

| orderId       | long    | `150695552109032492` | Order ID (Generated by System)                                                                                                                                                                     |
| ------------- | ------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clientOrderId | string  | `213443`             | Customer Order ID (sent by the customer)                                                                                                                                                           |
| symbol        | string  | `BTCUSDT`            | Currency paire name                                                                                                                                                                                |
| transactTime  | integer | `1273774892913`      | Order transaction time                                                                                                                                                                             |
| price         | float   | `4765.29`            | Order price                                                                                                                                                                                        |
| origQty       | float   | `1.01`               | Order volume                                                                                                                                                                                       |
| executedQty   | float   | `1.01`               | Deal order volume                                                                                                                                                                                  |
| avgPrice      | float   | `4754.24`            | Deal order average price                                                                                                                                                                           |
| side          | string  | `BUY`                | Order direction. The possible values can only be: BUY (buy to go long) and SELL (sell to go short).                                                                                                |
| status        | string  | `NEW`                | Order status. The possible values are: NEW(new order, no transaction), PARTIALLY\_FILLED (partial transaction), FILLED (all transaction), CANCELED (cancelled), and REJECTED (order rejected).POST |
| transactTime  | string  | 1574327555669        | Order create time                                                                                                                                                                                  |

#### 11.Cancel order, cancelOrder()

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.cancelOrder({'symbol':'BTC/USDT','orderId':'90909'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Headers**

|             |        |           |
| ----------- | ------ | --------- |
| X-CH-SIGN   | String | Signature |
| X-CH-APIKEY | String | API-key   |
| X-CH-TS     | String | Timestamp |

**Request Body**

|                                           |        |                                              |
| ----------------------------------------- | ------ | -------------------------------------------- |
| orderId<mark style="color:red;">\*</mark> | String | Order id                                     |
| newClientOrderId                          | String | Client order id                              |
| symbol<mark style="color:red;">\*</mark>  | String | Currency pair name E.g.`BTCUSDT or BTC/USDT` |

{% tabs %}
{% tab title="200: OK Success cancel order" %}
```javascript
{
    'symbol': 'BHTUSDT', 
    'clientOrderId': '0', 
    'orderId': '499890200602846976', 
    'status': 'CANCELED'
}

```
{% endtab %}
{% endtabs %}

**Response:**

| orderId       | long   | `150695552109032492` | Order ID (Generated by System)                                                                                                                                                                     |
| ------------- | ------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clientorderId | string | `213443`             | Customer Order ID (sent by customer)                                                                                                                                                               |
| symbol        | string | `BTCUSDT`            | Currency pai name                                                                                                                                                                                  |
| status        | string | `NEW`                | Order status. The possible values are: NEW(new order, no transaction), PARTIALLY\_FILLED (partial transaction), FILLED (all transaction), CANCELED (cancelled), and REJECTED (order rejected).POST |

#### 12.Batch cancek order, private\_post\_batchCancel\_order()

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     cancelOrders = [123,321]
     markets = exchange.private_post_batchCancel_order({'symbol':'BTC/USDT','orderIds':cancelOrders})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

The maximum batch size is 10 orders at a time

**Headers**

|             |        |           |
| ----------- | ------ | --------- |
| X-CH-SIGN   | String | Signature |
| X-CH-APIKEY | String | API-key   |
| X-CH-TS     | String | Timestamp |

**Request Body**

|                                            |        |                                                 |
| ------------------------------------------ | ------ | ----------------------------------------------- |
| orderIds<mark style="color:red;">\*</mark> | String | The set of order ids to be cancelled \[123,456] |
| symbol<mark style="color:red;">\*</mark>   | String | Currency pair name E.g.`BTC/USDT`               |

{% tabs %}
{% tab title="200: OK" %}
```javascript
{
    "success": [
        165964665990709251,
        165964665990709252,
        165964665990709253
    ],
    "failed": [ //Cancellation failure is usually due to the fact that the order does not exist or the order status has reached the final state
        165964665990709250  
    ]
}
```
{% endtab %}
{% endtabs %}

#### 13. Current order, fetchOpenOrders()

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.fetchOpenOrders({'symbol':'BTC/USDT','limit':2})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**uery Parameters**

|        |        |                                                                                                           |
| ------ | ------ | --------------------------------------------------------------------------------------------------------- |
| symbol | String | Currency pair nameE.g.`BTC/USDT` When this parameter is not passed, the api occupies a very large weight. |
| limit  | String | Default: 100; Maximum 1000                                                                                |

**Headers**

|             |        |           |
| ----------- | ------ | --------- |
| X-CH-SIGN   | String | Signature |
| X-CH-APIKEY | String | API-key   |
| X-CH-TS     | String | Timestamp |

{% tabs %}
{% tab title="200: OK" %}
```javascript
[
    {
        'orderId': '499902955766523648', 
        'symbol': 'BHTUSDT', 
        'price': '0.01', 
        'origQty': '50', 
        'executedQty': '0', 
        'avgPrice': '0', 
        'status': 'NEW', 
        'type': 'LIMIT', 
        'side': 'BUY', 
        'time': '1574329076202',
        'stopPrice': 123321,
        'isWorking':true        
        },...
]
```
{% endtab %}
{% endtabs %}

**Response:**

| orderId       | long    | `150695552109032492`   | Order ID (Generated by System)                                                                                                                                                                     |
| ------------- | ------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| orderIdString | String  | "`150695552109032492"` | Order ID of string type (recommended)                                                                                                                                                              |
| clientorderId | string  | `213443`               | Customer Order ID (sent by customer)                                                                                                                                                               |
| symbol        | string  | `BTCUSDT`              | Symbol name                                                                                                                                                                                        |
| price         | float   | `4765.29`              | Order price                                                                                                                                                                                        |
| origQty       | float   | `1.01`                 | Order volume                                                                                                                                                                                       |
| executedQty   | float   | `1.01`                 | Deal order volume                                                                                                                                                                                  |
| avgPrice      | float   | `4754.24`              | The average price at which the order has been executed                                                                                                                                             |
| type          | string  | `LIMIT`                | Order type: `LIMIT/MARKET`                                                                                                                                                                         |
| side          | string  | `BUY`                  | Order direction. The possible values can only be: BUY /SELL                                                                                                                                        |
| status        | string  | `NEW`                  | Order status. The possible values are: NEW(new order, no transaction), PARTIALLY\_FILLED (partial transaction), FILLED (all transaction), CANCELED (cancelled), and REJECTED (order rejected).POST |
| time          | string  | 1574327555669          | Create time                                                                                                                                                                                        |
| stopPrice     | float   | 21323.32               | Take-profit and stop-loss trigger prices                                                                                                                                                           |
| isWorking     | boolean | true                   | Whether the order appears in the orderbook                                                                                                                                                         |

#### 14.Trade record, fetchMyTrades()

```
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.fetchMyTrades({'symbol':'BTC/USDT','limit':2})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

|                                          |        |                                   |
| ---------------------------------------- | ------ | --------------------------------- |
| symbol<mark style="color:red;">\*</mark> | String | Currency pair name E.g.`BTC/USDT` |
| limit                                    | String | Default: 100; Maximum 1000        |
| fromId                                   | String | From this id to query             |

**Headers**

|             |        |           |
| ----------- | ------ | --------- |
| X-CH-SIGN   | String | Signature |
| X-CH-APIKEY | String | API-key   |
| X-CH-TS     | String | Timestamp |

{% tabs %}
{% tab title="200: OK" %}
```javascript
[
  {
    "symbol": "ETHBTC",
    "id": 100211,
    "bidId": 150695552109032492,
    "askId": 150695552109032493,
    "price": "4.00000100",
    "qty": "12.00000000",
    "time": 1499865549590,
    "isBuyer": true,
    "isMaker": false,
    "feeCoin": "ETH",
    "fee":"0.001",
    "bidUserId":23334,
    "askUserId":44112
  },...
]
```
{% endtab %}
{% endtabs %}

**Response:**

| id        | long    | `150695552109032492` | Deal id                                                                                        |
| --------- | ------- | -------------------- | ---------------------------------------------------------------------------------------------- |
| symbol    | String  | Currency pair        | Order ID of string type (recommended)                                                          |
| time      | long    | 1499865549590        | Create time                                                                                    |
| qty       | string  | `12`                 | Trade volume                                                                                   |
| price     | float   | `4765.29`            | Order price                                                                                    |
| fee       | string  | `0.001`              | Transaction fee                                                                                |
| feeCoin   | String  | `xxx`                | Currency of Transaction fee                                                                    |
| isBuyer   | boolean | `true`               | `true`= buy `false`= sell                                                                      |
| isMaker   | boolean | false                | `true`=market price `false`=limit price                                                        |
| bidId     | long    | `1200000200`         | buy order id                                                                                   |
| askId     | long    | `1200000200`         | sell order id                                                                                  |
| side      | string  | `BUY`                | Order side. The possible values can only be: BUY (buy to go long) and SELL (sell to go short). |
| bidUserId | long    | 23334                | buy side uid                                                                                   |
| askUserId | long    | 44112                | sell side uid                                                                                  |
| isSelf    | boolean | true                 | Is it a self-transaction?                                                                      |

#### 15.Account information fetchBalance()

**Security type: USER\_DATA**

```python
# Test python document (test_bitwind.py)
import ccxt 

# init exchange
exchange = ccxt.bitwind()
 
 #public_get_sapi_v2_depth
 try:
     markets = exchange.fetchBalance()
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Headers**

|             |        |           |
| ----------- | ------ | --------- |
| X-CH-SIGN   | String | Signature |
| X-CH-APIKEY | String | API-key   |
| X-CH-TS     | String | Timestamp |
