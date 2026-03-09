# Sub Account

### Master Account API

#### Sub Account Management

**Get All Active Sub Accounts Under Master Account**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/get_sub_user_List`

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

| Name              | Type   | Description                                 |
| ----------------- | ------ | ------------------------------------------- |
| code              | String | Response code                               |
| msg               | String | Response message                            |
| data              | Object | Response data                               |
| data.subUserList  | Array  | Sub account list                            |
| ├─ subUid         | Number | Sub account uid                             |
| ├─ parentUid      | Number | Master account uid                          |
| ├─ loginType      | Number | Login method (0:virtual email 1:real email) |
| ├─ status         | Number | Sub account status (1:enabled 0:disabled)   |
| ├─ contractStatus | Number | Contract status (1:enabled 0:disabled)      |
| ├─ leverStatus    | Number | Leverage status (1:enabled 0:disabled)      |
| ├─ etfStatus      | Number | ETF status (1:enabled 0:disabled)           |
| ├─ depositStatus  | Number | Deposit status (1:enabled 0:disabled)       |
| ├─ remark         | String | Remarks                                     |
| ├─ email          | String | Email                                       |
| └─ mobileNumber   | String | Mobile number                               |

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

**Create a Virtual Sub Account for Your Master Account**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/create_sub_user`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name         | Type   | Required | Description                    |
| ------------ | ------ | -------- | ------------------------------ |
| subUserEmail | String | Required | Virtual email prefix length<=5 |

```javascript
{
    "subUserEmail": "661a"
}
```

**Enable/Disable Sub Account Trading**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/update_trade_status`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name   | Type   | Required | Description                                                      |
| ------ | ------ | -------- | ---------------------------------------------------------------- |
| type   | String | Required | Leverage:"lever" Contract:"contract" ETF:"etf" Deposit:"deposit" |
| subUid | String | Required | Sub account uid                                                  |
| status | String | Required | 1:enable 0:disable                                               |

```javascript
{
    "type": "lever",
    "subUid": "24006129",
    "status": "0"
}
```

#### Sub Account API Key Management

**Query Sub Account API Key IP Whitelist**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/sub_account_api/list`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name   | Type   | Required | Description     |
| ------ | ------ | -------- | --------------- |
| subUid | String | Required | Sub account uid |

```javascript
{
    "subUid": "24006297"
}
```

**Response**

| Name          | Type   | Description                                                                                                                                       |
| ------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| code          | String | Response code                                                                                                                                     |
| msg           | String | Response message                                                                                                                                  |
| data          | Object | Response data                                                                                                                                     |
| data.apiList  | Array  | API Key list                                                                                                                                      |
| ├─ uid        | Number | Sub account uid                                                                                                                                   |
| ├─ apiKey     | String | API Key                                                                                                                                           |
| ├─ believeIps | String | Trusted IP list, comma separated                                                                                                                  |
| ├─ label      | String | API Key label                                                                                                                                     |
| └─ authority  | String | Permission configuration, comma separated 0:allow read 1:allow spot 2:allow leverage 3:allow contract 4:allow withdraw 8:allow sub-master account |

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

**Set IP Whitelist for Sub Account API Key**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/sub_account_api/update_ip`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name             | Type   | Required | Description                                                        |
| ---------------- | ------ | -------- | ------------------------------------------------------------------ |
| subUid           | String | Required | Sub account uid                                                    |
| subAccountApiKey | String | Required | Sub account apikey                                                 |
| status           | String | Required | 1=IP unrestricted. 2 = Only trusted IP access                      |
| ipAddress        | String | Required | Can batch enter IPs, separated by commas (effective when status=2) |

```javascript
{
    "subUid": "24006297",
    "subAccountApiKey": "be85fe2a52606a8338f1d34c7e921822",
    "status": "2",
    "ipAddress": "123.123.123.123,111.111.111.192"
}
```

**Delete Sub Account API Key**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/sub_account_api/delete`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name             | Type   | Required | Description        |
| ---------------- | ------ | -------- | ------------------ |
| subUid           | String | Required | Sub account uid    |
| subAccountApiKey | String | Required | Sub account apikey |

```javascript
{
    "subUid": "24006297",
    "subAccountApiKey": "be85fe2a52606a8338f1d34c7e921822"
}
```

#### Asset Transfer

**Master to Sub / Sub to Master Transfer (Spot Account)**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/asset/root_transfer`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name       | Type   | Required | Description                     |
| ---------- | ------ | -------- | ------------------------------- |
| subUid     | String | Required | Sub account uid                 |
| amount     | String | Required | Amount                          |
| coinSymbol | String | Required | Coin symbol                     |
| type       | String | Required | 0:sub to master 1:master to sub |

```javascript
{
    "subUid": "24006139",
    "amount": "0.02",
    "coinSymbol": "btc",
    "type": "1"
}
```

**Master to Sub / Sub to Master Transfer Records**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/asset/root_transfer_query`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name       | Type   | Required | Description     |
| ---------- | ------ | -------- | --------------- |
| pageSize   | String | Required | Page size       |
| page       | String | Required | Page number     |
| subUid     | String | Required | Sub account uid |
| coinSymbol | String | Required | Coin symbol     |

```javascript
{
    "pageSize": "5",
    "page": "1",
    "subUid": 24006139,
    "coinSymbol": "USDT"
}
```

**Response**

