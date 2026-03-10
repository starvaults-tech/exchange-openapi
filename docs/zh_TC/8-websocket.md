# WebSocket推送-K線

### 概述

WebSocket是HTML5一種新的協議（Protocol）。它實現了客戶端與服務器全雙工通信， 使得數據可以快速地雙向傳播。通過一次簡單的握手就可以建立客戶端和服務器連接， 服務器根據業務規則可以主動推送信息給客戶端。其優點如下：

* 客戶端和服務器進行數據傳輸時，請求頭信息比較小，大概2個字節。
* 客戶端和服務器皆可以主動地發送數據給對方。
* 不需要多次創建TCP請求和銷毀，節約寬帶和服務器的資源。

**強烈建議開發者使用WebSocket API獲取市場行情和買賣深度等信息。**

### 基本信息

* 行情基礎站點: <mark style="color:blue;">wss://ws.star-vaults.com/kline-api/ws</mark>
* 返回數據都會二進制壓縮(用戶需要通過Gzip算法進行解壓）

### 心跳機制

服務器每 10 秒主動推送 ping 消息，客戶端接收到後可自行決定是否處理（服務器並不對客戶端的 pong 回覆進行嚴格的一對一校驗和時間校驗）。為了保障連接的有效性，建議客戶端在收到服務器的 ping 消息後立即回覆 pong。

* 服務端發送 ping 消息格式：`{"ping": 時間戳（秒級）}`
* 客戶端回覆 pong 消息格式：`{"pong": 時間戳（秒級）}`

**ping 範例：**

```json
{"ping": 1535975085052}
```

**pong 範例：**

```json
{"pong": 1535975085052}
```

### 參數示例 <a href="#can-shu-shi-li" id="can-shu-shi-li"></a>

<table data-header-hidden><thead><tr><th>event</th><th width="313">channel</th><th width="220">description</th></tr></thead><tbody><tr><td>sub</td><td><code>market_$symbol_depth_step0</code></td><td><code>訂閱深度</code></td></tr><tr><td>unsub</td><td><code>market_$symbol_depth_step0</code></td><td><code>取消訂閱深度</code></td></tr><tr><td>sub</td><td><code>market_$symbol_trade_ticker</code></td><td><code>訂閱實時成交</code></td></tr><tr><td>unsub</td><td><code>market_$symbol_trade_ticker</code></td><td><code>取消訂閱實時成交</code></td></tr><tr><td>sub</td><td><code>market_$symbol_ticker</code></td><td><code>訂閱24h行情數據</code></td></tr><tr><td>unsub</td><td><code>market_$symbol_ticker</code></td><td><code>取消訂閱24h行情數據</code></td></tr><tr><td>sub</td><td><code>market_$symbol_kline_1min</code></td><td><code>訂閱1min實時k線信息</code></td></tr><tr><td>reg</td><td><code>market_$symbol_kline_1month</code></td><td><code>請求1month歷史k線記錄</code></td></tr></tbody></table>

### 訂閱深度

**訂閱請求：**

```json
{
    "event": "sub",
    "params": {
        "channel": "market_$symbol_depth_step0",
        "cb_id": "1"// 業務id 非必填
    }
}
```

**返回（最多返回 30 筆）：**

```json
{
    "channel": "market_btcusdt_depth_step0",
    "ts": 1506584998239,
    "tick": {
        "asks": [
            [10000.19, 0.93],
            [10001.21, 0.2],
            [10002.22, 0.34]
        ],
        "buys": [
            [9999.53, 0.93],
            [9998.2, 0.2],
            [9997.19, 0.21]
        ]
    }
}
```

### 訂閱即時成交&#x20;

**訂閱請求：**

```javascript
{
    "event":"sub",
    "params":{
        "channel":"market_$symbol_depth_step0", // $symbol E.g. btcusdt
        "cb_id":"1" // 業務id 非必填
    }
}
```

**返回：**

```javascript
{
    "channel":"market_$symbol_trade_ticker",
    "ts":1506584998239,//request time
    "tick":{
        "data":[
            {
                "side":"buy",//buy,sell
                "price":32.233,
                "vol":232,
                "amount":323,
                "ds":'2017-09-10 23:12:21'
            }
        ]
    }
}
```

### 訂閱 K 線行情

**訂閱請求：**

```json
{
    "event": "sub",
    "params": {
        "channel": "market_$symbol_kline_[1min/5min/15min/30min/60min/1day/1week/1month]",
        "cb_id": "1"
    }
}
```

**返回：**

```json
{
    "channel": "market_$symbol_kline_1min",
    "ts": 1506584998239,
    "tick": {
        "id": 1506602880,
        "vol": 1212.12211,
        "open": 2233.22,
        "close": 1221.11,
        "high": 22322.22,
        "low": 2321.22
    }
}
```

| 欄位      | 說明                    |
| ------- | --------------------- |
| channel | 頻道名稱，1min 代表 1 分鐘 K 線 |
| ts      | 請求時間                  |
| id      | 時間刻度起始值               |
| vol     | 交易量                   |
| open    | 開盤價                   |
| close   | 收盤價                   |
| high    | 最高價                   |
| low     | 最低價                   |

### 訂閱 24h 行情 Ticker

**訂閱請求：**

```json
{
    "event": "sub",
    "params": {
        "channel": "market_$symbol_ticker",
        "cb_id": "1"
    }
}
```

**返回：**

```json
{
    "channel": "market_$symbol_ticker",
    "ts": 1506584998239,
    "tick": {
        "amount": 123.1221,
        "vol": 1212.12211,
        "open": 2233.22,
        "close": 1221.11,
        "high": 22322.22,
        "low": 2321.22,
        "rose": -0.2922
    }
}
```

| 欄位     | 說明   |
| ------ | ---- |
| ts     | 請求時間 |
| amount | 交易額  |
| vol    | 交易量  |
| open   | 開盤價  |
| close  | 收盤價  |
| high   | 最高價  |
| low    | 最低價  |
| rose   | 漲幅   |

### 請求 K 線歷史數據

**請求：**

```json
{
    "event": "req",
    "params": {
        "channel": "market_$symbol_kline_[1min/5min/15min/30min/60min/1day/1week/1month]",
        "cb_id": "1",
        "endIdx": "1506602880",
        "pageSize": 100
    }
}
```

> `endIdx`：返回 endIdx 前 pageSize 條數據，非必填\
> `pageSize`：非必填

**返回（最多 300 筆）：**

```json
{
    "event_rep": "rep",
    "channel": "market_$symbol_kline_5min",
    "cb_id": "原路返回",
    "ts": 1506584998239,
    "data": [
        {
            "id": 1506602880,
            "amount": 123.1221,
            "vol": 1212.12211,
            "open": 2233.22,
            "close": 1221.11,
            "high": 22322.22,
            "low": 2321.22
        },
        {
            "id": 1506602880,
            "amount": 123.1221,
            "vol": 1212.12211,
            "open": 2233.22,
            "close": 1221.11,
            "high": 22322.22,
            "low": 2321.22
        }
    ]
}
```

### 請求成交記錄

**請求：**

```json
{
    "event": "req",
    "params": {
        "channel": "market_$symbol_trade_ticker",
        "cb_id": "1"
    }
}
```

**返回：**

```json
{
    "event_rep": "rep",
    "channel": "market_$symbol_trade_ticker",
    "cb_id": "原路返回",
    "ts": 1506584998239,
    "status": "ok",
    "data": [
        {
            "side": "buy",
            "price": 32.233,
            "vol": 232,
            "amount": 323
        },
        {
            "side": "buy",
            "price": 32.233,
            "vol": 232,
            "amount": 323
        }
    ]
}
```

| 欄位     | 說明              |
| ------ | --------------- |
| side   | 買賣方向：buy / sell |
| price  | 單價              |
| vol    | 數量              |
| amount | 總額              |
