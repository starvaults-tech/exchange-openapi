# 幣幣交易

## 公共

#### 安全類型: None

### 測試連接

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/ping`

測試REST API的連通性

{% tabs %}
{% tab title="200: OK " %}

```javascript
{}
```

{% endtab %}
{% endtabs %}

### 服務器時間

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/time`

獲取服務器時間

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

### 幣對列表

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/symbols`

市場支持的幣對集合esponse:

名稱類型例子描述timelong`1595563624731`當前時間(Unix Timestamp, 毫秒ms)bidslist如下訂單薄買盤信息askslist如下訂單薄賣盤信息bids和asks所對應的信息代表了訂單薄的所有價格以及價格對應的數量的信息, 由最優價格從上倒下排列名稱類型例子描述' 'float`131.1`價格' 'float`2.3`當前價格對應的數量GEThttps\://openapi.xxx.com/sapi/v1/ticker\\

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
        },
        {
            "quantityPrecision": 3,
            "symbol": "bchusdt",
            "pricePrecision": 2,
            "baseAsset": "BCH",
            "quoteAsset": "USDT",
            "limitAmountMin": "100",
            "limitPriceMin": "123.45",
            "limitVolumeMin": "10",
            "feeRateMaker": "0.002",
            "feeRateTaker": "0.002"
        },
        {
            "quantityPrecision": 2,
            "symbol": "etcusdt",
            "pricePrecision": 2,
            "baseAsset": "ETC",
            "quoteAsset": "USDT",
            "limitAmountMin": "100",
            "limitPriceMin": "123.45",
            "limitVolumeMin": "10",
            "feeRateMaker": "0.002",
            "feeRateTaker": "0.002"
        },
        {
            "quantityPrecision": 2,
            "symbol": "ltcbtc",
            "pricePrecision": 6,
            "baseAsset": "LTC",
            "quoteAsset": "BTC",
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

**權重(IP/UID): 1**

#### Response: <a href="#bi-dui-lie-biao" id="bi-dui-lie-biao"></a>

| 名稱                | 類型      | 例子        | 描述             |
| ----------------- | ------- | --------- | -------------- |
| symbol            | string  | `BTCUSDT` | 幣對名稱           |
| baseAsset         | string  | `BTC`     | base貨幣         |
| quoteAsset        | string  | `USDT`    | 計價貨幣           |
| pricePrecision    | integer | `2`       | 價格精度           |
| quantityPrecision | integer | `6`       | 數量精度           |
| limitAmountMin    | String  | 100       | 限價單最小下單金額quote |
| limitPriceMin     | String  | 100       | 限價單最小價格        |
| limitVolumeMin    | String  | 100       | 限價單最小下單數量base  |
| baseAssetName     | String  | BTC       | 基準貨幣顯示名稱       |
| quoteAssetName    | String  | USDT      | 計價貨幣顯示名稱       |
| SymbolName        | String  | BTC/USDT  | 幣對顯示名稱         |
| feeRateMaker      | String  | 0.002     | maker手續費率      |
| feeRateMaker      | String  | 0.002     | taker手續費率      |
|                   |         |           |                |

## 行情

#### 安全類型: None

### 訂單薄

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/depth`

市場訂單薄深度信息

#### Query Parameters

| Name                                     | Type    | Description        |
| ---------------------------------------- | ------- | ------------------ |
| limit                                    | integer | 默認100; 最大100       |
| symbol<mark style="color:red;">\*</mark> | String  | 幣對名稱E.g.`BTC/USDT` |

{% tabs %}
{% tab title="200: OK  成功獲取深度信息" %}

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

**權重(IP/UID): 5**

#### Response: <a href="#bi-dui-lie-biao" id="bi-dui-lie-biao"></a>

| time | long | `1595563624731` | 當前時間(Unix Timestamp, 毫秒ms) |
| ---- | ---- | --------------- | -------------------------- |
| bids | list | 如下              | 訂單薄買盤信息                    |
| asks | list | 如下              | 訂單薄賣盤信息                    |

bids和asks所對應的信息代表了訂單薄的所有價格以及價格對應的數量的信息, 由最優價格從上倒下排列

| ' ' | float | `131.1` | 價格        |
| --- | ----- | ------- | --------- |
| ' ' | float | `2.3`   | 當前價格對應的數量 |

