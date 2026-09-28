# 🚀 AI-ML Automated Candlestick Pattern Recognition with Market Trend Analysis and Trading System

## 📌 Project Overview

This project presents an AI/ML-based trading analysis system that automatically identifies candlestick patterns, analyzes market structure and trends, detects trend reversals, evaluates multiple machine learning models, and generates trading decision-support signals.

The system uses historical OHLCV (Open, High, Low, Close, Volume) stock market data and combines technical analysis with machine learning techniques.

---

# 🚀 Implemented Modules

## 1. Data Collection

Historical stock market data is collected using the `yfinance` library.

### Dataset Information

```text
Stock: RELIANCE.NS
Source: Yahoo Finance
Interval: Daily
Start Date: 2020-01-01
```

The OHLCV dataset contains:

* Date
* Open
* High
* Low
* Close
* Adjusted Close
* Volume

The raw dataset is stored as:

```text
nse_ohlcv_raw.csv
```

---

## 2. Data Preprocessing

The collected dataset is cleaned before further analysis.

The preprocessing stage includes:

* Missing value detection
* Duplicate row detection
* Date conversion
* Date sorting
* Missing value removal
* Duplicate removal
* Index resetting
* Price value rounding

The cleaned dataset is stored as:

```text
nse_ohlcv_clean.csv
```

---

## 3. Feature Engineering

Technical features are derived from OHLC price data to represent candlestick characteristics.

### Generated Features

* Body
* Range
* Upper Wick
* Lower Wick
* Body Ratio
* Upper Wick Ratio
* Lower Wick Ratio

### Feature Formulas

```text
Body = Close - Open

Range = High - Low

Upper Wick = High - max(Open, Close)

Lower Wick = min(Open, Close) - Low

Body Ratio = |Body| / Range

Upper Wick Ratio = Upper Wick / Range

Lower Wick Ratio = Lower Wick / Range
```

The engineered dataset is stored as:

```text
candlestick_features.csv
```

---

# 4. Market Structure & Trend Analysis

Market structure is analyzed using swing highs and swing lows.

The system identifies:

* Pivot High
* Pivot Low
* Higher High (HH)
* Higher Low (HL)
* Lower High (LH)
* Lower Low (LL)

Based on the identified structure, the market is classified into:

```text
Uptrend
Downtrend
Sideways
```

The system also determines market control:

```text
Buyers
Sellers
Neutral
```

### Moving Average Analysis

Two exponential moving averages are used:

* EMA 50
* EMA 200

The higher-timeframe bias is determined as:

```text
EMA 50 > EMA 200  → Bullish
EMA 50 ≤ EMA 200  → Bearish
```

The resulting market structure dataset is stored as:

```text
market_structure_analysis.csv
```

---

# 5. Candlestick Pattern Recognition

The system identifies eight candlestick patterns:

1. Hammer
2. Inverted Hammer
3. Doji
4. Bullish Engulfing
5. Bearish Engulfing
6. Shooting Star
7. Morning Star
8. Evening Star

The identified patterns are stored in:

```text
candlestick_pattern_dataset.csv
```

These pattern labels are later used as target variables for machine learning.

---

# 6. Trend Reversal Identification

The system identifies changes in market trend and classifies them into reversal or breakout/breakdown conditions.

### Reversal and Market Transition Conditions

```text
Downtrend → Uptrend
→ Bullish Reversal

Uptrend → Downtrend
→ Bearish Reversal

Sideways → Uptrend
→ Bullish Breakout

Sideways → Downtrend
→ Bearish Breakdown
```

Other conditions are classified as:

```text
No Reversal
```

The system also stores:

* Pattern Context
* Reversal Confirmed

The reversal dataset is stored as:

```text
trend_reversal_dataset.csv
```

---

# 7. Machine Learning Dataset Preparation

The final ML dataset combines candlestick features, market structure information, trend information, and historical lagged features.

Previous candle information is included using lagged features from:

```text
Previous 1 Candle
Previous 2 Candles
```

Categorical market information is encoded numerically, including:

* Trend
* Market Control
* Higher-Timeframe Bias
* Trend Reversal
* Reversal Confirmation

The final dataset contains eight target variables corresponding to the eight candlestick patterns.

The dataset is stored as:

```text
multi_pattern_ml_dataset.csv
```

---

# 🤖 8. Machine Learning Models

Five machine learning algorithms are implemented and compared.

### 1. Logistic Regression

Used as a linear classification model and baseline for comparison.

### 2. Decision Tree

