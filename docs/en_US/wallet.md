# Wallet

### Universal Transfer

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/universal_transfer`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name            | Type   | Required | Description                                             |
| --------------- | ------ | -------- | ------------------------------------------------------- |
| fromAccountType | String | Required | From account 1:spot 2:isolated 3:cross 4:otc 5:contract |
| toAccountType   | String | Required | To account 1:spot 2:isolated 3:cross 4:otc 5:contract   |
| symbol          | String | Optional | Symbol (required for isolated)                          |
| coinSymbol      | String | Required | Coin symbol                                             |
| amount          | String | Required | Amount                                                  |

```javascript
{
    "fromAccountType": "2",
    "toAccountType": "4",
    "symbol": "ethusdt",
    "coinSymbol": "usdt",
    "amount": "0.1"
}
```

### Universal Transfer Record Query

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/universal_transfer_query`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name            | Type   | Required | Description                                             |
| --------------- | ------ | -------- | ------------------------------------------------------- |
| fromAccountType | String | Required | From account 1:spot 2:isolated 3:cross 4:otc 5:contract |
| toAccountType   | String | Required | To account 1:spot 2:isolated 3:cross 4:otc 5:contract   |
| symbol          | String | Optional | Symbol (effective for isolated)                         |
| coinSymbol      | String | Optional | Coin symbol                                             |
| page            | Number | Optional | Default 1                                               |
| pageSize        | Number | Optional | Default 20                                              |

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

| Name             | Type   | Description                                             |
| ---------------- | ------ | ------------------------------------------------------- |
| code             | String | Response code                                           |
| msg              | String | Response message                                        |
| data             | Object | Response data                                           |
| data.pages       | Number | Total pages                                             |
| data.records     | Array  | Transfer record list                                    |
| ├─ uid           | Number | uid                                                     |
| ├─ time          | Number | Operation time                                          |
| ├─ coinSymbol    | String | Coin symbol                                             |
| │ coinSymbolName | String | Coin symbol name                                        |
| ├─ amount        | String | Amount                                                  |
| ├─ fromAccount   | Number | From account 1:spot 2:isolated 3:cross 4:otc 5:contract |
| └─ toAccount     | Number | To account 1:spot 2:isolated 3:cross 4:otc 5:contract   |
| data.count       | Number | Total count                                             |
| data.pageSize    | Number | Page size                                               |
| data.page        | Number | Current page number                                     |

```javascript
{
    "code": "0",
    "msg": "Success",
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

### Query Deposit History

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/deposit/his_list`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name      | Type   | Required | Description |
| --------- | ------ | -------- | ----------- |
| startTime | String | Required | Start time  |
| endTime   | String | Required | End time    |
| page      | String | Required | Page number |
| pageSize  | String | Required | Page size   |

```javascript
{
    "startTime": "1746585661000",
    "endTime": "1746585663000",
    "page": "1",
    "pageSize": "5"
}
```

**Response**

| Name              | Type   | Description                                            |
| ----------------- | ------ | ------------------------------------------------------ |
| code              | String | Response code                                          |
| msg               | String | Response message                                       |
| data              | Object | Response data                                          |
| data.pageSize     | Number | Page size                                              |
| data.total        | Number | Total count                                            |
| data.page         | Number | Page number                                            |
| data.pages        | Number | Total pages                                            |
| data.records      | Array  | Deposit record list                                    |
| ├─ createdAtTime  | Number | Creation time                                          |
| ├─ addressTo      | String | Receiving address                                      |
| ├─ amount         | String | Amount                                                 |
| ├─ txid           | String | Transaction ID                                         |
| ├─ status         | Number | Deposit status: 0 unconfirmed, 1 completed, 2 abnormal |
| ├─ symbol         | String | Coin symbol                                            |
| ├─ status\_text   | String | Deposit status description                             |
| ├─ uid            | Number | uid                                                    |
| ├─ depositType    | Number | Deposit type: 0 external deposit, 1 internal deposit   |
| ├─ mainChainName  | String | Main coin (same coin different chain)                  |
| ├─ tokenBase      | String | Network information                                    |
| └─ completionTime | Number | Completion time                                        |

```javascript
{
    "code": "0",
    "msg": "Success",
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
                "status_text": "Received",
                "uid": 23998561,
                "depositType": 1,
                "mainChainName": "ETH",
                "completionTime": 1746585662000
            }
        ]
    }
}
```

