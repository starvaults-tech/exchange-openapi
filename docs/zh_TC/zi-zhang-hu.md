# 子帳戶

### 母帳戶接口

#### 子帳戶管理

**獲取母帳戶下所有開啟的子帳戶**

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/sub_user/get_sub_user_List`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的 API-key  |

**Request Body**

此接口無需請求參數

```javascript
{}
```

**Response**

| Name              | Type   | Description          |
| ----------------- | ------ | -------------------- |
| code              | String | 響應碼                  |
| msg               | String | 響應消息                 |
| data              | Object | 響應數據                 |
| data.subUserList  | Array  | 子帳戶列表                |
| ├─ subUid         | Number | 子帳戶 UID              |
| ├─ parentUid      | Number | 母帳戶 UID              |
| ├─ loginType      | Number | 登錄方式 (0:虛擬郵箱 1:真實郵箱) |
| ├─ status         | Number | 子帳戶狀態 (1:啟用 0:禁用)    |
| ├─ contractStatus | Number | 合約狀態 (1:開啟 0:關閉)     |
| ├─ leverStatus    | Number | 槓桿狀態 (1:開啟 0:關閉)     |
| ├─ etfStatus      | Number | ETF 狀態 (1:開啟 0:關閉)   |
| ├─ depositStatus  | Number | 充值狀態 (1:開啟 0:關閉)     |
| ├─ remark         | String | 備註                   |
| ├─ email          | String | 郵箱                   |
| └─ mobileNumber   | String | 手機號碼                 |

```javascript
{
    "code": "0",
    "msg": "Success",
    "data": {
        "subUserList": [
            {
                "subUid": 24006297,
                "parentUid": 23998561,
                "loginType": 0,
                "status": 1,
                "contractStatus": 0,
                "leverStatus": 0,
                "etfStatus": 0,
                "depositStatus": 0,
                "remark": "",
                "email": "661a_23998561@Virtual.com",
                "mobileNumber": ""
            },
            {
                "subUid": 24006139,
                "parentUid": 23998561,
                "loginType": 1,
                "status": 1,
                "contractStatus": 1,
                "leverStatus": 1,
                "etfStatus": 1,
                "depositStatus": 1,
                "remark": "",
                "email": "test176@qq.com",
                "mobileNumber": ""
            }
        ]
    }
}
```



**為您的母帳戶生成一個虛擬子帳戶**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/create_sub_user`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| subUserEmail | String | 必填 | 虛擬信箱前綴 長度 <= 5 |
| ------------ | ------ | -- | -------------- |

```javascript
{
    "subUserEmail": "661a"
}
```

**為子帳戶開通/關閉**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/update_trade_status`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name   | Type   | 是否必填 | Description                                     |
| ------ | ------ | ---- | ----------------------------------------------- |
| type   | String | 必填   | 槓桿:"lever" 合約:"contract" etf:"etf" 充值:"deposit" |
| subUid | String | 必填   | 子帳戶 UID                                         |
| status | String | 必填   | 1:開啟 0:關閉                                       |

```javascript
{
    "type": "lever",
    "subUid": "24006129",
    "status": "0"
}
```

#### 子帳戶API Key管理

**查詢子帳戶 API Key IP 白名單**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/sub_account_api/list`

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name   | Type   | 是否必填 | Description |
| ------ | ------ | ---- | ----------- |
| subUid | String | 必填   | 子帳戶 UID     |

```javascript
{
    "subUid": "24006297"
}
```

**Response**

| Name          | Type   | Description                                             |
| ------------- | ------ | ------------------------------------------------------- |
| code          | String | 響應碼                                                     |
| msg           | String | 響應消息                                                    |
| data          | Object | 響應數據                                                    |
| data.apiList  | Array  | API Key 列表                                              |
| ├─ uid        | Number | 子帳戶 UID                                                 |
| ├─ apiKey     | String | API Key                                                 |
| ├─ believeIps | String | 信任 IP 列表，以逗號分隔                                          |
| ├─ label      | String | API Key 標籤                                              |
| └─ authority  | String | 權限配置，逗號分隔 0:允許讀取 1:允許現貨 2:允許槓桿 3:允許合約 4:允許提現 8:允許子母帳戶劃轉 |

```javascript
{
    "code": "0",
    "msg": "Success",
    "data": {
        "apiList": [
            {
                "uid": 24006297,
                "apiKey": "be85fe2a52606a8338f1d34c7e921822",
                "believeIps": "123.123.123.123,111.111.111.192",
                "label": "test_api",
                "authority": "0,1,2,3"
            }
        ]
    }
}
```

