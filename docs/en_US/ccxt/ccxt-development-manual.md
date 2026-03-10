# CCXT Development Manual

#### 1. Overview

This exchange supports CCXT interface development based on Python version, which is convenient for strategy, quantitative, automated trading and other applications to land quickly.

* CCXT supported version: v4.x and above
* Trading market: Spot

***

#### 2. Access Environment Requirements

* Python version：≥ 3.7
* CCXT install：

```bash
pip install ccxt
```

* Verify Installation：

```python
import ccxt
print(ccxt.__version__)
```

***

#### 3. Preparation of content notes

| Project                             | Description                                                                                                                                  |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Apply for Exchange ApiKey/SecertKey | Log in to the exchange's front-end user page, create an API in API Management - Accounts - API Management, and get the APIKey and SecertKey. |

Sections of CCXT that need to be added/modified：

```
#Code structure
|-ccxt
    |-python
        |-ccxt
            |-__init__.py             #Modify, add exchange name for initialization
            |-bitwind.py              #New doc, main request methodology
            |-test
                |-test_bitwind.py     #New doc, for testing the calling interface
            |-abstract
                |-bitwind.py          #interface definition
```

***

#### 4. API Key Acquisition and Authentication

* Log in to the Exchange UI → API Management → New API Key.
* Parameters:
  * `apiKey`
  * `SecretKey`

**Example：**

For this part of the code, you need to create a new “exchange name.py” file in the ccxt folder in the ccxt directory and put this part of the code in that file to change the name of the exchange.

```python
import ccxt

#e.g. bitwind exchange
class bitwind(ccxt.Exchange,ImplicitAPI):

    def describe(self):
        return self.deep_extend(super().describe(), {
            'id': 'bitwind',
            'name': 'BitWind',
            'countries': ['CN'],
            'apiKey': '', # exchange user APIKEY
            'securityKey' : '', # exchange user SECURITYKEY
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

#### 5. Python Implementation Code

5.1 Add initialized exchange name

Add the name of the exchange to the list of exchanges in the `__init__.py` file in the ccxt folder directory in the pyhton folder

Note: Lowercase letters, can't contain special characters, can't contain spaces

```
#Add exchange name
exchanges = [
    'ace',
    ...
    'bitwind',
]
```

5.2 New interfaces

In the ccxt file under the abstract folder directory, create a new interface file. For example `bitwind.py` and add the interface content for example:

```
from ccxt.base.types import Entry

#Exchange Interface Configuration Content
class ImplicitAPI:
    #public
    public_get_sapi_v2_time = publicGetSapiV2Time = Entry('sapi/v2/time', 'public', 'GET', {})

    #private
    private_get_sapi_v1_account = privateGetSapiV2Account = Entry('sapi/v1/account', 'private', 'GET', {})

```

5.3 New Master Methods

In the ccxt folder, in the same directory as abstract, add a new `bitwind.py` file that implements the methods for requesting the Exchange OpenAPI, for example:

```
import ccxt
from ccxt.abstract.bitwind import ImplicitAPI
import hmac
import json
import urllib.parse
import time

# Exchange API DOC: https://star-vaults.gitbook.io/exchange-openapi/en_us
class bitwind(ccxt.Exchange,ImplicitAPI):

    def describe(self):
        return self.deep_extend(super().describe(), {
            'id': 'bitwind',
            'name': 'BitWind',
            'countries': ['CN'],
            'apiKey': '', # Exchange user APIKEY
            'securityKey' : '', # Exchange user SECURITYKEY
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
                        'ticker'  # Here publicGetMarkets() is defined to get the list of trading markets
                    ],
                },
                'private': {
                    'post': [
                        'sapi/v2/trades',
                        'order',
                        'cancelOrder' # e.g. privatePostOrder()
                    ],
                },
            },
        })


    def fetch_time(self, params={}):
        """Obtain time"""
        print("fetch_time")
        response = self.publicGetSapiV2Time(params)  # 不使用 await
        print("response:",response)
        return response

    # Obtian time
    def public_get_time(self,params={}):
        print("public_get_time params :",)
        response = self.publicGetSapiV2Time()
        print("response:", response)
        return response


    # Account information
    def private_get_account(self, params={}):
        print("private_get_account params :", )
        response = self.privateGetSapiV2Account()
        print("response:", response)
        return response



    # Generate sign and request methods via ak,sk
    def preCreateHash(self,timestamp, method, requestPath, queryString, body):
        # Splice signature
        pre = timestamp + method + requestPath
        if queryString.strip() != '':
            pre = pre + '?' +queryString.strip()
        if body.strip() != '':
            pre = pre + body.strip()
        return pre

    # Generate Signature
    #generate signature
    def toParamSign(self,timestamp, method, requestPath, queryString, body, secretKey):
        return hmac.new(secretKey.encode('UTF-8'), self.preCreateHash(timestamp, method, requestPath, queryString, body).encode('UTF-8'),"SHA256").hexdigest()


    # Sign and send the request
    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api] + '/' + path
        current = str(round((time.time()-3) * 1000))

        if params:
            body = json.dumps(params)
            print("first body",body)

        if api == 'public':
            if method == 'GET':
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

        # If it's a private API, add the authentication
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

5.4 Method invocation

New `test_bitwind.py` file in the test folder in the ccxt folder directory, example:

