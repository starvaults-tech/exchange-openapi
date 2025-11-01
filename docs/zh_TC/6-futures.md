# 合約交易

## 公共

### 安全類型

公共下方的接口不需要API-key或者簽名就能自由訪問

## 測試連接

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/ping`

測試REST API的連通性

{% tabs %}
{% tab title="200  連接正常" %}

```
{}
```

{% endtab %}
{% endtabs %}

## 獲取服務器時間

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/time`

{% tabs %}
{% tab title="200 " %}

```
{
    "serverTime":1607702400000,
    "timezone":中國標準時間
}
```

{% endtab %}
{% endtabs %}

#### Response:

| 名稱         | 類型     | 例子            | 描述     |
| ---------- | ------ | ------------- | ------ |
| serverTime | long   | 1607702400000 | 服務器時間戳 |
| timezone   | string | 中國標準時間        | 服務器時區  |

## 合約列表

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/contracts`

{% tabs %}
{% tab title="200 " %}

```json
[
    {
        "symbol": "H-HT-USDT",
        "pricePrecision": 8,
        "side": 1,
        "maxMarketVolume": 100000,
        "multiplier": 6,
        "minOrderVolume": 1,
        "maxMarketMoney": 10000000,
        "type": "H",
        "maxLimitVolume": 1000000,
        "maxValidOrder": 20,
        "multiplierCoin": "HT",
        "minOrderMoney": 0.001,
        "maxLimitMoney": 1000000,
        "status": 1,
        "minLever": 1,
        "maxLever": 75,
        "openTakerFee":0.0002,
        "openMakerFee":0.0002,
        "closeTakerFee":0.0002,
        "closeMakerFee":0.0002
    }
]
```

{% endtab %}
{% endtabs %}

#### Response:

| 名稱              | 類型     | 例子           | 描述                           |
| --------------- | ------ | ------------ | ---------------------------- |
| symbol          | string | `E-BTC-USDT` | 合約名稱                         |
| status          | number | `1`          | 合約狀態（0：不可交易，1：可交易            |
| type            | string | `S`          | 合約類型，E:永續合約, S:模擬合約, 其他為混合合約 |
| side            | number | `1`          | 合約方向(反向：0，1：正向)              |
| multiplier      | number | `0.5`        | 合約面值                         |
| multiplierCoin  | string | `BTC`        | 合約面值單位                       |
| pricePrecision  | number | `4`          | 價格精度                         |
| minOrderVolume  | number | `10`         | 最小下單量                        |
| minOrderMoney   | number | `10`         | 最小下單金額                       |
| maxMarketVolume | number | `100000`     | 市價單最大下單數量                    |
| maxMarketMoney  | number | `100000`     | 市價最大下單金額                     |
| maxLimitVolume  | number | `100000`     | 限價單最大下單數量                    |
| maxValidOrder   | number | `100000`     | 最大有效委托的訂單數量                  |
| minLever        | number | `5`          | 杠桿最小倍數                       |
| maxLever        | number | `5`          | 杠桿最大倍數                       |
| openTakerFee    | number | `0.0002`     | 開倉taker手續費                   |
| openMakerFee    | number | `0.0002`     | 開倉maker手續費                   |
| closeTakerFee   | number | `0.0002`     | 平倉taker手續費                   |
| closeMakerFee   | number | `0.0002`     | 平倉maker手續費                   |

## 行情相關

### 安全類型

行情下方的接口不需要API-Key或者簽名就能自由訪問

## 訂單薄

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/depth`

市場訂單薄深度信息

#### Query Parameters

| Name         | Type    | Description         |
| ------------ | ------- | ------------------- |
| limit        | integer | 默認100; 最大100        |
| contractName | string  | 合約合約名稱 如 E-BTC-USDT |

{% tabs %}
{% tab title="200  成功獲取深度信息" %}

