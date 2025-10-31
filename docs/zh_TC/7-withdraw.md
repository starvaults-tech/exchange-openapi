# 提現

## 提現

## 發起提現

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/withdraw/apply`

#### Headers

| Name                                          | Type    | Description |
| --------------------------------------------- | ------- | ----------- |
| X-CH-APIKEY<mark style="color:red;">\*</mark> | String  | 您的API-Key   |
| X-CH-SIGN<mark style="color:red;">\*</mark>   | String  | 簽名          |
| X-CH-TS<mark style="color:red;">\*</mark>     | Integer | 時間戳         |

#### Request Body

| Name                                              | Type   | Description                                                                         |
| ------------------------------------------------- | ------ | ----------------------------------------------------------------------------------- |
| withdrawOrderId<mark style="color:red;">\*</mark> | String | 自定義提現id，保證唯一                                                                        |
| amount<mark style="color:red;">\*</mark>          | String | 數量                                                                                  |
| address<mark style="color:red;">\*</mark>         | String | 提幣地址                                                                                |
| label                                             | String | 某些幣種例如 XRP,XMR 允許填寫次級地址標簽                                                           |
| symbol                                            | String | 幣種，支持多主鏈的幣需要傳實際的幣種名稱，參照[附錄1](https://openapi-1.gitbook.io/exchange-openapi/fu-lu-1) |

{% tabs %}
{% tab title="200: OK " %}

```json
{
    "code":"Ѳ",//返回碼，0代表成功，其他失敗
    "msg":"sucess",//返回信息
    "data":{
        "id":518353 //提現id
    }
}
```

{% endtab %}
{% endtabs %}

**權重(IP/UID): 100**

## 提現記錄查詢

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/withdraw/query`

#### Headers

| Name                                          | Type   | Description |
| --------------------------------------------- | ------ | ----------- |
| X-CH-APIKEY<mark style="color:red;">\*</mark> | String | 您的API-Key   |
| X-CH-SIGN<mark style="color:red;">\*</mark>   | String | 簽名          |
| X-CH-TS<mark style="color:red;">\*</mark>     | String | 時間戳         |

#### Request Body

| Name            | Type   | Description                                                                         |
| --------------- | ------ | ----------------------------------------------------------------------------------- |
| symbol          | String | 幣種，支持多主鏈的幣需要傳實際的幣種名稱，參照[附錄1](https://openapi-1.gitbook.io/exchange-openapi/fu-lu-1) |
| withdrawId      | String | 平台提現id                                                                              |
| withdrawOrderId | String | 自定義提現id                                                                             |
| startTime       | Number | 開始時間，時間戳，默認90天前                                                                     |
| endTime         | Number | 結束時間，時間戳，默認當前時間                                                                     |
| page            | String | 頁碼，從1開始                                                                             |

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
                "applyTime": 1666754820000,
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

**權重(IP/UID): 100**

#### Responses

| 參數              | 類型     | 示例                                 | 備注                                                |
| --------------- | ------ | ---------------------------------- | ------------------------------------------------- |
| symbol          | String | USDT                               | 提幣幣種                                              |
| amount          | Number | 9.99                               | 數量                                                |
| address         | String | TFFrjNfBAagmFWypE3Hnv6zPKAFhd3VcDf | 提幣地址                                              |
| withdrawOrderId | String | abc123                             | 自定義提現id                                           |
| fee             | Number | 0.01                               | 手續費                                               |
| ctime           | Number | 1605585397000                      | 創建時間                                              |
| txId            | String | 749864\_20201117115930             | 提現交易id                                            |
| id              | Number | 749864                             | 平台提現id                                            |
| applyTime       | Number | 1605585397000                      | 上鏈時間                                              |
| status          | Number | 2                                  | 提幣狀態，0-未審核 1-審核通過 2-審核拒絕 3-支付中 4-支付失敗 5-已完成 6-已撤銷 |
| info            | String | 提幣地址錯誤                             | 審核拒絕原因                                            |
