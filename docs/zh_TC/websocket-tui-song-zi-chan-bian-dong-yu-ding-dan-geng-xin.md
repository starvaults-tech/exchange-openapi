---
description: 餘額
---

# Websocket推送-資產變動與訂單更新

版本：1.0

#### 一、Token 連接

概述： 請求頭中攜帶 Token 與後端建立連接。連接建立後，發送訂閱消息。只有訂閱成功後，才能接收推送消息。

1. 請求路徑：

`wss://ws2.xxx.xxx/spotws_user/userData/ws`

將 `xxx` 替換為你自己的域名。

2. 請求頭（Request Header）

| 參數名   | 類型     | 必填 | 說明            |
| ----- | ------ | -- | ------------- |
| token | string | 是  | 登入後生成的 token。 |

3. 消息體（Message Body）

| 參數名   | 類型     | 必填 | 說明                        |
| ----- | ------ | -- | ------------------------- |
| event | string | 是  | `sub`：訂閱消息，`unsub`：取消訂閱消息 |
| token | string | 是  | 登入後生成的 token。             |

示例：

```json
{
  "event": "sub",
  "token": "9a2fce1e96cb42e76aa9519ee26468cd6d58efddd67d4bc1a9a0fa128734c0fe"
}
```

#### 二、API-Key 連接

概述： 請求頭中攜帶 `api-key` 與後端建立連接。連接建立後，發送訂閱消息。只有訂閱成功後，才能接收推送消息。

1. 請求路徑：

`wss://ws2.xxx.xxx/spotws_user/userData/ws`

將 `xxx` 替換為你自己的域名。

2. 請求頭（Request Header）

| 參數名     | 類型     | 必填 | 說明            |
| ------- | ------ | -- | ------------- |
| api-key | string | 是  | 前端建立的 apikey。 |

3. 消息體（Message Body）

| 參數名   | 類型     | 必填 | 說明                        |
| ----- | ------ | -- | ------------------------- |
| event | string | 是  | `sub`：訂閱消息，`unsub`：取消訂閱消息 |
| token | string | 是  | 前端建立的 apikey。             |

示例：

```json
{
  "event": "sub",
  "token": "9a2fce1e96cb42e76aa9519ee26468cd6d58efddd67d4bc1a9a0fa128734c0fe"
}
```

#### 三、連接與數據格式說明

連接成功後，後端會返回提示：`"connect success"`。

訂閱成功後，後端會返回提示：`"sub success"`。

正式消息體為 GZIP 壓縮後的二進位數據，需要先解壓後才能正常顯示。你可以根據自己的開發語言實現解壓工具。線上參考工具：

[Gzip Decompression Tool](https://www.bejson.com/encrypt/gzip/#google_vignette)

例如，收到如下二進位 Base64 數據：

```
H4sIAAAAAAAAA6vmUlBQSlWyUlDKLy1Jyi/NS3FMTgZSJQH5xZklmfl5SjoK+voKT3Z1P9m97fnG3U/ndY
N0uAJ1GJqamRgYm5iaGxoamOooIAO4jmfTt72cvgWkoxRFh4G5MYaOF1uWPevY/mzO6mdrFj6bveXZt
A0Q3c86NoMMcAIaEK2AE4Cs3Dvz5aK5XCBeNRdEVCkR5DXXEA8lHWw6XmxtebJr+dMJvc+Xb4DpSAP
pMDQAAj0DMEBoBep42r/++ZQVSDYBdeSAdMBVo9vxtG33892TkXTUAslYrloAfBt5w3oBAAA=
```

解壓後得到：

```json
{
  "e": "outboundAccountPosition", // 事件類型
  "E": 1564034571105, // 事件時間
  "u": 1564034571073, // 帳戶最後更新時間戳
  "B": [ // 餘額
    {
      "a": "ETH", // 資產名稱
      "f": "10000.000000", // 可用餘額
      "l": "0.000000" // 凍結餘額
    }
  ]
}
```

#### 四、事件說明

**1）帳戶變更時**

當帳戶餘額發生變化時，會推送 `outboundAccountPosition` 事件。該事件包含因本次變更而可能發生變化的資產資訊。

```json
{
  "e": "outboundAccountPosition", // 事件類型
  "E": 1564034571105, // 事件時間
  "u": 1564034571073, // 帳戶最後更新時間戳
  "B": [ // 餘額
    {
      "a": "ETH", // 資產名稱
      "f": "10000.000000", // 可用餘額
      "l": "0.000000" // 凍結餘額
    }
  ]
}
```

**2）訂單狀態變更回執示例**

訂單透過 `executionReport` 事件進行更新。\
注：市價單不推送該事件。

```json
{
  "E": 1745389508472, // 事件時間
  "L": "13000.0000000000000000", // 最近一次成交價
  "O": 1745389507000, // 訂單建立時間
  "P": "0", // 止盈止損觸發價
  "Q": "0.17861112", // Quote 訂單數量
  "S": "SELL", // 訂單方向
  "T": 1745389508418, // 成交時間
  "X": "PART_FILLED", // 當前訂單狀態
  "Y": "1300.0000000000000000", // 最近一次成交金額
  "Z": "2321.94456", // 累計成交金額
  "e": "executionReport", // 事件類型
  "i": "2690536306533246156", // 訂單 ID
  "l": "0.1000000000000000", // 最近一次成交數量
  "n": "7.8000000000000000", // 手續費數量
  "o": "LIMIT", // 訂單類型
  "p": "13000", // 訂單原始價格
  "q": "1", // 訂單原始數量
  "s": "BTCUSDT", // 交易對
  "x": "STATUS", // 當前事件對應的具體執行類型
  "z": "0.17861112" // 累計成交數量
}
```

`X` 欄位說明：

* `FILLED`：完全成交
* `PART_FILLED`：部分成交
* `CANCELED`：撤單成功
* `PENDING_CANCEL`：撤單中

**3）系統關閉時**

會固定推送如下數據：

```json
{
  "uid": 24005174,
  "channel": "SYSTEM",
  "et": "close"
}
```

#### 五、心跳

每 30 秒發送一次 `ping`。如果服務端在 40 秒內未收到 `ping`，會主動斷開連接。

參數：`{"ping":1713338308232}`

響應：`{"pong":1713338308233}`