```java
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

#### Response:

| 名稱   | 類型   | 例子              | 描述                         |
| ---- | ---- | --------------- | -------------------------- |
| time | long | `1595563624731` | 當前時間(Unix Timestamp, 毫秒ms) |
| bids | list | 如下              | 訂單薄買盤信息                    |
| asks | list | 如下              | 訂單薄賣盤信息                    |

bids和asks所對應的信息代表了訂單薄的所有價格以及價格對應的數量的信息, 由最優價格從上倒下排列

| 名稱  | 類型    | 例子      | 描述        |
| --- | ----- | ------- | --------- |
| ' ' | float | `131.1` | 價格        |
| ' ' | float | `2.3`   | 當前價格對應的數量 |

## 行情ticker

<mark style="color:blue;">`GET`</mark> `https://futuersopenapi.xxx.xx/fapi/v1/ticker`

24小時價格變化數據

#### Query Parameters

| Name         | Type   | Description       |
| ------------ | ------ | ----------------- |
| contractName | string | 合約名稱 如 E-BTC-USDT |

{% tabs %}
{% tab title="200  成功獲取ticker信息" %}

```java
{
    "high": "9279.0301",
    "vol": "1302",
    "last": "9200",
    "low": "9279.0301",
    "rose": "0",
    "time": 1595563624731
}
```

{% endtab %}
{% endtabs %}

#### Response:

| 名稱   | 類型     | 例子              | 描述  |
| ---- | ------ | --------------- | --- |
| time | long   | `1595563624731` | 時間戳 |
| high | float  | `9900`          | 最高價 |
| low  | float  | `8800.34`       | 最低價 |
| last | float  | `8900`          | 最新價 |
| vol  | float  | `4999`          | 交易量 |
| rose | string | +0.5            | 漲跌幅 |

## 所有行情ticker

<mark style="color:blue;">`GET`</mark> `https://futuersopenapi.xxx.xx/fapi/v1/ticker_all`

{% tabs %}
{% tab title="200  成功獲取ticker信息" %}

```json
{"e_btcusdt":{"high": "9279.0301",
    "vol": "1302",
    "last": "9200",
    "low": "9279.0301",
    "rose": "0",
    "time": 1595563624731
},"e_ethusdt":{
    "high": "9279.0301",
    "vol": "1302",
    "last": "9200",
    "low": "9279.0301",
    "rose": "0",
    "time": 1595563624731
}}
```

{% endtab %}
{% endtabs %}

#### Response:

| 名稱   | 類型     | 例子              | 描述  |   |
| ---- | ------ | --------------- | --- | - |
| time | long   | `1595563624731` | 時間戳 |   |
| high | float  | `9900`          | 最高價 |   |
| low  | float  | `8800.34`       | 最低價 |   |
| last | float  | `8900`          | 最新價 |   |
| vol  | float  | `4999`          | 交易量 |   |
| rose | string | +0.5            | 漲跌幅 |   |

## 獲取指數/標記價格

<mark style="color:blue;">`GET`</mark> `https://futuersopenapi.xxx.xx/fapi/v1/index`

#### Query Parameters

| Name         | Type   | Description       |
| ------------ | ------ | ----------------- |
| contractName | string | 合約名稱 如 E-BTC-USDT |
| limit        | string | 默認100; 最大1000     |

{% tabs %}
{% tab title="200 " %}

```java
{
    "markPrice": 581.5,
    "indexPrice": 646.3933333333333,
    "lastFundingRate": 0.001,
    "contractName": "E-ETH-USDT",
    "time": 1608273554063
}
```

{% endtab %}
{% endtabs %}

#### **Response:**

| 名稱                | 類型     | 例子           | 描述     |
| ----------------- | ------ | ------------ | ------ |
| `indexPrice`      | float  | `0.055`      | 指數價格   |
| `markPrice`       | float  | `0.0578`     | 標記價格   |
| `contractName`    | string | `E-BTC-USDT` | 合約名稱   |
| `lastFundingRate` | float  | `0.123`      | 本期資金費率 |

## K線/蠟燭圖數據

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/klines`

#### Query Parameters

| Name         | Type    | Description                                                                                                    |
| ------------ | ------- | -------------------------------------------------------------------------------------------------------------- |
| contractName | string  | 合約名稱 如 E-BTC-USDT                                                                                              |
| interval     | string  | k線圖區間, 可識別發送的值為： `1min`,`5min`,`15min`,`30min`,`1h`,`1day`,`1week`,`1month`（min=分鐘，h=小時,day=天，week=星期，month=月） |
| limit        | integer | 默認100; 最大300                                                                                                   |

{% tabs %}
{% tab title="200 " %}

```java
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