**為子帳戶 API Key 設置 IP 白名單**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/sub_account_api/update_ip`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name             | Te     | Text | DescriptionText               |
| ---------------- | ------ | ---- | ----------------------------- |
| subUid           | String | 必填   | 子帳戶 UID                       |
| subAccountApiKey | String | 必填   | 子帳戶 API Key                   |
| status           | String | 必填   | 1=IP 未受限。2=僅限受信任 IP 訪問        |
| ipAddress        | String | 必填   | 可批量填入 IP，以逗號區隔 (status=2 時有效) |

```javascript
{
    "subUid": "24006297",
    "subAccountApiKey": "be85fe2a52606a8338f1d34c7e921822",
    "status": "2",
    "ipAddress": "123.123.123.123,111.111.111.192"
}
```

**刪除子帳戶 API Key**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/sub_account_api/delete`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name             | Type   | 是否必填 | Description |
| ---------------- | ------ | ---- | ----------- |
| subUid           | String | 必填   | 子帳戶 UID     |
| subAccountApiKey | String | 必填   | 子帳戶 API Key |

```javascript
{
    "subUid": "24006297",
    "subAccountApiKey": "be85fe2a52606a8338f1d34c7e921822"
}
```

### 資產劃轉

**母帳戶劃轉到子帳戶 / 子帳戶劃轉到母帳戶 (現貨帳戶)**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/asset/root_transfer`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name       | Type   | 是否必填 | Description             |
| ---------- | ------ | ---- | ----------------------- |
| subUid     | String | 必填   | 子帳戶 UID                 |
| amount     | String | 必填   | 金額                      |
| coinSymbol | String | 必填   | 幣種                      |
| type       | String | 必填   | 0:子帳戶劃轉到母帳戶 1:母帳戶劃轉到子帳戶 |

```javascript
{
    "subUid": "24006139",
    "amount": "0.02",
    "coinSymbol": "btc",
    "type": "1"
}
```

**母劃轉到子 / 子劃轉到母劃轉記錄**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/asset/root_transfer_query`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name       | Type   | 是否必填 | Description |
| ---------- | ------ | ---- | ----------- |
| pageSize   | String | 必填   | 頁大小         |
| page       | String | 必填   | 分頁Page      |
| subUid     | String | 必填   | 子帳戶 UID     |
| coinSymbol | String | 必填   | 幣種          |

```javascript
{
    "pageSize": "5",
    "page": "1",
    "subUid": 24006139,
    "coinSymbol": "USDT"
}
```

**Response**

| Name              | Type   | Description             |
| ----------------- | ------ | ----------------------- |
| code              | String | 響應碼                     |
| msg               | String | 響應消息                    |
| data              | Object | 響應數據                    |
| data.count        | Number | 總數量                     |
| data.list         | Array  | 劃轉記錄列表                  |
| ├─ coinSymbol     | String | 幣種                      |
| ├─ coinSymbolName | String | 幣種name                  |
| ├─ subUid         | Number | 子帳戶 UID                 |
| ├─ subEmail       | String | 子帳戶信箱                   |
| ├─ amount         | String | 金額                      |
| ├─ opType         | Number | 0:子帳戶劃轉到母帳戶 1:母帳戶劃轉到子帳戶 |
| └─ time           | Number | 操作時間                    |

```javascript
{
    "code": "0",
    "msg": "Success",
    "data": {
        "count": 1,
        "list": [
            {
                "coinSymbol": "USDT",
                "coinSymbolName": "USDT4",
                "subUid": 24006139,
                "subEmail": "test176@qq.com",
                "amount": "100",
                "opType": 1,
                "time": 1745486549000
            }
        ]
    }
}

```

**子賬戶自己兩個不同賬戶劃轉**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/asset/transfer`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name        | Type   | 是否必填 | Description              |
| ----------- | ------ | ---- | ------------------------ |
| subUid      | String | 必填   | 子帳戶 UID                  |
| coinSymbol  | String | 必填   | 幣種                       |
| amount      | String | 必填   | 金額                       |
| type        | String | 必填   | 1:現貨到其他 2:其他到現貨          |
| accountType | String | 必填   | 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |

```javascript
{
    "subUid": "24006139",
    "amount": "0.123",
    "coinSymbol": "BTC",
    "symbol": "btcusdt",
    "type": "1",
    "accountType": "3"
}
```



**子賬戶自己兩個不同賬戶劃轉記錄**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/asset/transfer_query`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name        | Type   | 是否必填 | Description         |
| ----------- | ------ | ---- | ------------------- |
| subUid      | String | 必填   | 子帳戶 UID             |
| type        | String | 必填   | 1:現貨到其他 2:其他到現貨     |
| accountType | String | 必填   | 2:逐倉 3:全倉 4:場外 5:合約 |
| page        | Number | 必填   | 頁碼                  |
| pageSize    | String | 必填   | 頁大小                 |
| coinSymbol  | String | 必填   | 幣種                  |

```javascript
{
    "subUid": "24006139",
    "type": "1",
    "accountType": "5",
    "page": 1,
    "pageSize": "5",
    "coinSymbol": "USDT"
}
```

**Response**

