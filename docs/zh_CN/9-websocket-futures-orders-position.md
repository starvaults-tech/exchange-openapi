# WebSocket推送-合约订单仓位

## 目录

* 一.Token连接
  * 1.请求路径：
  * 2.请求头
  * 3.发送消息体
* 二.Apikey连接
  * 1.请求路径：
  * 2.请求头
  * 3.发送消息体
* 三.接收消息体
  * 1.当仓位和账户发生变化时
  * 2当用户持有仓位时
  * 3当系统关闭时
  * 4普通委托
  * 5计划委托返回数据
* 四.心跳

接口支持两种方式连接，一种是token连接，一种是apikey连接。

不论哪种方式连接订阅，返回的数据消息体是一样的。

## 一.Token连接

概述：请求头中携带token，与后端建立连接，建立连接后发送消息进行订阅，订阅成功后，才能接收到推送的消息。

### 1.请求路径：

wss\://futuresws.xxx.xxx/position\_order/ws

将xxx替换为自己的域名

### 2.请求头

| 参数名称  | 类型     | 是否必须 | 说明          |
| ----- | ------ | ---- | ----------- |
| token | string | 是    | 登录后生成的token |

### 3.发送消息体

| 参数名称   | 类型      | 是否必须 | 说明                            |
| ------ | ------- | ---- | ----------------------------- |
| event  | string  | 是    | <p>sub：订阅消息<br>unsub：取消订阅</p> |
| token  | string  | 是    | 登录后生成的token                   |
| broker | Integer | 是    | SaaS商户ID                      |

例子：

```json
{
    "event":"sub",
    "token":"9a2fce1e96cb42e76aa9519ee26468cd6d58efddd67d4bc1a9a0fa128734c0fe",
    "broker":1003
}
```

## 二.Apikey连接

概述：请求头中携带api-key，与后端建立连接，建立连接后发送消息进行订阅，订阅成功后，才能接收到推送的消息。

### 1.请求路径：

wss\://futuresws.xxx.xxx/position\_order/ws

将xxx替换为自己的域名

### 2.请求头

| 参数名称    | 类型     | 是否必须 | 说明        |
| ------- | ------ | ---- | --------- |
| api-key | string | 是    | 用户的Apikey |

### 3.发送消息体

| 参数名称   | 类型      | 是否必须 | 说明                            |
| ------ | ------- | ---- | ----------------------------- |
| event  | string  | 是    | <p>sub：订阅消息<br>unsub：取消订阅</p> |
| apiKey | string  | 是    | 登录后生成的token                   |
| broker | Integer | 是    | SaaS商户ID                      |

例子：

```json
{
    "event":"sub",
    "apiKey":"70556a7b653367858dfb0e4fc441cf00",
    "broker":1003
}
```

## 三.接收消息体

建立连接成功后，后端返回提示：connect success

订阅成功后，后端返回提示：sub success

