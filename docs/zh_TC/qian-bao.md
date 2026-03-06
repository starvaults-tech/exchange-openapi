# 錢包

## 錢包

### 萬向劃轉

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/universal_transfer`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的 API-key  |

**Request Body**

| Name            | Type   | 是否必填 | Description                   |
| --------------- | ------ | ---- | ----------------------------- |
| fromAccountType | String | 必填   | 發起帳戶 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |
| toAccountType   | String | 必填   | 接收帳戶 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |
| symbol          | String | 可選   | 幣對（逐倉必填）                      |
| coinSymbol      | String | 必填   | 幣種                            |
| amount          | String | 必填   | 金額                            |

```javascript
{
    "fromAccountType": "2",
    "toAccountType": "4",
    "symbol": "ethusdt",
    "coinSymbol": "usdt",
    "amount": "0.1"
}
```

***

### 萬向劃轉記錄查詢

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/universal_transfer_query`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的 API-key  |

**Request Body**

| Name            | Type   | 是否必填 | Description                   |
| --------------- | ------ | ---- | ----------------------------- |
| fromAccountType | String | 必填   | 發起帳戶 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |
| toAccountType   | String | 必填   | 接收帳戶 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |
| symbol          | String | 可選   | 幣對（逐倉有效）                      |
| coinSymbol      | String | 可選   | 幣種                            |
| page            | Number | 可選   | 預設 1                          |
| pageSize        | Number | 可選   | 預設 20                         |

```javascript
{
    "fromAccountType": "1",
    "toAccountType": "2",
    "symbol": "ethusdt",
    "coinSymbol": "usdt",
    "page": 1,
    "pageSize": 5
}
```

**Response**

| Name             | Type   | Description                   |
| ---------------- | ------ | ----------------------------- |
| code             | String | 響應碼                           |
| msg              | String | 響應訊息                          |
| data             | Object | 響應資料                          |
| data.pages       | Number | 總頁數                           |
| data.records     | Array  | 劃轉記錄列表                        |
| ├─ uid           | Number | uid                           |
| ├─ time          | Number | 操作時間                          |
| ├─ coinSymbol    | String | 幣種                            |
| │ coinSymbolName | String | 幣種名稱                          |
| ├─ amount        | String | 金額                            |
| ├─ fromAccount   | Number | 發起帳戶 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |
| └─ toAccount     | Number | 接收帳戶 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |
| data.count       | Number | 總數量                           |
| data.pageSize    | Number | 頁大小                           |
| data.page        | Number | 當前頁碼                          |

```javascript
{
    "code": "0",
    "msg": "成功",
    "data": {
        "pages": 1,
        "records": [
            {
                "uid": 23998561,
                "time": 1747969949000,
                "coinSymbol": "USDT",
                "coinSymbolName": "USDT4",
                "amount": "1.223344",
                "fromAccount": 1,
                "toAccount": 2
            }
        ],
        "count": 1,
        "pageSize": 5,
        "page": 1
    }
}
```

***

### 查詢充值歷史

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/deposit/his_list`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的 API-key  |

**Request Body**

| Name      | Type   | 是否必填 | Description |
| --------- | ------ | ---- | ----------- |
| startTime | String | 必填   | 起始時間        |
| endTime   | String | 必填   | 截止時間        |
| page      | String | 必填   | 分頁 page     |
| pageSize  | String | 必填   | 分頁 pageSize |

```javascript
{
    "startTime": "1746585661000",
    "endTime": "1746585663000",
    "page": "1",
    "pageSize": "5"
}
```

**Response**

| Name              | Type   | Description            |
| ----------------- | ------ | ---------------------- |
| code              | String | 響應碼                    |
| msg               | String | 響應訊息                   |
| data              | Object | 響應資料                   |
| data.pageSize     | Number | 頁大小                    |
| data.total        | Number | 總數                     |
| data.page         | Number | 頁碼                     |
| data.pages        | Number | 總頁數                    |
| data.records      | Array  | 充值記錄列表                 |
| ├─ createdAtTime  | Number | 建立時間                   |
| ├─ addressTo      | String | 接收地址                   |
| ├─ amount         | String | 金額                     |
| ├─ txid           | String | txid                   |
| ├─ status         | Number | 充值狀態：0 未確認，1 已完成，2 異常  |
| ├─ symbol         | String | 幣種                     |
| ├─ status\_text   | String | 充值狀態說明                 |
| ├─ uid            | Number | uid                    |
| ├─ depositType    | Number | 充值類型：0 平台外部充值，1 平台內部充值 |
| ├─ mainChainName  | String | 主幣種（同幣異鏈）              |
| ├─ tokenBase      | String | 網路資訊                   |
| └─ completionTime | Number | 完成時間                   |

```javascript
{
    "code": "0",
    "msg": "成功",
    "data": {
        "pageSize": 5,
        "total": 1,
        "page": 1,
        "pages": 1,
        "records": [
            {
                "createdAtTime": 1746585662000,
                "addressTo": "0x88x4e542b0ef413d9111ded7a11cff261d500100",
                "amount": "439.566665",
                "txid": "0xasdasdsadsadsadsads",
                "status": 1,
                "symbol": "ETH",
                "status_text": "已到帳",
                "uid": 23998561,
                "depositType": 1,
                "mainChainName": "ETH",
                "completionTime": 1746585662000
            }
        ]
    }
}
```

***

### 查詢充值地址

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/deposit/query_address`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的 API-key  |

