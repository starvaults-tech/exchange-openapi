# CCXT開發手冊

#### 目錄

1. 概述
2. 接入環境要求
3. 準備內容說明
4. API Key 取得與身份認證
5. Python 範例程式碼
6. 支援方法列表
7. 常見錯誤與排查
8. 通用伺服器和網路錯誤
9. 請求內容中的問題
10. 技術支援

***

#### 1. 概述

本交易所支援基於 **Python 版 CCXT** 介面開發，便於策略、量化、自動化交易等應用快速落地。

* CCXT 支援版本：**v4.x 及以上**
* 交易市場：現貨（Spot）

***

#### 2. 接入環境要求

* Python 版本：≥ 3.7
* CCXT 安裝：

```bash
pip install ccxt
```

* 驗證安裝：

```python
import ccxt
print(ccxt.__version__)
```

***

#### 3. 準備內容說明

| 項目                     | 說明                                                            |
| ---------------------- | ------------------------------------------------------------- |
| 申請交易所 ApiKey/SecertKey | 登入交易所前台用戶頁面，API 管理 - 帳戶 - API 管理中建立 API，取得 APIKey 和 SecertKey |

CCXT 需要新增/修改的部分：

```
# 程式碼結構
|-ccxt
    |-python
        |-ccxt
            |-__init__.py             # 修改，新增交易所名稱，用於初始化
            |-bitwind.py              # 新增，主要請求方法
            |-test
                |-test_bitwind.py     # 新增，用於測試呼叫介面
            |-abstract
                |-bitwind.py          # 介面定義
```

***

#### 4. API Key 取得與身份認證

* 登入交易所用戶介面 → API 管理 → 新建 API Key。
* 取得參數：
  * `apiKey`
  * `SecretKey`

**示例：**

此部分程式碼需要在 ccxt 目錄中的 ccxt 資料夾中，新建一個「交易所名稱.py」檔案，並將此部分程式碼放在該檔案中，修改交易所名稱

```python
import ccxt

# 以 bitwind 為例
class bitwind(ccxt.Exchange,ImplicitAPI):

    def describe(self):
        return self.deep_extend(super().describe(), {
            'id': 'bitwind',
            'name': 'BitWind',
            'countries': ['CN'],
            'apiKey': '', # 交易所 APIKEY
            'securityKey' : '', # 交易所 SECURITYKEY
            'urls': {
                'api': {
                    'public': 'https://openapi.bitwind.cc',
                    'private': 'https://openapi.bitwind.cc',
                },
            },
            'has': {
                'fetchMarkets': True,
                'fetchTicker': True,
                'createOrder': True,
                'cancelOrder': True,
                'fetchTime':True,
                'fetchTradeRecord':True,
                'loadMarkets':True
            },
            'api': {
                'public': {
                    'get': [
                        'load_markets',
                        'sapi/v2/time',
                        'sapi/v2/ping',
                        'markets',
                        'ticker'
                    ],
                },
                'private': {
                    'post': [
                        'sapi/v2/trades',
                        'order',
                        'cancelOrder'
                    ],
                },
            },
        })
```

***

#### 5. Python 實作程式碼

5.1 新增初始化交易所名稱

在 Python 資料夾中的 ccxt 資料夾目錄中的 `__init__.py` 檔案中的 exchanges 列表中新增交易所名稱

注：小寫字母，不能包含特殊字元，不能包含空格

```
# 交易所名稱
exchanges = [
    'ace',
    ...
    'bitwind',
]
```

5.2 新增介面

在 ccxt 檔案中 abstract 資料夾下目錄，新建介面檔案。例如 `bitwind.py` 並新增介面內容，例如：

```
from ccxt.base.types import Entry

# 交易所介面配置內容
class ImplicitAPI:
    # public
    public_get_sapi_v2_time = publicGetSapiV2Time = Entry('sapi/v2/time', 'public', 'GET', {})

    # private
    private_get_sapi_v1_account = privateGetSapiV2Account = Entry('sapi/v1/account', 'private', 'GET', {})
```

5.3 新增主方法

在 ccxt 資料夾下，與 abstract 同目錄新增 `bitwind.py` 檔案，用於實作請求交易所 OpenAPI 的方法，例如：

