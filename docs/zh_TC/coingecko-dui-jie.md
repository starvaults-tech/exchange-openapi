# Coingecko對接

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/pub/coingecko/tickers`

**請求參數**

```
無
```

**響應參數**

| 名稱               | 類型     | 例子                     | 描述                    |
| ---------------- | ------ | ---------------------- | --------------------- |
| ticker\_id       | string | BTC\_USDT              | 幣對                    |
| base\_currency   | string | BTC                    | 基準貨幣                  |
| target\_currency | string | USDT                   | 計價貨幣                  |
| last\_price      | number | 98000.0000000000000000 | 基於給定目標貨幣的基準貨幣的最後交易價格  |
| base\_volume     | number | 1.1200                 | 該幣對 24 小時單邊交易量（基準幣單位） |
| target\_volume   | number | 99000.0000000000       | 該幣對 24 小時單邊交易量（計價幣單位） |
| bid              | number | 97000                  | 當前最高買單價格              |
| ask              | number | 98000                  | 當前最低賣單價格              |
| high             | number | 98000                  | 滾動 24 小時最高交易價格        |
| low              | number | 98000                  | 滾動 24 小時最低交易價格        |

**響應示例**

```javascript
[
    {
        "ticker_id": "A_USDT",
        "base_currency": "A",
        "target_currency": "USDT",
        "last_price": 0.0897000000000000,
        "base_volume": 545657.3,
        "target_volume": 49595.5838,
        "bid": 0.0895,
        "ask": 0.09,
        "high": 0.0941,
        "low": 0.0877
    },
    {
        "ticker_id": "HYPE_USDT",
        "base_currency": "HYPE",
        "target_currency": "USDT",
        "last_price": 34.9940000000000000,
        "base_volume": 741733.37,
        "target_volume": 25429154.756,
        "bid": 34.906,
        "ask": 35.046,
        "high": 36.286,
        "low": 32.543
    }
]
```

#### 盤口數據

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/pub/coingecko/orderbook`

**請求參數**

| 名稱         | 類型             | 描述     |
| ---------- | -------------- | ------ |
| ticker\_id | string         | 幣對     |
| depth      | integer(int32) | 訂單深度數量 |

**響應參數**

| 名稱         | 類型             | 例子                                  | 描述                        |
| ---------- | -------------- | ----------------------------------- | ------------------------- |
| ticker\_id | string         | BTC\_USDT                           | 幣對                        |
| timestamp  | integer(int64) | 1766976278000                       | Unix 時間戳，以毫秒為單位，表示上次更新的時間 |
| bids       | array          | \[\["1000","0.1"], \["2000","0.2"]] | 包含兩個元素的陣列，每筆買單的報價及數量      |
| asks       | array          | \[\["2000","0.2"], \["3000","0.3"]] | 包含兩個元素的陣列，每筆賣單的報價及數量      |

**響應示例**

```javascript
{
    "ticker_id": "BTC_USDT",
    "timestamp": 1770297048000,
    "bids": [
        [
            "69662.14",
            "0.28558"
        ],
        [
            "69661.76",
            "0.01602"
        ]
    ],
    "asks": [
        [
            "69663.05",
            "0.48278"
        ],
        [
            "69663.43",
            "0.01097"
        ]
    ]
}
```