#### **Response:**

| 名稱      | 類型    | 例子              | 描述           |
| ------- | ----- | --------------- | ------------ |
| `idx`   | long  | `1538728740000` | 開始時間戳，毫秒（ms） |
| `open`  | float | `36.00000`      | 開盤價          |
| `close` | float | `33.00000`      | 收盤價          |
| `high`  | float | `36.00000`      | 最高價          |
| `low`   | float | `30.00000`      | 最低價          |
| `vol`   | float | `2456.111`      | 成交量          |

## 交易相關

### 安全類型

交易下方的接口都需要簽名和API-key驗證

## 創建訂單

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/order`

創建單個新訂單

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-TS     | string | 時間戳         |
| X-CH-APIKEY | string | 您的API-KEY   |
| X-CH-SIGN   | string | 簽名          |

#### Request Body

| Name          | Type   | Description           |
| ------------- | ------ | --------------------- |
| volume        | number | 下單數量                  |
| price         | number | 下單價格                  |
| contractName  | string | 合約名稱 如 `E-BTC-USDT`   |
| type          | string | 訂單類型, `LIMIT/MARKET`  |
| side          | string | 買賣方向, `BUY/SELL`      |
| open          | string | 開平倉方向, `OPEN/CLOSE`   |
| positionType  | number | 持倉類型, `1全倉/2逐倉`       |
| clientOrderId | string | 客戶端下單標識, 長度小於32位的字符串  |
| timeInForce   | string | `IOC, FOK, POST_ONLY` |

{% tabs %}
{% tab title="200 " %}

```java
{
    "orderId": 256609229205684228
}
```

{% endtab %}
{% endtabs %}

#### Response:

| 名稱      | 類型     | 例子                   | 描述   |
| ------- | ------ | -------------------- | ---- |
| orderId | string | `256609229205684228` | 訂單ID |

## 創建條件單

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/conditionOrder`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-TS     | string | 時間戳         |
| X-CH-APIKEY | string | 您的API-KEY   |
| X-CH-SIGN   | string | 簽名          |

#### Request Body

| Name          | Type   | Description          |
| ------------- | ------ | -------------------- |
| volume        | number | 下單數量                 |
| price         | number | 下單價格                 |
| contractName  | string | 合約名稱 如 `E-BTC-USDT`  |
| type          | string | 訂單類型, `LIMIT/MARKET` |
| side          | string | 買賣方向, `BUY/SELL`     |
| open          | string | 開平倉方向, `OPEN/CLOSE`  |
| positionType  | number | 持倉類型, `1全倉/2逐倉`      |
| clientOrderId | string | 客戶端下單標識, 長度小於32位的字符串 |
| triggerType   | string | 條件單類型，`3追漲/4殺跌`      |
| triggerPrice  | string | 觸發價                  |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "orderId": 256609229205684228
}
```

{% endtab %}
{% endtabs %}

## 取消訂單

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/cancel`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 簽名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 時間戳         |

#### Request Body

| Name         | Type   | Description        |
| ------------ | ------ | ------------------ |
| contractName | string | 合約名稱如 `E-BTC-USDT` |
| orderId      | string | 訂單ID               |

{% tabs %}
{% tab title="200 " %}

```java
{
    "orderId": 256609229205684228
}
```

{% endtab %}
{% endtabs %}

## 取消全部訂單

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/cancel_all`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 簽名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 時間戳         |

#### Request Body

{% tabs %}
{% tab title="200 : OK 成功code為0，code小於0為錯誤，msg為錯誤原因" %}

```json
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 訂單詳情

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/order`

#### Query Parameters

| Name                                           | Type   | Description |
| ---------------------------------------------- | ------ | ----------- |
| contractName<mark style="color:red;">\*</mark> | string | 合約名稱        |
| orderId<mark style="color:red;">\*</mark>      | string | 訂單ID        |
| clientOrderId                                  | string | 客戶端唯一標識     |

{% tabs %}
{% tab title="200 " %}

```
[
    {
       "side": "BUY",
       "executedQty": 0,
       "orderId": 259396989397942275,
       "price": 10000.0000000000000000,
       "origQty": 1.0000000000000000,
       "avgPrice": 0E-8,
       "transactTime": "1607702400000",
       "action": "OPEN",
       "contractName": "E-BTC-USDT",
       "type": "LIMIT",
       "status": "INIT"
    }
]