![](https://3090275533-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FldIEUBhG9c2o7BFGqB0s%2Fuploads%2Fgit-blob-dee6f3cb7369846cedd45e9efb152f671bd0febb%2Fimage_zkKOk6nA5c.png?alt=media)

正式消息的消息体是GZIP压缩后的二进制数据，需要解析后才能正常展示数据，解析工具根据自己的语言自己实现即可。

这里提供一个在线的参考工具：<https://www.bejson.com/encrypt/gzip/#google_vignette>

例如，接收到的二进制的Base64数据为：

```
H4sIAAAAAAAAAD2NywrCQAxF/yXrYchMkpmkO1EXggtxKyL1AQpapdZV6b87rWB2l3vuSQ+f2xkqymyiDk7Xumkud6hgtlgfNtvVfAkOSt718GihQo+olKKlGCIGplDaDiqVHNSzg2s9QSVpNGVGKlfEdXFEB+OvqEQsycH7OQ3RPDnoXj9L9hh0HJGZSSSL6OD4J4ujnUhG8crZiJIEwZQkpWE/fAGMewQM0AAAAA==
```

解析后为：

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

例子：

![](https://3090275533-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FldIEUBhG9c2o7BFGqB0s%2Fuploads%2Fgit-blob-7ecd3964a426ea84a9a4c44b8496609bd887f40c%2Fimage_hOakX3HDyH.png?alt=media)

消息字段说明：

#### 1.当仓位和账户发生变化时

```json
{
    "channel": "ACCOUNT_UPDATE",// channel：不同的事件类型，当仓位和账户发生变化时推送ACCOUNT_UPDATE事件
    "uid":1001, // 合约用户ID
    "t": "1564745798938", // 时间戳
    "d": { // 数据
        "et": "CREATE",// UPDATE、DELETE、DEFAULT
        // CREATE :新增一个仓位，此时p不为空，且返回仓位的全部数据
        // DELETE :删除一个仓位，此时p不为空，且只返回仓位id
        // UPDATE :更新一个仓位，此时p不为空，且只返回发生变化的字段
        // DEFAULT:仓位不变，只有账户信息发生了变化，此时p为空
        "a": [ // 账户列表
            {
                "c": "USDT",  // 币种名称 
                "an": "122624.12345678", // 账户余额
                "la": "100.12345678",  // 冻结账号余额
                "pn": "50.12345678"  // 逐仓保证金账户余额
            },{
                "c": "BTC", // 币种
                "an": "122624.12345678", // 账户余额
                "la": "100.12345678",  // 冻结账号余额
                "pn": "50.12345678"  // 逐仓保证金账户余额
            }
        ],
        "p": {// 仓位信息
            "id": 90762,  // 仓位ID
            "cid": 127, // 合约ID
            "pt": 1,  // 仓位类型：1 全仓，2 逐仓
            "cn": "S-BTC-USDT", //合约名称
            "con": "BTCUSDT-EXUSD", //合约别名
            "l": 20, // 杠杆倍数
            "pv": 12, // 仓位张数
            "op": 98533.6, // 持仓均价
            "rp": 68000.3, // 预估强平价格
            "hm": 98.22008325596366,  // 逐仓持保证金
            "ra": 2, // 已实现盈亏
            "s": "BUY", // 多空方向
            "mr": 0.0847015132701974, // 保证金率
            "oa": 0.0847015132701974, // 开仓保证金
            "ccv": 2 //可平张数
        }
    }
}
```

#### 2当用户持有仓位时

```json
{
    "channel": "ADL_PRICE",//当用户持有仓位时，会推送ADL_PRICE消息，每秒1次
    "uid":1001, // 合约用户ID
    "l": [
        {
            "id": 7001,// 仓位ID
            "al": 1,  // ADL等级
            "rp": 68000.3,  // 预估强平价格
            "ha": 98.22008325596366,  // 保证金
            "mr": 0.0847015132701974, // 保证金率
            "bo":79000, // 买一价
            "so":78000, // 卖一价
            "lt":78500, // 最新成交价
            "tp":78000  // 标记价格
        },
        {
            "id": 7002,// 仓位ID
            "al": 1,  // ADL等级
            "rp": 68000.3,  // 预估强平价格
            "ha": 98.22008325596366,  // 保证金
            "mr": 0.0847015132701974, // 保证金率
            "bo":79000, // 买一价
            "so":78000, // 卖一价
            "lt":78500, // 最新成交价
            "tp":78000  // 标记价格
        }
    ]
}
```

#### 3当系统关闭时

会固定推送以下数据

```json
{
    "channel": "SYSTEM",
    "uid":1001,
    "et": "close"
}
```

#### 4普通委托

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
        "orderAction": "1"// 1新增 2取消 3委托变更
    }
}
```

#### 5**计划委托返回数据**

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
        "orderAction": "1"//1新增 2取消 
    }
}
```

## 四.**心跳**

30s ping一次，服务端超过40s没有收到ping就主动断开连接

参数：{"ping":1713338308232}

返回 ：{“pong”:1713338308233}
