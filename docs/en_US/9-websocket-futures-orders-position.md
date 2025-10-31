# Websocket-Futures Orders Position

The interface supports two connection methods: token connection and apikey connection.\
Regardless of the connection and subscription method, the returned data message body is the same.

***

## 1. Token Connection

**Overview:**\
Carry the token in the request header to establish a connection with the backend. After the connection is established, send a message to subscribe. Only after a successful subscription can you receive pushed messages.

### 1.1 Request URL

```
wss://futuresws.xxx.xxx/position_order/ws
```

Replace `xxx` with your own domain name.

### 1.2 Request Headers

| Parameter Name | Type   | Required | Description                 |
| -------------- | ------ | -------- | --------------------------- |
| token          | string | Yes      | Token generated after login |

### 1.3 Message Body to Send

| Parameter Name | Type    | Required | Description                                                 |
| -------------- | ------- | -------- | ----------------------------------------------------------- |
| event          | string  | Yes      | \`sub\` : subscribe message \`unsub\` : unsubscribe message |
| token          | string  | Yes      | Token generated after login                                 |
| broker         | Integer | Yes      | SaaS merchant ID                                            |

**Example:**

```json
{
    "event": "sub",
    "token": "9a2fce1e96cb42e76aa9519ee26468cd6d58efddd67d4bc1a9a0fa128734c0fe",
    "broker": 1003
}
```

***

## 2. Apikey Connection

**Overview:**\
Carry the api-key in the request header to establish a connection with the backend. After the connection is established, send a message to subscribe. Only after a successful subscription can you receive pushed messages.

### 2.1 Request URL

```
wss://futuresws.xxx.xxx/position_order/ws
```

Replace `xxx` with your own domain name.

### 2.2 Request Headers

| Parameter Name | Type   | Required | Description   |
| -------------- | ------ | -------- | ------------- |
| api-key        | string | Yes      | User's Apikey |

### 2.3 Message Body to Send

| Parameter Name | Type    | Required | Description                                                 |
| -------------- | ------- | -------- | ----------------------------------------------------------- |
| event          | string  | Yes      | \`sub\` : subscribe message \`unsub\` : unsubscribe message |
| apiKey         | string  | Yes      | Token generated after login                                 |
| broker         | Integer | Yes      | SaaS merchant ID                                            |

**Example:**

```json
{
    "event": "sub",
    "apiKey": "70556a7b653367858dfb0e4fc441cf00",
    "broker": 1003
}
```

***

## 3. Receiving Messages

* After a successful connection, the backend returns: `connect success`
* After a successful subscription, the backend returns: `sub success`

![](https://1436431064-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FaaqHIATNpufmEk12r8vy%2Fuploads%2Fgit-blob-dee6f3cb7369846cedd45e9efb152f671bd0febb%2Fimage_jiZU8mcRBR.png?alt=media)

The actual message body is GZIP-compressed binary data, which needs to be parsed before it can be displayed properly. You can implement the parsing tool in your own language.\
Here is an online reference tool: <https://www.bejson.com/encrypt/gzip/#google_vignette>

For example, the received binary Base64 data:

```
H4sIAAAAAAAAAD2NywrCQAxF/yXrYchMkpmkO1EXggtxKyL1AQpapdZV6b87rWB2l3vuSQ+f2xkqymyiDk7Xumkud6hgtlgfNtvVfAkOSt718GihQo+olKKlGCIGplDaDiqVHNSzg2s9QSVpNGVGKlfEdXFEB+OvqEQsycH7OQ3RPDnoXj9L9hh0HJGZSSSL6OD4J4ujnUhG8crZiJIEwZQkpWE/fAGMewQM0AAAAA==
```

After parsing:

```json
{
    "uid": 374958,
    "channel": "ADL_PRICE",
    "l": [
        {
            "mr": 0.0083629621201431,
            "lt": 85718.4,
            "ha": 0.0718829844033338,
            "al": 2,
            "id": 2833456,
            "so": 85709.3,
            "tp": 85717.0183333399952392,
            "bo": 85709.2,
            "rp": 85405.8479336515066566
        }
    ]
}
```

***

![](https://1436431064-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FaaqHIATNpufmEk12r8vy%2Fuploads%2Fgit-blob-7ecd3964a426ea84a9a4c44b8496609bd887f40c%2Fimage_QxrECuYTR9.png?alt=media)

### Message Field Descriptions

#### 3.1 When Position or Account Changes

```json
{
    "channel": "ACCOUNT_UPDATE", // channel: different event types, ACCOUNT_UPDATE is pushed when position or account changes
    "uid": 1001, // Contract user ID
    "t": "1564745798938", // Timestamp
    "d": { // Data
        "et": "CREATE", // UPDATE, DELETE, DEFAULT
        // CREATE: Add a new position, p is not empty, and all position data is returned
        // DELETE: Delete a position, p is not empty, and only the position id is returned
        // UPDATE: Update a position, p is not empty, and only the changed fields are returned
        // DEFAULT: Position unchanged, only account info changed, p is empty
        "a": [ // Account list
            {
                "c": "USDT",  // Currency name
                "an": "122624.12345678", // Account balance
                "la": "100.12345678",  // Frozen account balance
                "pn": "50.12345678"  // Isolated margin account balance
            },
            {
                "c": "BTC", // Currency
                "an": "122624.12345678", // Account balance
                "la": "100.12345678",  // Frozen account balance
                "pn": "50.12345678"  // Isolated margin account balance
            }
        ],
        "p": { // Position info
            "id": 90762,  // Position ID
            "cid": 127, // Contract ID
            "pt": 1,  // Position type: 1 Cross, 2 Isolated
            "cn": "S-BTC-USDT", // Contract name
            "con": "BTCUSDT-EXUSD", // Contract alias
            "l": 20, // Leverage
            "pv": 12, // Position volume
            "op": 98533.6, // Average open price
            "rp": 68000.3, // Estimated liquidation price
            "hm": 98.22008325596366,  // Isolated margin held
            "ra": 2, // Realized PnL
            "s": "BUY", // Position direction
            "mr": 0.0847015132701974, // Margin rate
            "oa": 0.0847015132701974, // Opening margin
            "ccv": 2 // Closable volume
        }
    }
}
```

#### 3.2 When User Holds a Position

```json
{
    "channel": "ADL_PRICE", // When the user holds a position, ADL_PRICE message is pushed every second
    "uid": 1001, // Contract user ID
    "l": [
        {
            "id": 7001, // Position ID
            "al": 1,  // ADL level
            "rp": 68000.3,  // Estimated liquidation price
            "ha": 98.22008325596366,  // Margin
            "mr": 0.0847015132701974, // Margin rate
            "bo": 79000, // Best bid price
            "so": 78000, // Best ask price
            "lt": 78500, // Last traded price
            "tp": 78000  // Mark price
        },
        {
            "id": 7002, // Position ID
            "al": 1,  // ADL level
            "rp": 68000.3,  // Estimated liquidation price
            "ha": 98.22008325596366,  // Margin
            "mr": 0.0847015132701974, // Margin rate
            "bo": 79000, // Best bid price
            "so": 78000, // Best ask price
            "lt": 78500, // Last traded price
            "tp": 78000  // Mark price
        }
    ]
}
```

#### 3.3 When the System Closes

A fixed message will be pushed:

```json
{
    "channel": "SYSTEM",
    "uid": 1001,
    "et": "close"
}
```

#### 3.4 Normal Order

```json
{
    "channel": "order",
    "order": {
        "orderId": "2094043912705377045",
        "contractId": 127,
        "contractName": "E-BTC-USDT",
        "symbol": "BTC-USDT",
        "contractSide": "xxx",
        "type": 1,
        "price": 61001,
        "pricePrecision": 3,
        "dealVolume": 0,
        "volume": 100,
        "avgPrice": 0,
        "otoOrder": {
            "takerProfitStatus": false,
            "takerProfitTrigger": 61001,
            "takerProfitPrice": 0,
            "takerProfitTriggerId": null,
            "stopLossStatus": false,
            "stopLossTrigger": 61004,
            "stopLossPrice": 0,
            "stopLossTriggerId": null
        },
        "orderAction": "1" // 1: New, 2: Cancel, 3: Order change
    }
}
```

#### 3.5 Trigger Order Return Data

```json
{
    "channel": "trigOrder",
    "trigOrder": {
        "triggerOrderId": "1322738336974712854",
        "type": 1,
        "side": "buy",
        "triggerPrice": 61001,
        "price": 61003,
        "volume": 10,
        "triggerType": 3,
        "ctime": 1709550135000,
        "expireTime": 1710759735000,
        "orderAction": "1" // 1: New, 2: Cancel
    }
}
```

***

## 4. Heartbeat

Ping every 30 seconds. If the server does not receive a ping for more than 40 seconds, it will actively disconnect.

* Parameter sent: `{"ping":1713338308232}`
* Response: `{"pong":1713338308233}`