```

{% endtab %}
{% endtabs %}

#### Response:

| 名稱             | 類型     | 例子                   | 描述                                                                                                    |
| -------------- | ------ | -------------------- | ----------------------------------------------------------------------------------------------------- |
| `orderId`      | long   | `150695552109032492` | 訂單ID（系統生成                                                                                             |
| `contractName` | string | `E-BTC-USDT`         | 合約名稱                                                                                                  |
| `price`        | float  | `10.5`               | 委托價格                                                                                                  |
| `origQty`      | float  | `10.5`               | 委托數量                                                                                                  |
| `executedQty`  | float  | `20`                 | 委托數量                                                                                                  |
| `avgPrice`     | float  | `10.5`               | 成交均價                                                                                                  |
| `symbol`       | string | `BHTUSDT`            | 幣對名稱                                                                                                  |
| `status`       | string | `NEW`                | 訂單狀態。可能出現的值為：`NEW`(新訂單，無成交)、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和`REJECTED`（訂單被拒絕） |
| `side`         | string | `NEW`                | 訂單方向。可能出現的值只能為：BUY（買入做多） 和 SELL（賣出做空）                                                                 |
| `action`       | string | `OPEN`               | `OPEN/CLOSE`                                                                                          |
| `transactTime` | long   | `1607702400000`      | 訂單創建時間                                                                                                |

## 當前訂單

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/openOrders`

**限速規則:**\
**獲取當前合約, 該用戶的當前委托**

#### Query Parameters

| Name         | Type   | Description                     |
| ------------ | ------ | ------------------------------- |
| contractName | string | 不傳該字段，查詢全部合約。 合約名稱 `E-BTC-USDT` |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | string | 簽名          |
| X-CH-APIKEY | string | 您的API-key   |
| X-CH-TS     | string | 時間戳         |

{% tabs %}
{% tab title="200 " %}

```java
[
    {
       "side": "BUY",
       "executedQty": 0,
       "orderId": 259396989397942275,
       "price": 10000.0000000000000000,
       "origQty": 1.0000000000000000,
       "avgPrice": 0E-8,
       "transactTime": "1607702400000",
       "action": "OPEN",
       "contractName": "E-BTC-USDT",
       "type": "LIMIT",
       "status": "INIT"
    }
]

```

{% endtab %}
{% endtabs %}

#### **Response:**

| 名稱             | 類型     | 例子                   | 描述                                                                                                     |
| -------------- | ------ | -------------------- | ------------------------------------------------------------------------------------------------------ |
| `orderId`      | long   | `150695552109032492` | 訂單ID（系統生成）                                                                                             |
| `contractName` | string | `E-BTC-USDT`         | 合約名稱                                                                                                   |
| `price`        | float  | `4765.29`            | 訂單價格                                                                                                   |
| `origQty`      | float  | `1.01`               | 訂單數量                                                                                                   |
| `executedQty`  | float  | `1.01`               | 已經成交訂單數量                                                                                               |
| `avgPrice`     | float  | `4754.24`            | 訂單已經成交的平均價格                                                                                            |
| `type`         | string | `LIMIT`              | 訂單類型。可能出現的值只能為:`LIMIT`(限價)和`MARKET`（市價）                                                                |
| `side`         | string | `BUY`                | 訂單方向。可能出現的值只能為：`BUY`（買入做多） 和 `SELL`（賣出做空）                                                              |
| `status`       | string | `NEW`                | 訂單狀態。可能出現的值為：`NEW`(新訂單，無成交)、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和`REJECTED`（訂單被拒絕）. |
| `action`       | string | `OPEN`               | `OPEN/CLOSE`                                                                                           |
| `transactTime` | long   | `1607702400000`      | 訂單創建時間,                                                                                                |