```
import ccxt
from ccxt.abstract.bitwind import ImplicitAPI
import hmac
import json
import urllib.parse
import time

# 交易所 API 文件：https://exchangedocsv2.gitbook.io/open-api-doc-v2/
class bitwind(ccxt.Exchange,ImplicitAPI):

    def describe(self):
        return self.deep_extend(super().describe(), {
            'id': 'bitwind',
            'name': 'BitWind',
            'countries': ['CN'],
            'apiKey': '', # 交易所 APIKEY
            'securityKey' : '', # 交易所 SECURITYKEY
            'urls': {
                'api': {
                    'public': 'https://openapi.bitwind.cc',
                    'private': 'https://openapi.bitwind.cc',
                },
            },
            'has': {
                'fetchMarkets': True,
                'fetchTicker': True,
                'createOrder': True,
                'cancelOrder': True,
                'fetchTime':True,
                'fetchTradeRecord':True,
                'loadMarkets':True
            },
            'api': {
                'public': {
                    'get': [
                        'load_markets',
                        'sapi/v2/time',
                        'sapi/v2/ping',
                        'markets',
                        'ticker'  # 這裡定義了 publicGetMarkets()，用於取得交易市場列表
                    ],
                },
                'private': {
                    'post': [
                        'sapi/v2/trades',
                        'order',
                        'cancelOrder' # 例如 privatePostOrder()
                    ],
                },
            },
        })


    def fetch_time(self, params={}):
        """取得時間"""
        print("fetch_time")
        response = self.publicGetSapiV2Time(params)  # 不使用 await
        print("response:",response)
        return response

    # 取得時間
    def public_get_time(self,params={}):
        print("public_get_time params :",)
        response = self.publicGetSapiV2Time()
        print("response:", response)
        return response


    # 帳戶資訊
    def private_get_account(self, params={}):
        print("private_get_account params :", )
        response = self.privateGetSapiV2Account()
        print("response:", response)
        return response



    # 透過 ak、sk 生成 sign 和請求方法
    def preCreateHash(self,timestamp, method, requestPath, queryString, body):
        # 拼接簽名
        pre = timestamp + method + requestPath
        if queryString.strip() != '':
            pre = pre + '?' +queryString.strip()
        if body.strip() != '':
            pre = pre + body.strip()
        return pre

    # 生成簽名
    # generate signature
    def toParamSign(self,timestamp, method, requestPath, queryString, body, secretKey):
        return hmac.new(secretKey.encode('UTF-8'), self.preCreateHash(timestamp, method, requestPath, queryString, body).encode('UTF-8'),"SHA256").hexdigest()


    # 簽名並發送請求
    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api] + '/' + path
        current = str(round((time.time()-3) * 1000))

        if params:
            body = json.dumps(params)
            print("first body",body)

        if api == 'public':
            if method == 'GET':
                # 不用 ak、sk 都是功能介面
                if params:
                    query_string = urllib.parse.urlencode(json.loads(body)).replace("%2F", "/")
                    url = url + '?'+ query_string
                sign = self.toParamSign(current, method, '/' + path, '', body or '', self.securityKey)
                headers = {
                    'Content-Type': 'application/json',
                    'X-CH-APIKEY': self.apiKey,
                    'X-CH-TS': current,
                    'X-CH-SIGN': sign,
                }

        # 如果是 private 的 API，新增認證
        if api == 'private':
            if method == 'POST':
                sign = self.toParamSign(current, method, '/' + path, '', body or '', self.securityKey)
                headers = {
                    'Content-Type': 'application/json',
                    'X-CH-APIKEY': self.apiKey,
                    'X-CH-TS': current,
                    'X-CH-SIGN': sign,
                }


            if method == 'GET':
                query_string = ''
                if params:
                    query_string = urllib.parse.urlencode(json.loads(body)).replace("%2F", "/")
                    url = url + '?'+ query_string
                sign = self.toParamSign(current, method, '/' + path,  query_string, '', self.securityKey)
                headers = {
                    'Content-Type': 'application/json',
                    'X-CH-APIKEY': self.apiKey,
                    'X-CH-TS': current,
                    'X-CH-SIGN': sign,
                }

        return {'url': url, 'method': method, 'body': body, 'headers': headers}
```

5.4 方法呼叫

在 ccxt 資料夾目錄下的 test 資料夾新建 `test_bitwind.py` 檔案，示例：

```
import ccxt 

# 初始化交易所
exchange = ccxt.bitwind()

# 方法呼叫
# public_get_sapi_v2_time
 try:
     markets = exchange.public_get_time()
 except Exception as e:
     print("Error public_get_sapi_v2_time:", str(e))



# private_get_sapi_v1_account
 try:
     markets = exchange.private_get_account()
 except Exception as e:
     print("Error private_get_sapi_v1_account:", str(e))
```

***

#### 6. 支援方法列表

