# SDK开发库

### Demo地址

<https://github.com/exchange2021>

### 下面是创建订单的样例

签名规则请参考[**签名示例**](https://github.com/exhcange/OpenApi-en/blob/master/broken-reference/README.md)

* Java

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"symbol\":\"BTCUSDT\",\"volume\":1,\"side\":\"BUY\",\"type\":\"LIMIT\",\"price\":10000,\"newClientOrderId\":\"\",\"recvWindow\":5000}");
Request request = new Request.Builder()
  .url("https://openapi.xxx.com")
  .method("POST", body)
  .addHeader("X-CH-APIKEY", "Your API key")
  .addHeader("X-CH-TS", "1596543296058")
  .addHeader("Content-Type", "application/json")
  .addHeader("X-CH-SIGN", "encrypt sign")
  .build();
Response response = client.newCall(request).execute();
```

* Go

```java
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://openapi.xxx.com"
  method := "POST"

  payload := strings.NewReader("{\"symbol\":\"BTCUSDT\",\"volume\":1,\"side\":\"BUY\",\"type\":\"LIMIT\",\"price\":10000,\"newClientOrderId\":\"\",\"recvWindow\":5000}")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("X-CH-APIKEY", "Your API key")
  req.Header.Add("X-CH-TS", "1596543881257")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("X-CH-SIGN", "encrypt sign")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}
```

* Python

```java
import requests

url = "https://openapi.xxx.com"

payload = "{\"symbol\":\"BTCUSDT\",\"volume\":1,\"side\":\"BUY\",\"type\":\"LIMIT\",\"price\":10000,\"newClientOrderId\":\"\",\"recvWindow\":5000}"
headers = {
  'X-CH-APIKEY': 'Your API key',
  'X-CH-TS': '1596543881257',
  'Content-Type': 'application/json',
  'X-CH-SIGN': 'encrypt sign'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

```

* Php

```java
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('https://openapi.xxx.com');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'X-CH-APIKEY' => 'Your API key',
  'X-CH-TS' => '1596543881257',
  'Content-Type' => 'application/json',
  'X-CH-SIGN' => 'encrypt sign'
));
$request->setBody('{"symbol":"BTCUSDT","volume":1,"side":"BUY","type":"LIMIT","price":10000,"newClientOrderId":"","recvWindow":5000}');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

* NodeJs

```java
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://openapi.xxx.com',
  'headers': {
    'X-CH-APIKEY': 'Your API key',
    'X-CH-TS': '1596543881257',
    'Content-Type': 'application/json',
    'X-CH-SIGN': 'encrypt sign'
  },
  body: JSON.stringify({"symbol":"BTCUSDT","volume":1,"side":"BUY","type":"LIMIT","price":10000,"newClientOrderId":"","recvWindow":5000})

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

```