## 歷史委托

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/orderHistorical`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | string | 簽名          |
| X-CH-APIKEY | string | 您的API-key   |
| X-CH-TS     | string | 時間戳         |

#### Request Body

| Name         | Type   | Description         |
| ------------ | ------ | ------------------- |
| contractName | string | 合約名稱 `E-BTC-USDT`   |
| limit        | string | 分頁條數, 默認100; 最大1000 |
| fromId       | long   | 從這條記錄開始檢索           |

{% tabs %}
{% tab title="200: OK " %}

```javascript
[
    {
        "side":"BUY",
        "clientId":"0",
        "ctimeMs":1632903411000,
        "positionType":2,
        "orderId":777293886968070157,
        "avgPrice":41000,
        "openOrClose":"OPEN",
        "leverageLevel":26,
        "type":4,
        "closeTakerFeeRate":0.00065,
        "volume":2,
        "openMakerFeeRate":0.00025,
        "dealVolume":1,
        "price":41000,
        "closeMakerFeeRate":0.00025,
        "contractId":1,
        "ctime":"2021-09-29T16:16:51",
        "contractName":"E-BTC-USDT",
        "openTakerFeeRate":0.00065,
        "dealMoney":4.1,
        "status":4
    }
]
```

{% endtab %}
{% endtabs %}

## 盈虧記錄

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/profitHistorical`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | string | 簽名          |
| X-CH-APIKEY | string | 您的API-key   |
| X-CH-TS     | string | 時間戳         |

#### Request Body

| Name         | Type   | Description         |
| ------------ | ------ | ------------------- |
| contractName | string | 合約名稱 `E-BTC-USDT`   |
| limit        | string | 分頁條數, 默認100; 最大1000 |
| fromId       | long   | 從這條記錄開始檢索           |

{% tabs %}
{% tab title="200: OK " %}

```javascript
[
    {
        "side":"SELL",
        "positionType":2,
        "tradeFee":-5.23575,
        "realizedAmount":0,
        "leverageLevel":26,
        "openPrice":44500,
        "settleProfit":0,
        "mtime":1632882739000,
        "shareAmount":0,
        "openEndPrice":44500,
        "closeProfit":-45,
        "volume":900,
        "contractId":1,
        "historyRealizedAmount":-50.23575,
        "ctime":1632882691000,
        "id":8764,
        "capitalFee":0
    }
]
```

{% endtab %}
{% endtabs %}

## 交易記錄

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/myTrades`

#### Query Parameters

| Name         | Type   | Description         |
| ------------ | ------ | ------------------- |
| contractName | string | 合約名稱 如 E-BTC-USDT   |
| limit        | string | 分頁條數, 默認100; 最大1000 |
| fromId       | long   | 從這個tradeId開始檢索      |

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 簽名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 時間戳         |

{% tabs %}
{% tab title="200 " %}

```java
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
    "fee":"0.001"
  },...
]
```

{% endtab %}
{% endtabs %}

#### **Response:**

| 名稱           | 類型      | 例子                 | 描述                     |
| ------------ | ------- | ------------------ | ---------------------- |
| symbol       | string  | ETHBTC             | 幣種名稱(交易對)              |
| tradeId      | number  | 28457              | 交易ID                   |
| bidId        | long    | 150695552109032492 | 買方訂單ID                 |
| askId        | long    | 150695552109032493 | 賣方訂單ID                 |
| bidUserId    | integer | 10024              | 買方用戶ID                 |
| askUserId    | integer | 10025              | 賣方用戶ID                 |
| price        | float   | 4.01               | 成交價格                   |
| qty          | float   | 12                 | 交易數量                   |
| amount       | float   | 5.38               | 成交金額                   |
| time         | number  | 1499865549590      | 交易時間戳                  |
| fee          | number  | 0.001              | 交易手續費                  |
| side         | string  | buy                | 當前訂單方向 BUY 買入, SELL 賣出 |
| contractName | string  | E-BTC-USDT         | 合約名稱                   |
| isMaker      | boolean | true               | 是否是maker               |
| isBuyer      | boolean | true               | 是否買方                   |

## 更改持倉模式

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/edit_user_position_model`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 簽名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 時間戳         |

**Request Body**

| Name                                            | Type    | Description               |
| ----------------------------------------------- | ------- | ------------------------- |
| contractName<mark style="color:red;">\*</mark>  | string  | 合約名稱 `E-BTC-USDT`         |
| positionModel<mark style="color:red;">\*</mark> | integer | 持倉模式 （1.凈持倉 2.雙向持倉）傳入1或者2 |