### Query Deposit Address

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/deposit/query_address`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name           | Type   | Required | Description      |
| -------------- | ------ | -------- | ---------------- |
| mainCoinSymbol | String | Required | Main coin symbol |

```javascript
{
    "mainCoinSymbol": "usdt"
}
```

**Response**

| Name                 | Type   | Description                   |
| -------------------- | ------ | ----------------------------- |
| code                 | String | Response code                 |
| msg                  | String | Response message              |
| data                 | Object | Response data                 |
| data.depositAddrList | Array  | Deposit address list          |
| ├─ address           | String | Deposit address               |
| ├─ coinSymbol        | String | Coin symbol unique identifier |
| ├─ tokenBase         | String | Network information           |
| ├─ tokenBaseName     | String | Network information           |
| ├─ tokenBaseLongName | String | Network information           |
| └─ mainChainName     | String | Main coin symbol              |

```javascript
{
    "code": "0",
    "msg": "Success",
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

### Query Withdrawal Address

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/withdraw/address/query`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name           | Type   | Required | Description      |
| -------------- | ------ | -------- | ---------------- |
| mainCoinSymbol | String | Required | Main coin symbol |

```javascript
{
    "mainCoinSymbol": "usdt"
}
```

**Response**

| Name               | Type   | Description                                                                                 |
| ------------------ | ------ | ------------------------------------------------------------------------------------------- |
| code               | String | Response code                                                                               |
| msg                | String | Response message                                                                            |
| data               | Object | Response data                                                                               |
| data.addressList   | Array  | Withdrawal address list                                                                     |
| ├─ uid             | Number | uid                                                                                         |
| ├─ symbol          | String | Coin symbol (from coin)                                                                     |
| ├─ mainChainSymbol | String | Main chain coin symbol                                                                      |
| ├─ mainChainName   | String | Main chain coin symbol name                                                                 |
| ├─ address         | String | Address                                                                                     |
| ├─ label           | String | Custom label                                                                                |
| ├─ status          | Number | Availability status, 0 unavailable, 1 available                                             |
| ├─ ctime           | Number | Creation time                                                                               |
| ├─ trustType       | Number | Trust this address: 0: untrusted 1: trusted                                                 |
| ├─ addrType        | Number | Address type: 1, normal address (bound to symbol) 2, universal address (bound to tokenBase) |
| ├─ mainCoinSymbol  | String | Main coin                                                                                   |
| ├─ tokenBase       | String | Corresponding network                                                                       |
| └─ tagType         | Number | Tag type                                                                                    |

```javascript
{
    "code": "0",
    "msg": "Success",
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

### Query User Transferable Assets

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/account/by_type`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name        | Type   | Required | Description                                        |
| ----------- | ------ | -------- | -------------------------------------------------- |
| accountType | String | Required | Account 1:spot 2:isolated 3:cross 4:otc 5:contract |

```javascript
{
    "accountType":"1"
}
```

**Response**

| Name                  | Type   | Description                     |
| --------------------- | ------ | ------------------------------- |
| code                  | String | Response code                   |
| msg                   | String | Response message                |
| data                  | Object | Response data                   |
| data.accountList      | Array  | Account asset list              |
| ├─ symbol             | String | Symbol (effective for isolated) |
| ├─ coinSymbol         | String | Coin symbol                     |
| ├─ coinSymbolName     | String | Coin symbol name                |
| ├─ totalBalance       | String | Total assets                    |
| ├─ normalBalance      | String | Available                       |
| └─ canTransferBalance | String | Transferable amount             |

```javascript
{
    "code": "0",
    "msg": "Success",
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

### Query User Spot Account Assets

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/exchange/account`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

This endpoint requires no request parameters

```javascript
{}
```

**Response**

| Name              | Type   | Description        |
| ----------------- | ------ | ------------------ |
| code              | String | Response code      |
| msg               | String | Response message   |
| data              | Object | Response data      |
| data.accountList  | Array  | Account asset list |
| ├─ coinSymbol     | String | Coin symbol        |
| ├─ coinSymbolName | String | Coin symbol name   |
| ├─ totalBalance   | String | Total balance      |
| └─ normalBalance  | String | Available balance  |

```javascript
{
    "code": "0",
    "msg": "Success",
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
                "coinSymbol": "BRL1411",
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
                "normalBalance": "0"
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
