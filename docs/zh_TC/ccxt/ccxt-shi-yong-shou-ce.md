# CCXT使用手冊

根據 bitwind 的 CCXT 內容，可以直接使用以下功能介面

公共

### 1. 測試連結 public\_get\_ping()

測試 REST API 的連通性

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
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

### 2. 伺服器時間 public\_get\_time()

取得伺服器時間

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
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

### 3. 幣對列表 fetchMarkets()

交易所支援的幣對集合

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
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



**Response**&#x20;

<table><thead><tr><th width="154">名稱</th><th>類型</th><th>例子</th><th>描述</th></tr></thead><tbody><tr><td>symbol</td><td>string</td><td><code>BTCUSDT</code></td><td>幣對名稱</td></tr><tr><td>baseAsset</td><td>string</td><td><code>BTC</code></td><td>base 貨幣</td></tr><tr><td>quoteAsset</td><td>string</td><td><code>USDT</code></td><td>計價貨幣</td></tr><tr><td>pricePrecision</td><td>integer</td><td><code>2</code></td><td>價格精度</td></tr><tr><td>quantityPrecision</td><td>integer</td><td><code>6</code></td><td>數量精度</td></tr><tr><td>limitAmountMin</td><td>String</td><td>100</td><td>限價單最小下單金額 quote</td></tr><tr><td>limitPriceMin</td><td>String</td><td>100</td><td>限價單最小價格</td></tr><tr><td>limitVolumeMin</td><td>String</td><td>100</td><td>限價單最小下單數量 base</td></tr><tr><td>baseAssetName</td><td>String</td><td>BTC</td><td>基準貨幣顯示名稱</td></tr><tr><td>quoteAssetName</td><td>String</td><td>USDT</td><td>計價貨幣顯示名稱</td></tr><tr><td>SymbolName</td><td>String</td><td>BTC/USDT</td><td>幣對顯示名稱</td></tr><tr><td>feeRateMaker</td><td>String</td><td>0.002</td><td>maker 手續費率</td></tr><tr><td>feeRateMaker</td><td>String</td><td>0.002</td><td>taker 手續費率</td></tr></tbody></table>

### 4. 訂單簿 fetchOrderBook()

