# CMC docking

#### 24h summary

<mark style="color:blue;">`GET`</mark> `https://openapi.star-vaults.com/v2/pub/summary`

**Request parameters**

no

**Response parameters**

| Name             | type    | Example | description                  |
| ---------------- | ------- | ------- | ---------------------------- |
| code             | string  |         |                              |
| msg              | string  |         |                              |
| data             | object  |         |                              |
| data.symbol      | object  |         |                              |
| ├─ id            | integer | 46      | Token id                     |
| ├─ isFrozen      | string  | 0       | Whether to freeze            |
| ├─ last          | string  | 98000   | Latest price                 |
| ├─ high24hr      | string  | 98000   | High 24h                     |
| ├─ low24hr       | string  | 98000   | 24h lowest price             |
| ├─ quoteVolume   | string  | 0       | 24h volume                   |
| ├─ baseVolume    | string  | 0       | 24h transactions             |
| ├─ percentChange | string  | 0       | percentchange                |
| ├─ lowestAsk     | string  | 0       | 24h seller's lowest price    |
| ├─ highestBid    | string  | 0       | 24h buyer's highest price    |
| coins            | object  |         |                              |
| ├─ name          | string  | USDT    | Currency name                |
| ├─ withdrew      | string  | ON      | Whether to start withdrawing |
| ├─ deposit       | string  | ON      | Whether to open deposit      |

**Sample response**

{% tabs %}
{% tab title="200" %}
<pre class="language-json"><code class="lang-json"><strong>{
</strong>    "msg": "success",
    "code": "200",
    "data": {
        "ETH_USDT": {
            "high24hr": "238.2",
            "percentChange": "0",
            "last": "238.2",
            "highestBid": "0",
            "id": 47,
            "quoteVolume": "0",
            "isFrozen": "0",
            "baseVolume": "0",
            "lowestAsk": "0",
            "low24hr": "238.2"
        },
        "BCH_USDT": {
            "high24hr": "1",
            "percentChange": "0",
            "last": "1",
            "highestBid": "0",
            "id": 49,
            "quoteVolume": "0",
            "isFrozen": "0",
            "baseVolume": "0",
            "lowestAsk": "0",
            "low24hr": "1"
        }
    },
    "coins": {
        "MATIC": {
            "withdrew": "ON",
            "name": "MATIC",
            "deposit": "ON"
        },
        "FAIR": {
            "withdrew": "ON",
            "name": "FAIR",
            "deposit": "ON"
        }
    }
}
</code></pre>
{% endtab %}
{% endtabs %}

#### List of currencies

<mark style="color:blue;">`GET`</mark> `https://openapi.star-vaults.com/v2/pub/asset`

**Request parameters**

no

**Response parameters**

| Name                     | type    | Example              | description                          |
| ------------------------ | ------- | -------------------- | ------------------------------------ |
| name                     | string  | Bitcoin              | currency name                        |
| unified\_cryptoasset\_id | integer | 1                    | Currency id                          |
| can\_withdraw            | integer | 1                    | Whether withdrawal is enabled        |
| can\_deposit             | integer | 1                    | Whether deposit is enabled           |
| min\_withdraw            | number  | 0.2000000000000000   | Minimum value of a single withdrawal |
| max\_withdraw            | number  | 120.0000000000000000 | Maximum value of a single withdrawal |
| maker\_fee               | number  | 0.00100000           | Handling fee                         |
| taker\_fee               | number  | 0.00100000           | Take a single fee                    |

**Sample response**

{% tabs %}
{% tab title="200" %}
```json
{
    "BTC": {
        "max_withdraw": 120.0000000000000000,
        "maker_fee": 0.00100000,
        "name": "Bitcoin",
        "taker_fee": 0.00100000,
        "can_withdraw": 1,
        "can_deposit": 1,
        "unified_cryptoasset_id": 1,
        "min_withdraw": 0.2000000000000000
    },
    "ATC": {
        "max_withdraw": 100000.0000000000000000,
        "maker_fee": 0.00100000,
        "name": "ATC",
        "taker_fee": 0.00100000,
        "can_withdraw": 1,
        "can_deposit": 1,
        "unified_cryptoasset_id": 1465,
        "min_withdraw": 50.0000000000000000
    }
}
```
{% endtab %}
{% endtabs %}



#### Coin quotes

<mark style="color:blue;">`GET`</mark> `https://openapi.star-vaults.com/v2/pub/ticker`

**Request parameters**

no

**Response parameters**

