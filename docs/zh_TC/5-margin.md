# 杠桿交易

## 交易

### 安全類型: TRADE

交易下方的接口都需要簽名API Key驗證

## 創建杠桿訂單

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/margin/order`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的API-key   |

#### Request Body

| Name             | Type   | Description           |
| ---------------- | ------ | --------------------- |
| type             | String | 訂單類型, `LIMIT/MARKET`  |
| recwwindow       | String | 時間窗口                  |
| price            | number | 訂單價格, 對於`LIMIT`訂單必須發送 |
| newClientOrderId | String | 客戶端訂單標識,不能超過32位       |
| side             | String | 訂單方向, `BUY/SELL`      |
| volume           | number | 訂單數量                  |
| symbol           | String | 幣對名稱E.g.`BTC/USDT`    |

{% tabs %}
{% tab title="200: OK  發送杠桿訂單成功" %}

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

**權重(IP/UID): 5**

## 杠桿訂單查詢

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v1/margin/order`

#### Query Parameters

| Name             | Type   | Description        |
| ---------------- | ------ | ------------------ |
| orderId          | String | 訂單ID               |
| newClientOrderId | String | 客戶端訂單標識            |
| symbol           | String | 幣對名稱E.g.`BTC/USDT` |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的API-key   |

{% tabs %}
{% tab title="200: OK  查詢杠桿訂單成功" %}

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

**權重(IP/UID): 5**

## 撤銷杠桿訂單

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/margin/cancel`

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的API-key   |

#### Request Body

| Name             | Type   | Description        |
| ---------------- | ------ | ------------------ |
| newClientOrderId | String | 客戶端訂單標識            |
| symbol           | String | 幣對名稱E.g.`BTC/USDT` |
| orderId          | String | 訂單id               |

{% tabs %}
{% tab title="200: OK  發送杠桿訂單成功" %}

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

**權重(IP/UID): 5**

## 杠桿當前委托

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v1/margin/openOrders`

**權重(IP/UID): 5**

#### Query Parameters

| Name   | Type   | Description        |
| ------ | ------ | ------------------ |
| symbol | String | 幣對名稱E.g.`BTC/USDT` |
| limit  | String | 默認100; 最大1000      |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
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

**權重(IP/UID): 1**

## 杠桿交易記錄

<mark style="color:blue;">`GET`</mark> `https://openapi.xxx.xx/sapi/v1/margin/myTrades`

#### Query Parameters

| Name   | Type   | Description        |
| ------ | ------ | ------------------ |
| symbol | String | 幣對名稱E.g.`BTC/USDT` |
| limit  | String | 默認100；最大1000       |
| fromId | String | 從這個tradeld開始檢索     |

#### Headers

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
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

**權重(IP/UID): 1**