| Name              | Type   | Description                   |
| ----------------- | ------ | ----------------------------- |
| code              | String | 響應碼                           |
| msg               | String | 響應消息                          |
| data              | Object | 響應數據                          |
| data.list         | Array  | 帳戶資產列表                        |
| ├─ subUid         | Number | 子帳戶 UID                       |
| ├─ time           | Number | 時間                            |
| ├─ coinSymbol     | String | 幣種                            |
| ├─ coinSymbolName | String | 幣種名稱                          |
| ├─ fromAccount    | Number | 發起帳戶 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |
| ├─ toAccount      | Number | 接收帳戶 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |
| └─ amount         | String | 金額                            |
| data.count        | Number | 總數量                           |

```javascript
{
    "code": "0",
    "msg": "Success",
    "data": {
        "count": 1,
        "list": [
            {
                "subUid": 24006139,
                "time": 1745489512000,
                "coinSymbol": "USDT",
                "coinSymbolName": "USDT4",
                "amount": "1.1",
                "fromAccount": 1,
                "toAccount": 5
            }
        ]
    }
}
```



#### 資產查詢

**查詢子帳戶資產**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/sub_user/asset/account`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name        | Type   | 是否必填 | Description              |
| ----------- | ------ | ---- | ------------------------ |
| subUid      | String | 必填   | 子帳戶 UID                  |
| accountType | String | 必填   | 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |

```javascript
{
    "subUid": "24006129",
    "accountType": "2"
}
```

**Response**

| Name                  | Type   | Description |
| --------------------- | ------ | ----------- |
| code                  | String | 響應碼         |
| msg                   | String | 響應消息        |
| data                  | Object | 響應數據        |
| data.accountList      | Array  | 帳戶資產列表      |
| ├─ symbol             | String | 幣對(槓桿帳戶)    |
| ├─ coinSymbol         | String | 幣種          |
| ├─ totalBalance       | String | 總餘額         |
| ├─ normalBalance      | String | 正常餘額        |
| └─ canTransferBalance | String | 可劃轉餘額       |

```javascript
{
    "code": "0",
    "msg": "Success",
    "data": {
        "accountList": [
            {
                "symbol": "btcusdt",
                "coinSymbol": "BTC",
                "totalBalance": "0.344",
                "normalBalance": "0.344",
                "canTransferBalance": "0.344"
            },
            {
                "symbol": "ethusdt",
                "coinSymbol": "USDT",
                "totalBalance": "19",
                "normalBalance": "19",
                "canTransferBalance": "19"
            }
        ]
    }
}
```



### 子帳戶接口

#### 資產劃轉

**向母帳戶劃轉**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/asset/subaccount/transfer`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name       | Type   | 是否必填 | Description |
| ---------- | ------ | ---- | ----------- |
| coinSymbol | String | 必填   | 幣種          |
| amount     | String | 必填   | 金額          |

```javascript
{
    "amount":"20",
    "coinSymbol":"USDT"
}
```

**查詢與母帳戶的劃轉記錄**

<mark style="color:green;">`POST`</mark>`https://openapi.xxx.xx/sapi/v1/asset/subaccount/transfer_query`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳記        |
| X-CH-APIKEY | String | 您的API-key   |

**Request Body**

| Name       | Type   | 是否必填 | Description   |
| ---------- | ------ | ---- | ------------- |
| coinSymbol | String | 必填   | 幣種            |
| page       | String | 必填   | 分頁信息 非必填 默認1  |
| pageSize   | String | 必填   | 分頁信息 非必填 默認20 |

```javascript
{
    "coinSymbol":"BTC",
    "page":"1",
    "pageSize":"5"
}
```

**Response**

| Name              | Type   | Description     |
| ----------------- | ------ | --------------- |
| code              | String | 響應碼             |
| msg               | String | 響應消息            |
| data              | Object | 響應數據            |
| data.count        | Number | 總數量             |
| data.list         | Array  | 劃轉記錄列表          |
| ├─ coinSymbol     | String | 幣種              |
| ├─ coinSymbolName | String | 幣種名稱            |
| ├─ subUid         | Number | 子帳戶 UID         |
| ├─ subEmail       | String | 子帳戶信箱           |
| ├─ amount         | String | 金額              |
| ├─ opType         | Number | 0:轉至母帳戶 1:轉至子帳戶 |
| ├─ time           | Number | 操作時間            |
| └─ parentUid      | Number | 母帳戶 UID         |

```javascript
{
    "code": "0",
    "msg": "Success",
    "data": {
        "count": 3,
        "list": [
            {
                "coinSymbol": "BTC",
                "coinSymbolName": "BTC",
                "subUid": 24006139,
                "subEmail": "test176@qq.com",
                "amount": "1.6",
                "opType": 0,
                "time": 1758265812000,
                "parentUid": 23998561
            },
            {
                "coinSymbol": "BTC",
                "coinSymbolName": "BTC",
                "subUid": 24006139,
                "subEmail": "test176@qq.com",
                "amount": "0.02",
                "opType": 1,
                "time": 1747810116000,
                "parentUid": 23998561
            },
            {
                "coinSymbol": "BTC",
                "coinSymbolName": "BTC",
                "subUid": 24006139,
                "subEmail": "test176@qq.com",
                "amount": "10",
                "opType": 1,
                "time": 1745486529000,
                "parentUid": 23998561
            }
        ]
    }
}
```