### 行情ticker

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/ticker`

24小時價格變化數據

#### Query Parameters

ps: 參數 `symbol` 和 `symbols` 同時提供,則優先取symbol 如果都不提供, 所有symbol的ticker數據都會返回.

| Name    | Type   | Description                                                                       |
| ------- | ------ | --------------------------------------------------------------------------------- |
| symbol  | String | <p>幣對名稱E.g.<code>BTC/USDT</code><br><code>(不傳此參數時, api占用權重極大, 返回結構也不同)</code></p> |
| symbols | String | 幣對名稱，多個使用英文逗號分隔 btcusdt,ethusdt                                                   |

{% tabs %}
{% tab title="200: OK  傳入symbol成功獲取ticker信息" %}

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
{% endtabs %}

{% tabs %}
{% tab title="200: OK  不傳symbol成功獲取ticker信息" %}

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
    },{
        "high": "9279.0301",
        "vol": "1302",
        "last": "9200",
        "low": "9279.0301",
        "rose": "0",
        "time": 1595563624731,
        "symbol": "ethusdt",
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

\
**權重(IP/UID): 5**

**symbol 未提供: 權重 = 80**

**symbols 未提供: 權重 = 80**

**symbols 1-20: 權重 = 5**

**symbols 21-100: 權重 = 40**

**symbols ≥ 101: 權重 = 80**

#### Response:

| time      | long   | `1595563624731` | 時間戳         |   |
| --------- | ------ | --------------- | ----------- | - |
| high      | float  | `9900`          | 最高價         |   |
| low       | float  | `8800.34`       | 最低價         |   |
| open      | float  | `8700`          | 開盤價         |   |
| last      | float  | `8900`          | 最新價         |   |
| vol       | float  | `4999`          | 交易量         |   |
| rose      | float  | 0               | 漲幅          |   |
| symbol    | String | btcusdt         | 幣對          |   |
| amount    | String | 1233            | 交易額，計價貨幣成交量 |   |
| askPrice  | String | 23321           | 賣一價         |   |
| askVolume | String | 3321            | 賣一數量        |   |
| bidPrice  | String | 21              | 買一價         |   |
| bidVolume | String | 12              | 買一數量        |   |

### 最近成交

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/trades`

#### Query Parameters

| Name                                     | Type   | Description        |
| ---------------------------------------- | ------ | ------------------ |
| symbol<mark style="color:red;">\*</mark> | String | 幣對名稱E.g.`BTC/USDT` |
| limit                                    | String | `默認100:最大1000`     |

{% tabs %}
{% tab title="200: OK 成功" %}

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

**權重(IP/UID): 5**

#### Response:

| price | float  | `0.055`         | 交易價格             |   |
| ----- | ------ | --------------- | ---------------- | - |
| time  | long   | `1537797044116` | 當前Unix時間戳，毫秒(ms) |   |
| qty   | float  | `5`             | 數量（張數）           |   |
| side  | string | `BUY/SELL`      | 主動單方向            |   |

### K線/蠟燭圖數據

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/klines`

#### Query Parameters

| Name                                       | Type   | Description                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| symbol<mark style="color:red;">\*</mark>   |        | 幣對名稱E.g.`BTC/USDT`                                                                                                                                                                                                                                                                                                              |
| interval<mark style="color:red;">\*</mark> | String | <p>k線圖區間, 可識別發送的值為：</p><p><code>1min</code></p><p>,</p><p><code>5min</code></p><p>,</p><p><code>15min</code></p><p>,</p><p><code>30min</code></p><p>,</p><p><code>60min</code></p><p>,</p><p><code>1day</code></p><p>,</p><p><code>1week</code></p><p>,</p><p><code>1month</code></p><p>（min=分鐘，h=小時,day=天，week=星期，month=月）</p> |
| startTime                                  | long   | 起始時間點                                                                                                                                                                                                                                                                                                                           |
| endTime                                    | long   | 截止時間點                                                                                                                                                                                                                                                                                                                           |

{% tabs %}
{% tab title="200: OK 成功" %}

```javascript
[
    {
        "high": "6228.77",
        "vol": "111",
        "low": "6228.77",
        "idx": 1594640340,
        "close": "6228.77",
        "open": "6228.77"
    },
    {
        "high": "6228.77",
        "vol": "222",
        "low": "6228.77",
        "idx": 1587632160,
        "close": "6228.77",
        "open": "6228.77"
    },
    {
        "high": "6228.77",
        "vol": "333",
        "low": "6228.77",
        "idx": 1587632100,
        "close": "6228.77",
        "open": "6228.77"
    }
]
```

{% endtab %}
{% endtabs %}

**權重(IP/UID): 1**

#### Response:

| `idx` | long  | `1538728740000` | 開始時間戳，毫秒（ms）   |   |
| ----- | ----- | --------------- | -------------- | - |
| open  | float | `36.00000`      | 開盤價            |   |
| close | float | `33.00000`      | 收盤價            |   |
| high  | float | `36.00000`      | 最高價            |   |
| low   | float | `30.00000`      | 最低價            |   |
| vol   | float | `2456.111`      | <p>成交量<br></p> |   |

## 交易

#### 安全類型: TRADE

交易下方的接口都需要簽名和API-Key驗證

### 創建新訂單

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v2/order`