| Name              | type    | Example                | description            |
| ----------------- | ------- | ---------------------- | ---------------------- |
| base\_id          | integer | 50                     | Base currency          |
| quote\_id         | integer | 49                     | currency of account    |
| last\_price       | number  | 98000.0000000000000000 | last transaction price |
| base\_volume      | number  | 0.1020408100000000     | Last volume            |
| quote\_volume     | number  | 0.0000010412327551     | Last turnover          |
| 24\_base\_volume  | string  | 0.000000               | 24h volume             |
| 24\_quote\_volume | string  | 0.0000000000           | 24h turnover           |

**Sample response**

{% tabs %}
{% tab title="200" %}
```json
{
    "ETH_BTC": {
        "24_base_volume": "0.0000",
        "base_id": 51,
        "quote_volume": 46.6795548917722849,
        "quote_id": 50,
        "base_volume": 2.0000000000000000,
        "24_quote_volume": "0.0000",
        "last_price": 0.0428453100000000
    },
    "BTC_USDT": {
        "24_base_volume": "0.000000",
        "base_id": 50,
        "quote_volume": 0.0000010412327551,
        "quote_id": 49,
        "base_volume": 0.1020408100000000,
        "24_quote_volume": "0.0000000000",
        "last_price": 98000.0000000000000000
    }
}
```
{% endtab %}
{% endtabs %}

\
Disc data

<mark style="color:blue;">`GET`</mark> `https://openapi.star-vaults.com/v2/pub/orderbook`

**Request parameters**

| Name   | type    | description                                                                  |
| ------ | ------- | ---------------------------------------------------------------------------- |
| base   | string  | base currency                                                                |
| quote  | string  | Quote currency                                                               |
| symbol | string  | Token name (not required if base and quote are provided, otherwise required) |
| depth  | integer | Precision, 0-0.01, 1-0.1, 2-0, default is 0                                  |
| bids   | integer | The amount to buy, the default is 100                                        |
| asks   | integer | Number of sell orders, defaults to 100                                       |

**Response parameters**

| Name | type           | Example                     | description                                                              |
| ---- | -------------- | --------------------------- | ------------------------------------------------------------------------ |
| date | integer(int64) | 1766991308472               | Unix timestamp, in milliseconds, of the last update                      |
| bids | array          | \[\[1000,0.1], \[2000,0.2]] | An array with two elements, the bid and quantity for each purchase       |
| asks | array          | \[\[2000,0.2], \[3000,0.3]] | An array of two elements with the price and quantity for each sell order |

**Sample response**

{% tabs %}
{% tab title="200" %}
```json
{
    "date": 1766991308472,
    "asks": [
        [
            196000,
            0.46938777
        ],
        [
            197001.86,
            0.1
        ]
    ],
    "bids": [
        [
            196000,
            0.46938777
        ],
        [
            197001.86,
            0.1
        ]
    ]
}
```
{% endtab %}
{% endtabs %}

#### List of deals

<mark style="color:blue;">`GET`</mark> `https://openapi.star-vaults.com/v2/pub/trades`

**Request parameters**

| Name   | type    | description                                                                  |
| ------ | ------- | ---------------------------------------------------------------------------- |
| base   | string  | base currency                                                                |
| quote  | string  | Quote currency                                                               |
| symbol | string  | Token name (not required if base and quote are provided, otherwise required) |
| trades | integer | Number of trades, defaults to 100                                            |

**Response parameters**

| Name          | type           | Example                | description             |
| ------------- | -------------- | ---------------------- | ----------------------- |
| trade\_id     | integer(int64) | 52594124               | Transaction id          |
| price         | number         | 98000.0000000000000000 | Transaction price       |
| type          | string         | BUY                    | active single direction |
| timestamp     | integer(int64) | 1762965571597          | Transaction timestamp   |
| base\_volume  | number         | 0.1020408100000000     | Volume                  |
| quote\_volume | number         | 0.0000010412327551     | Turnover                |

**Sample response**

{% tabs %}
{% tab title="200" %}
```json
[
    {
        "trade_id": 52594124,
        "price": 98000.0000000000000000,
        "quote_volume": 0.0000010412327551,
        "base_volume": 0.1020408100000000,
        "type": "BUY",
        "timestamp": 1762965571597
    },
    {
        "trade_id": 52594123,
        "price": 35000.0000000000000000,
        "Quote_volume" : 7000.00000000000000000000000000000000,
        "base_volume": 0.2000000000000000,
        "type": "SELL",
        "timestamp": 1762965519813
    }
}
```
{% endtab %}
{% endtabs %}
