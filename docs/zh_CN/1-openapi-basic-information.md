# OpenApi 基本信息

## API基本信息

* 本篇列出REST接口的baseurl `https://openapi.xxx.xx`
* 所有接口都会返回一个JSON object或者array.
* 响应中如有数组，数组元素以时间倒序排列，越早的数据越提前.
* 所有时间、时间戳均为UNIX时间，单位为毫秒.

## HTTP返回代码

* HTTP `4XX` 错误码用于指示错误的请求内容、行为、格式.
* HTTP `410` 错误码表示警告访问频次超限，即将被封IP.
* HTTP `418` 表示收到429后继续访问，会被封禁IP,频繁违反限制，封禁时间会逐渐延长，从最短2分钟到最长3天.
* HTTP `5XX` 返回错误码是内部系统错误；这说明这个问题是在服务器这边。在对待这个错误时，千万 不要把它当成一个失败的任务，因为执行状态 未知，有可能是成功也有可能是失败.
* HTTP `504` 表示API服务端已经向业务核心提交了请求但未能获取响应，特别需要注意的是`504`代码不代表请求失败，而是未知。很可能已经得到了执行，也有可能执行失败，需要做进一步确认.
* 任何接口都可能返回ERROR(错误); 错误的返回payload如下:

```java
{
  "code": -1121,
  "msg": "Invalid symbol."
}
```

## 接口通用信息

* 所有请求基于Https协议，请求头信息中`Content-Type`需要统一设置为: `'application/json'.`
* `GET`方法的接口, 参数必须在`query string`中发送.
* `POST`方法的接口, 参数必须在`request body`中发送.
* 对参数的顺序不做要求.

## 访问限制

* 访问限制是基于IP或者UID的，而不是API Key.
* 按IP和按UID(account)两种模式分别统计, 两者互相独立.
* 按照IP统计的权重单接口权重总额为每分钟12000.
* 按照UID统计的接口权重总额是每分钟60000.
* 每个接口会标明是按照IP或者按照UID统计, 以及相应请求一次的权重值
* 在每个接口下面会有限频的说明.
* 违反频率限制都会收到HTTP 429，这是一个警告.
* 当收到429告警时，调用者应当降低访问频率或者停止访问.

## 接口鉴权类型

* 每个接口都有自己的鉴权类型，鉴权类型决定了访问时应当进行何种鉴权
* 如果需要 API-key，应当在HTTP头中以`X-CH-APIKEY`字段传递
* API-key 与 API-secret 是大小写敏感的
* 可以在网页用户中心修改API-key 所具有的权限，例如读取账户信息、发送交易指令、发送提现指令

| 鉴权类型         | 描述              |
| ------------ | --------------- |
| NONE         | 不需要鉴权的接口        |
| TRADE        | 需要有效的API-KEY和签名 |
| USER\_DATA   | 需要有效的API-KEY和签名 |
| USER\_STREAM | 需要有效的API-KEY    |
| MARKET\_DATA | 需要有效的API-KEY    |

## 需要签名的接口 (TRADE 与 USER\_DATA)

* 调用`TRADE`或者`USER_DATA`接口时，应当在HTTP头中以`X-CH-SIGN`字段传递签名参数.
* 签名使用`HMAC SHA256`算法. API-KEY所对应的API-Secret作为 `HMAC SHA256` 的密钥.
* `X-CH-SIGN`的请求头是以timestamp + method + requestPath + body字符串(+表示字符串连接)作为操作对象
* 其中timestamp的值与`X-CH-TS`请求头相同, method是请求方法，字母全部大写：GET/POST.
* requestPath是请求接口路径 例如:/sapi/v1/order?orderId=211222334\&symbol=BTCUSDT
* `body`是请求主体的字符串(post only) 如果是`GET`请求则`body`可省略
* 签名大小写不敏感。

## 时间同步安全

* 签名接口均需要在HTTP头中以`X-CH-TS`字段传递时间戳, 其值应当是请求发送时刻的unix时间戳（毫秒） e.g. 1528394129373
* 服务器收到请求时会判断请求中的时间戳，如果是5000毫秒之前发出的，则请求会被认为无效。这个时间窗口值可以通过发送可选参数`recvWindow`来自定义。
* 另外，如果服务器计算得出客户端时间戳在服务器时间的‘未来’一秒以上，也会拒绝请求。
* 逻辑伪代码：

```java
if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow) {
  // process request
} else {
  // reject request
}
```

**关于交易时效性** 互联网状况并不100%可靠，不可完全依赖,因此你的程序本地到交易所服务器的时延会有抖动. 这是我们设置`recvWindow`的目的所在，如果你从事高频交易，对交易时效性有较高的要求，可以灵活设置`recvWindow`以达到你的要求。 不推荐使用5秒以上的`recvWindow`

## POST /sapi/v1/order/test 的示例

以下是在linux bash环境下使用 echo openssl 和curl工具实现的一个调用接口下单的示例 apikey、secret仅供示范

| Key       | Value                            |
| --------- | -------------------------------- |
| apiKey    | vmPUZE6mv9SD5V5e14y7Ju91duEh8A   |
| secretKey | 902ae3cb34ecee2779aa4d3e1d226686 |

| 参数     | 取值      |
| ------ | ------- |
| symbol | BTCUSDT |
| side   | BUY     |
| type   | LIMIT   |
| volume | 1       |
| price  | 9300    |

## 签名示例

* **body:**

```java
{"symbol":"BTCUSDT","price":"9300","volume":"1","side":"BUY","type":"LIMIT"}
```

* **HMAC SHA256 签名:**

```bash
[linux]$ echo -n "1588591856950POST/sapi/v1/order/test{\"symbol\":\"BTCUSDT\",\"price\":\"9300\",\"volume\":\"1\",\"side\":\"BUY\",\"type\":\"LIMIT\"}" | openssl dgst -sha256 -hmac "902ae3cb34ecee2779aa4d3e1d226686"
(stdin)= c50d0a74bb9427a9a03933d0eded03af9bf50115dc5b706882a4fcf07a26b761
```

* **curl 调用:**

```bash
  (HMAC SHA256)
  [linux]$ curl -H "X-CH-APIKEY: c3b165fd5218cdd2c2874c65da468b1e" -H "X-CH-SIGN: c50d0a74bb9427a9a03933d0eded03af9bf50115dc5b706882a4fcf07a26b761" -H "X-CH-TS: 1588591856950" -H "Content-Type:application/json" -X POST 'http://localhost:30000/sapi/v1/order/test' -d '{"symbol":"BTCUSDT","price":"9300","quantity":"1","side":"BUY","type":"LIMIT"}'
```
