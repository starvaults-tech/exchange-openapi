# 合约交易

## 公共

### 安全类型: [None](https://github.com/exhcange/OpenApi-en/blob/master/broken-reference/README.md)

公共下方的接口不需要API-key或者签名就能自由访问

## 测试连接

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/ping`

测试REST API的连通性

{% tabs %}
{% tab title="200  连接正常" %}

```
{}
```

{% endtab %}
{% endtabs %}

## 获取服务器时间

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/time`

{% tabs %}
{% tab title="200 " %}

```
{
    "serverTime":1607702400000,
    "timezone":中国标准时间
}
```

{% endtab %}
{% endtabs %}

#### Response:

| 名称         | 类型     | 例子            | 描述     |
| ---------- | ------ | ------------- | ------ |
| serverTime | long   | 1607702400000 | 服务器时间戳 |
| timezone   | string | 中国标准时间        | 服务器时区  |

## 合约列表

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

| 名称              | 类型     | 例子           | 描述                           |
| --------------- | ------ | ------------ | ---------------------------- |
| symbol          | string | `E-BTC-USDT` | 合约名称                         |
| status          | number | `1`          | 合约状态（0：不可交易，1：可交易            |
| type            | string | `S`          | 合约类型，E:永续合约, S:模拟合约, 其他为混合合约 |
| side            | number | `1`          | 合约方向(反向：0，1：正向)              |
| multiplier      | number | `0.5`        | 合约面值                         |
| multiplierCoin  | string | `BTC`        | 合约面值单位                       |
| pricePrecision  | number | `4`          | 价格精度                         |
| minOrderVolume  | number | `10`         | 最小下单量                        |
| minOrderMoney   | number | `10`         | 最小下单金额                       |
| maxMarketVolume | number | `100000`     | 市价单最大下单数量                    |
| maxMarketMoney  | number | `100000`     | 市价最大下单金额                     |
| maxLimitVolume  | number | `100000`     | 限价单最大下单数量                    |
| maxValidOrder   | number | `100000`     | 最大有效委托的订单数量                  |
| minLever        | number | `5`          | 杠杆最小倍数                       |
| maxLever        | number | `5`          | 杠杆最大倍数                       |
| openTakerFee    | number | `0.0002`     | 开仓taker手续费                   |
| openMakerFee    | number | `0.0002`     | 开仓maker手续费                   |
| closeTakerFee   | number | `0.0002`     | 平仓taker手续费                   |
| closeMakerFee   | number | `0.0002`     | 平仓maker手续费                   |

## 行情相关

### 安全类型: [None](https://github.com/exhcange/OpenApi-en/blob/master/broken-reference/README.md)

行情下方的接口不需要API-Key或者签名就能自由访问

