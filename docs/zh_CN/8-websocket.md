# WebSocket推送-K线

### 概述

WebSocket是HTML5一种新的协议（Protocol）。它实现了客户端与服务器全双工通信， 使得数据可以快速地双向传播。通过一次简单的握手就可以建立客户端和服务器连接， 服务器根据业务规则可以主动推送信息给客户端。其优点如下：

* 客户端和服务器进行数据传输时，请求头信息比较小，大概2个字节。
* 客户端和服务器皆可以主动地发送数据给对方。
* 不需要多次创建TCP请求和销毁，节约宽带和服务器的资源。

**强烈建议开发者使用WebSocket API获取市场行情和买卖深度等信息。**

### 基本信息

* 行情基础站点: <mark style="color:blue;">wss\://ws.xxx.com/kline-api/ws</mark>
* 返回数据都会二进制压缩(用户需要通过Gzip算法进行解压）

### 心跳机制

服务器每10秒主动推送ping消息，客户端接收到后可自行决定是否处理（服务器并不对客户端的pong回复进行严格的一对一校验和时间校验）。 为了保障链接的有效性，建议客户端在收到服务器的ping消息后立即回复pong。 服务端发送ping消息格式： {"ping": 时间戳（秒级）} 客户端回复pong消息格式： {"pong": 时间戳（秒级）} 示例： {"pong":1694416595}

### 参数示例 <a href="#can-shu-shi-li" id="can-shu-shi-li"></a>

<table data-header-hidden><thead><tr><th>event</th><th width="313">channel</th><th width="220">description</th><th></th><th>描述</th></tr></thead><tbody><tr><td>sub</td><td><code>market_$symbol_depth_step0</code></td><td><code>订阅深度</code></td><td></td><td>描述</td></tr><tr><td>unsub</td><td><code>market_$symbol_depth_step0</code></td><td><code>取消订阅深度</code></td><td></td><td>币对名称</td></tr><tr><td>sub</td><td><code>market_$symbol_trade_ticker</code></td><td><code>订阅实时成交</code></td><td></td><td>base货币</td></tr><tr><td>unsub</td><td><code>market_$symbol_trade_ticker</code></td><td><code>取消订阅实时成交</code></td><td></td><td>计价货币</td></tr><tr><td>sub</td><td><code>market_$symbol_ticker</code></td><td><code>订阅24h行情数据</code></td><td></td><td>价格精度</td></tr><tr><td>unsub</td><td><code>market_$symbol_ticker</code></td><td><code>取消订阅24h行情数据</code></td><td></td><td>数量精度</td></tr><tr><td>sub</td><td><code>market_$symbol_kline_1min</code></td><td><code>订阅1min实时k线信息</code></td><td></td><td></td></tr><tr><td>reg</td><td><code>market_$symbol_kline_1month</code></td><td><code>请求1month历史k线记录</code></td><td></td><td></td></tr></tbody></table>

```java
{
    "event":"sub",
    "params":{
        "channel":"market_$symbol_kline_[1min/5min/15min/30min/60min/1day/1week/1month]", // $symbol E.g. btcusdt 
        "cb_id":"1" // 业务id 非必填
    }
}
```

* 返回

```java
{
    "channel":"market_$symbol_kline_1min", //1min代表1分钟k线
    "ts":1506584998239,//请求时间
    "tick":{
        "id":1506602880,//时间刻度起始值
        "vol":1212.12211,//交易量
        "open":2233.22,//开盘价
        "close":1221.11,//收盘价
        "high":22322.22,//最高价
        "low":2321.22//最低价
    }
}
```

### 订阅24h行情ticker

* 订阅数据样例

```java
{
    "event":"sub",
    "params":{
        "channel":"market_$symbol_ticker", // $symbol E.g. btcusdt 
        "cb_id":"1" // 业务id 非必填
    }
}
```

* 返回

```java
{
    "channel":"market_$symbol_ticker",
    "ts":1506584998239,//请求时间
    "tick":{
        "amount":123.1221,//交易额
        "vol":1212.12211,//交易量
        "open":2233.22,//开盘价
        "close":1221.11,//收盘价
        "high":22322.22,//最高价
        "low":2321.22,//最低价
        "rose":-0.2922,//涨幅
    }
}
```

### 请求k线历史数据

* 请求数据样例

```java
{
    "event":"req",
    "params":{
        "channel":"market_$symbol_kline_[1min/5min/15min/30min/60min/1day/1week/1month]",
        "cb_id":"1",
        "endIdx":"1506602880", //返回endIdx前pageSize条数据  非必填
        "pageSize":100 // 非必填
    }
}
```

* 返回

```java
{
    "event_rep":"rep","channel":"market_$symbol_kline_5min","cb_id":"原路返回",
    "ts":1506584998239,//请求时间
    "data":[ //最多300条
        {
            "id":1506602880,//时间刻度起始值
            "amount":123.1221,//交易额
            "vol":1212.12211,//交易量
            "open":2233.22,//开盘价
            "close":1221.11,//收盘价
            "high":22322.22,//最高价
            "low":2321.22//最低价
        },
        {
            "id":1506602880,//时间刻度起始值
            "amount":123.1221,//交易额
            "vol":1212.12211,//交易量
            "open":2233.22,//开盘价
            "close":1221.11,//收盘价
            "high":22322.22,//最高价
            "low":2321.22//最低价
        }
    ]
}
```

### 请求成交记录

* 请求数据样例

```java
{
    "event":"req",
    "params":{
        "channel":"market_$symbol_trade_ticker", // $symbol E.g. btcusdt 
        "cb_id":"1" // 业务id 非必填
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
            "side":"buy",//买卖方向buy,sell
            "price":32.233,//单价
            "vol":232,//数量
            "amount":323//总额
        },
        {
            "side":"buy",//买卖方向buy,sell
            "price":32.233,//单价
            "vol":232,//数量
            "amount":323//总额
        }
    ]
}
```