```
import ccxt 

# Initializing the Exchange
exchange = ccxt.bitwind()

# method invocation
#public_get_sapi_v2_time
 try:
     markets = exchange.public_get_time()
 except Exception as e:
     print("Error public_get_sapi_v2_time:", str(e))



#private_get_sapi_v1_account
 try:
     markets = exchange.private_get_account()
 except Exception as e:
     print("Error private_get_sapi_v1_account:", str(e))
```

***

#### 6. List of supported methods

| Bitwind                             | Description              |
| ----------------------------------- | ------------------------ |
| public\_get\_ping()                 | Test link                |
| public\_get\_time()                 | Server time              |
| fetchMarkets()                      | List of Currency Pairs   |
| fetchOrderBook()                    | Order book               |
| fetchTicker()                       | Ticker                   |
| public\_get\_trades()               | Recent transactions      |
| fetchOHLCV()                        | K-line/Candlestick Data  |
| createOrder()                       | Create New Order         |
| private\_post\_batchOrders()        | Batch order              |
| fetchOrder()                        | Order Inquiry            |
| cancelOrder()                       | Withdrawal of orders     |
| private\_post\_batchCancel\_order() | Batch Order Cancellation |
| fetchOpenOrders()                   | Current Orders           |
| fetchMyTrades()                     | Transaction records      |
| fetchBalance()                      | Account Information      |

***

#### 7. Common errors and troubleshooting

Returning an error report generally consists of two parts: an error code and an error message. The error code is generic, but the error message is different. The following is an example of an error JSON Payload:

```json
{
  "code":-1121,
  "msg":"Invalid symbol."
}
```

#### 8. Generic server and network errors

| -1000 | An unknown error occurred while processing the request                                                                                                                                                                                                                                                                                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| -1001 | Internal error, could not process your request, please try again.                                                                                                                                                                                                                                                                                                                          |
| -1002 | You are not authorized to execute this request. Requests need to send an API key, and we recommend appending an API key to all request headers.                                                                                                                                                                                                                                            |
| -1003 | Requests exceeding limits too often                                                                                                                                                                                                                                                                                                                                                        |
| -1004 | You are not authorized to execute this request,User not exit Company                                                                                                                                                                                                                                                                                                                       |
| -1006 | Received a message that does not conform to the preset format, order status unknown                                                                                                                                                                                                                                                                                                        |
| -1007 | Waiting for backend server response timeout. Send status unknown, Execute status unknown                                                                                                                                                                                                                                                                                                   |
| -1014 | Unsupported order combinations                                                                                                                                                                                                                                                                                                                                                             |
| -1015 | Too many new orders, please reduce the frequency of your requests.                                                                                                                                                                                                                                                                                                                         |
| -1016 | Server offline                                                                                                                                                                                                                                                                                                                                                                             |
| -1017 | We recommend appending the Content-Type to all request headers and setting it to application/json.                                                                                                                                                                                                                                                                                         |
| -1020 | This operation is not supported                                                                                                                                                                                                                                                                                                                                                            |
| -1021 | The time delay is too large, the server decides that the time consumed has exceeded the receivevWindow according to the timestamp in the request, please improve the network conditions or increase the receivevWindow The time offset is too large, the server decides that the client's time is more than 1 second ahead of the server's time according to the timestamp in the request. |
| -1022 | The signature of this request is invalid                                                                                                                                                                                                                                                                                                                                                   |
| -1023 | You are not authorized to execute this request, and we recommend that you append X-CH-TS to all request headers.                                                                                                                                                                                                                                                                           |
| -1024 | You are not authorized to execute this request, we recommend that you append X-CH-SIGN to the request header.                                                                                                                                                                                                                                                                              |

#### 9. Issues in the content of the request

| -1100 | Illegal characters found in parameters                                                  |
| ----- | --------------------------------------------------------------------------------------- |
| -1101 | Too many parameters are sent.                                                           |
| -1102 | Mandatory parameter not sent, the parameter is null/empty or incorrectly formatted      |
| -1103 | <p>Unknown parameters were sent.</p><p>Each request requires at least one parameter</p> |
| -1104 | Not all parameters sent are read.                                                       |
| -1105 | Parameter is null                                                                       |
| -1106 | Parameters have been sent when not needed.                                              |
| -1111 | Accuracy exceeds the maximum value defined for this asset.                              |
| -1112 | Pair has no pending orders                                                              |
| -1116 | Invalid order type.                                                                     |
| -1117 | Invalid Direction of Sale and Purchase                                                  |
| -1118 | New customer order ID is empty                                                          |
| -1121 | Invalid symbol                                                                          |
| -1136 | Order quantity is less than the minimum value                                           |
| -1138 | Order price exceeds the allowable range                                                 |
| -1139 | This pair does not support market price trading                                         |
| -1145 | Cancellation is not supported for this order type                                       |
| -2013 | Order doesn't exist.                                                                    |
| -2015 | Invalid API key, IP or operating privileges                                             |
| -2016 | Transactions frozen                                                                     |
| -2017 | The balance is insufficient.                                                            |

***

#### 10. technical documentation

* OpenAPI Documentation Site：[https://star-vaults.gitbook.io/exchange-openapi/](https://star-vaults.gitbook.io/exchange-openapi/en_us)
* CCXT Official Documentation：[https://docs.ccxt.com](https://docs.ccxt.com)
