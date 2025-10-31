# 杠杆交易

## 交易

### 安全类型: TRADE

交易下方的接口都需要签名API Key验证

## 创建杠杆订单

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/margin/order`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 签名          |
| X-CH-TS     | String | 时间戳         |
| X-CH-APIKEY | String | 您的API-key   |

#### Request Body

| Name             | Type   | Description           |
| ---------------- | ------ | --------------------- |
| type             | String | 订单类型, `LIMIT/MARKET`  |
| recwwindow       | String | 时间窗口                  |
| price            | number | 订单价格, 对于`LIMIT`订单必须发送 |
| newClientOrderId | String | 客户端订单标识,不能超过32位       |
| side             | String | 订单方向, `BUY/SELL`      |
| volume           | number | 订单数量                  |
| symbol           | String | 币对名称E.g.`BTC/USDT`    |

{% tabs %}
{% tab title="200: OK  发送杠杆订单成功" %}

```javascript
{
    'symbol': 'LXTUSDT', 
    'orderId': '494736827050147840', 
    'clientOrderId': '157371322565051',
    'transactTime': '1573713225668', 
    'price': '0.005452', 
    'origQty': '110', 
    'executedQty': '0', 
    'status': 'NEW',
    'type': 'LIMIT', 
    'side': 'SELL'
}
```

{% endtab %}
{% endtabs %}

**权重(IP/UID): 5**

## 杠杆订单查询

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v1/margin/order`

#### Query Parameters

| Name             | Type   | Description        |
| ---------------- | ------ | ------------------ |
| orderId          | String | 订单ID               |
| newClientOrderId | String | 客户端订单标识            |
| symbol           | String | 币对名称E.g.`BTC/USDT` |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 签名          |
| X-CH-TS     | String | 时间戳         |
| X-CH-APIKEY | String | 您的API-key   |

{% tabs %}
{% tab title="200: OK  查询杠杆订单成功" %}

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

**权重(IP/UID): 5**

## 撤销杠杆订单

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/margin/cancel`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 签名          |
| X-CH-TS     | String | 时间戳         |
| X-CH-APIKEY | String | 您的API-key   |

#### Request Body

| Name             | Type   | Description        |
| ---------------- | ------ | ------------------ |
| newClientOrderId | String | 客户端订单标识            |
| symbol           | String | 币对名称E.g.`BTC/USDT` |
| orderId          | String | 订单id               |

{% tabs %}
{% tab title="200: OK  发送杠杆订单成功" %}

```javascript
{
    'symbol': 'LXTUSDT', 
    'orderId': '494736827050147840', 
    'clientOrderId': '157371322565051',
    'transactTime': '1573713225668', 
    'price': '0.005452', 
    'origQty': '110', 
    'executedQty': '0', 
    'status': 'NEW',
    'type': 'LIMIT', 
    'side': 'SELL'
}
```

{% endtab %}
{% endtabs %}

**权重(IP/UID): 5**

## 杠杆当前委托

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v1/margin/openOrders`

**权重(IP/UID): 5**

#### Query Parameters

| Name   | Type   | Description        |
| ------ | ------ | ------------------ |
| symbol | String | 币对名称E.g.`BTC/USDT` |
| limit  | String | 默认100; 最大1000      |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 签名          |
| X-CH-TS     | String | 时间戳         |
| X-CH-APIKEY | String | 您的API-key   |

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
        'time': '1574329076202'
        },...
]
```

{% endtab %}
{% endtabs %}

**权重(IP/UID): 1**

## 杠杆交易记录

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v1/margin/myTrades`

#### Query Parameters

| Name   | Type   | Description        |
| ------ | ------ | ------------------ |
| symbol | String | 币对名称E.g.`BTC/USDT` |
| limit  | String | 默认100；最大1000       |
| fromId | String | 从这个tradeld开始检索     |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 签名          |
| X-CH-TS     | String | 时间戳         |
| X-CH-APIKEY | String | 您的API-key   |

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
    "fee":"0.001"
  },...
]
```

{% endtab %}
{% endtabs %}

**权重(IP/UID): 1**