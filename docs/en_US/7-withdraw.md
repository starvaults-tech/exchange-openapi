# Withdraw

## Apply for withdrawal

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/withdraw/apply`

#### Headers

| Name                                          | Type    | Description  |
| --------------------------------------------- | ------- | ------------ |
| X-CH-APIKEY<mark style="color:red;">\*</mark> | String  | Your API-key |
| X-CH-SIGN<mark style="color:red;">\*</mark>   | String  | Sign         |
| X-CH-TS<mark style="color:red;">\*</mark>     | Integer | timestamp    |

#### Request Body

| Name                                              | Type   | Description                                                                                                                                                                                               |
| ------------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| withdrawOrderId<mark style="color:red;">\*</mark> | String | Custom withdrawal id, guaranteed to be unique                                                                                                                                                             |
| amount<mark style="color:red;">\*</mark>          | String | quantity                                                                                                                                                                                                  |
| address<mark style="color:red;">\*</mark>         | String | Withdrawal address                                                                                                                                                                                        |
| label                                             | String | Some currencies such as XRP, XMR allow filling of secondary address labels                                                                                                                                |
| symbol                                            | String | currency name，For coins that support multiple mainchains, the actual currency name needs to be transmitted, as shown in [Appendix 1](https://openapi-1.gitbook.io/exchange-openapi/openapi-en/appendix-1) |

{% tabs %}
{% tab title="200: OK " %}

```json
{
    "code":"Ѳ",//Return code, 0 for success, other failures
    "msg":"sucess",//returned messages
    "data":{
        "id":518353 //Platform withdrawal id
    }
}
```

{% endtab %}
{% endtabs %}

**weight(IP/UID): 100**

## Withdrawal record query

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/withdraw/query`

#### Headers

| Name                                          | Type   | Description  |
| --------------------------------------------- | ------ | ------------ |
| X-CH-APIKEY<mark style="color:red;">\*</mark> | String | Your API-key |
| X-CH-SIGN<mark style="color:red;">\*</mark>   | String | Sign         |
| X-CH-TS<mark style="color:red;">\*</mark>     | String | timestamp    |

#### Request Body

| Name            | Type   | Description                                                                                                                                                                                                |
| --------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| symbol          | String | Currency Name, For coins that support multiple mainchains, the actual currency name needs to be transmitted, as shown in [Appendix 1](https://openapi-1.gitbook.io/exchange-openapi/openapi-en/appendix-1) |
| withdrawId      | String | Platform withdrawal id                                                                                                                                                                                     |
| withdrawOrderId | String | Custom withdrawal id                                                                                                                                                                                       |
| startTime       | String | Start time, timestamp, default 90 days ago                                                                                                                                                                 |
| endTime         | String | end time, timestamp, default current time                                                                                                                                                                  |
| page            | String | Page number, starting at 1                                                                                                                                                                                 |

{% tabs %}
{% tab title="200: OK " %}

```json
{
    "code": "0",
    "msg": "成功",
    "data": {
        "withdrawList": [
            {
                "symbol": "TUSDT",
                "amount": 19.99999,
                "address": "TFFrjNfBAagmFWypE3Hnv6zPKAFhd3VcDf",
                "withdrawOrderId": "abc123",
                "fee": 0.00001,
                "ctime": 1605585397000,
                "txId": "749864_20201117115930",
                "id": 749864,
                "applyTime": 1666754820000,
                "status": 5,
                "info": ""
            },
            {
                "symbol": "TUSDT",
                "amount": 10.50999,
                "address": "TYsTiVVDU5VmnUPufzGD52CD1hSbPATT3Q",
                "withdrawOrderId": "abc456",
                "fee": 0.00001,
                "ctime": 1607089149000,
                "txId": "764294_20201204094130",
                "id": 764294,
                "applyTime": 1666754820000",
                "status": 5,
                "info": ""
            }
        ],
        "count": 2
    }
}
```

{% endtab %}
{% endtabs %}

**weight(IP/UID): 100**

#### Responses

| Parameter       | Type   | Example                            | Remark                                                                                                                |
| --------------- | ------ | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| symbol          | String | USDT                               | Withdrawal currency                                                                                                   |
| amount          | Number | 9.99                               | quantity                                                                                                              |
| address         | String | TFFrjNfBAagmFWypE3Hnv6zPKAFhd3VcDf | Withdrawal address                                                                                                    |
| withdrawOrderId | String | abc123                             | Custom withdrawal id                                                                                                  |
| fee             | Number | 0.01                               | fee                                                                                                                   |
| ctime           | Number | 1605585397000                      | creation time                                                                                                         |
| txId            | String | 749864\_20201117115930             | Withdrawal transaction id                                                                                             |
| id              | Number | 749864                             | Platform withdrawal id                                                                                                |
| applyTime       | Number | 1605585397000                      | On-chain time                                                                                                         |
| status          | Number | 2                                  | Withdrawal status, 0-unapproved, 1-approved, 2-approved rejected, 3-payment, 4-payment failed, 5-completed, 6-revoked |
| info            | String | Withdrawal address error           | Review rejection reasons                                                                                              |
