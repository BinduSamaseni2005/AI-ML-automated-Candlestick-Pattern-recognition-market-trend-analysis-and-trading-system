# AI/ML Automated Candlestick Pattern Recognition, Market Trend Analysis and Trading System

## Project Overview

This project aims to develop an AI/ML-based trading analysis system that combines:

- Candlestick Pattern Recognition
- Market Structure Analysis
- Trend Analysis
- Trend Reversal Identification
- Machine Learning-Based Pattern Prediction
- Trading Signal Generation (Future Work)

The system uses historical stock market data to identify market structure, detect candlestick patterns, analyze trends and reversals, and prepare datasets for machine learning model development.

---

## Project Flow

```text
Stock Data
      ↓
OHLCV Dataset
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Market Structure Analysis
      ↓
Trend Analysis
      ↓
Trend Reversal Identification
      ↓
Candlestick Pattern Recognition
      ↓
ML Dataset Preparation
      ↓
Machine Learning Models
      ↓
Model Evaluation
      ↓
Buy/Sell Recommendations
      ↓
Dashboard
```

---

# Project Structure

```text
Candlestick/

├── data
│   ├── raw
│   │   └── nse_ohlcv_raw.csv
│   │
│   ├── processed
│   │   ├── nse_ohlcv_clean.csv
│   │   ├── candlestick_features.csv
│   │   ├── market_structure_analysis.csv
│   │   ├── candlestick_pattern_dataset.csv
│   │   ├── trend_reversal_dataset.csv
│   │   │
│   │   └── multi_pattern_ml_dataset.csv
│
├── notebooks
│   └── Candlestick_Pattern_Recognition_Project.ipynb
│
├── README.md
```

---

# Completed Modules

---

## Step 1: Data Collection and Understanding

### Implemented

- Yahoo Finance Data Collection
- RELIANCE.NS Historical Data Download
- OHLCV Dataset Generation
- Dataset Exploration
- Statistical Analysis
- Data Inspection

### Dataset Columns

- Open
- High
- Low
- Close
- Volume

### Output

```text
nse_ohlcv_raw.csv
```

---

## Step 2: Data Preprocessing

### Implemented

- Missing Value Handling
- Duplicate Removal
- Date Conversion
- Data Sorting
- Dataset Cleaning
- Dataset Validation

### Output

```text
nse_ohlcv_clean.csv
```

---

## Step 3: Feature Engineering

### Implemented

#### Candle Features

- Body
- Range
- Upper Wick
- Lower Wick

#### Ratio Features

- Body Ratio
- Upper Wick Ratio
- Lower Wick Ratio

### Feature Formulas

```text
Body = |Close - Open|

Range = High - Low

Upper Wick =
High - max(Open, Close)

Lower Wick =
min(Open, Close) - Low
```

### Output

```text
candlestick_features.csv
```

---

## Step 4: Market Structure & Trend Analysis

### Implemented

#### Swing Detection

- Pivot High Detection
- Pivot Low Detection

#### Market Structure

- Higher High (HH)
- Higher Low (HL)
- Lower High (LH)
- Lower Low (LL)

#### Trend Classification

- Uptrend
- Downtrend
- Sideways

#### Market Analysis

- Market Control Detection
- Higher Timeframe Bias (HTF Bias)

#### Visualization

- Market Structure Plot
- Pivot High Visualization
- Pivot Low Visualization
- HH/HL/LH/LL Annotation

### Output

```text
market_structure_analysis.csv
```

---

## Step 5: Candlestick Pattern Recognition

### Implemented Patterns

### Single Candle Patterns

- Hammer
- Inverted Hammer
- Doji
- Shooting Star

### Double Candle Patterns

- Bullish Engulfing
- Bearish Engulfing

### Triple Candle Patterns

- Morning Star
- Evening Star

### Output

```text
candlestick_pattern_dataset.csv
```

---

## Step 6: Trend Reversal Identification

### Implemented

#### Trend Transition Detection

- Downtrend → Uptrend
- Uptrend → Downtrend
- Sideways → Uptrend
- Sideways → Downtrend

#### Reversal Categories

- Bullish Reversal
- Bearish Reversal
- Bullish Breakout
- Bearish Breakdown

#### Confirmation Logic

Bullish Reversal Confirmation:

- Hammer
- Bullish Engulfing
- Morning Star

Bearish Reversal Confirmation:

- Shooting Star
- Bearish Engulfing
- Evening Star

### Output

```text
trend_reversal_dataset.csv
```

---

## Step 7: Multi-Pattern ML Dataset Preparation

### Implemented

#### Current Candle Features

- OHLCV Features
- Engineered Candle Features

#### Previous Candle Features

- Previous Candle OHLC
- Previous Candle Wick Features
- Previous Candle Ratios

#### Previous Two Candle Features

- Two-Candle Historical Context
- Historical Candle Ratios

#### Encoded Features

- Trend Encoding
- Market Control Encoding
- HTF Bias Encoding
- Trend Reversal Encoding
- Reversal Confirmation Encoding

#### Target Labels

- Hammer
- Inverted Hammer
- Doji
- Bullish Engulfing
- Bearish Engulfing
- Shooting Star
- Morning Star
- Evening Star

### Dataset Statistics

```text
Dataset Shape : 1659 × 47

Feature Count : 39

Target Count : 8
```

### Output

```text
multi_pattern_ml_dataset.csv
```

---

# Candlestick Patterns Implemented

| Pattern | Type |
|----------|----------|
| Hammer | Single Candle |
| Inverted Hammer | Single Candle |
| Doji | Single Candle |
| Shooting Star | Single Candle |
| Bullish Engulfing | Two Candle |
| Bearish Engulfing | Two Candle |
| Morning Star | Three Candle |
| Evening Star | Three Candle |

---

# Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

### Data Source

- Yahoo Finance API (yfinance)

### Development Environment

- Jupyter Notebook
- VS Code

---

# Current Progress

### Completed

✅ Data Collection

✅ Data Preprocessing

✅ Feature Engineering

✅ Market Structure Analysis

✅ Trend Analysis

✅ Candlestick Pattern Recognition

✅ Trend Reversal Identification

✅ Multi-Pattern ML Dataset Preparation

---

# Upcoming Modules

---

## Step 8: Machine Learning Model Development

### Planned

- Random Forest
- XGBoost
- Logistic Regression
- Multi-Pattern Classification
- Trend Prediction Models

---

## Step 9: Model Evaluation

### Planned

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Feature Importance Analysis

---

## Step 10: Trading Signal Generation

### Planned

- Buy Signal Detection
- Sell Signal Detection
- Confidence Score Calculation
- Risk Management Rules

---

## Step 11: Visualization Dashboard

### Planned

- Market Structure Dashboard
- Trend Dashboard
- Pattern Dashboard
- Reversal Dashboard
- Signal Dashboard
- Interactive Charts

---

## Step 12: Automated Trading System (Future Scope)

### Planned

- Real-Time Market Data Integration
- Live Pattern Detection
- Automated Trade Execution
- Portfolio Monitoring
- Performance Analytics

---

# Current Status

```text
Project Status:
Completed up to Step 7

Current Stage:
ML Dataset Preparation Completed

Next Stage:
Machine Learning Model Development
```

---
**Author:** Bindu Samaseni  
**Project:** AI/ML Automated Candlestick Pattern Recognition, Market Trend Analysis and Trading System
