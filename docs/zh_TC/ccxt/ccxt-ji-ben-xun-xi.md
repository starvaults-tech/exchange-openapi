# CCXT基本訊息

**一、CCXT 簡介**

CCXT（CryptoCurrency eXchange Trading Library）是一個開源的加密貨幣交易所統一 API 庫，支援多個主流程式語言（Python、JavaScript/Node.js、PHP），用於簡化多家數位貨幣交易所的介面對接問題。

CCXT 提供了統一的資料結構和介面封裝，讓開發者可以使用一套標準化方法來呼叫不同交易所（如 Binance、Huobi、OKX、Coinbase、Bitfinex 等）的行情查詢、下單、資產管理等功能，無需分別適配每個交易所各異的 API。

**適用領域**

* 量化交易、自動化交易系統
* 資料爬取、行情監控系統
* 多交易所套利系統
* 投資組合管理工具
* 區塊鏈應用與金融服務平台
* 交易資料分析與視覺化工具

***

**二、核心特性**

1. **支援 100+ 主流交易所**
   * 覆蓋全球主流中心化交易所（CEX）
   * 相容部分去中心化交易所（DEX）
2. **統一介面設計**
   * REST API 標準化封裝
   * 統一的市場資料結構（Market Structure）
   * 相容不同交易所不同風格的參數（例如 symbol、order type 等）
3. **多語言支援**
   * Python
   * JavaScript (Node.js)
   * PHP
4. **良好的社群支援與開源活躍度**
   * GitHub 20K+ Stars
   * 社群貢獻活躍、更新及時
   * 定期新增交易所與功能
5. **相容 REST 與 WebSocket（部分交易所）**
   * REST：取得市場資料、帳戶資訊、下單操作
   * WebSocket：即時推送價格、成交等資料（需交易所支援）
6. **支援多種交易操作**
   * 取得市場行情（Ticker, Order Book, Trades）
   * 帳戶資產查詢
   * 限價單、止損單、市價單等下單操作
   * 訂單管理（撤單、查詢訂單狀態）

***

**三、架構設計**

```
應用層
   │
   ├── Python/JS/PHP 語言呼叫
   │
   ├── CCXT Core（統一 API 封裝層）
   │
   ├── 各交易所驅動（Binance/OKX/Huobi 等）
   │
   └── 各交易所實際 REST/WebSocket 介面
```

* 各交易所的特殊參數、限制、格式統一封裝
* CCXT 負責轉換成統一標準格式，簡化開發者工作量
* 方便進行多交易所資料整合和策略遷移

***

**四、適用場景舉例**

| 場景          | 描述                        |
| ----------- | ------------------------- |
| 多交易所行情聚合    | 同時取得多個交易所某幣種即時行情          |
| 自動化交易（機器人）  | 根據策略程式自動下單、撤單             |
| 資產帳戶管理      | 自動化定時拉取帳戶資產，進行持倉管理        |
| 交易所套利系統（搬磚） | 比較不同交易所價差，自動化下單套利         |
| 交易資料分析平台    | 採集歷史 K 線、成交資料，做視覺化分析或建模預測 |

***

**五、支援的部分交易所**

完整支援交易所列表參見：[https://docs.ccxt.com/#/README?id=exchanges](https://docs.ccxt.com/#/README?id=exchanges)

***

**六、官方資源**

* OpenAPI 文件站：[https://star-vaults.gitbook.io/exchange-openapi](https://star-vaults.gitbook.io/exchange-openapi)
* CCXT 官方文件：[https://docs.ccxt.com](https://docs.ccxt.com/)

***

**九、安全性建議**

* API Key 權限最小化（僅開行情/交易權限）
* 正式環境請妥善加密儲存 API Key
* 及時處理網路錯誤、交易失敗、異常狀態
* 建議使用 Testnet 進行開發測試（如 Binance、OKX 均支援）

***
