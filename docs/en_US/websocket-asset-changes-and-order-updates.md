---
description: 'Version: 1.0'
---

# WebSocket – Asset Changes and Order Updates

#### I. Token Connection

Overview: The request header carries a Token to establish a connection with the backend. After the connection is established, send a message to subscribe. Only after a successful subscription can you receive pushed messages.

1. Request Path:

`wss://ws2.star-vaults.com/spotws_user/userData/ws`

2. Request Header

| Parameter Name | Type   | Required | Description                           |
| -------------- | ------ | -------- | ------------------------------------- |
| token          | string | Yes      | The token generated after logging in. |

3. Message Body

| Parameter Name | Type   | Required | Description                                                  |
| -------------- | ------ | -------- | ------------------------------------------------------------ |
| event          | string | Yes      | sub: subscribe to messages, unsub: unsubscribe from messages |
| token          | string | Yes      | The token generated after logging in.                        |

Example:

```json
{
  "event": "sub",
  "token": "9a2fce1e96cb42e76aa9519ee26468cd6d58efddd67d4bc1a9a0fa128734c0fe"
}
```

#### II. API-Key Connection

Overview: The request header carries an api-key to establish a connection with the backend. After the connection is established, send a message to subscribe. Only after a successful subscription can you receive pushed messages.

1. Request Path:

`wss://ws2.star-vaults.com/spotws_user/userData/ws`

Replace "xxx" with your own domain name.

2. Request Header

| Parameter Name | Type   | Required | Description                         |
| -------------- | ------ | -------- | ----------------------------------- |
| api-key        | string | Yes      | The apikey created on the frontend. |

3. Message Body

| Parameter Name | Type   | Required | Description                                                  |
| -------------- | ------ | -------- | ------------------------------------------------------------ |
| event          | string | Yes      | sub: subscribe to messages, unsub: unsubscribe from messages |
| token          | string | Yes      | The apikey created on the frontend.                          |

Example:

```json
{
  "event": "sub",
  "token": "9a2fce1e96cb42e76aa9519ee26468cd6d58efddd67d4bc1a9a0fa128734c0fe"
}
```

#### III. Connection and Data Format

After a successful connection, the backend returns a prompt: "connect success". After a successful subscription, the backend returns a prompt: "sub success".

The formal message body is binary data compressed with GZIP and needs to be decompressed to display the data normally. You can implement the decompression tool according to your own language. Here is an online reference tool: [Gzip Decompression Tool](https://www.bejson.com/encrypt/gzip/#google_vignette)

For example, if you receive a binary Base64 data like this:

```
H4sIAAAAAAAAA6vmUlBQSlWyUlDKLy1Jyi/NS3FMTgZSJQH5xZklmfl5SjoK+voKT3Z1P9m97fnG3U/ndY
N0uAJ1GJqamRgYm5iaGxoamOooIAO4jmfTt72cvgWkoxRFh4G5MYaOF1uWPevY/mzO6mdrFj6bveXZt
A0Q3c86NoMMcAIaEK2AE4Cs3Dvz5aK5XCBeNRdEVCkR5DXXEA8lHWw6XmxtebJr+dMJvc+Xb4DpSAP
pMDQAAj0DMEBoBep42r/++ZQVSDYBdeSAdMBVo9vxtG33892TkXTUAslYrloAfBt5w3oBAAA=
```

After decompression, it becomes:

```json
{
  "e": "outboundAccountPosition", // Event type
  "E": 1564034571105, // Event time
  "u": 1564034571073, // Account last update timestamp
  "B": [ // Balance
    {
      "a": "ETH", // Asset name
      "f": "10000.000000", // Available balance
      "l": "0.000000" // Frozen balance
    }
  ]
}
```

#### IV. Event Explanations

**1. When the account changes**

Whenever the account balance changes, an event `outboundAccountPosition` is sent, which includes assets that may have changed due to the event that generated the balance change.

```json
{
  "e": "outboundAccountPosition", // Event type
  "E": 1564034571105, // Event time
  "u": 1564034571073, // Account last update timestamp
  "B": [ // Balance
    {
      "a": "ETH", // Asset name
      "f": "10000.000000", // Available balance
      "l": "0.000000" // Frozen balance
    }
  ]
}
```

**2. Order status change return data example**

Orders are updated through the `executionReport` event.

Note: Market orders do not trigger this event.

```json
{
  "E": 1745389508472, // Event time
  "L": "13000.0000000000000000", // Last execution price
  "O": 1745389507000, // Order creation time
  "P": "0", // Take profit/stop loss order trigger price
  "Q": "0.17861112", // Quote Order Quantity
  "S": "SELL", // Order direction
  "T": 1745389508418, // Execution time
  "X": "PART_FILLED", // Current status of the order
  "Y": "1300.0000000000000000", // Last execution amount
  "Z": "2321.94456", // Cumulative execution amount
  "e": "executionReport", // Event type
  "i": "2690536306533246156", // Order ID
  "l": "0.1000000000000000", // Last execution quantity
  "n": "7.8000000000000000", // Fee quantity
  "o": "LIMIT", // Order type
  "p": "13000", // Order original price
  "q": "1", // Order original quantity
  "s": "BTCUSDT", // Trading pair
  "x": "STATUS", // Specific execution type of this event
  "z": "0.17861112" // Cumulative execution quantity
}
```

`X` Field Description

* `FILLED`: Complete filled
* `PART_FILLED`: partially filled
* `CANCELED`: cancel success
* `PENDING_CANCEL`: Pending cancel

**3. When the system is closed**

A fixed push of the following data will occur:

```json
{
  "uid": 24005174,
  "channel": "SYSTEM",
  "et": "close"
}
```

#### V. Heartbeat

Ping every 30 seconds, if the server does not receive a ping within 40 seconds, it will actively disconnect.

Parameter: `{"ping":1713338308232}`

Response: `{"pong":1713338308233}`
