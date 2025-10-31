# 提现

## 提现

## 发起提现

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/withdraw/apply`

#### Headers

| Name                                          | Type    | Description |
| --------------------------------------------- | ------- | ----------- |
| X-CH-APIKEY<mark style="color:red;">\*</mark> | String  | 您的API-Key   |
| X-CH-SIGN<mark style="color:red;">\*</mark>   | String  | 签名          |
| X-CH-TS<mark style="color:red;">\*</mark>     | Integer | 时间戳         |

#### Request Body

| Name                                              | Type   | Description                                                                         |
| ------------------------------------------------- | ------ | ----------------------------------------------------------------------------------- |
| withdrawOrderId<mark style="color:red;">\*</mark> | String | 自定义提现id，保证唯一                                                                        |
| amount<mark style="color:red;">\*</mark>          | String | 数量                                                                                  |
| address<mark style="color:red;">\*</mark>         | String | 提币地址                                                                                |
| label                                             | String | 某些币种例如 XRP,XMR 允许填写次级地址标签                                                           |
| symbol                                            | String | 币种，支持多主链的币需要传实际的币种名称，参照[附录1](https://openapi-1.gitbook.io/exchange-openapi/fu-lu-1) |

{% tabs %}
{% tab title="200: OK " %}

```json
{
    "code":"Ѳ",//返回码，0代表成功，其他失败
    "msg":"sucess",//返回信息
    "data":{
        "id":518353 //提现id
    }
}
```

{% endtab %}
{% endtabs %}

**权重(IP/UID): 100**

## 提现记录查询

<mark style="color:green;">`POST`</mark> `https://openapi.xxx.xx/sapi/v1/withdraw/query`

#### Headers

| Name                                          | Type   | Description |
| --------------------------------------------- | ------ | ----------- |
| X-CH-APIKEY<mark style="color:red;">\*</mark> | String | 您的API-Key   |
| X-CH-SIGN<mark style="color:red;">\*</mark>   | String | 签名          |
| X-CH-TS<mark style="color:red;">\*</mark>     | String | 时间戳         |

#### Request Body

| Name            | Type   | Description                                                                         |
| --------------- | ------ | ----------------------------------------------------------------------------------- |
| symbol          | String | 币种，支持多主链的币需要传实际的币种名称，参照[附录1](https://openapi-1.gitbook.io/exchange-openapi/fu-lu-1) |
| withdrawId      | String | 平台提现id                                                                              |
| withdrawOrderId | String | 自定义提现id                                                                             |
| startTime       | Number | 开始时间，时间戳，默认90天前                                                                     |
| endTime         | Number | 结束时间，时间戳，默认当前时间                                                                     |
| page            | String | 页码，从1开始                                                                             |

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

**权重(IP/UID): 100**

#### Responses

| 参数              | 类型     | 示例                                 | 备注                                                |
| --------------- | ------ | ---------------------------------- | ------------------------------------------------- |
| symbol          | String | USDT                               | 提币币种                                              |
| amount          | Number | 9.99                               | 数量                                                |
| address         | String | TFFrjNfBAagmFWypE3Hnv6zPKAFhd3VcDf | 提币地址                                              |
| withdrawOrderId | String | abc123                             | 自定义提现id                                           |
| fee             | Number | 0.01                               | 手续费                                               |
| ctime           | Number | 1605585397000                      | 创建时间                                              |
| txId            | String | 749864\_20201117115930             | 提现交易id                                            |
| id              | Number | 749864                             | 平台提现id                                            |
| applyTime       | Number | 1605585397000                      | 上链时间                                              |
| status          | Number | 2                                  | 提币状态，0-未审核 1-审核通过 2-审核拒绝 3-支付中 4-支付失败 5-已完成 6-已撤销 |
| info            | String | 提币地址错误                             | 审核拒绝原因                                            |