**Request Body**

| Name           | Type   | 是否必填 | Description |
| -------------- | ------ | ---- | ----------- |
| mainCoinSymbol | String | 必填   | 主幣種         |

```javascript
{
    "mainCoinSymbol": "usdt"
}
```

**Response**

| Name                 | Type   | Description |
| -------------------- | ------ | ----------- |
| code                 | String | 響應碼         |
| msg                  | String | 響應訊息        |
| data                 | Object | 響應資料        |
| data.depositAddrList | Array  | 充值地址列表      |
| ├─ address           | String | 充值地址        |
| ├─ coinSymbol        | String | 幣種唯一標示      |
| ├─ tokenBase         | String | 網路資訊        |
| ├─ tokenBaseName     | String | 網路資訊        |
| ├─ tokenBaseLongName | String | 網路資訊        |
| └─ mainChainName     | String | 主幣種         |

```javascript
{
    "code": "0",
    "msg": "成功",
    "data": {
        "depositAddrList": [
            {
                "address": "1PoddHTWhJV9UNVaUwdFexFyGMYJpjtNaL824",
                "coinSymbol": "USDT",
                "tokenBase": "BTC",
                "tokenBaseName": "BTC1",
                "tokenBaseLongName": "Bitcoin",
                "mainChainName": "USDT"
            },
            {
                "address": "0x88x4e542b0ef413d9111ded7a11cff261d500017",
                "coinSymbol": "EUSDT",
                "tokenBase": "ETH",
                "tokenBaseName": "ETH",
                "tokenBaseLongName": "Ethereum",
                "mainChainName": "USDT"
            },
            {
                "address": "T9yQaJwibznTZSK46GEpNTPXa6vvDsH2Ea",
                "coinSymbol": "TUSDT",
                "tokenBase": "TRX",
                "tokenBaseName": "TRX",
                "tokenBaseLongName": "Tron Network",
                "mainChainName": "USDT"
            },
            {
                "address": null,
                "coinSymbol": "USDTBSC",
                "tokenBase": "BNB",
                "tokenBaseName": "BNB",
                "tokenBaseLongName": "Binance Coin",
                "mainChainName": "USDT"
            }
        ]
    }
}
```

***

### 查詢提現地址

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/withdraw/address/query`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的 API-key  |

**Request Body**

| Name           | Type   | 是否必填 | Description |
| -------------- | ------ | ---- | ----------- |
| mainCoinSymbol | String | 必填   | 主幣種         |

```javascript
{
    "mainCoinSymbol": "usdt"
}
```

**Response**

| Name               | Type   | Description                                   |
| ------------------ | ------ | --------------------------------------------- |
| code               | String | 響應碼                                           |
| msg                | String | 響應訊息                                          |
| data               | Object | 響應資料                                          |
| data.addressList   | Array  | 提現地址列表                                        |
| ├─ uid             | Number | uid                                           |
| ├─ symbol          | String | 幣種（從幣）                                        |
| ├─ mainChainSymbol | String | 主鏈幣種                                          |
| ├─ mainChainName   | String | 主鏈幣種主幣種name                                   |
| ├─ address         | String | 地址                                            |
| ├─ label           | String | 標籤自訂義                                         |
| ├─ status          | Number | 是否可用狀態：0 不可用，1 可用                             |
| ├─ ctime           | Number | 建立時間                                          |
| ├─ trustType       | Number | 是否信任此地址：0:不信任，1: 信任                           |
| ├─ addrType        | Number | 地址類型：1、 普通地址（綁定 symbol），2、 通用地址（綁定 tokenBase） |
| ├─ mainCoinSymbol  | String | 主幣                                            |
| ├─ tokenBase       | String | 對應網路                                          |
| └─ tagType         | Number | 標籤類型                                          |

```javascript
{
    "code": "0",
    "msg": "成功",
    "data": {
        "addressList": [
            {
                "uid": 23998561,
                "symbol": "USDT(OMNI)",
                "mainChainSymbol": "USDT",
                "mainChainName": "BTC",
                "address": "1PoddHTWhJV9UNVaUwdFexFyGMYJpjtNaL825",
                "label": "1",
                "status": 1,
                "ctime": 1685360019000,
                "trustType": 0,
                "addrType": 1,
                "mainCoinSymbol": "USDT",
                "tokenBase": "BTC",
                "tagType": 0
            },
            {
                "uid": 23998561,
                "symbol": "USDT(OMNI)",
                "mainChainSymbol": "USDT",
                "mainChainName": "BTC",
                "address": "1PoddHTWhJV9UNVaUwdFexFyGMYJpjtNaL821",
                "label": "test",
                "status": 1,
                "ctime": 1700624256000,
                "trustType": 1,
                "addrType": 1,
                "mainCoinSymbol": "USDT",
                "tokenBase": "BTC",
                "tagType": 0
            },
            {
                "uid": 23998561,
                "symbol": "USDT(TRC20)",
                "mainChainSymbol": "USDT",
                "mainChainName": "TRX",
                "address": "1PoddHTWhJV9UNVaUwdFexFyGMYJpjtNaL829",
                "label": "test",
                "status": 1,
                "ctime": 1700624587000,
                "trustType": 1,
                "addrType": 1,
                "mainCoinSymbol": "USDT",
                "tokenBase": "TRX",
                "tagType": 0
            },
            {
                "uid": 23998561,
                "symbol": "USDT(TRC20)",
                "mainChainSymbol": "USDT",
                "mainChainName": "TRX",
                "address": "asdasd",
                "label": "aaaa",
                "status": 1,
                "ctime": 1700624689000,
                "trustType": 1,
                "addrType": 1,
                "mainCoinSymbol": "USDT",
                "tokenBase": "TRX",
                "tagType": 0
            }
        ]
    }
}
```

***

### 查詢用戶可劃轉資產

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/account/by_type`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的 API-key  |

