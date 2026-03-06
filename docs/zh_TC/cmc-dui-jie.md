# CMC對接

#### 24h摘要

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/v2/pub/summary`

**請求參數**

```
無
```

**響應參數**

| 名稱               | 類型      | 例子    | 描述        |
| ---------------- | ------- | ----- | --------- |
| code             | string  |       |           |
| msg              | string  |       |           |
| data             | object  |       |           |
| data.symbol      | object  |       |           |
| ├─ id            | integer | 46    | 幣對 id     |
| ├─ isFrozen      | string  | 0     | 是否凍結      |
| ├─ last          | string  | 98000 | 最新成交價     |
| ├─ high24hr      | string  | 98000 | 24h 最高價   |
| ├─ low24hr       | string  | 98000 | 24h 最低價   |
| ├─ quoteVolume   | string  | 0     | 24h 交易量   |
| ├─ baseVolume    | string  | 0     | 24h 交易額   |
| ├─ percentChange | string  | 0     | 漲跌幅       |
| ├─ lowestAsk     | string  | 0     | 24h 賣方最低價 |
| ├─ highestBid    | string  | 0     | 24h 買方最高價 |
| coins            | object  |       |           |
| ├─ name          | string  | USDT  | 幣種名       |
| ├─ withdrew      | string  | ON    | 是否開啟提現    |
| ├─ deposit       | string  | ON    | 是否開啟充值    |

**響應示例**

{% tabs %}
{% tab title="200" %}
```json
{
    "msg": "success",
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
```


{% endtab %}
{% endtabs %}

#### 幣種列表

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/v2/pub/asset`

**請求參數**

```
無
```

**響應參數**

| 名稱                       | 類型      | 例子                   | 描述      |
| ------------------------ | ------- | -------------------- | ------- |
| name                     | string  | Bitcoin              | 幣種名     |
| unified\_cryptoasset\_id | integer | 1                    | 幣種 id   |
| can\_withdraw            | integer | 1                    | 是否開啟提現  |
| can\_deposit             | integer | 1                    | 是否開啟充值  |
| min\_withdraw            | number  | 0.2000000000000000   | 單次提現最小值 |
| max\_withdraw            | number  | 120.0000000000000000 | 單次提現最大值 |
| maker\_fee               | number  | 0.00100000           | 掛單手續費   |
| taker\_fee               | number  | 0.00100000           | 吃單手續費   |

**響應示例**

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

#### 幣對行情

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/v2/pub/ticker`

**請求參數**

```
無
```

**響應參數**

| 名稱                | 類型      | 例子                     | 描述      |
| ----------------- | ------- | ---------------------- | ------- |
| base\_id          | integer | 50                     | 基準幣種    |
| quote\_id         | integer | 49                     | 計價幣種    |
| last\_price       | number  | 98000.0000000000000000 | 最後一次成交價 |
| base\_volume      | number  | 0.1020408100000000     | 最後一次成交量 |
| quote\_volume     | number  | 0.0000010412327551     | 最後一次成交額 |
| 24\_base\_volume  | string  | 0.000000               | 24h 成交量 |
| 24\_quote\_volume | string  | 0.0000000000           | 24h 成交額 |

**響應示例**

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

#### 盤口數據

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/v2/pub/orderbook`

**請求參數**

| 名稱     | 類型      | 描述                                |
| ------ | ------- | --------------------------------- |
| base   | string  | 基準幣種                              |
| quote  | string  | 計價幣種                              |
| symbol | string  | 幣對名（如果提供了 base 和 quote 則不需要，否則需要） |
| depth  | integer | 精度，0-0.01，1-0.1，2-0，預設為 0         |
| bids   | integer | 買單數量，預設為 100                      |
| asks   | integer | 賣單數量，預設為 100                      |

**響應參數**

| 名稱   | 類型             | 例子                          |
| ---- | -------------- | --------------------------- |
| date | integer(int64) | 1766991308472               |
| bids | array          | \[\[1000,0.1], \[2000,0.2]] |
| asks | array          | \[\[2000,0.2], \[3000,0.3]] |

**響應示例**

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

#### 交易列表

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/v2/pub/trades`

**請求參數**

| 名稱     | 類型      | 描述                                |
| ------ | ------- | --------------------------------- |
| base   | string  | 基準幣種                              |
| quote  | string  | 計價幣種                              |
| symbol | string  | 幣對名（如果提供了 base 和 quote 則不需要，否則需要） |
| trades | integer | 交易數量，預設為 100                      |

**響應參數**

| 名稱            | 類型             | 例子                     | 描述    |
| ------------- | -------------- | ---------------------- | ----- |
| trade\_id     | integer(int64) | 52594124               | 成交 id |
| price         | number         | 98000.0000000000000000 | 成交價格  |
| type          | string         | BUY                    | 主動單方向 |
| timestamp     | integer(int64) | 1762965571597          | 交易時間戳 |
| base\_volume  | number         | 0.1020408100000000     | 成交量   |
| quote\_volume | number         | 0.0000010412327551     | 成交額   |

**響應示例**

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
        "quote_volume": 7000.00000000000000000000000000000000,
        "base_volume": 0.2000000000000000,
        "type": "SELL",
        "timestamp": 1762965519813
    }
}
```
{% endtab %}
{% endtabs %}

\{% endtab %\} \{% endtabs %\}