市場訂單簿深度資訊

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.fetchOrderBook({'symbol':'BTC/USDT'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

Query Parameters

| Name                                         | Type    | Description        |
| -------------------------------------------- | ------- | ------------------ |
| limit                                        | integer | 預設 100；最大 100      |
| symbol<mark style="color:$danger;">\*</mark> | String  | 幣對名稱 e.g. BTC/USDT |

{% tabs %}
{% tab title="200: OK " %}
```javascript
{
  "bids": [
    [
      "3.90000000",   // 價格
      "431.00000000"  // 數量
    ],
    [
      "4.00000000",
      "431.00000000"
    ]
  ],
  "asks": [
    [
      "4.00000200",  // 價格
      "12.00000000"  // 數量
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

| time | long | `1595563624731` | 當前時間（Unix Timestamp，毫秒 ms） |
| ---- | ---- | --------------- | -------------------------- |
| bids | list | 如下              | 訂單簿買盤資訊                    |
| asks | list | 如下              | 訂單簿賣盤資訊                    |

bids 和 asks 所對應的資訊代表了訂單簿的所有價格以及價格對應的數量資訊，由最優價格從上到下排列

| ' ' | float | `131.1` | 價格        |
| --- | ----- | ------- | --------- |
| ' ' | float | `2.3`   | 當前價格對應的數量 |

### 5. 行情 ticker fetchTicker()

24 小時價格變化數據

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.fetchTicker({'symbol':'BTC/USDT'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

注：參數 `symbol` 和 `symbols` 同時提供時，則優先取 symbol。如果都不提供，所有 symbol 的 ticker 數據都會返回。

| Name    | Type   | Description                                     |
| ------- | ------ | ----------------------------------------------- |
| symbol  | String | 幣對名稱 E.g. `BTC/USDT（不傳此參數時，api 佔用權重極大，返回結構也不同）` |
| symbols | String | 幣對名稱，多個使用英文逗號分隔 btcusdt,ethusdt                 |

{% tabs %}
{% tab title="200: OK 傳入 symbol 成功取得 ticker 資訊  " %}
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

{% tab title="200: OK 不傳入 symbol 成功取得 ticker 資訊 " %}
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

| time      | long   | `1595563624731` | 時間戳         |
| --------- | ------ | --------------- | ----------- |
| high      | float  | `9900`          | 最高價         |
| low       | float  | `8800.34`       | 最低價         |
| open      | float  | `8700`          | 開盤價         |
| last      | float  | `8900`          | 最新價         |
| vol       | float  | `4999`          | 交易量         |
| rose      | float  | 0               | 漲幅          |
| symbol    | String | btcusdt         | 幣對          |
| amount    | String | 1233            | 交易額，計價貨幣成交量 |
| askPrice  | String | 23321           | 賣一價         |
| askVolume | String | 3321            | 賣一數量        |
| bidPrice  | String | 21              | 買一價         |
| bidVolume | String | 12              | 買一數量        |

### 6. 最近成交 public\_get\_trades()

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.public_get_trades({'symbol':'BTC/USDT','limit':1})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

| Name                                     | Type   | Description          |
| ---------------------------------------- | ------ | -------------------- |
| symbol<mark style="color:red;">\*</mark> | String | 幣對名稱 E.g. `BTC/USDT` |
| limit                                    | String | `預設 100；最大 1000`     |

{% tabs %}
{% tab title="200: OK 成功" %}
```json
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

| price | float  | `0.055`         | 交易價格               |   |
| ----- | ------ | --------------- | ------------------ | - |
| time  | long   | `1537797044116` | 當前 Unix 時間戳，毫秒（ms） |   |
| qty   | float  | `5`             | 數量（張數）             |   |
| side  | string | `BUY/SELL`      | 主動單方向              |   |

### 7. K 線/蠟燭圖數據 fetchOHLCV()

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.fetchOHLCV({'symbol':'BTC/USDT','interval':'1min'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

| Name                                       | Type   | Description                                                                                                      |
| ------------------------------------------ | ------ | ---------------------------------------------------------------------------------------------------------------- |
| symbol<mark style="color:red;">\*</mark>   |        | 幣對名稱 E.g. `BTC/USDT`                                                                                             |
| interval<mark style="color:red;">\*</mark> | String | K 線圖區間，可識別發送的值為：`1min`、`5min`、`15min`、`30min`、`60min`、`1day`、`1week`、`1month`（min=分鐘，h=小時，day=天，week=星期，month=月） |
| startTime                                  | long   | 起始時間點                                                                                                            |
| endTime                                    | long   | 截止時間點                                                                                                            |

{% tabs %}
{% tab title="200: OK 成功" %}
```json
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

| `idx` | long  | `1538728740000` | 開始時間戳，毫秒（ms） |
| ----- | ----- | --------------- | ------------ |
| open  | float | `36.00000`      | 開盤價          |
| close | float | `33.00000`      | 收盤價          |
| high  | float | `36.00000`      | 最高價          |
| low   | float | `30.00000`      | 最低價          |
| vol   | float | `2456.111`      | 成交量          |

### 交易

**安全類型：TRADE**

交易下方的介面都需要簽名和 API-Key 驗證

### 8. 建立新訂單 createOrder()

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.createOrder({'symbol':'BTC/USDT','volume':'0.01','side':'BUY','type':'MARKET'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

| X-CH-SIGN   | string  | 簽名         |
| ----------- | ------- | ---------- |
| X-CH-APIKEY | string  | 您的 API-Key |
| X-CH-TS     | integer | 時間戳        |

**Request Body**

| symbol           | String  | 幣對名稱 E.g. `BTC/USDT`                          |
| ---------------- | ------- | --------------------------------------------- |
| volume\*         | number  | 訂單數量                                          |
| side\*           | String  | 訂單方向，`BUY/SELL`                               |
| type\*           | String  | 訂單類型，`LIMIT/MARKET/FOK/POST_ONLY/IOC/STOP`    |
| price            | number  | 訂單價格，對於 `LIMIT` 訂單必須發送                        |
| newClientOrderId | String  | 客戶端訂單標識                                       |
| recvwindow       | integer | 時間視窗                                          |
| triggerPrice     | number  | 止盈止損觸發價格（當類型為 STOP 時，price 和 triggerPrice 必填） |

{% tabs %}
{% tab title="200: OK" %}
```javascript
{
    'symbol': 'LXTUSDT', 
    'orderId': '150695552109032492', // Long 類型的訂單號
    'clientOrderId': '157371322565051',
    'transactTime': '1573713225668', 
    'price': '0.005452', 
    'origQty': '110', 
    'executedQty': '0', 
    'status': '0',
    'type': 'LIMIT', 
    'side': 'SELL',
    "orderIdString": "1642655717519015937" // 字串類型的訂單號，推薦使用這個
}
```
{% endtab %}
{% endtabs %}

**Response:**

| orderId       | long    | `150695552109032492`   | 訂單 ID（系統生成）                              |
| ------------- | ------- | ---------------------- | ---------------------------------------- |
| orderIdString | string  | `"150695552109032492"` | 字串類型的訂單 ID（推薦使用）                         |
| clientOrderId | string  | `213443`               | 訂單 ID（自己發送的）                             |
| symbol        | string  | `BTCUSDT`              | 幣對名稱                                     |
| transactTime  | integer | `1273774892913`        | 訂單建立時間                                   |
| price         | float   | `4765.29`              | 訂單價格                                     |
| origQty       | float   | `1.01`                 | 訂單數量                                     |
| executedQty   | float   | `1.01`                 | 已成交訂單數量                                  |
| type          | string  | `LIMIT`                | 訂單類型 `LIMIT`（限價）`MARKET`（市價）STOP（止盈止損）   |
| side          | string  | `BUY`                  | 訂單方向。可能出現的值只能為：`BUY`（買入做多）和 `SELL`（賣出做空） |
| status        | string  | `0`                    | 0 = 新訂單                                  |

### 9. 批量下單 private\_post\_batchOrders()

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
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

| X-CH-SIGN   | String | 簽名         |
| ----------- | ------ | ---------- |
| X-CH-APIKEY | String | 您的 API-key |
| X-CH-TS     | String | 時間戳        |

**Request Body**

| symbol\* | String | 幣對名稱 E.g. `BTC/USDT` |
| -------- | ------ | -------------------- |
| orders   | number | 批量訂單資訊，最多 10 條       |

{% tabs %}
{% tab title="200: OK" %}
```javascript
{
    "idsString": [ // 字串類型的訂單 id（推薦使用）
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

| 名稱        | 類型     | 例子             | 描述 |
| --------- | ------ | -------------- | -- |
| price     | float  | 1000           | 價格 |
| volume    | float  | 20.1           | 數量 |
| side      | String | BUY/SELL       | 方向 |
| batchType | String | `LIMIT/MARKET` | 類型 |

**Resquest:**

| idsString | String  | Example | String 類型的訂單號集合 |
| --------- | ------- | ------- | --------------- |
| ids       | integer | 2100    | 訂單號集合           |

### 10. 訂單查詢 fetchOrder()

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.fetchOrder({'symbol':'BTC/USDT','orderId':'90909'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

| orderId\*        | String | 訂單 id                |
| ---------------- | ------ | -------------------- |
| newClientOrderId | String | 客戶端訂單標識              |
| symbol\*         | String | 幣對名稱 E.g. `BTC/USDT` |

**Headers**

| X-CH-SIGN   | String | 簽名         |
| ----------- | ------ | ---------- |
| X-CH-APIKEY | String | 您的 API-key |
| X-CH-TS     | String | 時間戳        |

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

| orderId       | long    | `150695552109032492` | 訂單 ID（系統生成）                                                                                            |
| ------------- | ------- | -------------------- | ------------------------------------------------------------------------------------------------------ |
| clientOrderId | string  | `213443`             | 訂單 ID（自己發送的）                                                                                           |
| symbol        | string  | `BTCUSDT`            | 幣對名稱                                                                                                   |
| transactTime  | integer | `1273774892913`      | 訂單建立時間                                                                                                 |
| price         | float   | `4765.29`            | 訂單價格                                                                                                   |
| origQty       | float   | `1.01`               | 訂單數量                                                                                                   |
| executedQty   | float   | `1.01`               | 已成交訂單數量                                                                                                |
| avgPrice      | float   | `4754.24`            | 訂單已成交的平均價格                                                                                             |
| side          | string  | `BUY`                | 訂單方向。可能出現的值只能為：`BUY`（買入做多）和 `SELL`（賣出做空）                                                               |
| status        | string  | `NEW`                | 訂單狀態。可能出現的值為：`NEW`（新訂單，無成交）、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和 `REJECTED`（訂單被拒絕） |
| transactTime  | string  | 1574327555669        | 訂單建立時間                                                                                                 |

### 11. 撤銷訂單 cancelOrder()

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.cancelOrder({'symbol':'BTC/USDT','orderId':'90909'})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Headers**

| X-CH-SIGN   | String | 簽名         |
| ----------- | ------ | ---------- |
| X-CH-APIKEY | String | 您的 API-key |
| X-CH-TS     | String | 時間戳        |

**Request Body**

| orderId\*        | String | 訂單 id                           |
| ---------------- | ------ | ------------------------------- |
| newClientOrderId | String | 客戶端訂單標識                         |
| symbol\*         | String | 幣對名稱 E.g. `BTCUSDT 或者 BTC/USDT` |

{% tabs %}
{% tab title="200: OK 撤銷訂單成功" %}
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

| orderId       | long   | `150695552109032492` | 訂單 ID（系統生成）                                                                                            |   |
| ------------- | ------ | -------------------- | ------------------------------------------------------------------------------------------------------ | - |
| clientorderId | string | `213443`             | 訂單 ID（自己發送的）                                                                                           |   |
| symbol        | string | `BTCUSDT`            | 幣對名稱                                                                                                   |   |
| status        | string | `NEW`                | 訂單狀態。可能出現的值為：`NEW`（新訂單，無成交）、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和 `REJECTED`（訂單被拒絕） |   |

### 12. 批量撤銷訂單 private\_post\_batchCancel\_order()

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     cancelOrders = [123,321]
     markets = exchange.private_post_batchCancel_order({'symbol':'BTC/USDT','orderIds':cancelOrders})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**一次批量最多 10 個訂單**

**Headers**

| X-CH-SIGN   | String | 簽名         |
| ----------- | ------ | ---------- |
| X-CH-APIKEY | String | 您的 API-key |
| X-CH-TS     | String | 時間戳        |

**Request Body**

| orderIds<mark style="color:red;">\*</mark> | String | 要取消的訂單 id 集合 `[123,456]` |
| ------------------------------------------ | ------ | ------------------------ |
| symbol<mark style="color:red;">\*</mark>   | String | 幣對名稱 E.g. `BTC/USDT`     |

{% tabs %}
{% tab title="200: OK" %}
```javascript
{
    "success": [
        165964665990709251,
        165964665990709252,
        165964665990709253
    ],
    "failed": [ // 取消失敗一般是因為訂單不存在或訂單狀態已到終態
        165964665990709250  
    ]
}
```
{% endtab %}
{% endtabs %}

### 13. 當前訂單 fetchOpenOrders()

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.fetchOpenOrders({'symbol':'BTC/USDT','limit':2})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

| symbol | String | 幣對名稱 E.g. `BTC/USDT（不傳此參數時，api 佔用權重極大）` |
| ------ | ------ | --------------------------------------- |
| limit  | String | 預設 100；最大 1000                          |

**Headers**

| X-CH-SIGN   | String | 簽名         |
| ----------- | ------ | ---------- |
| X-CH-APIKEY | String | 您的 API-key |
| X-CH-TS     | String | 時間戳        |

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

| orderId       | long    | `150695552109032492`   | 訂單 ID（系統生成）                                                                                            |
| ------------- | ------- | ---------------------- | ------------------------------------------------------------------------------------------------------ |
| orderIdString | String  | `"150695552109032492"` | 字串類型的訂單 ID（推薦使用）                                                                                       |
| clientorderId | string  | `213443`               | 訂單 ID（自己發送的）                                                                                           |
| symbol        | string  | `BTCUSDT`              | 幣對名稱                                                                                                   |
| price         | float   | `4765.29`              | 訂單價格                                                                                                   |
| origQty       | float   | `1.01`                 | 訂單數量                                                                                                   |
| executedQty   | float   | `1.01`                 | 已成交訂單數量                                                                                                |
| avgPrice      | float   | `4754.24`              | 訂單已成交的平均價格                                                                                             |
| type          | string  | `LIMIT`                | 訂單類型 `LIMIT`（限價）`MARKET`（市價）                                                                           |
| side          | string  | `BUY`                  | 訂單方向。可能出現的值只能為：`BUY`（買入做多）和 `SELL`（賣出做空）                                                               |
| status        | string  | `NEW`                  | 訂單狀態。可能出現的值為：`NEW`（新訂單，無成交）、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和 `REJECTED`（訂單被拒絕） |
| time          | string  | 1574327555669          | 建立時間                                                                                                   |
| stopPrice     | float   | 21323.32               | 止盈止損觸發價                                                                                                |
| isWorking     | boolean | true                   | 訂單是否出現在 orderbook 中                                                                                    |

### 14. 交易記錄 fetchMyTrades()

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.fetchMyTrades({'symbol':'BTC/USDT','limit':2})
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Query Parameters**

| symbol<mark style="color:red;">\*</mark> | String | 幣對名稱 E.g. `BTC/USDT` |
| ---------------------------------------- | ------ | -------------------- |
| limit                                    | String | 預設 100；最大 1000       |
| fromId                                   | String | 從這個 tradeId 開始檢索     |

**Headers**

| X-CH-SIGN   | String | 簽名         |
| ----------- | ------ | ---------- |
| X-CH-APIKEY | String | 您的 API-key |
| X-CH-TS     | String | 時間戳        |

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

| id        | long    | `150695552109032492` | 成交 id                                    |    |
| --------- | ------- | -------------------- | ---------------------------------------- | -- |
| symbol    | String  | 幣對                   | 字串類型的訂單 ID（推薦使用）                         | ti |
| time      | long    | 1499865549590        | 建立時間                                     |    |
| qty       | string  | `12`                 | 交易數量                                     |    |
| price     | float   | `4765.29`            | 訂單價格                                     |    |
| fee       | string  | `0.001`              | 交易手續費                                    |    |
| feeCoin   | String  | `xxx`                | 手續費幣種                                    |    |
| isBuyer   | boolean | `true`               | `true` = 買，`false` = 賣                   |    |
| isMaker   | boolean | false                | `true` = 市價，`false` = 限價                 |    |
| bidId     | long    | `1200000200`         | 買單 id                                    |    |
| askId     | long    | `1200000200`         | 賣單 id                                    |    |
| side      | string  | `BUY`                | 訂單方向。可能出現的值只能為：`BUY`（買入做多）和 `SELL`（賣出做空） |    |
| bidUserId | long    | 23334                | 買方 uid                                   |    |
| askUserId | long    | 44112                | 賣方 uid                                   |    |
| isSelf    | boolean | true                 | 是否是自成交                                   |    |

### 15. 帳戶資訊 fetchBalance()

**安全類型：USER\_DATA**

```
# Test python document (test_bitwind.py)
import ccxt  # 同步版本

# 初始化交易所
exchange = ccxt.bitwind()
 
 # public_get_sapi_v2_depth
 try:
     markets = exchange.fetchBalance()
     print("Markets:", markets)
 except Exception as e:
     print("Error public_get_sapi_v2_depth:", str(e))
```

**Headers**

| X-CH-SIGN   | String | 簽名         |
| ----------- | ------ | ---------- |
| X-CH-APIKEY | String | 您的 API-key |
| X-CH-TS     | String | 時間戳        |