**Request Body**

| Name        | Type   | 是否必填 | Description                 |
| ----------- | ------ | ---- | --------------------------- |
| accountType | String | 必填   | 帳戶 1:現貨 2:逐倉 3:全倉 4:場外 5:合約 |

```javascript
{
    "accountType": "1"
}
```

**Response**

| Name                  | Type   | Description |
| --------------------- | ------ | ----------- |
| code                  | String | 響應碼         |
| msg                   | String | 響應訊息        |
| data                  | Object | 響應資料        |
| data.accountList      | Array  | 帳戶資產列表      |
| ├─ symbol             | String | 幣對（逐倉有效）    |
| ├─ coinSymbol         | String | 幣種          |
| ├─ coinSymbolName     | String | 幣種名稱        |
| ├─ totalBalance       | String | 總資產         |
| ├─ normalBalance      | String | 可用          |
| └─ canTransferBalance | String | 可劃轉金額       |

```javascript
{
    "code": "0",
    "msg": "成功",
    "data": {
        "accountList": [
            {
                "symbol": null,
                "coinSymbol": "SOL",
                "coinSymbolName": "SOL",
                "totalBalance": "49990",
                "normalBalance": "49990",
                "canTransferBalance": "49990"
            },
            {
                "symbol": null,
                "coinSymbol": "ETH",
                "coinSymbolName": "ETH",
                "totalBalance": "982.989",
                "normalBalance": "982.989",
                "canTransferBalance": "982.989"
            },
            {
                "symbol": null,
                "coinSymbol": "BCH",
                "coinSymbolName": "BCH",
                "totalBalance": "499.213",
                "normalBalance": "499.213",
                "canTransferBalance": "499.213"
            },
            {
                "symbol": null,
                "coinSymbol": "BTC1",
                "coinSymbolName": "BTC",
                "totalBalance": "85.941708603828",
                "normalBalance": "85.941708603828",
                "canTransferBalance": "85.941708603828"
            },
            {
                "symbol": null,
                "coinSymbol": "LTC123",
                "coinSymbolName": "LTC",
                "totalBalance": "50000",
                "normalBalance": "50000",
                "canTransferBalance": "50000"
            },
            {
                "symbol": null,
                "coinSymbol": "USDT4",
                "coinSymbolName": "USDT",
                "totalBalance": "411542.4341956856",
                "normalBalance": "411442.4341956856",
                "canTransferBalance": "411442.4341956856"
            }
        ]
    }
}
```

***

