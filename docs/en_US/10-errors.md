# Errors

Errors consist of two parts: an error code and a message. Codes are universal, but messages can vary. Here is the error JSON payload:

```java
{
  "code":-1121,
  "msg":"Invalid symbol."
}
```

## General Server or Network issues

| code  | 描述                                                                                                                                                                                                                                                   |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -1000 | An unknown error occured while processing the request.                                                                                                                                                                                               |
| -1001 | Internal error; unable to process your request. Please try again.                                                                                                                                                                                    |
| -1002 | You are not authorized to execute this request. Request need API Key included in . We suggest that API Key be included in any request.                                                                                                               |
| -1003 | Requests exceed the limit too frequently.                                                                                                                                                                                                            |
| -1004 | You are not authorized to execute this request. User not exit Company                                                                                                                                                                                |
| -1006 | An unexpected response was received from the message bus. Execution status unknown. OPEN API server find some exception in execute request .Please report to Customer service.                                                                       |
| -1007 | Timeout waiting for response from backend server. Send status unknown; execution status unknown.                                                                                                                                                     |
| -1014 | Unsupported order combination.                                                                                                                                                                                                                       |
| -1015 | Too many new orders.                                                                                                                                                                                                                                 |
| -1016 | This service is no longer available.                                                                                                                                                                                                                 |
| -1017 | We recommend attaching Content-Type to all request headers and setting it to application/json                                                                                                                                                        |
| -1020 | This operation is not supported.                                                                                                                                                                                                                     |
| -1021 | <ul><li>Timestamp for this request is outside of the recvWindow.</li></ul><ul><li>Timestamp for this request was 1000ms ahead of the server's time.</li></ul><ul><li>Please check the difference between your local time and server time .</li></ul> |
| -1022 | Signature for this request is not valid.                                                                                                                                                                                                             |
| -1023 | You are not authorized to execute this request, we recommend that you add X-CH-TS to all request headers                                                                                                                                             |
| -1024 | You are not authorized to execute this request, we recommend that you add X-CH-SIGN to the request header                                                                                                                                            |

## Request issues

| code  | 描述                                                                                                                                                                                                                                                    |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -1100 | Illegal characters found in a parameter.                                                                                                                                                                                                              |
| -1101 | Too many parameters sent for this endpoint                                                                                                                                                                                                            |
| -1102 | <ul><li>A mandatory parameter was not sent, was empty/null, or malformed.</li></ul><ul><li>Mandatory parameter '%s' was not sent, was empty/null, or malformed.</li></ul><ul><li>Param '%s' or '%s' must be sent, but both were empty/null!</li></ul> |
| -1103 | <ul><li>An unknown parameter was sent.</li></ul><ul><li>each request requires at least one parameter. {Timestamp}.</li></ul>                                                                                                                          |
| -1104 | <ul><li>Not all sent parameters were read.</li></ul><ul><li>Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.</li></ul>                                                                                                    |
| -1105 | <ul><li>A parameter was empty.</li></ul><ul><li>Parameter '%s' was empty.</li></ul>                                                                                                                                                                   |
| -1106 | <ul><li>A parameter was sent when not required.</li></ul><ul><li>Parameter '%s' sent when not required.</li></ul>                                                                                                                                     |
| -1111 | Precision is over the maximum defined for this asset.                                                                                                                                                                                                 |
| -1112 | No orders on book for symbol.                                                                                                                                                                                                                         |
| -1116 | <ul><li>Invalid orderType.</li></ul><ul><li>In the current version , ORDER\_TYPE values is LIMIT or MARKET.</li></ul>                                                                                                                                 |
| -1117 | <ul><li>Invalid side.</li></ul><ul><li>ORDER\_SIDE values is BUY or SELL</li></ul>                                                                                                                                                                    |
| -1118 | New client order ID was empty.                                                                                                                                                                                                                        |
| -1121 | Invalid symbol.                                                                                                                                                                                                                                       |
| -1136 | Order volume lower than the minimum.                                                                                                                                                                                                                  |
| -1138 | Order price exceeds permissible range.                                                                                                                                                                                                                |
| -1139 | This trading pair does not support market trading                                                                                                                                                                                                     |
| -1145 | This order type does not support cancellation                                                                                                                                                                                                         |
| -2013 | Order does not exist.                                                                                                                                                                                                                                 |
| -2015 | Invalid API-key, IP, or permissions for action.                                                                                                                                                                                                       |
| -2016 | Transaction is frozen                                                                                                                                                                                                                                 |
| -2017 | Insufficient balance                                                                                                                                                                                                                                  |