| Name              | Type   | Description                     |
| ----------------- | ------ | ------------------------------- |
| code              | String | Response code                   |
| msg               | String | Response message                |
| data              | Object | Response data                   |
| data.count        | Number | Total count                     |
| data.list         | Array  | Transfer record list            |
| ├─ coinSymbol     | String | Coin symbol                     |
| ├─ coinSymbolName | String | Coin symbol name                |
| ├─ subUid         | Number | Sub account uid                 |
| ├─ subEmail       | String | Sub account email               |
| ├─ amount         | String | Amount                          |
| ├─ opType         | Number | 0:sub to master 1:master to sub |
| └─ time           | Number | Operation time                  |

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

**Sub Account Internal Transfer Between Different Accounts**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/asset/transfer`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name        | Type   | Required | Description                                |
| ----------- | ------ | -------- | ------------------------------------------ |
| subUid      | String | Required | Sub account uid                            |
| coinSymbol  | String | Required | Coin symbol                                |
| amount      | String | Required | Amount                                     |
| type        | String | Required | 1:spot to others 2:others to spot          |
| accountType | String | Required | 1:spot 2:isolated 3:cross 4:otc 5:contract |

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

**Sub Account Internal Transfer Records**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/asset/transfer_query`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name        | Type   | Required | Description                         |
| ----------- | ------ | -------- | ----------------------------------- |
| subUid      | String | Required | Sub account uid                     |
| type        | String | Required | 1:spot to others 2:others to spot   |
| accountType | String | Required | 2:isolated 3:cross 4:otc 5:contract |
| page        | Number | Required | Page number                         |
| pageSize    | String | Required | Page size                           |
| coinSymbol  | String | Required | Coin symbol                         |

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

| Name              | Type   | Description                                             |
| ----------------- | ------ | ------------------------------------------------------- |
| code              | String | Response code                                           |
| msg               | String | Response message                                        |
| data              | Object | Response data                                           |
| data.list         | Array  | Account asset list                                      |
| ├─ subUid         | Number | Sub account uid                                         |
| ├─ time           | Number | Time                                                    |
| ├─ coinSymbol     | String | Coin symbol                                             |
| ├─ coinSymbolName | String | Coin symbol name                                        |
| ├─ fromAccount    | Number | From account 1:spot 2:isolated 3:cross 4:otc 5:contract |
| ├─ toAccount      | Number | To account 1:spot 2:isolated 3:cross 4:otc 5:contract   |
| └─ amount         | String | Amount                                                  |
| data.count        | Number | Total count                                             |

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

#### Asset Query

**Query Sub Account Assets**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/sub_user/asset/account`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name        | Type   | Required | Description                                |
| ----------- | ------ | -------- | ------------------------------------------ |
| subUid      | String | Required | Sub account uid                            |
| accountType | String | Required | 1:spot 2:isolated 3:cross 4:otc 5:contract |

```javascript
{
    "subUid": "24006129",
    "accountType": "2"
}
```

**Response**

| Name                  | Type   | Description               |
| --------------------- | ------ | ------------------------- |
| code                  | String | Response code             |
| msg                   | String | Response message          |
| data                  | Object | Response data             |
| data.accountList      | Array  | Account asset list        |
| ├─ symbol             | String | Symbol (leverage account) |
| ├─ coinSymbol         | String | Coin symbol               |
| ├─ totalBalance       | String | Total balance             |
| ├─ normalBalance      | String | Available balance         |
| └─ canTransferBalance | String | Transferable balance      |

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

### Sub Account API

#### Asset Transfer

**Transfer to Master Account**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/subaccount/transfer`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name       | Type   | Required | Description |
| ---------- | ------ | -------- | ----------- |
| coinSymbol | String | Required | Coin symbol |
| amount     | String | Required | Amount      |

```javascript
{
    "amount":"20",
    "coinSymbol":"USDT"
}
```

**Query Transfer Records with Master Account**

<mark style="color:green;">`POST`</mark>`https://openapi.star-vaults.com/sapi/v1/asset/subaccount/transfer_query`

**Headers**

| Name        | Type   | Description  |
| ----------- | ------ | ------------ |
| X-CH-SIGN   | String | Signature    |
| X-CH-TS     | String | Timestamp    |
| X-CH-APIKEY | String | Your API-key |

**Request Body**

| Name       | Type   | Required | Description                       |
| ---------- | ------ | -------- | --------------------------------- |
| coinSymbol | String | Required | Coin symbol                       |
| page       | String | Required | Page number (optional, default 1) |
| pageSize   | String | Required | Page size (optional, default 20)  |

```javascript
{
    "coinSymbol":"BTC",
    "page":"1",
    "pageSize":"5"
}
```

**Response**

| Name              | Type   | Description                  |
| ----------------- | ------ | ---------------------------- |
| code              | String | Response code                |
| msg               | String | Response message             |
| data              | Object | Response data                |
| data.count        | Number | Total count                  |
| data.list         | Array  | Transfer record list         |
| ├─ coinSymbol     | String | Coin symbol                  |
| ├─ coinSymbolName | String | Coin symbol name             |
| ├─ subUid         | Number | Sub account uid              |
| ├─ subEmail       | String | Sub account email            |
| ├─ amount         | String | Amount                       |
| ├─ opType         | Number | 0:to master 1:to sub account |
| ├─ time           | Number | Operation time               |
| └─ parentUid      | Number | Master account uid           |

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