### 查詢用戶幣幣帳戶資產

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/exchange/account`

**Headers**

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| X-CH-SIGN   | String | 簽名          |
| X-CH-TS     | String | 時間戳         |
| X-CH-APIKEY | String | 您的 API-key  |

**Request Body**

此接口無需請求參數

```javascript
{}
```

**Response**

| Name              | Type   | Description |
| ----------------- | ------ | ----------- |
| code              | String | 響應碼         |
| msg               | String | 響應訊息        |
| data              | Object | 響應資料        |
| data.accountList  | Array  | 帳戶資產列表      |
| ├─ coinSymbol     | String | 幣種          |
| ├─ coinSymbolName | String | 幣種名稱        |
| ├─ totalBalance   | String | 總額          |
| └─ normalBalance  | String | 可用額         |

```javascript
{
    "code": "0",
    "msg": "成功",
    " data": {
        "accountList": [
            {
                "coinSymbol": "USD",
                "coinSymbolName": "USD",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "USDT1641",
                "coinSymbolName": "USDT",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "EOS",
                "coinSymbolName": "EOS",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "MAB05",
                "coinSymbolName": "MAB05",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "MAB04",
                "coinSymbolName": "MAB04",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "COW",
                "coinSymbolName": "COW",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "INR1643",
                "coinSymbolName": "INRMACK",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "SOL",
                "coinSymbolName": "SOL",
                "totalBalance": "49990",
                "normalBalance": "49990"
            },
            {
                "coinSymbol(): "BRL1411",
                "coinSymbolName": "BRL",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "YSL",
                "coinSymbolName": "YSL",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "BNB1426",
                "coinSymbolName": "BNB1426",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "ETC",
                "coinSymbolName": "ETC",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "MAB02",
                "coinSymbolName": "MAB02",
                "totalBalance": "0",
                "normalBalance': "0"
            },
            {
                "coinSymbol": "BNB",
                "coinSymbolName": "BNB",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "MATIC1",
                "coinSymbolName": "MATIC",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "NEO",
                "coinSymbolName": "NEO",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "ETH",
                "coinSymbolName": "ETH",

                "totalBalance": "982.989",
                "normalBalance": "982.989"
            },
            {
                "coinSymbol": "JAP",
                "coinSymbolName": "JAPces",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "USDC",
                "coinSymbolName": "USDC",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "CHI1411",
                "coinSymbolName": "CHI",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "USDT1649",
                "coinSymbolName": "USDT2223",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "STETH1411",
                "coinSymbolName": "STETH",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "ETH3L",
                "coinSymbolName": "ETH3L",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "BIKI1445",
                "coinSymbolName": "BIKI",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "GMTT",
                "coinSymbolName": "GMTT",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "RVK",
                "coinSymbolName": "RvK",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "LBB",
                "coinSymbolName": "LBBtest",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "BBK",
                "coinSymbolName": "BBK",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "HT",
                "coinSymbolName": "HT",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "ETH3S",
                "coinSymbolName": "ETH3S",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "TRX",
                "coinSymbolName": "TRX",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "LINK",
                "coinSymbolName": "LINK",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "BTC3L",
                "coinSymbolName": "BTC3lllL",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "MDX",
                "coinSymbolName": "MDX",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "BCH",
                "coinSymbolName": "BCH",
                "totalBalance": "499.213",
                "normalBalance": "499.213"
            },
            {
                "coinSymbol": "DOT",
                "coinSymbolName": "DOT",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "XFNH1411",
                "coinSymbolName": "XFNH",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "QUMT",
                "coinSymbolName": "QUMTB",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "FILCOIN",
                "coinSymbolName": "FIL",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "MM001",
                "coinSymbolName": "MM001",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "BTC",
                "coinSymbolName": "BTC1",
                "totalBalance": "85.941708603828",
                "normalBalance": "85.941708603828"
            },
            {
                "coinSymbol": "TON",
                "coinSymbolName": "TON",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "NB",
                "coinSymbolName": "NB",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "BOX1411",
                "coinSymbolName": "BOX",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "BTC3S",
                "coinSymbolName": "BTC3S",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "LTC",
                "coinSymbolName": "LTC123",
                "totalBalance": "50000",
                "normalBalance": "50000"
            },
            {
                "coinSymbol": "DPK",
                "coinSymbolName": "DPK",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "WBTC1411",
                "coinSymbolName": "WBTC",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "DOGE",
                "coinSymbolName": "DOGE",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "ETH3434",
                "coinSymbolName": "ETHK",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "USDT",
                "coinSymbolName": "USDT4",
                "totalBalance": "411542.4341956856",
                "normalBalance": "411442.4341956856"
            },
            {
                "coinSymbol": "INR",
                "coinSymbolName": "INR14111",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "ATOM",
                "coinSymbolName": "ATOM",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "UNI",
                "coinSymbolName": "UNI",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "BRL1445",
                "coinSymbolName": "BRL",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "MNT",
                "coinSymbolName": "MNT",
                "totalBalance": "0",
                "normalBalance": "0"
            },
            {
                "coinSymbol": "MAB123",
                "coinSymbolName": "xwz",
                "totalBalance": "0",
                "normalBalance": "0"
            }
        ]
    }
}
```