Used to capture non-linear decision rules from the engineered features.

### 3. Random Forest

An ensemble of decision trees used for classification and feature importance analysis.

### 4. XGBoost

A gradient boosting algorithm used for classification and comparison with the other models.

### 5. Support Vector Machine

An RBF-kernel SVM is used for non-linear classification.

---

# 🎯 Target Variables

Each model is evaluated against the following eight candlestick pattern targets:

```text
Hammer
Inverted_Hammer
Doji
Bullish_Engulfing
Bearish_Engulfing
Shooting_Star
Morning_Star
Evening_Star
```

Therefore, the project evaluates:

```text
5 Machine Learning Models
×
8 Candlestick Pattern Targets
```

---

# 📊 9. Model Evaluation

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The dataset is divided chronologically using an:

```text
80% Training
20% Testing
```

split.

A chronological split is used to maintain the time-series ordering of the financial data.

---

## Model Result Files

Individual model results are stored in:

```text
results/logistic_regression/logistic_regression_results.csv

results/decision_tree/decision_tree_results.csv

results/random_forest/random_forest_results.csv

results/xgboost/xgboost_results.csv

results/svm/svm_results.csv
```

The overall model comparison is stored in:

```text
results/model_comparison.csv
```

The best-performing model for each evaluation metric is summarized in:

```text
results/best_model_summary.csv
```

---

# 🔍 10. Confusion Matrix Analysis

Confusion matrices are generated for the eight candlestick pattern targets.

They are stored inside:

```text
results/confusion_matrices/
```

The confusion matrices provide a detailed view of:

* True Positives
* True Negatives
* False Positives
* False Negatives

This helps evaluate the classification behavior for individual candlestick patterns.

---

# 🌳 11. Feature Importance Analysis

Random Forest feature importance is calculated for each candlestick pattern target.

The analysis helps identify which input features contribute most to the classification of each pattern.

Feature importance results are stored in:

```text
results/feature_importance/
```

A combined feature importance dataset is also generated:

```text
results/random_forest_feature_importance.csv
```

---

# 📈 12. Trading Signal Generation

The system generates historical trading decision-support signals based on the combination of:

* Market trend
* Market structure
* Candlestick patterns
* Higher-timeframe bias
* Trend reversals
* Reversal confirmation
* Breakouts and breakdowns

The generated signals are:

```text
BUY
SELL
HOLD
```

### BUY Signal Conditions

A BUY signal can be generated when bullish market conditions are satisfied, such as:

```text
Bullish Reversal
+
Reversal Confirmed
+
Bullish Higher-Timeframe Bias
```

or:

```text
Uptrend
+
Bullish Candlestick Pattern
+
Bullish Higher-Timeframe Bias
```

or:

```text
Bullish Breakout
+
Bullish Candlestick Pattern
```

### SELL Signal Conditions

A SELL signal can be generated under corresponding bearish conditions, such as:

```text
Bearish Reversal
+
Reversal Confirmed
+
Bearish Higher-Timeframe Bias
```

or:

```text
Downtrend
+
Bearish Candlestick Pattern
+
Bearish Higher-Timeframe Bias
```

or:

```text
Bearish Breakdown
+
Bearish Candlestick Pattern
```

The generated signals are stored in:

```text
results/trading_signals.csv
```

> **Note:** The current signal-generation module is a rule-based decision-support component. It does not execute actual broker orders.

---

# 📊 13. Trading Analytics & Visualization

The system generates several analytical visualizations.

### Trading Signal Distribution

```text
results/trading_signal_distribution.png
```

### Price Chart with Trading Signals

```text
results/price_trading_signals.png
```

### Market Trend Distribution

```text
results/market_trend_distribution.png
```

### Candlestick Pattern Distribution

```text
results/candlestick_pattern_distribution.png
```

### Trend Reversal Distribution

```text
results/trend_reversal_distribution.png
```

The system also generates:

```text
results/trading_analytics.csv
```

containing overall trading analysis such as:

* Total Records
* BUY Signals
* SELL Signals
* HOLD Signals
* Bullish Reversals
* Bearish Reversals
* Confirmed Reversals

The final combined analysis is stored in:

```text
results/final_trading_analysis.csv
```

---

# 🖥️ 14. Streamlit Dashboard

A Streamlit-based dashboard is developed to provide an interactive view of the analysis results.

## Current Market Status

Displays the latest available:

* Stock price
* Market trend
* Trading signal
* Candlestick pattern
* Trend reversal
* Market structure
* Higher-timeframe bias

