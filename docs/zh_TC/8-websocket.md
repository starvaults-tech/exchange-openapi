# WebSocket推送-K線

### 概述

WebSocket是HTML5一種新的協議（Protocol）。它實現了客戶端與服務器全雙工通信， 使得數據可以快速地雙向傳播。通過一次簡單的握手就可以建立客戶端和服務器連接， 服務器根據業務規則可以主動推送信息給客戶端。其優點如下：

* 客戶端和服務器進行數據傳輸時，請求頭信息比較小，大概2個字節。
* 客戶端和服務器皆可以主動地發送數據給對方。
* 不需要多次創建TCP請求和銷毀，節約寬帶和服務器的資源。

**強烈建議開發者使用WebSocket API獲取市場行情和買賣深度等信息。**

### 基本信息

* 行情基礎站點: <mark style="color:blue;">wss\://ws.xxx.com/kline-api/ws</mark>
* 返回數據都會二進制壓縮(用戶需要通過Gzip算法進行解壓）

### 心跳機制

服務器每10秒主動推送ping消息，客戶端接收到後可自行決定是否處理（服務器並不對客戶端的pong回覆進行嚴格的一對一校驗和時間校驗）。 為了保障鏈接的有效性，建議客戶端在收到服務器的ping消息後立即回覆pong。 服務端發送ping消息格式： {"ping": 時間戳（秒級）} 客戶端回覆pong消息格式： {"pong": 時間戳（秒級）} 示例： {"pong":1694416595}

### 參數示例 <a href="#can-shu-shi-li" id="can-shu-shi-li"></a>

<table data-header-hidden><thead><tr><th>event</th><th width="313">channel</th><th width="220">description</th><th></th><th>描述</th></tr></thead><tbody><tr><td>sub</td><td><code>market_$symbol_depth_step0</code></td><td><code>訂閱深度</code></td><td></td><td>描述</td></tr><tr><td>unsub</td><td><code>market_$symbol_depth_step0</code></td><td><code>取消訂閱深度</code></td><td></td><td>幣對名稱</td></tr><tr><td>sub</td><td><code>market_$symbol_trade_ticker</code></td><td><code>訂閱實時成交</code></td><td></td><td>base貨幣</td></tr><tr><td>unsub</td><td><code>market_$symbol_trade_ticker</code></td><td><code>取消訂閱實時成交</code></td><td></td><td>計價貨幣</td></tr><tr><td>sub</td><td><code>market_$symbol_ticker</code></td><td><code>訂閱24h行情數據</code></td><td></td><td>價格精度</td></tr><tr><td>unsub</td><td><code>market_$symbol_ticker</code></td><td><code>取消訂閱24h行情數據</code></td><td></td><td>數量精度</td></tr><tr><td>sub</td><td><code>market_$symbol_kline_1min</code></td><td><code>訂閱1min實時k線信息</code></td><td></td><td></td></tr><tr><td>reg</td><td><code>market_$symbol_kline_1month</code></td><td><code>請求1month歷史k線記錄</code></td><td></td><td></td></tr></tbody></table>

```java
{
    "event":"sub",
    "params":{
        "channel":"market_$symbol_kline_[1min/5min/15min/30min/60min/1day/1week/1month]", // $symbol E.g. btcusdt 
        "cb_id":"1" // 業務id 非必填
    }
}
```

* 返回

```java
{
    "channel":"market_$symbol_kline_1min", //1min代表1分鐘k線
    "ts":1506584998239,//請求時間
    "tick":{
        "id":1506602880,//時間刻度起始值
        "vol":1212.12211,//交易量
        "open":2233.22,//開盤價
        "close":1221.11,//收盤價
        "high":22322.22,//最高價
        "low":2321.22//最低價
    }
}
```

### 訂閱24h行情ticker

* 訂閱數據樣例

```java
{
    "event":"sub",
    "params":{
        "channel":"market_$symbol_ticker", // $symbol E.g. btcusdt 
        "cb_id":"1" // 業務id 非必填
    }
}
```

* 返回

```java
{
    "channel":"market_$symbol_ticker",
    "ts":1506584998239,//請求時間
    "tick":{
        "amount":123.1221,//交易額
        "vol":1212.12211,//交易量
        "open":2233.22,//開盤價
        "close":1221.11,//收盤價
        "high":22322.22,//最高價
        "low":2321.22,//最低價
        "rose":-0.2922,//漲幅
    }
}
```

### 請求k線歷史數據

* 請求數據樣例

```java
{
    "event":"req",
    "params":{
        "channel":"market_$symbol_kline_[1min/5min/15min/30min/60min/1day/1week/1month]",
        "cb_id":"1",
        "endIdx":"1506602880", //返回endIdx前pageSize條數據  非必填
        "pageSize":100 // 非必填
    }
}
```

* 返回

```java
{
    "event_rep":"rep","channel":"market_$symbol_kline_5min","cb_id":"原路返回",
    "ts":1506584998239,//請求時間
    "data":[ //最多300條
        {
            "id":1506602880,//時間刻度起始值
            "amount":123.1221,//交易額
            "vol":1212.12211,//交易量
            "open":2233.22,//開盤價
            "close":1221.11,//收盤價
            "high":22322.22,//最高價
            "low":2321.22//最低價
        },
        {
            "id":1506602880,//時間刻度起始值
            "amount":123.1221,//交易額
            "vol":1212.12211,//交易量
            "open":2233.22,//開盤價
            "close":1221.11,//收盤價
            "high":22322.22,//最高價
            "low":2321.22//最低價
        }
    ]
}
```

### 請求成交記錄

* 請求數據樣例

```java
{
    "event":"req",
    "params":{
        "channel":"market_$symbol_trade_ticker", // $symbol E.g. btcusdt 
        "cb_id":"1" // 業務id 非必填
    }
}
```

* 返回

```java
{
    "event_rep":"rep","channel":"market_$symbol_trade_ticker",
    "cb_id":"原路返回",
    "ts":1506584998239,"status":"ok",
    "data":[
        {
            "side":"buy",//買賣方向buy,sell
            "price":32.233,//單價
            "vol":232,//數量
            "amount":323//總額
        },
        {
            "side":"buy",//買賣方向buy,sell
            "price":32.233,//單價
            "vol":232,//數量
            "amount":323//總額
        }
    ]
}
```