| Bitwind                             | 說明        |
| ----------------------------------- | --------- |
| public\_get\_ping()                 | 測試連結      |
| public\_get\_time()                 | 伺服器時間     |
| fetchMarkets()                      | 幣對列表      |
| fetchOrderBook()                    | 訂單簿       |
| fetchTicker()                       | 行情 ticker |
| public\_get\_trades()               | 最近成交      |
| fetchOHLCV()                        | K 線/蠟燭圖數據 |
| createOrder()                       | 建立新訂單     |
| private\_post\_batchOrders()        | 批量下單      |
| fetchOrder()                        | 訂單查詢      |
| cancelOrder()                       | 撤銷訂單      |
| private\_post\_batchCancel\_order() | 批量撤銷訂單    |
| fetchOpenOrders()                   | 當前訂單      |
| fetchMyTrades()                     | 交易記錄      |
| fetchBalance()                      | 帳戶資訊      |

***

#### 7. 常見錯誤與排查

返回報錯一般由兩個部分組成：錯誤碼和錯誤訊息。錯誤碼是通用的，但是錯誤訊息會有所不同。如下是一個報錯 JSON Payload 示例：

```
{
  "code":-1121,
  "msg":"Invalid symbol."
}
```

#### 8. 通用伺服器和網路錯誤&#x20;

| -1000 | 處理請求時發生未知錯誤                                                                                               |
| ----- | --------------------------------------------------------------------------------------------------------- |
| -1001 | 內部錯誤，無法處理您的請求，請再試一次                                                                                       |
| -1002 | 您無權執行此請求。請求需要發送 API key，我們建議在所有的請求頭附加 APIkey                                                              |
| -1003 | 請求過於頻繁超過限制                                                                                                |
| -1004 | 您無權執行此請求，User not exit Company                                                                            |
| -1006 | 接收到了不符合預設格式的消息，下單狀態未知                                                                                     |
| -1007 | 等待後端伺服器響應逾時。發送狀態未知，執行狀態未知                                                                                 |
| -1014 | 不支援的訂單組合                                                                                                  |
| -1015 | 新訂單太多，請降低您的請求頻率                                                                                           |
| -1016 | 伺服器下線                                                                                                     |
| -1017 | 我們建議在所有的請求頭附加 Content-Type，並設置成 application/json                                                          |
| -1020 | 不支援此操作                                                                                                    |
| -1021 | 時延過大，伺服器根據請求中的時間戳判定耗時已經超出了 recevWindow。請改善網路條件或者增大 recevWindow。時間偏移過大，伺服器根據請求中的時間戳判定客戶端時間比伺服器時間提前了 1 秒鐘以上 |
| -1022 | 此請求的簽名無效                                                                                                  |
| -1023 | 您無權執行此請求，我們建議您在所有的請求頭附加 X-CH-TS                                                                           |
| -1024 | 您無權執行此請求，我們建議您在請求頭附加 X-CH-SIGN                                                                            |

#### 9. 請求內容中的問題

| -1100 | 在參數中發現非法字元                                                    |
| ----- | ------------------------------------------------------------- |
| -1101 | 發送的參數太多。偵測到的參數值重複                                             |
| -1102 | 未發送必填參數，該參數為空或格式錯誤。必填參數「%s」未發送，為空或格式錯誤。必須發送參數「%s」或「%s」，但兩者均為空 |
| -1103 | 發送了未知參數。每條請求需要至少一個參數 {Timestamp}                              |
| -1104 | 並非所有發送的參數都被讀取。並非所有發送的參數都被讀取；讀取了「%s」參數，但被發送了「%s」               |
| -1105 | 參數為空。參數「%s」為空。                                                |
| -1106 | 不需要時已發送參數。不需要時發送參數「%s」。                                       |
| -1111 | 精度超過為此資產定義的最大值。                                               |
| -1112 | 交易對沒有掛單                                                       |
| -1116 | 無效訂單類型。                                                       |
| -1117 | 無效買賣方向                                                        |
| -1118 | 新的客戶訂單 ID 為空                                                  |
| -1121 | 無效的 symbol                                                    |
| -1136 | 訂單 quantity 小於最小值                                             |
| -1138 | 訂單價格超出允許範圍                                                    |
| -1139 | 該交易對不支援市價交易                                                   |
| -1145 | 該訂單類型不支援撤銷                                                    |
| -2013 | Order 不存在                                                     |
| -2015 | 無效的 API 金鑰，IP 或操作權限                                           |
| -2016 | 交易被凍結                                                         |
| -2017 | 餘額不足                                                          |

***

#### 10. 技術文件

* OpenAPI 文件站：[https://star-vaults.gitbook.io/exchange-openapi/](https://star-vaults.gitbook.io/exchange-openapi/)
* CCXT 官方文件：[https://docs.ccxt.com](https://docs.ccxt.com/)