#### 合約產品資訊及類型

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/pub/coingecko/contracts`

**請求參數**

```
無
```

**響應參數**

| **字段名**                        | **類型**    | **例子**        | **描述**                                               |
| ------------------------------ | --------- | ------------- | ---------------------------------------------------- |
| ticker\_id                     | string    | E-BTC-USDT    | 合約識別碼，使用分隔符區分基礎貨幣/目標貨幣，例如 BTC-PERP                   |
| base\_currency                 | string    | BTC           | 基礎貨幣的符號/貨幣代碼，例如 BTC                                  |
| target\_currency               | string    | USDT          | 目標貨幣的符號/貨幣代碼，例如 ETH                                  |
| last\_price                    | decimal   | 92000.36      | 基礎貨幣相對於目標貨幣的最新成交價格                                   |
| base\_volume                   | decimal   | 0.2           | 24 小時單邊成交量（以基礎貨幣為單位）                                 |
| target\_volume                 | decimal   | 0.2           | 24 小時單邊成交量（以目標貨幣為單位）                                 |
| bid                            | decimal   | 92000.36      | 當前最高買單價格                                             |
| ask                            | decimal   | 92000.36      | 當前最低賣單價格                                             |
| high                           | decimal   | 92100.36      | 過去 24 小時最高成交價格                                       |
| low                            | decimal   | 91900.36      | 過去 24 小時最低成交價格                                       |
| product\_type                  | string    | Perpetual     | 產品類型：期貨（Futures）、永續合約（Perpetual）、期權（Options）         |
| open\_interest                 | decimal   | 1116.3655     | 過去 24 小時未平倉合約量（以基礎貨幣為單位）                             |
| open\_interest\_usd            | decimal   | 102573030.064 | 過去 24 小時未平倉合約量（美元計價）                                 |
| index\_price                   | decimal   | 92100.36      | 標的指數價格                                               |
| index\_name                    | string    | BTC-USDT      | 標的指數名稱（如有）                                           |
| index\_currency                | string    | BTC           | 指數的標的貨幣                                              |
| start\_timestamp               | timestamp | 0             | 衍生品產品的生效時間（適用於到期型期貨或期權）                              |
| end\_timestamp                 | timestamp | 0             | 衍生品產品的到期時間（適用於到期型期貨或期權）                              |
| funding\_rate                  | decimal   | 0             | 當前資金費率                                               |
| next\_funding\_rate            | decimal   | 0             | 即將到來的預測資金費率                                          |
| next\_funding\_rate\_timestamp | timestamp | 1768291200000 | 下一次資金費率調整的時間戳                                        |
| contract\_type                 | string    | Vanilla       | 合約類型描述 - 普通型（Vanilla）、反向型（Inverse）或 quanto 型（Quanto） |
| contract\_price\_currency      | string    | USDT          | 合約定價貨幣                                               |
| contract\_price                | decimal   | 92100.36      | 每份合約的價格（若與最新價格不同）                                    |
| timestamp                      | timestamp | 1768289995029 | 查詢時間戳                                                |

**請求示例**

```
https://futuresopenapi.xxx.xx/pub/coingecko/contracts
```

**響應示例**

```json
[
    {
        "ticker_id": "E-BTC-USDT",
        "base_currency": "BTC",
        "target_currency": "USDT",
        "last_price": 0,
        "base_volume": 0,
        "target_volume": 0,
        "bid": null,
        "ask": 9.8E+4,
        "high": 0,
        "low": 0,
        "product_type": "Perpetual",
        "open_interest": 1116.3655,
        "open_interest_usd": 102573030.06495740245,
        "index_price": 0,
        "index_name": "BTC-USDT",
        "index_currency": "BTC",
        "start_timestamp": 0,
        "end_timestamp": 0,
        "funding_rate": 0,
        "next_funding_rate": 0,
        "next_funding_rate_timestamp": 1768291200000,
        "contract_type": "Vanilla",
        "contract_price_currency": "USDT",
        "contract_price": 0,
        "timestamp": 1768289995029
    },
    {
        "ticker_id": "E-ETH-USDT",
        "base_currency": "ETH",
        "target_currency": "USDT",
        "last_price": 0,
        "base_volume": 0,
        "target_volume": 0,
        "bid": null,
        "ask": null,
        "high": 0,
        "low": 0,
        "product_type": "Perpetual",
        "open_interest": 3004.17,
        "open_interest_usd": 9383427.795980901,
        "index_price": 0,
        "index_name": "ETH-USDT",
        "index_currency": "ETH",
        "start_timestamp": 0,
        "end_timestamp": 0,
        "funding_rate": 0,
        "next_funding_rate": 0,
        "next_funding_rate_timestamp": 1768291200000,
        "contract_type": "Vanilla",
        "contract_price_currency": "USDT",
        "contract_price": 0,
        "timestamp": 1768289995029
    }
]
```

#### 合約訂單簿深度詳情

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/pub/coingecko/orderbook`

**請求參數**

| 名稱         | 類型             | 描述                     |
| ---------- | -------------- | ---------------------- |
| ticker\_id | string         | 合約名稱【可選】，例如：E-BTC-USDT |
| depth      | integer(int32) | 訂單深度數量                 |

**響應參數**

| 名稱         | 類型             | 例子                                                              | 描述                        |
| ---------- | -------------- | --------------------------------------------------------------- | ------------------------- |
| ticker\_id | string         | E-BTC-USDT                                                      | 幣對                        |
| timestamp  | integer(int64) | 1768289995029                                                   | Unix 時間戳，以毫秒為單位，表示上次更新的時間 |
| bids       | array          | \<p>\[\<br>\["97000","100"],\<br>\["96500.93","100"]\<br>]\</p> | 包含兩個元素的陣列，每筆買單的報價及數量      |
| asks       | array          | \<p>\[\<br>\["97000","100"],\<br>\["96500.93","100"]\<br>]\</p> | 包含兩個元素的陣列，每筆賣單的報價及數量      |

**請求示例**

```
https://futuresopenapi.xxx.xx/pub/coingecko/orderbook?ticker_id=E-BTC-USDT&dept=100
```

**響應示例**

```json
{
    "ticker_id": "E-BTC-USDT",
    "asks": [
        [
            "98000",
            "100"
        ],
        [
            "98500.93",
            "100"
        ],
        [
            "100000",
            "100"
        ],
        [
            "1800000",
            "100"
        ],
        [
            "2000000",
            "100"
        ]
    ],
    "bids": [
        [
            "97000",
            "100"
        ],
        [
            "96500.93",
            "100"
        ],
        [
            "96000",
            "100"
        ],
        [
            "95500",
            "100"
        ],
        [
            "95000",
            "100"
        ]
    ],
    "timestamp": 1768289995029
}
```