## Price & Trading Signals

Displays historical price movement along with generated BUY and SELL signals.

## Market Analytics

Provides visualizations for:

* Market trends
* Candlestick patterns
* Trend reversals
* Trading signals

## Machine Learning Analysis

Displays:

* Model comparison
* Accuracy
* Precision
* Recall
* F1-Score
* Best model summary
* Feature importance

## Data Export

The dashboard provides access to the generated trading analysis data.

---

# 🛠️ Technologies Used

### Programming Language

* Python

### Data Collection

* yfinance

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* XGBoost

### Visualization

* Matplotlib

### Dashboard

* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code

---

# 📁 Important Output Files

## Datasets

```text
nse_ohlcv_raw.csv
nse_ohlcv_clean.csv
candlestick_features.csv
market_structure_analysis.csv
candlestick_pattern_dataset.csv
trend_reversal_dataset.csv
multi_pattern_ml_dataset.csv
```

## ML Results

```text
results/model_comparison.csv
results/best_model_summary.csv
```

## Trading Results

```text
results/trading_signals.csv
results/trading_analytics.csv
results/final_trading_analysis.csv
```

---

# 📂 Project Structure

```text
Candlestick/
│
├── README.md
├── app.py
├── requirements.txt
│
├── data/
│   ├── nse_ohlcv_raw.csv
│   ├── nse_ohlcv_clean.csv
│   ├── candlestick_features.csv
│   ├── market_structure_analysis.csv
│   ├── candlestick_pattern_dataset.csv
│   ├── trend_reversal_dataset.csv
│   └── multi_pattern_ml_dataset.csv
│
├── notebooks/
│   └── project notebooks
│
└── results/
    │
    ├── logistic_regression/
    │   └── logistic_regression_results.csv
    │
    ├── decision_tree/
    │   └── decision_tree_results.csv
    │
    ├── random_forest/
    │   └── random_forest_results.csv
    │
    ├── xgboost/
    │   └── xgboost_results.csv
    │
    ├── svm/
    │   └── svm_results.csv
    │
    ├── confusion_matrices/
    │
    ├── feature_importance/
    │
    ├── model_comparison.csv
    ├── best_model_summary.csv
    ├── random_forest_feature_importance.csv
    ├── trading_signals.csv
    ├── trading_analytics.csv
    ├── final_trading_analysis.csv
    ├── trading_signal_distribution.png
    ├── price_trading_signals.png
    ├── market_trend_distribution.png
    ├── candlestick_pattern_distribution.png
    └── trend_reversal_distribution.png
```

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/BinduSamaseni2005/Candlestick.git
```

Then enter the project directory:

```bash
cd Candlestick
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Notebook

Open the notebook inside:

```text
notebooks/
```

Execute the project modules sequentially.

The recommended execution order is:

```text
Data Collection
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Market Structure & Trend Analysis
        ↓
Candlestick Pattern Recognition
        ↓
Trend Reversal Identification
        ↓
Machine Learning Dataset Preparation
        ↓
Machine Learning Models
        ↓
Model Evaluation
        ↓
Trading Signal Generation
        ↓
Trading Analytics
```

---

## 5. Run the Streamlit Dashboard

Run:

```bash
streamlit run app.py
```

The dashboard will open in the browser at:

```text
http://localhost:8501
```

---

# 🔮 Future Scope

The following improvements can be considered in future development:

* Real-time market data integration
* Live candlestick pattern prediction
* Real-time trading signals
* Advanced deep learning models
* LSTM/Transformer-based market prediction
* Backtesting framework
* Risk-reward optimization
* Stop-loss and take-profit management
* Portfolio-level analysis
* Broker API integration
* Automated order execution

---

# ⚠️ Disclaimer

This project is developed for **academic, educational, and research purposes**.

The generated BUY, SELL, and HOLD signals are decision-support outputs based on historical market data and predefined analytical conditions.

They should not be considered financial advice or a guarantee of future market performance.

---

# 👩‍💻 Author

**Bindu Samaseni**

GitHub:

https://github.com/BinduSamaseni2005

---

# ⭐ Project Status

**Implementation Completed**

The project currently includes:

* Historical data collection
* Data preprocessing
* Feature engineering
* Market structure analysis
* Candlestick pattern recognition
* Trend reversal identification
* Machine learning model training
* Model comparison
* Confusion matrix analysis
* Feature importance analysis
* Trading signal generation
* Trading analytics
* Streamlit dashboard

Automated broker order execution is planned as future scope.