{% tabs %}
{% tab title="200 : OK 成功code為0，code小於0為錯誤，msg為錯誤原因" %}

```java
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 更改保證金模式

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/edit_user_margin_model`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 簽名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 時間戳         |

**Request Body**

| Name                                           | Type    | Description              |
| ---------------------------------------------- | ------- | ------------------------ |
| contractName<mark style="color:red;">\*</mark> | string  | 合約名稱 `E-BTC-USDT`        |
| marginModel<mark style="color:red;">\*</mark>  | integer | 持保證金模式 （1.全倉 2.逐倉）傳入1或者2 |

{% tabs %}
{% tab title="200 : OK 成功code為0，code小於0為錯誤，msg為錯誤原因" %}

```java
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 調整倉位保證金

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/edit_position_margin`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 簽名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 時間戳         |

**Request Body**

| Name                                         | Type    | Description |
| -------------------------------------------- | ------- | ----------- |
| positionId<mark style="color:red;">\*</mark> | integer | 倉位id        |
| amount<mark style="color:red;">\*</mark>     | number  | 調整數值        |

{% tabs %}
{% tab title="200 : OK 成功code為0，code小於0為錯誤，msg為錯誤原因" %}

```java
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 更改杠桿倍數

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/edit_lever`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 簽名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 時間戳         |

**Request Body**

| Name                                           | Type    | Description       |
| ---------------------------------------------- | ------- | ----------------- |
| contractName<mark style="color:red;">\*</mark> | string  | 合約名稱 `E-BTC-USDT` |
| nowLevel<mark style="color:red;">\*</mark>     | integer | 需要修改的杠桿倍數 如50     |

{% tabs %}
{% tab title="200 : OK 成功code為0，code小於0為錯誤，msg為錯誤原因" %}

```java
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 賬戶

### 安全類型 USER\_DATA

賬戶下方的接口都需要簽名和API-key驗證

## 賬戶信息

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.com/fapi/v1/account`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 簽名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 時間戳         |

{% tabs %}
{% tab title="200  獲取賬戶信息成功" %}

