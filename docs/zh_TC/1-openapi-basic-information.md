# OpenApi 基本信息

## API基本信息

* 本篇列出REST接口的baseurl `https://openapi.xxx.xx`
* 所有接口都會返回一個JSON object或者array.
* 響應中如有數組，數組元素以時間倒序排列，越早的數據越提前.
* 所有時間、時間戳均為UNIX時間，單位為毫秒.

## HTTP返回代碼

* HTTP `4XX` 錯誤碼用於指示錯誤的請求內容、行為、格式.
* HTTP `410` 錯誤碼表示警告訪問頻次超限，即將被封IP.
* HTTP `418` 表示收到429後繼續訪問，會被封禁IP,頻繁違反限制，封禁時間會逐漸延長，從最短2分鐘到最長3天.
* HTTP `5XX` 返回錯誤碼是內部系統錯誤；這說明這個問題是在服務器這邊。在對待這個錯誤時，千萬 不要把它當成一個失敗的任務，因為執行狀態 未知，有可能是成功也有可能是失敗.
* HTTP `504` 表示API服務端已經向業務核心提交了請求但未能獲取響應，特別需要注意的是`504`代碼不代表請求失敗，而是未知。很可能已經得到了執行，也有可能執行失敗，需要做進一步確認.
* 任何接口都可能返回ERROR(錯誤); 錯誤的返回payload如下:

```java
{
  "code": -1121,
  "msg": "Invalid symbol."
}
```

## 接口通用信息

* 所有請求基於Https協議，請求頭信息中`Content-Type`需要統一設置為: `'application/json'.`
* `GET`方法的接口, 參數必須在`query string`中發送.
* `POST`方法的接口, 參數必須在`request body`中發送.
* 對參數的順序不做要求.

## 訪問限制

* 訪問限制是基於IP或者UID的，而不是API Key.
* 按IP和按UID(account)兩種模式分別統計, 兩者互相獨立.
* 按照IP統計的權重單接口權重總額為每分鐘12000.
* 按照UID統計的接口權重總額是每分鐘60000.
* 每個接口會標明是按照IP或者按照UID統計, 以及相應請求一次的權重值
* 在每個接口下面會有限頻的說明.
* 違反頻率限制都會收到HTTP 429，這是一個警告.
* 當收到429告警時，調用者應當降低訪問頻率或者停止訪問.

## 接口鑒權類型

* 每個接口都有自己的鑒權類型，鑒權類型決定了訪問時應當進行何種鑒權
* 如果需要 API-key，應當在HTTP頭中以`X-CH-APIKEY`字段傳遞
* API-key 與 API-secret 是大小寫敏感的
* 可以在網頁用戶中心修改API-key 所具有的權限，例如讀取賬戶信息、發送交易指令、發送提現指令

| 鑒權類型         | 描述              |
| ------------ | --------------- |
| NONE         | 不需要鑒權的接口        |
| TRADE        | 需要有效的API-KEY和簽名 |
| USER\_DATA   | 需要有效的API-KEY和簽名 |
| USER\_STREAM | 需要有效的API-KEY    |
| MARKET\_DATA | 需要有效的API-KEY    |

## 需要簽名的接口 (TRADE 與 USER\_DATA)

* 調用`TRADE`或者`USER_DATA`接口時，應當在HTTP頭中以`X-CH-SIGN`字段傳遞簽名參數.
* 簽名使用`HMAC SHA256`算法. API-KEY所對應的API-Secret作為 `HMAC SHA256` 的密鑰.
* `X-CH-SIGN`的請求頭是以timestamp + method + requestPath + body字符串(+表示字符串連接)作為操作對象
* 其中timestamp的值與`X-CH-TS`請求頭相同, method是請求方法，字母全部大寫：GET/POST.
* requestPath是請求接口路徑 例如:/sapi/v1/order?orderId=211222334\&symbol=BTCUSDT
* `body`是請求主體的字符串(post only) 如果是`GET`請求則`body`可省略
* 簽名大小寫不敏感。

## 時間同步安全

* 簽名接口均需要在HTTP頭中以`X-CH-TS`字段傳遞時間戳, 其值應當是請求發送時刻的unix時間戳（毫秒） e.g. 1528394129373
* 服務器收到請求時會判斷請求中的時間戳，如果是5000毫秒之前發出的，則請求會被認為無效。這個時間窗口值可以通過發送可選參數`recvWindow`來自定義。
* 另外，如果服務器計算得出客戶端時間戳在服務器時間的‘未來’一秒以上，也會拒絕請求。
* 邏輯偽代碼：

```java
if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow) {
  // process request
} else {
  // reject request
}
```

**關於交易時效性** 互聯網狀況並不100%可靠，不可完全依賴,因此你的程序本地到交易所服務器的時延會有抖動. 這是我們設置`recvWindow`的目的所在，如果你從事高頻交易，對交易時效性有較高的要求，可以靈活設置`recvWindow`以達到你的要求。 不推薦使用5秒以上的`recvWindow`

## POST /sapi/v1/order/test 的示例

以下是在linux bash環境下使用 echo openssl 和curl工具實現的一個調用接口下單的示例 apikey、secret僅供示範

| Key       | Value                            |
| --------- | -------------------------------- |
| apiKey    | vmPUZE6mv9SD5V5e14y7Ju91duEh8A   |
| secretKey | 902ae3cb34ecee2779aa4d3e1d226686 |

| 參數     | 取值      |
| ------ | ------- |
| symbol | BTCUSDT |
| side   | BUY     |
| type   | LIMIT   |
| volume | 1       |
| price  | 9300    |

## 簽名示例

* **body:**

```java
{"symbol":"BTCUSDT","price":"9300","volume":"1","side":"BUY","type":"LIMIT"}
```

* **HMAC SHA256 簽名:**

```bash
[linux]$ echo -n "1588591856950POST/sapi/v1/order/test{\"symbol\":\"BTCUSDT\",\"price\":\"9300\",\"volume\":\"1\",\"side\":\"BUY\",\"type\":\"LIMIT\"}" | openssl dgst -sha256 -hmac "902ae3cb34ecee2779aa4d3e1d226686"
(stdin)= c50d0a74bb9427a9a03933d0eded03af9bf50115dc5b706882a4fcf07a26b761
```

* **curl 調用:**

```bash
  (HMAC SHA256)
  [linux]$ curl -H "X-CH-APIKEY: c3b165fd5218cdd2c2874c65da468b1e" -H "X-CH-SIGN: c50d0a74bb9427a9a03933d0eded03af9bf50115dc5b706882a4fcf07a26b761" -H "X-CH-TS: 1588591856950" -H "Content-Type:application/json" -X POST 'http://localhost:30000/sapi/v1/order/test' -d '{"symbol":"BTCUSDT","price":"9300","quantity":"1","side":"BUY","type":"LIMIT"}'
```
