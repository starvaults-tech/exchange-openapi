# WebSocket推送-合約訂單倉位

### 目錄

* 一.Token連接
  * 1.請求路徑：
  * 2.請求頭
  * 3.發送消息體
* 二.Apikey連接
  * 1.請求路徑：
  * 2.請求頭
  * 3.發送消息體
* 三.接收消息體
  * 1.當倉位和帳戶發生變化時
  * 2.當用戶持有倉位時
  * 3.當系統關閉時
  * 4.普通委託
  * 5.計劃委託返回數據
* 四.心跳

接口支持兩種方式連接，一種是token連接，一種是apikey連接。\
不論哪種方式連接訂閱，返回的數據消息體是一樣的。

## 一.Token連接

概述：請求頭中攜帶token，與後端建立連接，建立連接後發送消息進行訂閱，訂閱成功後，才能接收到推送的消息。

### 1.請求路徑：

wss://futuresws.star-vaults.com/position\_order/ws

### 2.請求頭

| 參數名稱  | 類型     | 是否必須 | 說明          |
| ----- | ------ | ---- | ----------- |
| token | string | 是    | 登錄後生成的token |

### 3.發送消息體

| 參數名稱   | 類型      | 是否必須 | 說明                            |
| ------ | ------- | ---- | ----------------------------- |
| event  | string  | 是    | <p>sub：訂閱消息<br>unsub：取消訂閱</p> |
| token  | string  | 是    | 登入後生成的 token                  |
| broker | Integer | 是    | SaaS 商戶 ID                    |

例子：

```json
{
    "event":"sub",
    "token":"9a2fce1e96cb42e76aa9519ee26468cd6d58efddd67d4bc1a9a0fa128734c0fe",
    "broker":1003
}
```

## 二.Apikey連接

概述：請求頭中攜帶 api-key，與後端建立連接，建立連接後發送消息進行訂閱，訂閱成功後，才能接收到推送的消息。

### 1.請求路徑：

wss://futuresws.star-vaults.com/position\_order/ws

### 2.請求頭

| 參數名稱    | 類型     | 是否必須 | 說明         |
| ------- | ------ | ---- | ---------- |
| api-key | string | 是    | 用戶的 Apikey |

### 3.發送消息體

| 參數名稱   | 類型      | 是否必須 | 說明                            |
| ------ | ------- | ---- | ----------------------------- |
| event  | string  | 是    | <p>sub：訂閱消息<br>unsub：取消訂閱</p> |
| apiKey | string  | 是    | 登入後生成的 token                  |
| broker | Integer | 是    | SaaS 商戶 ID                    |

例子：

```json
{
    "event":"sub",
    "apiKey":"70556a7b653367858dfb0e4fc441cf00",
    "broker":1003
}
```

## 三.接收消息體

建立連接成功後，後端返回提示：connect success

訂閱成功後，後端返回提示：sub success

![](https://3090275533-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FldIEUBhG9c2o7BFGqB0s%2Fuploads%2Fgit-blob-dee6f3cb7369846cedd45e9efb152f671bd0febb%2Fimage_zkKOk6nA5c.png?alt=media)

正式消息的消息體是 GZIP 壓縮後的二進位數據，需要解析後才能正常顯示數據，解析工具根據自己的語言自己實現即可。

這裡提供一個線上的參考工具：[https://www.bejson.com/encrypt/gzip/#google\_vignette](https://www.bejson.com/encrypt/gzip/#google_vignette)

例如，接收到的二進位 Base64 數據為：

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

消息欄位說明：

#### 1.當倉位和帳戶發生變化時

```json
{
    "channel": "ACCOUNT_UPDATE",// channel：不同的事件類型，當倉位和帳戶發生變化時推送 ACCOUNT_UPDATE 事件
    "uid":1001, // 合約用戶 ID
    "t": "1564745798938", // 時間戳
    "d": { // 數據
        "et": "CREATE",// UPDATE、DELETE、DEFAULT
        // CREATE :新增一個倉位，此時 p 不為空，且返回倉位的全部數據
        // DELETE :刪除一個倉位，此時 p 不為空，且只返回倉位 id
        // UPDATE :更新一個倉位，此時 p 不為空，且只返回發生變化的欄位
        // DEFAULT:倉位不變，只有帳戶資訊發生了變化，此時 p 為空
        "a": [ // 帳戶列表
            {
                "c": "USDT",  // 幣種名稱
                "an": "122624.12345678", // 帳戶餘額
                "la": "100.12345678",  // 凍結帳戶餘額
                "pn": "50.12345678"  // 逐倉保證金帳戶餘額
            },{
                "c": "BTC", // 幣種
                "an": "122624.12345678", // 帳戶餘額
                "la": "100.12345678",  // 凍結帳戶餘額
                "pn": "50.12345678"  // 逐倉保證金帳戶餘額
            }
        ],
        "p": {// 倉位資訊
            "id": 90762,  // 倉位 ID
            "cid": 127, // 合約 ID
            "pt": 1,  // 倉位類型：1 全倉，2 逐倉
            "cn": "S-BTC-USDT", // 合約名稱
            "con": "BTCUSDT-EXUSD", // 合約別名
            "l": 20, // 槓桿倍數
            "pv": 12, // 倉位張數
            "op": 98533.6, // 持倉均價
            "rp": 68000.3, // 預估強平價格
            "hm": 98.22008325596366,  // 逐倉持保證金
            "ra": 2, // 已實現盈虧
            "s": "BUY", // 多空方向
            "mr": 0.0847015132701974, // 保證金率
            "oa": 0.0847015132701974, // 開倉保證金
            "ccv": 2 // 可平張數
        }
    }
}
```

#### 2.當用戶持有倉位時

```json
{
    "channel": "ADL_PRICE",// 當用戶持有倉位時，會推送 ADL_PRICE 消息，每秒 1 次
    "uid":1001, // 合約用戶 ID
    "l": [
        {
            "id": 7001,// 倉位 ID
            "al": 1,  // ADL 等級
            "rp": 68000.3,  // 預估強平價格
            "ha": 98.22008325596366,  // 保證金
            "mr": 0.0847015132701974, // 保證金率
            "bo":79000, // 買一價
            "so":78000, // 賣一價
            "lt":78500, // 最新成交價
            "tp":78000  // 標記價格
        },
        {
            "id": 7002,// 倉位 ID
            "al": 1,  // ADL 等級
            "rp": 68000.3,  // 預估強平價格
            "ha": 98.22008325596366,  // 保證金
            "mr": 0.0847015132701974, // 保證金率
            "bo":79000, // 買一價
            "so":78000, // 賣一價
            "lt":78500, // 最新成交價
            "tp":78000  // 標記價格
        }
    ]
}
```

#### 3.當系統關閉時

會固定推送以下數據

```json
{
    "channel": "SYSTEM",
    "uid":1001,
    "et": "close"
}
```

#### 4.普通委託

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
        "tradeFee": 3.2,
        "realizedAmount": 10.6,
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
        "orderAction": "1"// 1 新增 2 取消 3 委託變更（部分成交、完全成交等）
    }
}
```

#### 5.計劃委託返回數據

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
        "orderAction": "1"// 1 新增 2 取消
    }
}
```

## 四.**心跳**

每 30 秒 ping 一次，服務端超過 40 秒沒有收到 ping 就主動斷開連接。

參數：{"ping":1713338308232}

返回：{"pong":1713338308233}