```java
{
    "account": [
        {
            "marginCoin": "USDT",
            "accountNormal": 999.5606,
            "accountLock": 23799.5017,
            "partPositionNormal": 9110.7294,
            "totalPositionNormal": 0,
            "achievedAmount": 4156.5072,
            "unrealizedAmount": 650.6385,
            "totalMarginRate": 0,
            "totalEquity": 99964804.560,
            "partEquity": 13917.8753,
            "totalCost": 0,
            "sumMarginRate": 873.4608,
            "positionVos": [
                {
                    "contractId": 1,
                    "contractName": "E-BTC-USDT",
                    "contractSymbol": "BTC-USDT",
                    "positions": [
                        {
                            "id": 13603,
                            "uid": 10023,
                            "contractId": 1,
                            "positionType": 2,
                            "side": "BUY",
                            "volume": 69642.0,
                            "openPrice": 11840.2394,
                            "avgPrice": 11840.3095,
                            "closePrice": 12155.3005,
                            "leverageLevel": 24,
                            "holdAmount": 7014.2111,
                            "closeVolume": 40502.0,
                            "pendingCloseVolume": 0,
                            "realizedAmount": 8115.9125,
                            "historyRealizedAmount": 1865.3985,
                            "tradeFee": -432.0072,
                            "capitalFee": 2891.2281,
                            "closeProfit": 8117.6903,
                            "shareAmount": 0.1112,
                            "freezeLock": 0,
                            "status": 1,
                            "ctime": "2020-12-11T17:42:10",
                            "mtime": "2020-12-18T20:35:43",
                            "brokerId": 21,
                            "marginRate": 0.2097,
                            "reducePrice": 9740.8083,
                            "returnRate": 0.3086,
                            "unRealizedAmount": 2164.5289,
                            "openRealizedAmount": 2165.0173,
                            "positionBalance": 82458.2839,
                            "settleProfit": 0.4883,
                            "indexPrice": 12151.1175,
                            "keepRate": 0.005,
                            "maxFeeRate": 0.0025
                        }
                    ]
                }
            ]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

#### Response:

| 名稱        | 類型   | 描述   |
| --------- | ---- | ---- |
| `account` | `[]` | 余額集合 |

`account` field:

| 名稱                  | 類型     | 例子    | 描述         |
| ------------------- | ------ | ----- | ---------- |
| marginCoin          | string | USDT  | 保證金幣種      |
| accountNormal       | float  | 10.05 | 余額帳戶       |
| accountLock         | float  | 10.07 | 保證金凍結帳戶    |
| partPositionNormal  | float  | 10.07 | 逐倉保證金余額    |
| totalPositionNormal | float  | 10.07 | 全倉占用的初始保證金 |
| achievedAmount      | float  | 10.07 | 已實現盈虧      |
| unrealizedAmount    | float  | 10.05 | 未實現盈虧      |
| totalMarginRate     | float  | 10.05 | 全倉保證金率     |
| totalEquity         | float  | 10.07 | 全倉權益       |
| partEquity          | float  | 10.07 | 逐倉權益       |
| totalCost           | float  | 10.07 | 全倉占用的成本    |
| sumMarginRate       | float  | 10.07 | 全賬戶的保證金率   |
| positionVos         | \[ ]   |       | 倉位合約記錄     |

`positionVos` field:

| 名稱             | 類型      | 例子         | 描述   |
| -------------- | ------- | ---------- | ---- |
| contractId     | integer | 2          | 合約id |
| contractName   | string  | E-BTC-USDT | 合約名稱 |
| contractSymbol | string  | BTC-USDT   | 合約幣對 |
| positions      | \[ ]    |            | 倉位明細 |

`positions` field:

| 名稱                    | 類型      | 例子    | 描述                       |
| --------------------- | ------- | ----- | ------------------------ |
| id                    | integer | 2     | 倉位id                     |
| uid                   | integer | 10023 | 用戶ID                     |
| positionType          | integer | 1     | 持倉類型(1 全倉，2 倉逐)          |
| side                  | string  | SELL  | 持倉方向 BUY 多倉, SELL 空倉     |
| volume                | float   | 1.05  | 持倉數量                     |
| openPrice             | float   | 1.05  | 開倉價格                     |
| avgPrice              | float   | 1.05  | 持倉均價                     |
| closePrice            | float   | 1.05  | 平倉均價                     |
| leverageLevel         | float   | 1.05  | 杠桿倍數                     |
| holdAmount            | float   | 1.05  | 持倉保證金                    |
| closeVolume           | float   | 1.05  | 已平倉數量                    |
| pendingCloseVolume    | float   | 1.05  | 已掛出平倉單的數量                |
| realizedAmount        | float   | 1.05  | 已實現盈虧                    |
| historyRealizedAmount | float   | 1.05  | 歷史累計已實現盈虧                |
| tradeFee              | float   | 1.05  | 交易手續費                    |
| capitalFee            | float   | 1.05  | 資金費用                     |
| closeProfit           | float   | 1.05  | 平倉盈虧                     |
| shareAmount           | float   | 1.05  | 分攤金額                     |
| freezeLock            | integer | 0     | 持倉凍結狀態：0 正常，1爆倉凍結，2 交割凍結 |
| status                | integer | 0     | 倉位有效性，0無效 1有效            |
| ctime                 | time    |       | 創建時間                     |
| mtime                 | time    |       | 更新時間                     |
| brokerId              | integer | 1023  | 商戶id                     |
| lockTime              | time    |       | 爆倉鎖倉時間                   |
| marginRate            | float   | 1.05  | 保證金率                     |
| reducePrice           | float   | 1.05  | 強減價格                     |
| returnRate            | float   | 1.05  | 回報率(收益率)                 |
| unRealizedAmount      | float   | 1.05  | 未實現盈虧                    |
| openRealizedAmount    | float   | 1.05  | 開倉未實現盈虧                  |
| positionBalance       | float   | 1.05  | 倉位價值                     |
| indexPrice            | float   | 1.05  | 最新標記價格                   |
| keepRate              | float   | 1.05  | 階梯最低維持保證金率               |
| maxFeeRate            | float   | 1.05  | 平倉最大手續費率                 |