#### Query Parameters

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 簽名          |
| X-CH-APIKEY | string  | 您的API-Key   |
| X-CH-TS     | integer | 時間戳         |

#### Request Body

| Name                                     | Type    | Description                                                          |
| ---------------------------------------- | ------- | -------------------------------------------------------------------- |
| symbol                                   | String  | 幣對名稱E.g.`BTC/USDT`                                                   |
| volume<mark style="color:red;">\*</mark> | number  | 訂單數量                                                                 |
| side<mark style="color:red;">\*</mark>   | String  | <p>訂單方向,</p><p><code>BUY/SELL</code></p>                             |
| type<mark style="color:red;">\*</mark>   | String  | <p>訂單類型,</p><p><code>LIMIT/MARKET/FOK/POST\_ONLY/IOC/STOP</code></p> |
| price                                    | number  | <p>訂單價格, 對於</p><p><code>LIMIT</code></p><p>訂單必須發送</p>                |
| newClientOrderId                         | String  | 客戶端訂單標識                                                              |
| recvwindow                               | integer | 時間窗口                                                                 |
| triggerPrice                             | number  | <p>止盈止損 觸發價格<br>(當類型為STOP時,price和triggerPrice必填)</p>                 |

{% tabs %}
{% tab title="200: OK " %}

<pre class="language-javascript"><code class="lang-javascript">{
    'symbol': 'LXTUSDT', 
    'orderId': '150695552109032492', //Long類型的訂單號
    'clientOrderId': '157371322565051',
    'transactTime': '1573713225668', 
    'price': '0.005452', 
    'origQty': '110', 
    'executedQty': '0', 
    'status': '0',
    'type': 'LIMIT', 
    'side': 'SELL',
<strong>    "orderIdString": "1642655717519015937" //字符串類型的訂單號,推薦使用這個
</strong>

}
</code></pre>

{% endtab %}
{% endtabs %}

**權重(IP/UID): 5**

#### Response:

| orderId       | long    | `150695552109032492`   | 訂單ID（系統生成）                                                             |   |
| ------------- | ------- | ---------------------- | ---------------------------------------------------------------------- | - |
| orderIdString | string  | "`150695552109032492"` | 字符串類型的訂單ID(推薦使用)                                                       |   |
| clientOrderId | string  | `213443`               | 訂單ID（自己發送的）                                                            |   |
| symbol        | string  | `BTCUSDT`              | 幣對名稱                                                                   |   |
| transactTime  | integer | `1273774892913`        | 訂單創建時間                                                                 |   |
| price         | float   | `4765.29`              | 訂單價格                                                                   |   |
| origQty       | float   | `1.01`                 | 訂單數量                                                                   |   |
| executedQty   | float   | `1.01`                 | 已經成交訂單數量                                                               |   |
| type          | string  | `LIMIT`                | <p>訂單類型<code>LIMIT</code>(限價)<code>MARKET</code>（市價）<br>STOP(止盈止損)</p> |   |
| side          | string  | `BUY`                  | 訂單方向。可能出現的值只能為：`BUY`（買入做多） 和 `SELL`（賣出做空）                              |   |
| status        | string  | `0`                    | 0 = 新訂單                                                                |   |

### 創建測試訂單

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v2/order/test`

創建和驗證新訂單, 但不會送入撮合引擎

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

#### Request Body