## 订单薄

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/depth`

市场订单薄深度信息

#### Query Parameters

| Name         | Type    | Description         |
| ------------ | ------- | ------------------- |
| limit        | integer | 默认100; 最大100        |
| contractName | string  | 合约合约名称 如 E-BTC-USDT |

{% tabs %}
{% tab title="200  成功获取深度信息" %}

```java
{
  "bids": [
    [
      "3.90000000",   // 价格
      "431.00000000"  // 数量
    ],
    [
      "4.00000000",
      "431.00000000"
    ]
  ],
  "asks": [
    [
      "4.00000200",  // 价格
      "12.00000000"  // 数量
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

| 名称   | 类型   | 例子              | 描述                         |
| ---- | ---- | --------------- | -------------------------- |
| time | long | `1595563624731` | 当前时间(Unix Timestamp, 毫秒ms) |
| bids | list | 如下              | 订单薄买盘信息                    |
| asks | list | 如下              | 订单薄卖盘信息                    |

bids和asks所对应的信息代表了订单薄的所有价格以及价格对应的数量的信息, 由最优价格从上倒下排列

| 名称  | 类型    | 例子      | 描述        |
| --- | ----- | ------- | --------- |
| ' ' | float | `131.1` | 价格        |
| ' ' | float | `2.3`   | 当前价格对应的数量 |

## 行情ticker

<mark style="color:blue;">`GET`</mark> `https://futuersopenapi.xxx.xx/fapi/v1/ticker`

24小时价格变化数据

#### Query Parameters

| Name         | Type   | Description       |
| ------------ | ------ | ----------------- |
| contractName | string | 合约名称 如 E-BTC-USDT |

{% tabs %}
{% tab title="200  成功获取ticker信息" %}

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

| 名称   | 类型     | 例子              | 描述  |
| ---- | ------ | --------------- | --- |
| time | long   | `1595563624731` | 时间戳 |
| high | float  | `9900`          | 最高价 |
| low  | float  | `8800.34`       | 最低价 |
| last | float  | `8900`          | 最新价 |
| vol  | float  | `4999`          | 交易量 |
| rose | string | +0.5            | 涨跌幅 |

## 所有行情ticker

<mark style="color:blue;">`GET`</mark> `https://futuersopenapi.xxx.xx/fapi/v1/ticker_all`

{% tabs %}
{% tab title="200  成功获取ticker信息" %}

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

| 名称   | 类型     | 例子              | 描述  |   |
| ---- | ------ | --------------- | --- | - |
| time | long   | `1595563624731` | 时间戳 |   |
| high | float  | `9900`          | 最高价 |   |
| low  | float  | `8800.34`       | 最低价 |   |
| last | float  | `8900`          | 最新价 |   |
| vol  | float  | `4999`          | 交易量 |   |
| rose | string | +0.5            | 涨跌幅 |   |

## 获取指数/标记价格

<mark style="color:blue;">`GET`</mark> `https://futuersopenapi.xxx.xx/fapi/v1/index`

#### Query Parameters

| Name         | Type   | Description       |
| ------------ | ------ | ----------------- |
| contractName | string | 合约名称 如 E-BTC-USDT |
| limit        | string | 默认100; 最大1000     |

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

| 名称                | 类型     | 例子           | 描述     |
| ----------------- | ------ | ------------ | ------ |
| `indexPrice`      | float  | `0.055`      | 指数价格   |
| `markPrice`       | float  | `0.0578`     | 标记价格   |
| `contractName`    | string | `E-BTC-USDT` | 合约名称   |
| `lastFundingRate` | float  | `0.123`      | 本期资金费率 |

## K线/蜡烛图数据

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/klines`

#### Query Parameters

| Name         | Type    | Description                                                                                                    |
| ------------ | ------- | -------------------------------------------------------------------------------------------------------------- |
| contractName | string  | 合约名称 如 E-BTC-USDT                                                                                              |
| interval     | string  | k线图区间, 可识别发送的值为： `1min`,`5min`,`15min`,`30min`,`1h`,`1day`,`1week`,`1month`（min=分钟，h=小时,day=天，week=星期，month=月） |
| limit        | integer | 默认100; 最大300                                                                                                   |

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

| 名称      | 类型    | 例子              | 描述           |
| ------- | ----- | --------------- | ------------ |
| `idx`   | long  | `1538728740000` | 开始时间戳，毫秒（ms） |
| `open`  | float | `36.00000`      | 开盘价          |
| `close` | float | `33.00000`      | 收盘价          |
| `high`  | float | `36.00000`      | 最高价          |
| `low`   | float | `30.00000`      | 最低价          |
| `vol`   | float | `2456.111`      | 成交量          |

## 交易相关

### 安全类型: [TRADE](https://github.com/exhcange/OpenApi-en/blob/master/broken-reference/README.md)

交易下方的接口都需要[签名和API-key验证](https://github.com/exhcange/OpenApi-en/blob/master/broken-reference/README.md)

## 创建订单

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/order`

创建单个新订单

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-TS     | string | 时间戳         |
| X-CH-APIKEY | string | 您的API-KEY   |
| X-CH-SIGN   | string | 签名          |

#### Request Body

| Name          | Type   | Description           |
| ------------- | ------ | --------------------- |
| volume        | number | 下单数量                  |
| price         | number | 下单价格                  |
| contractName  | string | 合约名称 如 `E-BTC-USDT`   |
| type          | string | 订单类型, `LIMIT/MARKET`  |
| side          | string | 买卖方向, `BUY/SELL`      |
| open          | string | 开平仓方向, `OPEN/CLOSE`   |
| positionType  | number | 持仓类型, `1全仓/2逐仓`       |
| clientOrderId | string | 客户端下单标识, 长度小于32位的字符串  |
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

| 名称      | 类型     | 例子                   | 描述   |
| ------- | ------ | -------------------- | ---- |
| orderId | string | `256609229205684228` | 订单ID |

## 创建条件单

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/conditionOrder`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-TS     | string | 时间戳         |
| X-CH-APIKEY | string | 您的API-KEY   |
| X-CH-SIGN   | string | 签名          |

#### Request Body

| Name          | Type   | Description          |
| ------------- | ------ | -------------------- |
| volume        | number | 下单数量                 |
| price         | number | 下单价格                 |
| contractName  | string | 合约名称 如 `E-BTC-USDT`  |
| type          | string | 订单类型, `LIMIT/MARKET` |
| side          | string | 买卖方向, `BUY/SELL`     |
| open          | string | 开平仓方向, `OPEN/CLOSE`  |
| positionType  | number | 持仓类型, `1全仓/2逐仓`      |
| clientOrderId | string | 客户端下单标识, 长度小于32位的字符串 |
| triggerType   | string | 条件单类型，`3追涨/4杀跌`      |
| triggerPrice  | string | 触发价                  |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "orderId": 256609229205684228
}
```

{% endtab %}
{% endtabs %}

## 取消订单

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/cancel`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 签名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 时间戳         |

#### Request Body

| Name         | Type   | Description        |
| ------------ | ------ | ------------------ |
| contractName | string | 合约名称如 `E-BTC-USDT` |
| orderId      | string | 订单ID               |

{% tabs %}
{% tab title="200 " %}

```java
{
    "orderId": 256609229205684228
}
```

{% endtab %}
{% endtabs %}

## 取消全部订单

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/cancel_all`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 签名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 时间戳         |

#### Request Body

{% tabs %}
{% tab title="200 : OK 成功code为0，code小于0为错误，msg为错误原因" %}

```json
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 订单详情

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/order`

#### Query Parameters

| Name                                           | Type   | Description |
| ---------------------------------------------- | ------ | ----------- |
| contractName<mark style="color:red;">\*</mark> | string | 合约名称        |
| orderId<mark style="color:red;">\*</mark>      | string | 订单ID        |
| clientOrderId                                  | string | 客户端唯一标识     |

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

| 名称             | 类型     | 例子                   | 描述                                                                                                    |
| -------------- | ------ | -------------------- | ----------------------------------------------------------------------------------------------------- |
| `orderId`      | long   | `150695552109032492` | 订单ID（系统生成                                                                                             |
| `contractName` | string | `E-BTC-USDT`         | 合约名称                                                                                                  |
| `price`        | float  | `10.5`               | 委托价格                                                                                                  |
| `origQty`      | float  | `10.5`               | 委托数量                                                                                                  |
| `executedQty`  | float  | `20`                 | 委托数量                                                                                                  |
| `avgPrice`     | float  | `10.5`               | 成交均价                                                                                                  |
| `symbol`       | string | `BHTUSDT`            | 币对名称                                                                                                  |
| `status`       | string | `NEW`                | 订单状态。可能出现的值为：`NEW`(新订单，无成交)、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和`REJECTED`（订单被拒绝） |
| `side`         | string | `NEW`                | 订单方向。可能出现的值只能为：BUY（买入做多） 和 SELL（卖出做空）                                                                 |
| `action`       | string | `OPEN`               | `OPEN/CLOSE`                                                                                          |
| `transactTime` | long   | `1607702400000`      | 订单创建时间                                                                                                |

## 当前订单

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/openOrders`

**限速规则:**\
**获取当前合约, 该用户的当前委托**

#### Query Parameters

| Name         | Type   | Description                     |
| ------------ | ------ | ------------------------------- |
| contractName | string | 不传该字段，查询全部合约。 合约名称 `E-BTC-USDT` |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | string | 签名          |
| X-CH-APIKEY | string | 您的API-key   |
| X-CH-TS     | string | 时间戳         |

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

| 名称             | 类型     | 例子                   | 描述                                                                                                     |
| -------------- | ------ | -------------------- | ------------------------------------------------------------------------------------------------------ |
| `orderId`      | long   | `150695552109032492` | 订单ID（系统生成）                                                                                             |
| `contractName` | string | `E-BTC-USDT`         | 合约名称                                                                                                   |
| `price`        | float  | `4765.29`            | 订单价格                                                                                                   |
| `origQty`      | float  | `1.01`               | 订单数量                                                                                                   |
| `executedQty`  | float  | `1.01`               | 已经成交订单数量                                                                                               |
| `avgPrice`     | float  | `4754.24`            | 订单已经成交的平均价格                                                                                            |
| `type`         | string | `LIMIT`              | 订单类型。可能出现的值只能为:`LIMIT`(限价)和`MARKET`（市价）                                                                |
| `side`         | string | `BUY`                | 订单方向。可能出现的值只能为：`BUY`（买入做多） 和 `SELL`（卖出做空）                                                              |
| `status`       | string | `NEW`                | 订单状态。可能出现的值为：`NEW`(新订单，无成交)、`PARTIALLY_FILLED`（部分成交）、`FILLED`（全部成交）、`CANCELED`（已取消）和`REJECTED`（订单被拒绝）. |
| `action`       | string | `OPEN`               | `OPEN/CLOSE`                                                                                           |
| `transactTime` | long   | `1607702400000`      | 订单创建时间,                                                                                                |

## 历史委托

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/orderHistorical`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | string | 签名          |
| X-CH-APIKEY | string | 您的API-key   |
| X-CH-TS     | string | 时间戳         |

#### Request Body

| Name         | Type   | Description         |
| ------------ | ------ | ------------------- |
| contractName | string | 合约名称 `E-BTC-USDT`   |
| limit        | string | 分页条数, 默认100; 最大1000 |
| fromId       | long   | 从这条记录开始检索           |

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

## 盈亏记录

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/profitHistorical`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | string | 签名          |
| X-CH-APIKEY | string | 您的API-key   |
| X-CH-TS     | string | 时间戳         |

#### Request Body

| Name         | Type   | Description         |
| ------------ | ------ | ------------------- |
| contractName | string | 合约名称 `E-BTC-USDT`   |
| limit        | string | 分页条数, 默认100; 最大1000 |
| fromId       | long   | 从这条记录开始检索           |

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

## 交易记录

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/myTrades`

#### Query Parameters

| Name         | Type   | Description         |
| ------------ | ------ | ------------------- |
| contractName | string | 合约名称 如 E-BTC-USDT   |
| limit        | string | 分页条数, 默认100; 最大1000 |
| fromId       | long   | 从这个tradeId开始检索      |

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 签名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 时间戳         |

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

| 名称           | 类型      | 例子                 | 描述                     |
| ------------ | ------- | ------------------ | ---------------------- |
| symbol       | string  | ETHBTC             | 币种名称(交易对)              |
| tradeId      | number  | 28457              | 交易ID                   |
| bidId        | long    | 150695552109032492 | 买方订单ID                 |
| askId        | long    | 150695552109032493 | 卖方订单ID                 |
| bidUserId    | integer | 10024              | 买方用户ID                 |
| askUserId    | integer | 10025              | 卖方用户ID                 |
| price        | float   | 4.01               | 成交价格                   |
| qty          | float   | 12                 | 交易数量                   |
| amount       | float   | 5.38               | 成交金额                   |
| time         | number  | 1499865549590      | 交易时间戳                  |
| fee          | number  | 0.001              | 交易手续费                  |
| side         | string  | buy                | 当前订单方向 BUY 买入, SELL 卖出 |
| contractName | string  | E-BTC-USDT         | 合约名称                   |
| isMaker      | boolean | true               | 是否是maker               |
| isBuyer      | boolean | true               | 是否买方                   |

## 更改持仓模式

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/edit_user_position_model`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 签名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 时间戳         |

**Request Body**

| Name                                            | Type    | Description               |
| ----------------------------------------------- | ------- | ------------------------- |
| contractName<mark style="color:red;">\*</mark>  | string  | 合约名称 `E-BTC-USDT`         |
| positionModel<mark style="color:red;">\*</mark> | integer | 持仓模式 （1.净持仓 2.双向持仓）传入1或者2 |

{% tabs %}
{% tab title="200 : OK 成功code为0，code小于0为错误，msg为错误原因" %}

```java
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 更改保证金模式

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/edit_user_margin_model`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 签名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 时间戳         |

**Request Body**

| Name                                           | Type    | Description              |
| ---------------------------------------------- | ------- | ------------------------ |
| contractName<mark style="color:red;">\*</mark> | string  | 合约名称 `E-BTC-USDT`        |
| marginModel<mark style="color:red;">\*</mark>  | integer | 持保证金模式 （1.全仓 2.逐仓）传入1或者2 |

{% tabs %}
{% tab title="200 : OK 成功code为0，code小于0为错误，msg为错误原因" %}

```java
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 调整仓位保证金

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/edit_position_margin`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 签名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 时间戳         |

**Request Body**

| Name                                         | Type    | Description |
| -------------------------------------------- | ------- | ----------- |
| positionId<mark style="color:red;">\*</mark> | integer | 仓位id        |
| amount<mark style="color:red;">\*</mark>     | number  | 调整数值        |

{% tabs %}
{% tab title="200 : OK 成功code为0，code小于0为错误，msg为错误原因" %}

```java
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 更改杠杆倍数

<mark style="color:green;">`POST`</mark> `https://futuresopenapi.xxx.xx/fapi/v1/edit_lever`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 签名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 时间戳         |

**Request Body**

| Name                                           | Type    | Description       |
| ---------------------------------------------- | ------- | ----------------- |
| contractName<mark style="color:red;">\*</mark> | string  | 合约名称 `E-BTC-USDT` |
| nowLevel<mark style="color:red;">\*</mark>     | integer | 需要修改的杠杆倍数 如50     |

{% tabs %}
{% tab title="200 : OK 成功code为0，code小于0为错误，msg为错误原因" %}

```java
{ 
    "code": "0", 
    "msg": "成功", 
    "data": null 
}
```

{% endtab %}
{% endtabs %}

## 账户

### 安全类型:[ USER\_DATA](https://github.com/exhcange/OpenApi-en/blob/master/broken-reference/README.md)

账户下方的接口都需要[签名和API-key验证](https://github.com/exhcange/OpenApi-en/blob/master/broken-reference/README.md)

## 账户信息

<mark style="color:blue;">`GET`</mark> `https://futuresopenapi.xxx.com/fapi/v1/account`

#### Headers

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| X-CH-SIGN   | string  | 签名          |
| X-CH-APIKEY | string  | 您的API-key   |
| X-CH-TS     | integer | 时间戳         |

{% tabs %}
{% tab title="200  获取账户信息成功" %}

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

| 名称        | 类型   | 描述   |
| --------- | ---- | ---- |
| `account` | `[]` | 余额集合 |

`account` field:

| 名称                  | 类型     | 例子    | 描述         |
| ------------------- | ------ | ----- | ---------- |
| marginCoin          | string | USDT  | 保证金币种      |
| accountNormal       | float  | 10.05 | 余额帐户       |
| accountLock         | float  | 10.07 | 保证金冻结帐户    |
| partPositionNormal  | float  | 10.07 | 逐仓保证金余额    |
| totalPositionNormal | float  | 10.07 | 全仓占用的初始保证金 |
| achievedAmount      | float  | 10.07 | 已实现盈亏      |
| unrealizedAmount    | float  | 10.05 | 未实现盈亏      |
| totalMarginRate     | float  | 10.05 | 全仓保证金率     |
| totalEquity         | float  | 10.07 | 全仓权益       |
| partEquity          | float  | 10.07 | 逐仓权益       |
| totalCost           | float  | 10.07 | 全仓占用的成本    |
| sumMarginRate       | float  | 10.07 | 全账户的保证金率   |
| positionVos         | \[ ]   |       | 仓位合约记录     |

`positionVos` field:

| 名称             | 类型      | 例子         | 描述   |
| -------------- | ------- | ---------- | ---- |
| contractId     | integer | 2          | 合约id |
| contractName   | string  | E-BTC-USDT | 合约名称 |
| contractSymbol | string  | BTC-USDT   | 合约币对 |
| positions      | \[ ]    |            | 仓位明细 |

`positions` field:

| 名称                    | 类型      | 例子    | 描述                       |
| --------------------- | ------- | ----- | ------------------------ |
| id                    | integer | 2     | 仓位id                     |
| uid                   | integer | 10023 | 用户ID                     |
| positionType          | integer | 1     | 持仓类型(1 全仓，2 仓逐)          |
| side                  | string  | SELL  | 持仓方向 BUY 多仓, SELL 空仓     |
| volume                | float   | 1.05  | 持仓数量                     |
| openPrice             | float   | 1.05  | 开仓价格                     |
| avgPrice              | float   | 1.05  | 持仓均价                     |
| closePrice            | float   | 1.05  | 平仓均价                     |
| leverageLevel         | float   | 1.05  | 杠杆倍数                     |
| holdAmount            | float   | 1.05  | 持仓保证金                    |
| closeVolume           | float   | 1.05  | 已平仓数量                    |
| pendingCloseVolume    | float   | 1.05  | 已挂出平仓单的数量                |
| realizedAmount        | float   | 1.05  | 已实现盈亏                    |
| historyRealizedAmount | float   | 1.05  | 历史累计已实现盈亏                |
| tradeFee              | float   | 1.05  | 交易手续费                    |
| capitalFee            | float   | 1.05  | 资金费用                     |
| closeProfit           | float   | 1.05  | 平仓盈亏                     |
| shareAmount           | float   | 1.05  | 分摊金额                     |
| freezeLock            | integer | 0     | 持仓冻结状态：0 正常，1爆仓冻结，2 交割冻结 |
| status                | integer | 0     | 仓位有效性，0无效 1有效            |
| ctime                 | time    |       | 创建时间                     |
| mtime                 | time    |       | 更新时间                     |
| brokerId              | integer | 1023  | 商户id                     |
| lockTime              | time    |       | 爆仓锁仓时间                   |
| marginRate            | float   | 1.05  | 保证金率                     |
| reducePrice           | float   | 1.05  | 强减价格                     |
| returnRate            | float   | 1.05  | 回报率(收益率)                 |
| unRealizedAmount      | float   | 1.05  | 未实现盈亏                    |
| openRealizedAmount    | float   | 1.05  | 开仓未实现盈亏                  |
| positionBalance       | float   | 1.05  | 仓位价值                     |
| indexPrice            | float   | 1.05  | 最新标记价格                   |
| keepRate              | float   | 1.05  | 阶梯最低维持保证金率               |
| maxFeeRate            | float   | 1.05  | 平仓最大手续费率                 |
