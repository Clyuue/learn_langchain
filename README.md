# LangChain Agents 學習專案

這是一個使用 LangChain 框架學習 Agent 開發的專案，目前包含兩個 Agent 範例。

## 環境設置

### 1. 安裝依賴

```bash
pip install langchain langchain-openai langchain-tavily python-dotenv requests
```

### 2. 建立 `.env` 檔案

```env
OPENAI_API_KEY=your_openai_api_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Agents

### 1. 天氣查詢 Agent (`weather_agent.py`)

使用 OpenWeatherMap API 查詢指定城市的當前天氣資訊。

**功能：**
- 查詢城市天氣（溫度、濕度、風速、天氣狀況等）
- 回傳繁體中文天氣資訊

**使用方式：**
```bash
python weather_agent.py
```

**環境變數：**
- `OPENWEATHERMAP_API_KEY`：OpenWeatherMap API 金鑰

### 2. 網路搜尋 Agent (`tavily_agent.py`)

使用 Tavily 搜尋引擎進行情境式網路搜尋。

**功能：**
- 即時網路資訊搜尋
- 可設定搜尋結果數量

**使用方式：**
```bash
python tavily_agent.py
```

## 技術栈

- **LangChain**：Agent 框架
- **OpenAI**：GPT-5 模型 (gpt-5-nano-2025-08-07)
- **OpenWeatherMap API**：天氣數據
- **Tavily**：網路搜尋