| Name                                     | Type    | Description                                           |
| ---------------------------------------- | ------- | ----------------------------------------------------- |
| recvwindow                               | integer | 時間窗口                                                  |
| symbol<mark style="color:red;">\*</mark> | String  | <p>幣對名稱 E.g.</p><p><code>BTCUSDT或者BTC/USDT</code></p> |
| volume<mark style="color:red;">\*</mark> | number  | 訂單數量                                                  |
| side<mark style="color:red;">\*</mark>   | String  | <p>訂單方向,</p><p><code>BUY/SELL</code></p>              |
| type<mark style="color:red;">\*</mark>   | String  | <p>訂單類型,</p><p><code>LIMIT/MARKET</code></p>          |
| price<mark style="color:red;">\*</mark>  | number  | <p>訂單價格, 對於</p><p><code>LIMIT</code></p><p>訂單必須發送</p> |
| newClientorderId                         | String  | 客戶端訂單標識                                               |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    // Response
}
```

{% endtab %}
{% endtabs %}

**權重(IP/UID): 1**

***

***

### 批量下單

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v2/batchOrders`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

#### Request Body

| Name                                     | Type   | Description        |
| ---------------------------------------- | ------ | ------------------ |
| symbol<mark style="color:red;">\*</mark> | String | 幣對名稱E.g.`BTC/USDT` |
| orders                                   | number | 批量訂單信息 最多10條       |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "idsString": [ //字符串類型的訂單id(推薦使用)
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

**權重(IP/UID): 10**

#### Resquest `orders` field:

| 名稱        | 類型     | 例子             | 描述 |
| --------- | ------ | -------------- | -- |
| price     | folat  | 1000           | 價格 |
| volume    | folat  | 20.1           | 數量 |
| side      | String | BUY/SELL       | 方向 |
| batchType | String | `LIMIT/MARKET` | 類型 |

#### Resquest: <a href="#resquest-orders-field" id="resquest-orders-field"></a>

| idsString | String  | “3213213” | String類型的訂單號集合 |   |
| --------- | ------- | --------- | -------------- | - |
| ids       | integer | 2100      | 訂單號集合          |   |

### 訂單查詢

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/order`

#### Query Parameters

| Name                                      | Type   | Description        |
| ----------------------------------------- | ------ | ------------------ |
| orderId<mark style="color:red;">\*</mark> | String | 訂單id               |
| newClientOrderId                          | String | 客戶端訂單標識            |
| symbol<mark style="color:red;">\*</mark>  | String | 幣對名稱E.g.`BTC/USDT` |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

{% tabs %}
{% tab title="200: OK " %}

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

**權重(IP/UID): 1**

#### **Response:**

| orderId       | long    | `150695552109032492` | 訂單ID（系統生成）                                                                                                 |   |
| ------------- | ------- | -------------------- | ---------------------------------------------------------------------------------------------------------- | - |
| clientOrderId | string  | `213443`             | 訂單ID（自己發送的）                                                                                                |   |
| symbol        | string  | `BTCUSDT`            | 幣對名稱                                                                                                       |   |
| transactTime  | integer | `1273774892913`      | 訂單創建時間                                                                                                     |   |
| price         | float   | `4765.29`            | 訂單價格                                                                                                       |   |
| origQty       | float   | `1.01`               | 訂單數量                                                                                                       |   |
| executedQty   | float   | `1.01`               | 已經成交訂單數量                                                                                                   |   |
| avgPrice      | float   | `4754.24`            | 訂單已經成交的平均價格                                                                                                |   |
| side          | string  | `BUY`                | 訂單方向。可能出現的值只能為：`BUY`（買入做多） 和 `SELL`（賣出做空）                                                                  |   |
| status        | string  | `NEW`                | 訂單狀態。可能出現的值為：`NEW`(新訂單，無成交)、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和`REJECTED`（訂單被拒絕）.POST |   |
| transactTime  | string  | 1574327555669        | 訂單創建時間                                                                                                     |   |

### 撤銷訂單

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v2/cancel`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

#### Request Body

| Name                                      | Type   | Description                                           |
| ----------------------------------------- | ------ | ----------------------------------------------------- |
| orderId<mark style="color:red;">\*</mark> | String | 訂單id                                                  |
| newClientOrderId                          | String | 客戶端訂單標識                                               |
| symbol<mark style="color:red;">\*</mark>  | String | <p>幣對名稱 E.g.</p><p><code>BTCUSDT或者BTC/USDT</code></p> |

{% tabs %}
{% tab title="200: OK  撤銷訂單成功" %}

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

**權重(IP/UID): 5**

#### Response:

| orderId       | long   | `150695552109032492` | 訂單ID（系統生成）                                                                                                 |   |
| ------------- | ------ | -------------------- | ---------------------------------------------------------------------------------------------------------- | - |
| clientorderId | string | `213443`             | 訂單ID（自己發送的）                                                                                                |   |
| symbol        | string | `BTCUSDT`            | 幣對名稱                                                                                                       |   |
| status        | string | `NEW`                | 訂單狀態。可能出現的值為：`NEW`(新訂單，無成交)、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和`REJECTED`（訂單被拒絕）.POST |   |

### 批量撤銷訂單

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v2/batchCancel`

**一次批量最多10個訂單**

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

#### Request Body

| Name                                       | Type   | Description                                     |
| ------------------------------------------ | ------ | ----------------------------------------------- |
| orderIds<mark style="color:red;">\*</mark> | String | <p>要取消的訂單id集合</p><p><code>\[123,456]</code></p> |
| symbol<mark style="color:red;">\*</mark>   | String | 幣對名稱E.g.`BTC/USDT`                              |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "success": [
        165964665990709251,
        165964665990709252,
        165964665990709253
    ],
    "failed": [ //取消失敗一般是因為訂單不存在或訂單狀態已經到終態
        165964665990709250  
    ]
}
```

{% endtab %}
{% endtabs %}

**權重(IP/UID): 10**

***

***

### 當前訂單

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/openOrders`

#### Query Parameters

| Name   | Type   | Description                                                              |
| ------ | ------ | ------------------------------------------------------------------------ |
| symbol | String | <p>幣對名稱E.g.<code>BTC/USDT</code><br><code>(不傳此參數時, api占用權重極大)</code></p> |
| limit  | String | 默認100; 最大1000                                                            |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

{% tabs %}
{% tab title="200: OK " %}

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

#### **權重(IP/UID): 1**

#### Response:

| orderId       | long    | `150695552109032492`   | 訂單ID（系統生成）                                                                                                 |   |
| ------------- | ------- | ---------------------- | ---------------------------------------------------------------------------------------------------------- | - |
| orderIdString | String  | "`150695552109032492"` | 字符串類型的訂單ID(推薦使用)                                                                                           |   |
| clientorderId | string  | `213443`               | 訂單ID（自己發送的）                                                                                                |   |
| symbol        | string  | `BTCUSDT`              | 幣對名稱                                                                                                       |   |
| price         | float   | `4765.29`              | 訂單價格                                                                                                       |   |
| origQty       | float   | `1.01`                 | 訂單數量                                                                                                       |   |
| executedQty   | float   | `1.01`                 | 已經成交訂單數量                                                                                                   |   |
| avgPrice      | float   | `4754.24`              | 訂單已經成交的平均價格                                                                                                |   |
| type          | string  | `LIMIT`                | 訂單類型`LIMIT`(限價)`MARKET`（市價）                                                                                |   |
| side          | string  | `BUY`                  | 訂單方向。可能出現的值只能為：`BUY`（買入做多） 和 `SELL`（賣出做空）                                                                  |   |
| status        | string  | `NEW`                  | 訂單狀態。可能出現的值為：`NEW`(新訂單，無成交)、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和`REJECTED`（訂單被拒絕）.POST |   |
| time          | string  | 1574327555669          | 創建時間                                                                                                       |   |
| stopPrice     | float   | 21323.32               | 止盈止損觸發價                                                                                                    |   |
| isWorking     | boolean | true                   | 訂單是否出現在orderbook中                                                                                          |   |

### 交易記錄

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v2/myTrades`

#### Query Parameters

| Name                                     | Type   | Description        |
| ---------------------------------------- | ------ | ------------------ |
| symbol<mark style="color:red;">\*</mark> | String | 幣對名稱E.g.`BTC/USDT` |
| limit                                    | String | 默認100; 最大1000      |
| fromId                                   | String | 從這個tradeId開始檢索     |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

{% tabs %}
{% tab title="200: OK " %}

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

**權重(IP/UID): 1**

#### Response:

| id        | long    | `150695552109032492` | 成交id                                      |    |
| --------- | ------- | -------------------- | ----------------------------------------- | -- |
| symbol    | String  | 幣對                   | 字符串類型的訂單ID(推薦使用)                          | ti |
| time      | long    | 1499865549590        | 創建時間                                      |    |
| qty       | string  | `12`                 | 交易數量                                      |    |
| price     | float   | `4765.29`            | 訂單價格                                      |    |
| fee       | string  | `0.001`              | 交易手續費幣                                    |    |
| feeCoin   | String  | `xxx`                | 手續費幣種                                     |    |
| isBuyer   | boolean | `true`               | `true`= 買 `false`= 賣                      |    |
| isMaker   | boolean | false                | `true`=市價 `false`=限價                      |    |
| bidId     | long    | `1200000200`         | 買單id                                      |    |
| askId     | long    | `1200000200`         | 賣單id                                      |    |
| side      | string  | `BUY`                | 訂單方向。可能出現的值只能為：`BUY`（買入做多） 和 `SELL`（賣出做空） |    |
| bidUserId | long    | 23334                | 買方uid                                     |    |
| askUserId | long    | 44112                | 賣方uid                                     |    |
| isSelf    | boolean | true                 | 是否是自成交                                    |    |

## 賬戶

#### 安全類型: USER\_DATA

### 賬戶信息

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v1/account`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

{% tabs %}
{% tab title="200: OK " %}

```javascript
```

{% endtab %}
{% endtabs %}

**權重(IP/UID): 1**

### 劃轉

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/asset/transfer`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

#### Request Body

| Name                                          | Type   | Description                                    |
| --------------------------------------------- | ------ | ---------------------------------------------- |
| coinSymbol<mark style="color:red;">\*</mark>  | String | 幣種                                             |
| amount<mark style="color:red;">\*</mark>      | float  | 數量                                             |
| fromAccount<mark style="color:red;">\*</mark> | String | <p>轉出賬戶<br>EXCHANGE 現貨賬戶</p><p>FUTURE 合約賬戶</p> |
| toAccount<mark style="color:red;">\*</mark>   | String | <p>轉入賬戶<br>EXCHANGE 現貨賬戶</p><p>FUTURE 合約賬戶</p> |

{% tabs %}
{% tab title="200: OK  劃轉成功" %}

```javascript
{
    "code": "0",
    "msg": "成功",
    "data": {
        "transferId": "1a9ec387-8b81-4789-a98e-bc6a606c8736"
    }
}
```

{% endtab %}
{% endtabs %}

**權重(IP/UID): 5**

#### Response:

| transferId | String |

```
1a9ec387-8b81-4789-a98e-bc6a606c8736
```

| 劃轉id | |\
| ---------- | ------ | ------------------------------------------------------------- | ---- | - |

### 劃轉記錄查詢

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/asset/transferQuery`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-APIKEY | String | 您的API-key   |
| X-CH-TS     | String | 時間戳         |

#### Request Body

ps:\
transferId不傳時，fromAccount/toAccount必填\
startTime和endTime不傳時，默認返回最近7天數據\
僅支持查詢最近6個月數據

| Name        | Type    | Description                                           |
| ----------- | ------- | ----------------------------------------------------- |
| transferId  | String  | 劃轉id                                                  |
| coinSymbol  | String  | 幣種                                                    |
| fromAccount | String  | <p>轉出賬戶</p><p>EXCHANGE 現貨賬戶</p><p>FUTURE 合約賬戶<br></p> |
| toAccount   | String  | <p>轉入賬戶<br>EXCHANGE 現貨賬戶</p><p>FUTURE 合約賬戶</p>        |
| startTime   | long    | 開始時間, 13位時間戳                                          |
| endTime     | long    | 結束時間, 13位時間戳                                          |
| page        | Integer | page不傳默認為1                                            |
| limit       | Integer | limit不傳默認為20，最大為100                                   |

{% tabs %}
{% tab title="200: OK  劃轉成功" %}

```javascript
{
    "code": "0",
    "msg": "成功",
    "data": {
        "list": [
            {
                "transferId": "1a9ec387-8b81-4789-a98e-bc6a606c8736",
                "fromAccount": "EXCHANGE",
                "toAccount": "FUTURE",
                "coinSymbol": "USDT",
                "createTime": 1742369830000,
                "amount": "1",
                "status": "SUCCESS"
            }
        ]
    }
}
```

{% endtab %}
{% endtabs %}

**權重(IP/UID): 5**

#### Response:

| transferId | String |

```
1a9ec387-8b81-4789-a98e-bc6a606c8736
```

| 劃轉id | |\
| ----------- | ------ | ------------------------------------------------------------- | --------------------------------------------------------- | - |\
| fromAccount | String | EXCHANGE | 轉出賬戶 | |\
| toAccount | String | FUTURE | 轉入賬戶 | |\
| coinSymbol | String | USDT | 幣種 | |\
| createTime | long | 1742300000000 | 創建時間戳 | |\
| amount | String | 1 | 數量 | |\
| status | String | SUCCESS |

狀態\
SUCCESS = 成功\
PENDING = 劃轉中\
FAILED = 失敗